# IGSD - Information Gained Subgroup Discovery Algorithm

This repository contains the implementation of IGSD: A new algorithm for Subgroup Set Discovery based on Information Gained, it contains:

1. pysubgroup_mod: The project code.
2. results: Directory in which the algortihm will store the results produced.
3. datasets: Directory in which datasets to be used in the algortihm are stored.


# 1. IGSD Project Scripts
Inside the folder pysubgroup_mod you can find the scripts of IGSD and other useful scripts.
Moreover, main.py is the principal script in charge of executing the main approach.

# 2. Execution commands
The main.py file required several arguments to be used, so the following command line will execute the python file:



```python3 main.py --dataname <FILE> --class_column <CLASS_COLUMN> --class_value <CLASS_VALUE> --mode <MODE> --depth <DEPTH> --list_ignore <LIST_IGNORE> --list_conds <LIST_CONDS>```


With:
* ```<FILE>```: The name of the dataset input file.
* ```<CLASS_COLUMN>```: The attribute (column) used as target (studied class).
* ```<CLASS_VALUE>```: The value of <CLASS_COLUMN> that we want to analize.
* ```<MODE>```: The mode that IGSD will employ to perfom the analysis when IG threshold is calculated (dynamic, maximum). If you want to employ another algorithm, the default value is used.
* ```<DEPTH>```: The number of attributes that the algortihms will consider.
* ```<LIST_IGNORE>```: A list with the attributes (columns) of the dataset that the user does not want to be consider in the anaylis.
* ```<LIST_CONDS>```: A list with the attributes (columns) of the dataset that the user wants to be present in the patterns obtained.

