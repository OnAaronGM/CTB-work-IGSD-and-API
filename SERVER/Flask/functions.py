import os, sys, json
import pandas as pd
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from Common import dictVars as dv
from Flask import create_plots, search_sg, generate_sankey
from copy import deepcopy


def create_list_dict(data):
    data["PDL1Result"] = "PDL1_"+data["PDL1Result"]
    d_vars = {k: v for k, v in zip(dv.vars_corresp_input_form_with_df.values(), data.values())}
    d_vars_info = {"orgfam":d_vars["indante"],"marmolre":d_vars["marmol"]}
    orgfam_value = d_vars["indante"]
    if orgfam_value[0] == "No":
        d_vars["indante"] = "No"
    elif orgfam_value[0] == "Other organs":
        d_vars["indante"] = "Unknown"
    else:
        d_vars["indante"] = "Yes"

    marmolre_value = d_vars["marmol"]
    if marmolre_value != "No":
        d_vars["marmol"] = "Yes"
    
    return d_vars,list(d_vars.values()),d_vars_info

def check_input(input):
    keys_order_prior = ["Cancer_stage","Histology","marmol","Gender","PDL1","Smoking_habit","indante"]
    keys_dict = list(input.keys())
    datasetRute = parentdir+"/datasets"
    df = pd.read_csv(datasetRute+"/UpdateData_Processed_English.csv",index_col=[0])
    dict_return = deepcopy(dv.vars_dicc_english)
    found = True
    for i,v in enumerate(keys_order_prior):
        options = list(df.groupby(v).groups.keys())
        if input[v] in options:
            df = df[df[v] == input[v]]
        else:
            found = False
    if found == True:
        return found, dict_return
    for i,v in enumerate(keys_order_prior):
        options = list(df.groupby(v).groups.keys())
        if v == "indante":
            if "Yes" not in options:
                dict_return[list(dict_return.keys())[keys_dict.index(v)]] = ["No","Other organs"]
            if "No" not in options:
                dict_return[list(dict_return.keys())[keys_dict.index(v)]].remove("No")
            if "Unknown" not in options:
                dict_return[list(dict_return.keys())[keys_dict.index(v)]].remove("Other organs")
        elif v == "marmol":
            if "No" not in options:
                dict_return[list(dict_return.keys())[keys_dict.index(v)]].remove("No")
            elif "Yes" not in options:
                dict_return[list(dict_return.keys())[keys_dict.index(v)]] = ["No"]
        else:
            if v == "PDL1":
                options = [op[5:] for op in options]
            dict_return[list(dict_return.keys())[keys_dict.index(v)]] = options
    return found, dict_return
            
def getItems(df,key):
    l_return = []
    if key == "orgfam":
        dicc = dv.organ_familiar
    else:
        dicc = dv.molecular_markers_result
    for index, row in df.iterrows():
        item = eval(row[key])
        for elem in item:
            if "No" in elem:
                elem = "No"
            elif "Unkown" in elem:
                elem = "Unkown"
            if elem not in l_return:
                l_return.append(elem)
    return l_return

def getValues(l_vars):

    estadio_patient = l_vars[3]

    datasetRute = parentdir+"/datasets"
    total_patients = pd.read_csv(datasetRute+"/UpdateData_Processed_English.csv") # Load all the patients.

    df_estadio_patient = total_patients[total_patients["Cancer_stage"]==estadio_patient] # Only need patients with the same stage lung cancer as input.

    combinations_features = df_estadio_patient.groupby(["Gender","Smoking_habit","indante","Histology","marmol","PDL1"]).size().sort_values(ascending=False)
    data, index_profile = create_plots.createColorsFeatures(combinations_features,l_vars) # Function that will assign colors for the labels that will be included in barh graph.
    graph_general = {'Profiles':list(data.index),"Count":(data.values).tolist(),"Index_to_color":index_profile}
    graph_tox, graph_prog, graph_more_tox, graph_more_prog = create_plots.create_plots_info_dataset(l_vars,total_patients) # Function that will generate barh Treatments vs Tox or Prog graph and pie charts with specific information about tox and prog.
    
    return graph_general,graph_tox, graph_prog, graph_more_tox, graph_more_prog

# Function that will ask for graphs and patterns.
def createGraphs_patterns(request_data):
    data = json.loads(request_data) # Load data
    
    graph_general,graph_tox, graph_prog, graph_more_tox, graph_more_prog = getValues(data[1]) # Function that will generate graphs
    records_tox, records_prog, cols_tox, cols_prog = generate_sankey.getSankey(data[1],data[2])
    data[0].pop("orgfam",None)
    data[0]["marmolre"] = data[2]["marmolre"]
    sg = search_sg.search(data[0])
    # Return 201 HTTP response that also returns corresponding URIs to the graphs generated and patterns found.
    return {'data_chart_profiles':graph_general,'data_chart_toxicities_in_treatments':graph_tox,
            'data_chart_progression_in_treatments':graph_prog, 'data_chart_toxicities_details':graph_more_tox,
            'data_chart_progression_details':graph_more_prog,'sankey_tox_records':records_tox,'sankey_prog_records':records_prog,
            'sankey_tox_cols':cols_tox, 'sankey_prog_cols':cols_prog, 'total_groups':sg},201


if __name__ == '__main__':
    found, d = check_input({'Gender': 'Male', 'Smoking_habit': 'Ex smoker(>1 year)', 'indante': 'Yes', 'Cancer_stage': 'IV', 'Histology': 'Adenocarcinoma', 'marmol': 'ALK gene/Immunohistochemistry/Positive', 'PDL1': 'PDL1_Unknown'})
    
    print(found)