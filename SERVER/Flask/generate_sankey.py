import os, sys
import pandas as pd
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)


datasetRute = parentdir + "/datasets"

def getSankey(l_vars, d_vars_info):
    orgfam_info = str(d_vars_info["orgfam"]).replace("'", "")
    marmol_info = str(d_vars_info["marmolre"]).replace("'", "")
    l_vars.append(marmol_info)
    l_vars.append(orgfam_info)

    total_patients = pd.read_csv(datasetRute + "/df_final_ATC.csv", index_col=0)

    mypatient = total_patients[(total_patients["sexo"] == l_vars[0]) &
                               (total_patients["habitotab"] == l_vars[1]) &
                               (total_patients["indante"] == l_vars[2]) & (
                                       total_patients["estadioini"] == l_vars[3]) & (
                                       total_patients["hist"] == l_vars[4]) & (
                                       total_patients["marmol"] == l_vars[5]) & (
                                       total_patients["PDL1"] == l_vars[6])]
    mypatient_input = mypatient
    mypatient_input_tox = mypatient_input.groupby(
        ['sexo', 'habitotab', 'indante', 'Cluster', 'estadioini', 'hist', 'marmolre', 'PDL1', 'orgfam', 'PrimTratCon',
         'ToxBin', 'Tox']).agg('count')
    mypatient_input_progrec = mypatient_input.groupby(
        ['sexo', 'habitotab', 'indante', 'Cluster', 'estadioini', 'hist', 'marmolre', 'PDL1', 'orgfam', 'PrimTratCon',
         'Prog_Rec']).agg('count')

    records_tox, cols_tox = inputToPlot(mypatient_input_tox, l_vars, 'ToxBin')
    records_prog, cols_prog = inputToPlot(mypatient_input_progrec, l_vars, 'Prog_Rec')

    return records_tox, records_prog, cols_tox, cols_prog


def genSankeyGraph(df, l_vars, cat_cols=[], value_cols=''):

    # maximum of 6 value cols -> 6 colors

    labelList = []
    colorNumList = []
    for catCol in cat_cols:
        labelListTemp = list(set(df[catCol].values))
        colorNumList.append(len(labelListTemp))
        labelList = labelList + labelListTemp
    # remove duplicates from labelList
    labelList = list(dict.fromkeys(labelList))
    newLabelList = []
    newList = []
    for i in labelList:
        temp = i
        newList = []
        if "[" in i:
            temp = eval(i)
            if len(temp) > 1:
                for i, j in enumerate(temp):
                    newList.append('<br>' + j)
                temp = str(newList).replace("'", "").replace("[", "").replace("]", "").replace('"', "")
        newLabelList.append(temp)

    # transform df into a source-target pair
    for i in range(len(cat_cols) - 1):
        if i == 0:
            sourceTargetDf = df[[cat_cols[i], cat_cols[i + 1], value_cols]]
            sourceTargetDf.columns = ['Origen', 'Objetivo', 'Total']
        else:
            tempDf = df[[cat_cols[i], cat_cols[i + 1], value_cols]]
            tempDf.columns = ['Origen', 'Objetivo', 'Total']
            sourceTargetDf = pd.concat([sourceTargetDf, tempDf])
        sourceTargetDf = sourceTargetDf.groupby(['Origen', 'Objetivo']).agg({'Total': 'sum'}).reset_index()
    # add index for source-target pair
    sourceTargetDf['sourceID'] = sourceTargetDf['Origen'].apply(lambda x: labelList.index(x))
    sourceTargetDf['targetID'] = sourceTargetDf['Objetivo'].apply(lambda x: labelList.index(x))

    tuperfil = []
    clusters_list = df.groupby(['Cluster']).size().sort_values(ascending=False).index.to_list()
  
    # Remove cluster labels
    complete_clusters = []
    for cluster in clusters_list:
        complete_clusters.append('Cluster' + str(cluster))
    for complete in complete_clusters:
        sourceTargetDf['Origen'] = sourceTargetDf['Origen'].str.replace(complete, '')
        sourceTargetDf['Objetivo'] = sourceTargetDf['Objetivo'].str.replace(complete, '')
        for counter, elem in enumerate(newLabelList):
            if complete in elem:
                newLabelList[counter] = str(elem).replace('<br>' + complete + ',', '')

    # creating the sankey diagram
    data = dict(
        node=dict(
            label=newLabelList
        ),
        link=dict(
            source=sourceTargetDf['sourceID'],
            target=sourceTargetDf['targetID'],
            value=sourceTargetDf['Total']
        )
    )
    labels = data["node"]["label"]
    labels = [str(elem).replace(' <br>',"").replace(',',', ').replace("'","") for elem in labels]
    source_id = list(data["link"]["source"])
    target_id = list(data["link"]["target"])
    values = list(data["link"]["value"])
    records = []
    print(labels)
    print(sourceTargetDf)
    exit(0)
    for i, elem in enumerate(source_id):
        color = 0 ## Different color for path joining source and target label
        origen = ""
        for st in labels[elem].split(", "):
            st += ",\n"
            origen += st
        origen = origen[:-2]
        destino = ""
        input_organs = l_vars[8][1:-1].split(", ")
        list_items_destino = labels[target_id[i]].split(", ")
        if any(item in list_items_destino for item in input_organs) or l_vars[7] in list_items_destino:
            color = 1 ## Same color for path joining source and target label
        for st in labels[target_id[i]].split(", "):
            st += ",\n"
            destino += st
        destino = destino[:-2]
        weight = values[i]
        if origen == "Input profile" or destino == l_vars[6] or destino == l_vars[7] or destino in l_vars[8]:
            color = 1 ## Same color for path joining source and target label
        t = (elem,origen,target_id[i],destino,weight,color)
        records.append(t)
    # print(records)
    # exit(0)
    return records



