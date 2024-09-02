surgery = 'SUR'
chemo   = 'CT'
radio   =  'RT'

dictIniColumns = {surgery: ['feccir1','feccir2', 'feccir3'],
chemo:   ['fecinitto1','fecinitto2', 'fecinitto3', 'fecinitto4', 'fecinitto5', 'fecinitto6', 'fecinitto7', 'fecinitto8'],
radio:   ['fecinirt1', 'fecinirt2', 'fecinirt3', 'fecinirt4']}

dictRespuestaTrat = {chemo:   ['respuestatrat1','respuestatrat2', 'respuestatrat3', 'respuestatrat4', 'respuestatrat5', 'respuestatrat6', 'respuestatrat7', 'respuestatrat8'],
radio:   ['respuestart1', 'respuestart2', 'respuestart3', 'respuestart4']}

dictTraduccionRespuesta = {"-2":"Null","-1":"-","1":"RC","2":"RP","3":"EE","4":"PR","5":"NE","6":"NR"}

dictTrmntPrefixColumns = {surgery: 'feccir',
chemo:   'fecinitto',
radio:   'fecinirt'}

dictFinColumns = {'feccir1'   : 'feccir1',
                  'feccir2'   : 'feccir2',
                 'feccir3'    : 'feccir3',
                 'fecinitto1' : 'fecfintto1',
                 'fecinitto2' : 'fecfintto2',
                 'fecinitto3' : 'fecfintto3',
                 'fecinitto4' : 'fecfintto4',
                 'fecinitto5' : 'fecfintto5',
                 'fecinitto6' : 'fecfintto6',
                 'fecinitto7' : 'fecfintto7',
                 'fecinitto8' : 'fecfintto8',
                 'fecinirt1'  : 'fecfinrt1',
                 'fecinirt2'  : 'fecfinrt2',
                 'fecinirt3'  : 'fecfinrt3',
                 'fecinirt4'  : 'fecfinrt4'
                }

dictTrmntColumns = {surgery: 'tipocir',
chemo:   'tipoterapia',
radio:   'intencion'}


# RT -> intencion
# QT -> tipoterapia1
# CIR -> tipocir1

estadioini = {'-2':'Null','-1':'-','24':'I','1':'IA','25':'IA1','26':'IA2','28':'IA3','2':'IB','27':'II','3':'IIA',
              '4':'IIB','15':'III','5':'IIIA','6':'IIIB','18':'IIIC','7':'IV','20':'IVA','21':'IVB',
              '30':'Limitado','31':'Extendido','888':'Otros'}

# tipoterapia = {'-3':'Null','-1':'-','12':'Hormonal','10':'Inmunoterapia','4':'QT adyuvante','1':'QT intravenosa',
#                  '15':'QT intravenosa+inmunoterapia', '13':'QT intravenosa y oral','3':'QT neoadyuvante',
#                  '14':'QT oral','8':'QT-RT adyuvante','6':'QT-RT concomitante','9':'QT-RT neoadyuvante',
#                  '7':'QT-RT secuencial','2':'Terapia oral dirigida','11':'Otros'}
#
# intencion = {'-3':'Null','-1':'-','2':'Adyuvante','5':'Neoadyuvante','3':'Paliativa','4':'Profiláctica','1':'Radical'}
#
# tipocir = {'-3':'Null','-1':'-','2':'Curativa','1':'Diagnóstica','3':'Paliativa','4':'Rebiopsia'}


tipoterapia = {'-3':'Null','-1':'-','12':'Horm','10':'Imm','4':'Adj','1':'Intrav.',
                 '15':'Intrav+Imm', '13':'Intrav \& Oral','3':'Neoadj',
                 '14':'Oral','8':'CT-RT Adj','6':'CT-RT Conc','9':'CT-RT Neoadj.',
                 '7':'CT-RT Seq','2':'Drugs','11':'Otros'}

intencion = {'-3':'Null','-1':'-','2':'Adj','5':'Neoadj','3':'Pallia','4':'Prophy','1':'Radical'}

