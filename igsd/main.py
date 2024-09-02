import os, sys
import pandas as pd
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
sys.path.append(currentdir)
import pysubgroup_mod as ps
import argparse
import numpy as np


def eliminate_reps(elem,l):
    l.remove(elem)
    for li in l:
        if elem in li:
        #if set(elem.split(" AND ")).issubset(li.split(" AND ")):
        #if ', '.join(map(str,elem)) in ', '.join(map(str,li)):
            return False
    return True

def info_gained_algorithm(dataname,class_column,class_value,mode_parameter="default",depth=5,list_ignore=[],list_conds=[]):
    """
    Parameters
    ----------
    dataname: string
        The name of the dataset allocated in the datasets directory to be used for analysis.

    class_column: string
        A column of the dataset that will be used as target.

    class_value: ??
        A value of the class_column. It corresponds to the condition that has to be meet, i.e, class_column==class_Value.

    mode_parameter: string, optional (default=default)
        This parameter controls the behaviour of algorithms search. For InfoGained algorithm, it is necessary to
        use dynamic or maximum options. For other algorithms, the parameter has the value "default".
        (possible values: dynamic, maximum, default)
    
    depth: int, optional (default=5)
        This parameter indicates the number of variables that will be added to rules.

    list_ignore: list of strings, optional (default=None)
        List containing the column names that will not be used in search activity.

    list_conds: list of strings, optional (default=None)
        List containing the column names that are neccesary to appear in rules. It will only work with InfoGained algorithm.
    """
    df = pd.read_csv(currentdir+"/datasets/"+dataname+".csv",index_col=[0])
    if class_column not in df.columns:
        print("No class column")
        exit(0)
    if df[class_column].dtype in [np.int16, np.int32, np.int64]:
        class_value = int(class_value)
    if class_value not in df[class_column].unique():
        print("The class_value specified is not an option")
        exit(0)

    target = ps.BinaryTarget (class_column, class_value)
    searchspace = ps.create_selectors(df, ignore=list_ignore)
    mode_parameter = {'dynamic' : 0, 'maximum': 1, "default":2}[mode_parameter]
    task = ps.SubgroupDiscoveryTask (
        df, 
        target, 
        searchspace,
        mode=mode_parameter, 
        depth=depth,
        filter_vars = list_conds,
        min_quality = 0,
        qf=ps.WRAccQF())
    
    result = ps.BeamSearch().execute(task)
    df_result = result.to_dataframe(mode=mode_parameter)

    # result, result_cut = ps.BeamSearch().execute(task)
    # #df_result = result.to_dataframe()
    # df_result_cut = result_cut.to_dataframe(mode=mode_parameter)

    # df_result_cut.drop_duplicates(inplace=True)
    # df_result_cut.reset_index(drop=True,inplace=True)

    # #df_result = df_result[df_result.apply(lambda row: eliminate_reps(row['subgroup'],list(df_result["subgroup"])), axis=1)]
    # df_result_cut = df_result_cut[df_result_cut.apply(lambda row: eliminate_reps(row['subgroup'],list(df_result_cut["subgroup"])), axis=1)]
    df_result["target"] = [class_value] * df_result.shape[0]
    route = currentdir+"/results/"+dataname+"_"+class_column+"_"+str(class_value)+".csv"
    dir_type = "max"
    if mode_parameter == 0:
        dir_type = "threshold"
    df_result.to_csv(route, encoding="UTF-8",index=True)


if __name__ == "__main__":

    parser=argparse.ArgumentParser()

    parser.add_argument('--dataname', type=str, required=True)
    parser.add_argument('--class_column', type=str, required=True)
    parser.add_argument('--class_value', type=str, required=True)
    parser.add_argument('--mode', type=str, choices=["dynamic","maximum","default"], default="default")
    parser.add_argument('--depth', type=int, required=True)
    parser.add_argument("--list_ignore", nargs="*", type=str, default=[])
    parser.add_argument("--list_conds", nargs="*", type=str, default=[])

    args = parser.parse_args()

    info_gained_algorithm(args.dataname,args.class_column,args.class_value,args.mode,args.depth,args.list_ignore,args.list_conds)