def inputToPlot(mypatient_input, l_vars, target):
    mypatient_input = mypatient_input.reset_index()
    mypatient_input = mypatient_input.rename(columns={'marmol': 'Count'})
    mypatient_input = mypatient_input.loc[:, :'Count']
    clusters = mypatient_input.groupby(['Cluster']).size().sort_values(ascending=False).to_frame().rename(
        columns={0: "Count"})
    clusters = clusters.index
    marmolres = {}
    orgfams = {}
    primtratcons = {}
    for j in clusters:
        for i in mypatient_input.iterrows():
            patient = i[1].to_list()
            if patient[3] == j:
                curmarmolre = eval(patient[6])
                if 'No' in curmarmolre:
                    curmarmolre = ['No molecular marker']
                curorgfam = eval(patient[8])
                curprimtratcon = patient[9]
                if j not in marmolres.keys():
                    marmolres[j] = ['Cluster' + str(j)] + curmarmolre
                    orgfams[j] = ['Cluster' + str(j)] + curorgfam
                if j not in primtratcons.keys():
                    primtratcons[j] = ['Cluster' + str(j)] + [curprimtratcon]
                else:
                    for m in curmarmolre:
                        if m not in marmolres[j]:
                            marmolres[j] = marmolres[j] + [m]
                    for m in curorgfam:
                        if m not in orgfams[j]:
                            orgfams[j] = orgfams[j] + [m]
                    if curprimtratcon not in primtratcons[j]:
                        primtratcons[j] = primtratcons[j] + [curprimtratcon]

    def getCommonAndUniqueFeatures(dict_features, name):
        dict_shared = list(set(list(dict_features.values())[0]).intersection(*list(dict_features.values())))
        if not dict_shared:
            dict_shared = 'No common ' + name + ' found'
        if not dict_features:
            dict_features = dict_shared
        for i, j in dict_features.copy().items():
            if len(j) == 1:
                if 'Cluster' in str(j):
                    dict_features[i] = j + dict_shared
        return dict_shared, dict_features

    shared_marmolres, marmolres = getCommonAndUniqueFeatures(marmolres, 'mollecular markers')
    shared_orgfams, orgfams = getCommonAndUniqueFeatures(orgfams, "relatives' organs")
    shared_primtratcons, primtratconsnew = getCommonAndUniqueFeatures(primtratcons, 'primeros tratamientos')

    mypatient_input['CommonMarmol'] = str(shared_marmolres)
    mypatient_input['CommonOrgfam'] = str(shared_orgfams)
    mypatient_input['CommonPrimTratCon'] = str(shared_primtratcons)
    mypatient_input['ClusterMarmol'] = 'NaN'
    mypatient_input['ClusterOrgfam'] = 'NaN'
    mypatient_input['ClusterPrimTratCon'] = 'NaN'
    mypatient_input['ClusterPrimTratConTarget'] = 'NaN'
    mypatient_input['Perfil'] = 'Input profile'

    columns = [15, 16, 17]
    if target == 'ToxBin':
        columns = [16, 17, 18]
    for j in clusters:
        for i in mypatient_input.iterrows():
            patient = i[1].to_list()
            if patient[3] == j:
                mypatient_input.iloc[i[0], columns[0]] = str(marmolres[j])
                mypatient_input.iloc[i[0], columns[1]] = str(orgfams[j])
                mypatient_input.iloc[i[0], columns[2]] = str(primtratconsnew[j])
    if target == 'ToxBin':
        cat_cols = ['Perfil', 'CommonMarmol', 'ClusterMarmol','PDL1', 'CommonOrgfam', 'ClusterOrgfam',
                    'ClusterPrimTratCon', 'PrimTratCon', target, target[:3]]
        return_cols = ['Input Profile', 'Common Mollecular Marker', 'Cluster Mollecular Marker','PDL1', "Common Organs", "Cluster Organs",
                    'Cluster First treatment', 'First treatment', target, "Tox"]
    else:
        cat_cols = ['Perfil', 'CommonMarmol', 'ClusterMarmol','PDL1', 'CommonOrgfam', 'ClusterOrgfam',
                    'ClusterPrimTratCon', 'PrimTratCon', target]
        return_cols = ['Input Profile', 'Common Mollecular Marker', 'Cluster Mollecular Marker','PDL1', "Common Organs", "Cluster Organs",
                    'Cluster First treatment', 'First treatment', target]
        
    records = genSankeyGraph(mypatient_input, l_vars, cat_cols=cat_cols, value_cols='Count')
    return records, return_cols