tipocir = {'-3':'Null','-1':'-','2':'Curat','1':'Diag','3':'Pallia','4':'Rebiop'}

respuestaMarcador = {"-2":"Null","0":"No","1":"Si"}



    
# Diccionario que traduce los valores obtenidos para las claves de caracteristicas personales 
# Se decidio quitar fam ya que no considero que saber el familiar sirva.

sexo = {"0":"Varón","1":"Mujer"}
habitotab = {"-1":"Error","0":"Nunca Fumador","1":"Ex Fumador","2":"Fumador activo","3":"Desconocido"}
paqanio = {"nan":"Desconocido","NoNan":"Texto"}
indante = {"-1":"Desconocido","0":"No Antec Cancer Fam","1":"Si Antec Cancer Fam"}
numfampul = {"nan":"No Info","NoNan":"Texto"}
numfamotro = {"nan":"No Info","NoNan":"Texto"}
orgfam = {"-1.0":"Ninguno","1.0":"Mama","2.0":"Cabeza y cuello","3.0":"Tumor germinal","4.0":"Sarcoma","5.0":"SNC",
    "6.0":"COD","7.0":"Colon-recto","8.0":"Esófago-Gástrico","9.0":"Páncreas","10.0":"Vesícula","11.0":"Hígado",
    "12.0":"Melanoma","13.0":"Piel no melanoma","14.0":"Vejiga/Vías urinarias","15.0":"Renal","16.0":"Próstata",
    "17.0":"Útero/Cérvix","18.0":"Linfoma","19.0":"Leucemia","20.0":"Pulmón","21.0":"Otros","nan":"Desconocido"}
otroorgfam = {"nan":"No otro órgano fam afectado","NoNan":"Texto"}

#caracteristicas_Personales = {"sexo":sexo,"habitotab":habitotab,"indante":indante,"orgfam":orgfam,"fechaPac":"fechaPac"}
caracteristicas_Personales = {"sexo":sexo,"habitotab":habitotab,"indante":indante,"orgfam":orgfam}
# Diccionario que traduce los valores obtenidos para las claves de caracteristicas diagnostico

histologia_dict = {"-2":"Error","-1":"-","0":"Adenocarcinoma",
                "1":"Adenoescamoso","2":"Escamoso","3":"Carcinoma de células grandes","4":"Sarcomatoide","5":"NOS/Indiferenciado","6":"Carcinoma de célula pequeña (microcítico)",
                "7":"Carcinoma neuroendocrino de célula grande","8":"Tumor carcinoide","9":"Mesotelioma","10":"Timoma","11":"Carcinoma tímico","12":"Otros"}
marmol_dict = {"-2":"Error","0":"No estudio molecular","1":"Si estudio molecular"}
marmolre_dict = {"1":"EGFR","2":"ALK","3":"PDL1"}
egfrresultado_dict = {"0":"Negativo","1":"T790M +","2":"T790M -","3":"Exón 19","4":"Exón 21","5":"NOS","6":"Otros"}
indcomor_dict = {"0":"No existen comorbilidades","1":"Asma","2":"Cardiopatía","3":"Diabetes Mellitus (DM)","4":"Dislipemia","5":"EPOC","6":"Alcoholismo/Ex_Alcoholis","7":"Hepatitis","8":"Hipercolesterolemia","9":"Hipertensión (HTA)","10":"Nefropatía",
            "11":"Obesidad","12":"Síndrome depresivo/Ansiedad","13":"Tuberculosis","14":"Vasculopatía","15":"Otra","16":"Hepatopatía","17":"Enfermedad Gastrointest","18":"Enfermedad Neurodegenerativa","19":"Hiperplasia Benigna de Próstata (HBP)","20":"Síndrome de Apnea Obstructiva del Sueño"}
otrascomor_dict = {"nan":"No-info otrascomor","NoNan":"Texto"}
alkresultado_dict = {"1":"IHQ negativo","2":"IHQ positivo","3":"FISH traslocado","4":"FISH no traslocado","5":"RNA se detecta","6":"RNA no se detecta"}
pdl1resultado_dict = {"nan":"Error","-1.0":"Desconocido","0.0":"Negativo","1.0":"Positivo"}
positividad_dict = {"nan":"No-info Positividad","NoNan":"Texto"}

