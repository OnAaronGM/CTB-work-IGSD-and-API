import pandas as pd
import numpy as np

# Assign colors for the 30 most frequent profiles in dataset using stage lung cancer as primary key.
# It will include the given profile even if it is not a frequent profile.
# Red -> Given profile. Blue -> Frequent profiles.
def createColorsFeatures(data,l_vars):
    c = data.to_frame(name = "count").reset_index()
    reqd_Index = list(np.where((c["Gender"] == l_vars[0]) & (c["Smoking_habit"] == l_vars[1]) & (c["indante"] == l_vars[2])
            & (c["Histology"] == l_vars[4]) & (c["marmol"] == l_vars[5]) & (c["PDL1"] == l_vars[6]) ))[0][0]
    if reqd_Index < 30:
        return data[:30], int(reqd_Index)
    return data[:29].append(data[reqd_Index:reqd_Index+1]),30


def circle_graph_tox(df_treat,name_treat):
    si_tox = df_treat[df_treat["ToxBin"] == "YesTox"]
    dict_tox = {}
    for row in si_tox.itertuples():
        list_tox = eval(getattr(row, 'Tox'))
        if "[" in list_tox[0]:
            list_tox = eval(list_tox[0])
        for tox in list_tox:
            if tox not in dict_tox.keys():
                dict_tox[tox] = 1
            else:
                dict_tox[tox] += 1

    group_names = list(dict_tox.keys())
    group_values = list(dict_tox.values())
    count_treat = sum(group_values)
    
    return_dict = {'Treatment':name_treat,'Treatment_Count':count_treat,'Toxicities_list':group_names,'Toxicities_list_count':group_values}
    
    return return_dict


def circle_graph_prog(df_treat,name_treat):
    si_prog = df_treat[(df_treat["Prog_Rec"] == "Progression") | (df_treat["Prog_Rec"] == "Relapse")]

    group_names = ["Progression","Relapse"]
    list_names = []
    group_values = []
    group_tipo = []
    group_values_tipo = []
    group_terapia = []
    group_values_terapia = []

    list_prog = [{} for elem in group_names]
    for _,row in si_prog.iterrows():        
        pr = row["Prog_Rec"]
        tipo = row["Prog_type"]
        terapia = row["Prog_ther"]
        if pr == "Progression":
            if tipo not in list_prog[0].keys(): ## el formato es {tipoprog1:[cantidad,{terapia1:..,terapia2:..}]}
                list_prog[0][tipo] = [1,{terapia:1}]               
            else:
                list_prog[0][tipo][0] += 1
                if terapia not in list_prog[0][tipo][1].keys():
                    list_prog[0][tipo][1][terapia] = 1
                else:
                    list_prog[0][tipo][1][terapia] += 1
        else:
            if tipo not in list_prog[1].keys(): ## el formato es {tipoprog1:[cantidad,{terapia1:..,terapia2:..}]}
                list_prog[1][tipo] = [1,{terapia:1}]
            else:
                list_prog[1][tipo][0] += 1
                if terapia not in list_prog[1][tipo][1].keys():
                    list_prog[1][tipo][1][terapia] = 1
                else:
                    list_prog[1][tipo][1][terapia] += 1
        
    for index,val in enumerate(list_prog):
        if val:
            list_names.append(group_names[index]) ## Lista de labels progresion o recaida
            value = 0
            values_lists = val.values()
            total = sum(int(l[0]) for l in values_lists)## Obtenemos la suma de los tipoProg de Progresion o recaida para saber nº de progresiones/recaidas
            group_values.append(total) ## Lista de cantidad de progresion/recaida
            k1 = 1
            for key, value in val.items() :
                if index == 0:
                    group_tipo.append("ProgressionType"+str(k1)+": "+key) ##Lista de labels de tipoprog de cada label prog/recaida
                else:
                    group_tipo.append("RelapseType"+str(k1)+": "+key) ##Lista de labels de tipoprog de cada label prog/recaida
                group_values_tipo.append(value[0]) ##Lista de valores de cada tipoprog de cada label prog/recaida
                k2 = 1
                for key2, value2 in value[1].items():
                    if index == 0:
                        #group_terapia.append("ProgressionTherapy"+str(k1)+"."+str(k2)+": "+key2)
                        group_terapia.append("ProgressionType"+str(k1)+"Therapy"+str(k2)+": "+key2)
                    else:
                        #group_terapia.append("RelapseTherapy"+str(k1)+"."+str(k2)+": "+key2)
                        group_terapia.append("ProgressionType"+str(k1)+"Therapy"+str(k2)+": "+key2)
                    group_values_terapia.append(value2)
                    k2 += 1
                k1 += 1

        index += 1

    return_dict = {'Treatment':name_treat,'Category_list':list_names,'Category_list_count':group_values,
                   'Progression_type_list':group_tipo,"Progression_type_list_count":group_values_tipo,
                   'Progression_therapy_list':group_terapia,"Progression_therapy_list_count":group_values_terapia}
    return return_dict

