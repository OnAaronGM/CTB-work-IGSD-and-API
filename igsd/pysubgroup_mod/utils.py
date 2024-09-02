'''
Created on 02.05.2016

@author: lemmerfn
'''
import itertools
from functools import partial
from heapq import heappush, heappop
from collections.abc import Iterable
import math
import numpy as np
import pandas as pd
import pysubgroup_mod as ps
from math import sqrt

## Added
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
    p3 = 0
    if a != 0:
        p3 = b / a
    return calculate_entriopia(p1) - (x1)*calculate_entriopia(p2) - (x2)*calculate_entriopia(p3)

def calculate_odd_value(ID,IS,PD,PS):
    b = IS - PS
    c = PD - PS
    d = (ID - PD) - b
    if b == 0 or c == 0 or d == 0:
        odd_value = 100
    else:
        odd_value = (PS*d) / (b*c)
    return odd_value

def threshold(info_list,depth,mode):
    if len(np.unique(info_list)) == 1:
        return list(info_list)[0]
    n = len(info_list)
    c1 = np.sum(np.square(info_list))
    c2 = np.sum(info_list)
    a = n*c1
    b = c2**2
    c = n*(n-1)
    
    s = sqrt((a-b)/c)
    if depth > 0: # Parameter used to check if algorithm is in the first iteration (Beams: length == 1).
        if mode == 1: ## Parameter used to check if user wants dynamic threshold or max value.
            s = max(info_list)
        else:
            s = max(info_list) - s
    return s

def calculate_threshold(l1,l2,depth,mode):
    if len(l1) == 0:
        thr = threshold([elem[3][-1] for elem in l2],depth,mode)
        return [elem for elem in l2 if elem[3][-1] >= thr]
    thr = threshold([elem[3][-1] for elem in l1],depth,mode)
    return [elem for elem in l1 if elem[3][-1] >= thr]

def best_complex(elem,mode,filter_vars):
    #OR: <1.68, 1.68 - 3.47, 3.47 - 6.71, >6.71
    #l_quali, sg, l_stats, l_info, l_odd, idx
    
    ## Nos quedamos con las etiquetas de los items del grupo. Ej: "estadioini==IV" -> "estadioini"
    group_labels = [item.attribute_name for item in elem[1]._selectors]
    lenghts = [i for i in range(1,len(group_labels)+1)]
    selectors = list(elem[1]._selectors)
    odd_list = [(4,odd) if odd > 6.71 else (3,odd) if 3.47 < odd <= 6.71 else (2,odd) if 1.68 < odd <= 3.47 else (1,odd) for odd in elem[4]]

    l3 = [(i,v,g,l,p) for i,v,g,l,p in zip(elem[3],odd_list,group_labels,lenghts,elem[6])]
   
    ## Check si el grupo contiene PrimTratCon & estadioini
    if all(var in group_labels for var in filter_vars):
        l3 = [cand for idx,cand in enumerate(l3[1:],2) if(all(var in group_labels[:idx] for var in filter_vars))]
    ## Calculamos umbral threshold
    thr = threshold([it[0] for it in l3],len(l3),0)
 
    ## Lista con los candidatos a corte por encima del threshold info_gain and pvalue
    x_filter = [cand for cand in l3 if cand[0] >= thr and cand[4] <= 0.05]
    #x_filter = [cand for cand in l3 if cand[0] >= thr]
    if len(x_filter) == 0:
        return None

    if len(x_filter) == 1:
        index = group_labels.index(x_filter[0][2])
        sg = ps.Conjunction(selectors[:index+1],mode)
        tup = (elem[0][index],sg,elem[2][index],elem[3][index],elem[4][index],elem[5],elem[6][index])
        return tup
    return_cand = x_filter[0]
    for idx, cand in enumerate(x_filter[1:],start=1):
        if cand[1][0] > return_cand[1][0]: # If candidate upgrades odd range, it is selected as new return_cand
            return_cand = cand
        elif (cand[1][0] == return_cand[1][0] and cand[3] == x_filter[idx-1][3] + 1):
            return_cand = cand
        else:
            break
        #if return_cand[1][1] == 100:
        """ if return_cand[1][0] == 4: # Also, if return_cand has maximum odd range (odd value > 6.71), algorithm stops and returns return_cand.
            break """
    index = group_labels.index(return_cand[2])
    sg = ps.Conjunction(selectors[:index+1],mode)
    tup = (elem[0][index],sg,elem[2][index],elem[3][index],elem[4][index],elem[5],elem[6][index])
    return tup