# caracteristicas_Diagnostico = {"estadioini":estadioini,"histologia":histologia_dict,"marmol":marmol_dict,
# "marmolre": marmolre_dict,"egfrresultado":egfrresultado_dict,"indcomor":indcomor_dict,"alkresultado":alkresultado_dict,
# "pdl1resultado":pdl1resultado_dict,"positividad":positividad_dict}

caracteristicas_Diagnostico_v2 = {"estadioini":["estadioini"],"hist":["histologia"],"comor":["comorbilidades"],"marmolre":["marmol"]}
""" for i in range(1, 13):
    caracteristicas_Diagnostico_v2["marmolre___"+str(i)] = "marmolre___"+str(i)
    #caracteristicas_Diagnostico_v2["marmolre___" + str(i)+"_CUI"] = "marmolre___" + str(i) +"_CUI"
    caracteristicas_Diagnostico_v2["result___" + str(i)] = "result___" + str(i)
    #caracteristicas_Diagnostico_v2["result___" + str(i)+"_CUI"] = "result___" + str(i)+"_CUI" """

# Diccionario que traduce los valores obtenidos para las claves de caracteristicas Prog/Rec

recaida_dict = {"nan":"No-Info Recaida","-1.0":"No-Info Recaida","0.0":"No Progresión","1.0":"Progresión","2.0":"Recaída"}
tipoprog_dict = {"nan":"No-Info tipoprog","1.0":"A distancia","2.0":"Local","3.0":"Local & Distancia","4.0":"Progresión Clínica"}
locprogresion_dict = {"1":"Adenopatías extratorácicas","2":"Adenopatías torácicas","3":"Derrame pleural","4":"Hígado","5":"Hueso","6":"Linfangitis bilateral","7":"Nódulos pleurales","8":"Páncreas","9":"Peritoneales","10":"Pulmón","11":"SNC","12":"Subcutáneas","13":"Suprarrenal","14":"Tejidos blandos","15":"Otras","16":"Derrame pericárdico","17":"Carcinomatosis meníngea"}
terapiar_dict = {"nan":"No-Info terapiar","1.0":"Activa","2.0":"Pasiva"}

#caracteristicas_ProgRec = {"recaida":recaida_dict,"tipoprog":tipoprog_dict,"terapiar":terapiar_dict}
caracteristicas_ProgRec = {"Prog_Rec":recaida_dict}


dictTrmntMapping = {surgery: tipocir,
chemo:   tipoterapia,
radio:   intencion}

#Diccionario que permite relacionar el nombre de cada tratamiento con el nombre de las columnas que indican si ha habido toxicidad
#En el caso de cirugía (surgery), como no hay ninguna columna asociada a toxicidad he usado la columna morperi, que indica si se ha producido mortalidad perioperatoria (muerte antes de 90 días después de la cirugía)
#Pese a que hay  hasta 8 tratamientos de quimioterapia, solo se registra información de toxicidades en los 4 primeros
dictIniColumns_tox = {surgery: ['morperi1','morperi2','morperi3'],
chemo:   ['indtoxtra1','indtoxtra2','indtoxtra3','indtoxtra4'], #No exsite indtoxtra de 5 a 8
radio:   ['indtoxrt1', 'indtoxrt2', 'indtoxrt3', 'indtoxrt4']}

#Diccionario que relaciona la columna que indica la fecha de inicio de cada tratamiento con el nombre de la columna que indica si ha habido toxicidad en dicho tratamiento, el objetivo de este diccionario es poder relacionar la fecha de inicio con la toxicidad en cada tratamiento, útil en la función GetConcurrentTreatmentsToxicidad 
dictFinColumnsToxicidad = {'feccir1'   : 'morperi1',
                  'feccir2'   : 'morperi2',
                 'feccir3'    : 'morperi3',
                 'fecinitto1' : 'indtoxtra1',
                 'fecinitto2' : 'indtoxtra2',
                 'fecinitto3' : 'indtoxtra3',
                 'fecinitto4' : 'indtoxtra4',
                 'fecinirt1'  : 'indtoxrt1',
                 'fecinirt2'  : 'indtoxrt2',
                 'fecinirt3'  : 'indtoxrt3',
                 'fecinirt4'  : 'indtoxrt4'
                }