def create_plots_info_dataset(l_vars,total_patients):
    graph_more_tox = []
    graph_more_prog = []
    test = total_patients[(total_patients["Gender"] == l_vars[0]) & (total_patients["Smoking_habit"] == l_vars[1]) & 
                            (total_patients["indante"] == l_vars[2]) & (total_patients["Cancer_stage"] == l_vars[3]) & (total_patients["Histology"] == l_vars[4]) & 
                            (total_patients["marmol"] == l_vars[5]) & (total_patients["PDL1"] == l_vars[6]) ].reset_index(drop=True)                    
    com_filtro = test.groupby(["FirstTreatment"]).size().sort_values(ascending=False)
    com_filtro = com_filtro.to_frame().reset_index()

    dict_Tox = {"Trat":[],"YesTox":[],"NoTox":[],"Unknown":[]}
    dict_prog = {"Trat":[],"Progression":[],"Relapse":[],"No progression/relapse":[]}
    for _,row in com_filtro.iterrows():
        ## Toxicity graph
        dict_Tox["Trat"].append(row["FirstTreatment"])
        df_treat = test[test["FirstTreatment"] == row["FirstTreatment"]].reset_index(drop=True)
        si_Tox = 0
        no_Tox = 0
        desc_Tox = 0

        tox_filtro = df_treat.groupby(["ToxBin"]).size().sort_values(ascending=False)
        tox_filtro = tox_filtro.to_frame().reset_index()
        if "NoTox" in tox_filtro.ToxBin.values:
            no_Tox = tox_filtro[tox_filtro["ToxBin"] == "NoTox"].reset_index(drop=True)[0][0]
        if "YesTox" in tox_filtro.ToxBin.values:
            si_Tox = tox_filtro[tox_filtro["ToxBin"] == "YesTox"].reset_index(drop=True)[0][0]
        if "Unknown" in tox_filtro.ToxBin.values:
            desc_Tox = tox_filtro[tox_filtro["ToxBin"] == "Unknown"].reset_index(drop=True)[0][0]
        dict_Tox["YesTox"].append(si_Tox)
        dict_Tox["NoTox"].append(no_Tox)
        dict_Tox["Unknown"].append(desc_Tox)
        if si_Tox != 0:
            graph_more_tox.append(circle_graph_tox(df_treat,row["FirstTreatment"]))

        ## Progression graph
        dict_prog["Trat"].append(row["FirstTreatment"])
        progre, rec, noprog = 0, 0, 0
        prog_filtro = df_treat.groupby(["Prog_Rec"]).size().sort_values(ascending=False)
        
        prog_filtro = prog_filtro.to_frame().reset_index()
        if "Progression" in prog_filtro.Prog_Rec.values:
            progre = prog_filtro[prog_filtro["Prog_Rec"] == "Progression"].reset_index(drop=True)[0][0]
        if "Relapse" in prog_filtro.Prog_Rec.values:
            rec = prog_filtro[prog_filtro["Prog_Rec"] == "Relapse"].reset_index(drop=True)[0][0]
        if "No progression/relapse" in prog_filtro.Prog_Rec.values:
            noprog = prog_filtro[prog_filtro["Prog_Rec"] == "No progression/relapse"].reset_index(drop=True)[0][0]
        
        dict_prog["Progression"].append(progre)
        dict_prog["Relapse"].append(rec)
        dict_prog["No progression/relapse"].append(noprog)
        if progre != 0 or rec != 0:
            graph_more_prog.append(circle_graph_prog(df_treat,row["FirstTreatment"]))

    df_tox = pd.DataFrame(dict_Tox)
    df_prog = pd.DataFrame(dict_prog)
    
    graph_tox = {'Treatments':list(df_tox["Trat"]),'YesTox_count':list(df_tox["YesTox"]),'NoTox_count':list(df_tox["NoTox"]),'Unknown_count':list(df_tox["Unknown"])}
    graph_prog = {'Treatments':list(df_prog["Trat"]),'Progression_count':list(df_prog["Progression"]),'Relapse_count':list(df_prog["Relapse"]),'No progression/relapse_count':list(df_prog["No progression/relapse"])}

    return graph_tox, graph_prog, graph_more_tox, graph_more_prog


    