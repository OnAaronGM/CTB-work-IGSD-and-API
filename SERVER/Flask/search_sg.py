import os, sys, re, math
import pandas as pd
from itertools import combinations
from heapq import heappush, heappop
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

target_corresp = {1:"No Prog/Rel No Tox",2:"No Prog/Rel Yes Tox",3:"Yes Prog/Rel No Tox",4:"Yes Prog/Rel Yes Tox",}


def calculate_entriopia(x):
    if x in [0.0,1.0]:
        return 0
    return -x*math.log(x,2) - (1-x)*math.log(1-x,2)


def calculate_info_gained(ID,IS,PD,PS):
    a = ID - IS
    b = PD - PS
    x1 = IS / ID
    x2 = a / ID
    p1 = PD / ID
    p2 = PS / IS
    if a != 0:
        p3 = b / a
    else:
        p3 = 0
    return calculate_entriopia(p1) - (x1)*calculate_entriopia(p2) - (x2)*calculate_entriopia(p3)

def calculate_odd_value(ID,IS,PD,PS):
    b = IS - PS
    c = PD - PS
    d = (ID - PD) - b
    if b == 0 or c == 0 or d == 0:
        odd_value = 100
    else:
        odd_value = (PS*d) / (b*c)
    if odd_value > 6.71:
        return 4
    elif 3.47 < odd_value <= 6.71:
        return 3
    elif 1.68 < odd_value <= 3.47:
        return 2
    return 1


def getRates(row):
    
    """
        NEG: No cumplen target              -> ID - PD
        POS: Si cumplen target              -> PD
        TP: Cumplen ant y target            -> PS
        FP: Cumple ant pero no target       -> IS - PS
        TN: No cumplen ant ni target        -> NEG - FP
        FN: No cumple ant pero si target    -> POS - TP
        FPR = FP / NEG
        TPR = TP / POS
        Acurracy = TP + TN / TP + TN + FP + FN
    """
    newList = row.tolist()
    false_pos = row["size_sg"] - row["positives_sg"]
    true_neg = (row["size_dataset"] - row["positives_dataset"]) - false_pos
    false_neg = row["positives_dataset"] - row["positives_sg"]
    true_pos_rate = row["positives_sg"] / row["positives_dataset"]
    false_pos_rate = (false_pos) / (true_neg + false_pos)

    acc = (row["positives_sg"] + true_neg) / (row["positives_sg"] + true_neg + false_neg + false_pos)

    confidence = row["positives_sg"] / row["size_sg"]

    coverage = row["size_sg"] / row["size_dataset"]

    info_gained = calculate_info_gained(row["size_dataset"],row["size_sg"],row["positives_dataset"],row["positives_sg"])

    odd = calculate_odd_value(row["size_dataset"],row["size_sg"],row["positives_dataset"],row["positives_sg"])
        
    newList[list(row.index).index('TPR')] = true_pos_rate
    newList[list(row.index).index('FPR')] = false_pos_rate
    newList[list(row.index).index('accuracy')] = acc
    newList[list(row.index).index('confidence')] = confidence
    newList[list(row.index).index('coverage')] = coverage
    newList[list(row.index).index('info_gained')] = info_gained
    newList[list(row.index).index('odd')] = odd
    
    return pd.Series(newList, index=row.index)


def filter_with_keys(number_vars,df,keys,d_vars,heap,remaining=0):

    for key in keys:
        df = df[(df['subgroup'].str.contains(key+"=='"+d_vars[key]+"'"))]
        if df.empty:
            return None
    for row in df.itertuples():
        t = (re.sub("\"|\'","",str(getattr(row, 'subgroup'))),target_corresp[getattr(row, 'target')],getattr(row, 'confidence'),(number_vars+1))
        if len(heap) < remaining:
            heappush(heap, t)
        elif t[0] > heap[0][0]:
                heappop(heap)
                heappush(heap, t)

def search(d_vars):
    ## Devolvemos 20 grupos
    datasetRute = parentdir+"/datasets/"
    df = pd.read_csv(datasetRute+"All.csv",index_col=[0])
    df_filter = df[(df['subgroup'].str.contains("Cancer_stage=='"+d_vars["Cancer_stage"]+"'")) & (df['subgroup'].str.contains("FirstTreatment"))]
    df_filter_vars = df_filter.copy()
    d_vars.pop("Cancer_stage")
    keys = list(d_vars.keys())
    remaining = 20
    heap = []
    for i in range(len(keys),0,-1):
        if i < len(keys):
            l_combinations_vars = list(combinations(keys,i))
            for comb in l_combinations_vars:
                filter_with_keys(i,df_filter_vars,comb,d_vars,heap,remaining)
        else:
            filter_with_keys(i,df_filter_vars,keys,d_vars,heap,remaining)

        if len(heap) > 0:
            remaining -= len(heap)
        if remaining == 0:
            return heap
        

def eliminate_reps(elem,l):
    l.remove(elem)
    for li in l:
        if set(elem.split(" AND ")).issubset(li.split(" AND ")):
        #if ', '.join(map(str,elem)) in ', '.join(map(str,li)):
            return False
    return True