#Diccionario que relaciona las fechas de inicio de cada tratamiento con la columna que indica si ha desarrollado toxicidad en dicho tratamiento. Se diferencia de dictFinColumnsToxicidad en que en este caso no se han eliminado las fechas de inicio de tratamiento que no tienen toxicidad asociada, siendo ésto útil para la función ConversionTipoTox
dictFinColumnsTipoToxicidad = {'feccir1'   : 'morperi1',
                  'feccir2'   : 'morperi2',
                 'feccir3'    : 'morperi3',
                 'fecinitto1' : 'toxicidadt1',
                 'fecinitto2' : 'toxicidadt2',
                 'fecinitto3' : 'toxicidadt3',
                 'fecinitto4' : 'toxicidadt4',
                 'fecinitto5' : 'toxicidadt5',
                 'fecinitto6' : 'toxicidadt6',
                 'fecinitto7' : 'toxicidadt7',
                 'fecinitto8' : 'toxicidadt8',
                 'fecinirt1'  : 'toxicidadrt1',
                 'fecinirt2'  : 'toxicidadrt2',
                 'fecinirt3'  : 'toxicidadrt3',
                 'fecinirt4'  : 'toxicidadrt4'
                }
#Diccionario que relaciona el nombre de la columna que indica si ha habido toxicidad con cada una de las columnas que indican si se ha producido un tipo de toxicidad o no. Útil para la función ConversionTipoTox
#En el caso de las columnas morperi, como no tienen ningún tipo de toxicidad asociada, simplemente he puesto la misma columna como subtipo
dictTipoTox = {'indtoxrt1':['toxicidadrt1___1','toxicidadrt1___10','toxicidadrt1___13','toxicidadrt1___14','toxicidadrt1___15','toxicidadrt1___16','toxicidadrt1___12'],
                'indtoxrt2':['toxicidadrt2___1','toxicidadrt2___10','toxicidadrt2___13','toxicidadrt2___14','toxicidadrt2___15','toxicidadrt2___16','toxicidadrt2___12'],
                'indtoxrt3':['toxicidadrt3___1','toxicidadrt3___10','toxicidadrt3___13','toxicidadrt3___14','toxicidadrt3___15','toxicidadrt3___16','toxicidadrt3___12'],
                'indtoxrt4':['toxicidadrt4___1','toxicidadrt4___10','toxicidadrt4___13','toxicidadrt4___14','toxicidadrt4___15','toxicidadrt4___16','toxicidadrt4___12'],
              'indtoxtra1':['toxicidadt1___1','toxicidadt1___2','toxicidadt1___3','toxicidadt1___4','toxicidadt1___5','toxicidadt1___6','toxicidadt1___7','toxicidadt1___8','toxicidadt1___9','toxicidadt1___10','toxicidadt1___11','toxicidadt1___12'],
              'indtoxtra2':['toxicidadt2___1','toxicidadt2___2','toxicidadt2___3','toxicidadt2___4','toxicidadt2___5','toxicidadt2___6','toxicidadt2___7','toxicidadt2___8','toxicidadt2___9','toxicidadt2___10','toxicidadt2___11','toxicidadt2___12'],
              'indtoxtra3':['toxicidadt3___1','toxicidadt3___2','toxicidadt3___3','toxicidadt3___4','toxicidadt3___5','toxicidadt3___6','toxicidadt3___7','toxicidadt3___8','toxicidadt3___9','toxicidadt3___10','toxicidadt3___11','toxicidadt3___12'],
              'indtoxtra4':['otratoxt4'],
              'morperi1':['morperi1'],
              'morperi2':['morperi2'],
              'morperi3':['morperi3']}