#def add_if_required(result, sg, quality, task, check_for_duplicates=False, statistics=None):
def add_if_required(result, sg, quality, task, check_for_duplicates=False, statistics=None):
    if quality > task.min_quality:
        p_value = ps.ChiSquaredQF(stat="p").evaluate(sg, task.target, task.data, statistics) # Calculate pvalue stat.
        
        if not ps.constraints_satisfied(task.constraints, sg, statistics, task.data):
            return
        if check_for_duplicates and (quality, p_value, sg, statistics) in result:
            return
        
        if len(result) < task.result_set_size:
                heappush(result, (quality, p_value, sg, statistics))
        elif quality > result[0][0]:
            heappop(result)
            heappush(result, (quality, p_value, sg, statistics))


def minimum_required_quality(result, task):
    if len(result) < task.result_set_size:
        return task.min_quality
    else:
        return result[0][0]


# Returns the cutpoints for discretization
def equal_frequency_discretization(data, attribute_name, nbins=5, weighting_attribute=None):
    cutpoints = []
    if weighting_attribute is None:
        cleaned_data = data[attribute_name]
        cleaned_data = cleaned_data[~np.isnan(cleaned_data)]
        sorted_data = sorted(cleaned_data)
        number_instances = len(sorted_data)
        for i in range(1, nbins):
            position = i * number_instances // nbins
            while True:
                if position >= number_instances:
                    break
                val = sorted_data[position]
                if val not in cutpoints:
                    break
                position += 1
            # print (sorted_data [position])
            if val not in cutpoints:
                cutpoints.append(val)
    else:
        cleaned_data = data[[attribute_name, weighting_attribute]]
        cleaned_data = cleaned_data[~np.isnan(cleaned_data[attribute_name])]
        cleaned_data.sort(order=attribute_name)

        overall_weights = cleaned_data[weighting_attribute].sum()
        remaining_weights = overall_weights
        bin_size = overall_weights / nbins
        sum_of_weights = 0
        for row in cleaned_data:
            sum_of_weights += row[weighting_attribute]
            if sum_of_weights > bin_size:
                if not row[attribute_name] in cutpoints:
                    cutpoints.append(row[attribute_name])
                    remaining_weights = remaining_weights - sum_of_weights
                    if remaining_weights < 1.5 * (bin_size):
                        break
                    sum_of_weights = 0
    return cutpoints


def conditional_invert(val, invert):
    return - 2 * (invert - 0.5) * val


def results_df_autoround(df):
    return df.round({
        'quality': 3,
        'size_sg': 0,
        'size_dataset': 0,
        'positives_sg': 0,
        'positives_dataset': 0,
        'size_complement': 0,
        'relative_size_sg': 3,
        'relative_size_complement': 3,
        'coverage_sg': 3,
        'coverage_complement': 3,
        'target_share_sg': 3,
        'target_share_complement': 3,
        'target_share_dataset': 3,
        'lift': 3,

        'size_sg_weighted': 1,
        'size_dataset_weighted': 1,
        'positives_sg_weighted': 1,
        'positives_dataset_weighted': 1,
        'size_complement_weighted': 1,
        'relative_size_sg_weighted': 3,
        'relative_size_complement_weighted': 3,
        'coverage_sg_weighted': 3,
        'coverage_complement_weighted': 3,
        'target_share_sg_weighted': 3,
        'target_share_complement_weighted': 3,
        'target_share_dataset_weighted': 3,
        'lift_weighted': 3})


def perc_formatter(x):
    return "{0:.1f}%".format(x * 100)


def float_formatter(x, digits=2):
    return ("{0:." + str(digits) + "f}").format(x)


def is_categorical_attribute(data, attribute_name):
    return attribute_name in data.select_dtypes(exclude=['number']).columns.values


def is_numerical_attribute(data, attribute_name):
    return attribute_name in data.select_dtypes(include=['number']).columns.values


def remove_selectors_with_attributes(selector_list, attribute_list):
    return [x for x in selector_list if x.attributeName not in attribute_list]


def effective_sample_size(weights):
    return sum(weights) ** 2 / sum(weights ** 2)


