# IGSD - Information Gained Subgroup Discovery Algorithm

This repository contains the implementation of IGSD: A new algorithm for Subgroup Set Discovery based on Information Gained. Some works where IGSD was used are:
* Subgroup discovery analysis of treatments patterns in lung cancer patients. Daniel Gómez Bravo, Aaron García, Guillermo Vigueras, Belén Ríos-Sánchez, Belén        Otero, Roberto Hernández, María Torrente, Ernestina Menasalvas, Mariano Provencio, Alejandro Rodríguez González. July 2022, IEEE 35th International Symposium on   Computer-Based Medical Systems (CBMS).
* Clustering-based Pattern Discovery in Lung Cancer Treatments. Daniel Gómez-Bravo, Aaron García, Guillermo Vigueras, Belén Ríos-Sánchez, Alejandra Pérez-García,    Vanessa Ospina, María Torrente, Ernestina Menasalvas, Mariano Provencio, Alejandro Rodríguez González. June 2023, IEEE 36th International Symposium on Computer-Based Medical Systems (CBMS).
* Information Gained Subgroup Discovery. Daniel Gómez-Bravo, Aaron García, Guillermo  Vigueras, Belén Ríos-Sánchez, Mariano Provencio, Alejandro Rodríguez           González. July 2023, Preprint.
* Subgroup Discovery Analysis of Treatment Patterns in Lung Cancer Patients. Daniel Gómez Bravo, Aaron García, Guillermo Vigueras, Belén Ríos-Sánchez, Alejandra     Pérez-García, Vanessa Ospina, María Torrente, Ernestina Menasalvas, Mariano Provencio, Alejandro Rodríguez González October 2023. Preprint.

Moreover, the structure of the repository is at follows:

1. pysubgroup_mod: The project code.
2. results: Directory in which the algorithm will store the results produced.
3. datasets: Directory in which datasets for use in the algorithm are stored.

# 1. IGSD Project Scripts
Inside the folder pysubgroup_mod, you can find the scripts of IGSD and other useful scripts.
Additionally, main.py is the main script responsible for executing the main approach.

# 2. Execution commands
The main.py file required several arguments to be used, so the following command line will execute the python file:



```python3 main.py --dataname <FILE> --class_column <CLASS_COLUMN> --class_value <CLASS_VALUE> --mode <MODE> --depth <DEPTH> --list_ignore <LIST_IGNORE> --list_conds <LIST_CONDS>```


With:
* ```<FILE>```: The name of the dataset input file.
* ```<CLASS_COLUMN>```: The attribute (column) used as target (studied class).
* ```<CLASS_VALUE>```: The value of <CLASS_COLUMN> that we want to analize.
* ```<MODE>```: The mode that IGSD will employ to perform the analysis when IG threshold is calculated (dynamic, maximum). If you want to use another algorithm, the default value is used.
* ```<DEPTH>```: The number of attributes considered during the execution.
* ```<LIST_IGNORE>```: A list with the attributes (columns) of the dataset that the user does not want to be considered in the analysis.
* ```<LIST_CONDS>```: A list with the attributes (columns) of the dataset that the user wants to be present in the patterns obtained.