#Diccionario que relaciona el nombre de la columna que indica el tipo de toxicidad por tratamiento con el nombre de la toxicidad asociada.
#En el caso de cirugía, como no hay una columna de toxicidad como tal y he hecho el supuesto de que morperi es una toxicidad, lo he asociado al str 'Si', como indicador de que Sí se ha producido mortalidad perioperatoria
dictSignificadoTipoTox = {'toxicidadrt1___1':'Neutropenia',
                  'toxicidadrt1___10':'Neumonitis',
                  'toxicidadrt1___13':'Demencia precoz/Olvido',
                  'toxicidadrt1___14':'Diarrea',
                  'toxicidadrt1___15':'Toxicidad cutánea',
                  'toxicidadrt1___16':'Trombocitopenia',
                  'toxicidadrt1___12':'Otra toxicidad',
                  'toxicidadrt2___1':'Neutropenia',
                  'toxicidadrt2___10':'Neumonitis',
                  'toxicidadrt2___13':'Demencia precoz/Olvido',
                  'toxicidadrt2___14':'Diarrea',
                  'toxicidadrt2___15':'Toxicidad cutánea',
                  'toxicidadrt2___16':'Trombocitopenia',
                  'toxicidadrt2___12':'Otra toxicidad',
                  'toxicidadrt3___1':'Neutropenia',
                  'toxicidadrt3___10':'Neumonitis',
                  'toxicidadrt3___13':'Demencia precoz/Olvido',
                  'toxicidadrt3___14':'Diarrea',
                  'toxicidadrt3___15':'Toxicidad cutánea',
                  'toxicidadrt3___16':'Trombocitopenia',
                  'toxicidadrt3___12':'Otra toxicidad',
                  'toxicidadrt4___1':'Neutropenia',
                  'toxicidadrt4___10':'Neumonitis',
                  'toxicidadrt4___13':'Demencia precoz/Olvido',
                  'toxicidadrt4___14':'Diarrea',
                  'toxicidadrt4___15':'Toxicidad cutánea',
                  'toxicidadrt4___16':'Trombocitopenia',
                  'toxicidadrt4___12':'Otra toxicidad',
                  'toxicidadt1___1':'Neutropenia',
                  'toxicidadt1___2':'Neutropenia febril',
                  'toxicidadt1___3':'Anemia_trombopenia',
                  'toxicidadt1___4':'Neurotoxicidad',
                  'toxicidadt1___5':'Nefrotoxicidad',
                  'toxicidadt1___6':'Hepatotoxicidad',
                  'toxicidadt1___7':'Mucositis',
                  'toxicidadt1___8':'Emesis',
                  'toxicidadt1___9':'Astenia',
                  'toxicidadt1___10':'Neumonitis',
                  'toxicidadt1___11':'Obstrucción intestinal',
                  'toxicidadt1___12':'Otra toxicidad',
                  'toxicidadt2___1':'Neutropenia',
                  'toxicidadt2___2':'Neutropenia febril',
                  'toxicidadt2___3':'Anemia_trombopenia',
                  'toxicidadt2___4':'Neurotoxicidad',
                  'toxicidadt2___5':'Nefrotoxicidad',
                  'toxicidadt2___6':'Hepatotoxicidad',
                  'toxicidadt2___7':'Mucositis',
                  'toxicidadt2___8':'Emesis',
                  'toxicidadt2___9':'Astenia',
                  'toxicidadt2___10':'Neumonitis',
                  'toxicidadt2___11':'Obstrucción intestinal',
                  'toxicidadt2___12':'Otra toxicidad',
                  'toxicidadt3___1':'Neutropenia',
                  'toxicidadt3___2':'Neutropenia febril',
                  'toxicidadt3___3':'Anemia_trombopenia',
                  'toxicidadt3___4':'Neurotoxicidad',
                  'toxicidadt3___5':'Nefrotoxicidad',
                  'toxicidadt3___6':'Hepatotoxicidad',
                  'toxicidadt3___7':'Mucositis',
                  'toxicidadt3___8':'Emesis',
                  'toxicidadt3___9':'Astenia',
                  'toxicidadt3___10':'Neumonitis',
                  'toxicidadt3___11':'Obstrucción intestinal',
                  'toxicidadt3___12':'Otra toxicidad',
                  'otratoxt4':'Tiene otra toxicidad',
                  'morperi1':'Si',
                  'morperi2':'Si',
                  'morperi3':'Si'}