# from https://docs.python.org/3/library/itertools.html#recipes
def powerset(iterable, max_length=None):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    if max_length is None:
        max_length = len(s)
    if max_length < len(s):
        max_length = len(s)
    return itertools.chain.from_iterable(itertools.combinations(s, r) for r in range(max_length))


def overlap(sg, another_sg, data):
    cover_sg = sg.covers(data)
    cover_another_sg = another_sg.covers(data)
    union = np.logical_or(cover_sg, cover_another_sg)
    intercept = np.logical_and(cover_sg, cover_another_sg)
    sim = np.sum(intercept) / np.sum(union)
    return sim


#####
# bitset operations
#####
def to_bits(list_of_ints):
    v = 0
    for x in list_of_ints:
        v += 1 << x
    return v


def count_bits(bitset_as_int):
    c = 0
    while bitset_as_int > 0:
        c += 1
        bitset_as_int &= bitset_as_int - 1
    return c


def find_set_bits(bitset_as_int):
    while bitset_as_int > 0:
        x = bitset_as_int.bit_length() - 1
        yield x
        bitset_as_int = bitset_as_int - (1 << x)


#####
# TID-list operations
#####
def intersect_of_ordered_list(list_1, list_2):
    result = []
    i = 0
    j = 0
    while i < len(list_1) and j < len(list_2):
        if list_1[i] < list_2[j]:
            i += 1
        elif list_2[j] < list_1[i]:
            j += 1
        else:
            result.append(list_1[i])
            j += 1
            i += 1
    return result


class SubgroupDiscoveryResult:
    def __init__(self, results, task):
        self.task = task
        self.results = results
        assert isinstance(results, Iterable)

    def to_descriptions(self):
        return [(qual, sgd) for qual, sgd, stats in self.results]

    def to_table(self, statistics_to_show=None, print_header=True, include_target=False, mode=2):
        if statistics_to_show is None:
            statistics_to_show = type(self.task.target).statistic_types
        table = []
        if print_header:
            row = ["quality", "subgroup"]
            for stat in statistics_to_show:
                row.append(stat)
            if mode != 2:
                row.append("pvalue")
            table.append(row)
        if mode !=2:
            for (q, sg, stats,_,_,_,p_value) in self.results:
                stats = self.task.target.calculate_statistics(sg, self.task.data, stats)
                row = [str(q), str(sg)]
                if include_target:
                    row.append(str(self.task.target))
                for stat in statistics_to_show:
                    row.append(str(stats[stat]))
                row.append(str(p_value))
                table.append(row)
        else:
            for (q, _ ,sg, stats) in self.results:
                stats = self.task.target.calculate_statistics(sg, self.task.data, stats)
                row = [str(q), str(sg)]
                if include_target:
                    row.append(str(self.task.target))
                for stat in statistics_to_show:
                    row.append(str(stats[stat]))
                table.append(row)
        return table

    def to_dataframe(self, statistics_to_show=None, autoround=False, include_target=False, mode=2):
        if statistics_to_show is None:
            statistics_to_show = type(self.task.target).statistic_types
        res = self.to_table(statistics_to_show, True, include_target, mode)
        headers = res.pop(0)
        df = pd.DataFrame(res, columns=headers, dtype=np.float64)
        if autoround:
            df = results_df_autoround(df)
        return df

    def to_latex(self, statistics_to_show=None):
        if statistics_to_show is None:
            statistics_to_show = type(self.task.target).statistic_types
        df = self.to_dataframe(statistics_to_show)
        latex = df.to_latex(index=False, col_space=10, formatters={
            'quality': partial(float_formatter, digits=3),
            'size_sg': partial(float_formatter, digits=0),
            'size_dataset': partial(float_formatter, digits=0),
            'positives_sg': partial(float_formatter, digits=0),
            'positives_dataset': partial(float_formatter, digits=0),
            'size_complement': partial(float_formatter, digits=0),
            'relative_size_sg': perc_formatter,
            'relative_size_complement': perc_formatter,
            'coverage_sg': perc_formatter,
            'coverage_complement': perc_formatter,
            'target_share_sg': perc_formatter,
            'target_share_complement': perc_formatter,
            'target_share_dataset': perc_formatter,
            'lift': partial(float_formatter, digits=1)})
        latex = latex.replace(' AND ', r' $\wedge$ ')
        return latex