dictRelProg_FirstTreat = {"No prog asociada a primer trat":0,"Prog durante primer trat":[0,[]],
                          "Prog durante primer trat con varios":[0,[]],"Prog entre primer y segundo trat":[0,[]],"Prog posterior a primer trat":[0,[]]}
            
dictTest = {"Pacientes con CT":[0,[]],"Pacientes con RT":[0,[]]}
dictEstadiosEst = {"III":[0,[]],"IIIA":[0,[]],"IIIB":[0,[]],"IIIC":[0,[]],"IV":[0,[]],"IVA":[0,[]],"IVB":[0,[]]}

################### Input Flask vars ###############
sexo_f = ["Male","Female"]
habitotab_f = ["Never smoker (<100 cigarettes/life time)","Active smoker","Ex smoker(>1 year)","Unknown"]
indante_f = ['-',
"Neoplasms, Unknown Primary",
"Malignant Head and Neck Neoplasm",
"Malignant tumor of colon/Rectal Carcinoma",
"Malignant neoplasm of esophagus/Malignant neoplasm of stomach",
"Malignant neoplasm of liver",
"Leukemia",
"Lymphoma",
"Breast Carcinoma",
"Melanoma",
"Skin carcinoma",
"Malignant neoplasm of prostate",
"Carcinoma of lung",
"Malignant neoplasm of pancreas",
"Malignant neoplasm of kidney",
"Malignant Central Nervous System Neoplasm",
"Sarcoma",
"Germ cell tumor",
"Malignant neoplasm of urinary bladder/Urologic Neoplasms",
"Uterine Cancer/Metastatic Carcinoma to the Uterine Cervix",
"No",
"Other organs"]

estadio_list_f = ["IA","IA1","IA2","IB","IIA","IIB","III","IIIA","IIIB","IIIC","IV","IVA","IVB"]

histologia_f = ["Adenocarcinoma",
"Squamous cell carcinoma",
"Not Otherwise Specified/Undifferentiated",
"Carcinoma, Large Cell",
"Large cell neuroendocrine carcinoma of lung",
"Carcinoid Tumor",
"Adenosquamous carcinoma",
"Others",
"Squamous cell carcinoma,Spindle cell"]
#marmol_f = ["Sí","No"]
marmol_f = ["KRAS gene/Not detected",
 "ALK gene/Immunohistochemistry/Positive",
 "Epidermal Growth Factor Receptor/EGFR T790M Mutation Negative",
 "Epidermal Growth Factor Receptor/EGFR T790M Mutation Positive Non-Small Cell Lung Carcinoma",
 "BRAF gene/Detected (finding)",
 "Epidermal Growth Factor Receptor/EGFR Exon 21 Mutation",
 "ALK gene/Fluorescent in Situ Hybridization/ALK Gene Translocation",
 "Epidermal Growth Factor Receptor/EGFR Exon 19 Mutation",
 "Epidermal Growth Factor Receptor/EGFR Exon Unknown Mutation",
 "No"]

pdl1_f = ['Positive','Negative','Unknown']


vars_dicc = {"Sexo":sorted(sexo_f),"Habito Tabáquico":sorted(habitotab_f),"Antecedentes Familiares Cáncer":sorted(indante_f),"Estadio Cáncer":estadio_list_f,
            "Histología":sorted(histologia_f),"Estudio Marcadores moleculares":sorted(marmol_f),"PDL1":sorted(pdl1_f)}

vars_corresp = {"sexo":"Sexo","habitotab":"Habito Tabáquico","indante":"Antecedentes Familiares Cáncer","estadioini":"Estadio Cáncer",
            "hist":"Histología","marmol":"Estudio Marcadores moleculares","PDL1":"PDL1"}
vars_input = ["sexo","habitotab","indante","histologia","marmol"]

## ENGLISH MAP TRADUCTION
gender = {"Varón":"Male","Mujer":"Female"}
smoking_habit = {"Nunca fumador (<100 cigarrillos/life time)":"Never smoker (<100 cigarettes/life time)","Fumador activo":"Active smoker","Ex fumador(>1 año)":"Ex smoker(>1 year)","Desconocido":"Unknown"}
indante_english = {"Sí":"Yes","No":"No","Desconocido":"Unknown"}
organ_familiar = {"-":'-',
"COD(origen desconocido)":"Neoplasms, Unknown Primary",
"Cabeza y cuello":"Malignant Head and Neck Neoplasm",
"Colon-Recto":"Malignant tumor of colon/Rectal Carcinoma",
"Esófago-Gástrico":"Malignant neoplasm of esophagus/Malignant neoplasm of stomach",
"Hígado":"Malignant neoplasm of liver",
"Leucemia":"Leukemia",
"Linfoma":"Lymphoma",
"Mama":"Breast Carcinoma",
"Melanoma":"Melanoma",
"Piel no melanoma":"Skin carcinoma",
"Próstata":"Malignant neoplasm of prostate",
"Pulmón":"Carcinoma of lung",
"Páncreas":"Malignant neoplasm of pancreas",
"Renal":"Malignant neoplasm of kidney",
"SNC":"Malignant Central Nervous System Neoplasm",
"Sarcoma":"Sarcoma",
"Tumor germinal":"Germ cell tumor",
"Vejiga/Vías urinarias":"Malignant neoplasm of urinary bladder/Urologic Neoplasms",
"Útero/Cérvix":"Uterine Cancer/Metastatic Carcinoma to the Uterine Cervix",
"No orgfam":"No",
"Otros orgfam":"Other organs"}
marmol_english = {"Sí":"Yes","No":"No"}
histology = {"Adenocarcinoma":"Adenocarcinoma",
"Escamoso":"Squamous cell carcinoma",
"NOS/Indiferenciado":"Not Otherwise Specified/Undifferentiated",
"Carcinoma de células grandes":"Carcinoma, Large Cell",
"Carcinoma neuroendocrino de célula grande":"Large cell neuroendocrine carcinoma of lung",
"Tumor carcinoide":"Carcinoid Tumor",
"Adenoescamoso":"Adenosquamous carcinoma",
"Otros":"Others",
"Sarcomatoide":"Squamous cell carcinoma,Spindle cell"}
comor_english = {"Otra":"Another",
"EPOC":"Chronic Obstructive Airway Disease",
"Cardiopatía":"Heart Diseases",
"No existen comorbilidades":"No comorbidities"}
molecular_markers_result = {"KRAS_Se detecta":"KRAS gene/Detected",
 "ALK_IHQ positivo":"ALK gene/Immunohistochemistry/Positive",
 "EGFR_T790M -":"Epidermal Growth Factor Receptor/EGFR T790M Mutation Negative",
 "EGFR_T790M +":"Epidermal Growth Factor Receptor/EGFR T790M Mutation Positive Non-Small Cell Lung Carcinoma",
 "BRAF_Se detecta":"BRAF gene/Detected (finding)",
 "EGFR_Exón 21":"Epidermal Growth Factor Receptor/EGFR Exon 21 Mutation",
 "ALK_FISH traslocado":"ALK gene/Fluorescent in Situ Hybridization/ALK Gene Translocation",
 "EGFR_Exón 19":"Epidermal Growth Factor Receptor/EGFR Exon 19 Mutation",
 "EGFR_Otros":"Epidermal Growth Factor Receptor/EGFR Unknown Mutation",
 "No marmolre":"No"}
pdl1_result = {"PDL1_Positivo":'PDL1_Positive',"PDL1_Negativo":'PDL1_Negative',"PDL1_Desconocido":'PDL1_Unknown'}
primtratcon = {"Inmunoterapia":"Immunotherapy",
"Quimioterapia neoadyuvante":"Neoadjuvant chemotherapy",
"Quimioterapia neoadyuvante + Refractario": "Neoadjuvant chemotherapy + refractory",
"Quimioterapia paliativa":"Palliative chemotherapy",
"Radioterapia_Paliativa":"Palliative radiotherapy",
"Radioterapia_Radical":"Radical radiotherapy",
"SUR_Curativa":"Curative surgery",
"SUR_Paliativa":"Palliative surgery",
"Terapia oral dirigida":"Targeted Oral Therapy",
"Quimioterapia-Radioterapia Neoadyuvante":"Neoadjuvant chemotherapy-radiotherapy",
"Quimioterapia-Radioterapia Adyuvante":"Adjuvant chemotherapy-radiotherapy",
"Quimioterapia-Radioterapia Radical":"Radical chemotherapy-radiotherapy"}
progrec_english = {"Progresión":"Progression","Recaída":"Relapse","No tiene prog-rec":"No progression/relapse"}
terapia_prog = {"Activa":"Active","No tiene TerapiaProg":"No therapy","Cuidados paliativos":"Palliative care"}
tox_bin = {"NoTox":"NoTox","SíTox":"YesTox","Desc":"Unknown"}
tox_desc = {"Mielotoxicidad":"Dyserythropoietic Anemia with Thrombocytopenia",
"Astenia":"Asthenia",
"Demencia precoz/olvido":"Forgetful",
"Diarrea":"Diarrhea",
"Emesis":"Vomitus",
"Hepatotoxicidad":"Hepatotoxicity",
"Mucositis":"Gastrointestinal mucositis",
"Nefrotoxicidad":"Toxic nephropathy",
"Neumonitis":"Pneumonitis",
"Neurotoxicidad":"Neurotoxicity Syndromes",
"Neutropenia":"Neutropenia",
"Neutropenia febril":"Febrile Neutropenia",
"Obstrucción intestinal":"Intestinal Obstruction",
"Toxicodermia":"Skin toxicity",
"Trombocitopenia":"Thrombocytopenia",
"Ototoxicidad":"Ototoxicity",
"Alopecia":"Alopecia",
"Anorexia":"Anorexia",
"Artritis":"Arthritis",
"Disgeusia":"Dysgeusia",
"Dolor":"Pain",
"Enteritis":"Enteritis",
"Enterocolitis":"Enterocolitis",
"Xerostomía":"Xerostomia",
"Infecciones":"Infection",
"No toxicidad": "No toxicity",
"Desconocido toxicidad":"Unknown toxicity"}
tipo_prog_english = {"No tiene TipoProg":"No progression type",
"Local":"Local",
"A distancia": "Remote",
"Local y a distancia":"Local and remote",
"Progresión clínica": "Clinical progression"
}


vars_dicc_english = {"Gender":sorted(sexo_f),"SmokingHabit":sorted(habitotab_f),"OrganAffected":sorted(indante_f),"CancerStage":estadio_list_f,
            "Histology":sorted(histologia_f),"Biomarkers":sorted(marmol_f),"PDL1Result":sorted(pdl1_f)}

vars_corresp_english = {"sexo":"Gender","habitotab":"Smoking habit","indante":"Organ affected by the cancer of a familiar","estadioini":"Cancer stage",
            "hist":"Histology","marmol":"Molecular markers and associated result","PDL1":"PDL1 result"}

vars_corresp_input_form_with_df = {"Gender":"Gender","SmokingHabit":"Smoking_habit","OrganAffected":"indante"
                                   ,"CancerStage":"Cancer_stage","Histology":"Histology","Biomarkers":"marmol","PDL1Result":"PDL1"}

d_traductions = {"sexo":gender,"habitotab":smoking_habit,"indante":indante_english,"orgfam":organ_familiar,"marmol":marmol_english
,"hist":histology,"comor":comor_english,"marmolre":molecular_markers_result,"PDL1":pdl1_result,"PrimTratCon":primtratcon,"Prog_Rec":progrec_english,"TerapiaProg":terapia_prog,"ToxBin":tox_bin,
"Tox":tox_desc,"TipoProg":tipo_prog_english}


