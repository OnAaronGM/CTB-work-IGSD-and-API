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

estadioini = {'-2':'Null','-1':'-','0':'I','1':'IA','2':'IA1','3':'IA2','4':'IA3','5':'IB','6':'II','7':'IIA',
              '8':'IIB','9':'III','10':'IIIA','11':'IIIB','12':'IIIC','13':'IV','14':'IVA','15':'IVB',
              '16':'Limitado','17':'Extendido','18':'Otros'}

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
habitotab = {"-1":"Error","0":"Nunca fumador (<100 cigarrillos/life time)","1":"Ex fumador(>1 año)","2":"Fumador activo","3":"Desconocido"}
paqanio = {"nan":"Desconocido","NoNan":"Texto"}
indante = {"-1":"Desconocido","0":"No","1":"Sí"}
numfampul = {"nan":"No Info","NoNan":"Texto"}
numfamotro = {"nan":"No Info","NoNan":"Texto"}
orgfam = {"-1.0":"No orgfam","-2.0":"-","0.0":'Empty value',"1.0":"Mama","2.0":'Cabeza y cuello',"3.0":"Tumor germinal","4.0":"Sarcoma","5.0":"SNC",
    "6.0":"COD","7.0":'Colon-Recto',"8.0":"Esófago-Gástrico","9.0":"Páncreas","10.0":"Vesícula","Hígado":"11.0","11.0":"Hígado",
    "12.0":"Melanoma","13.0":"Piel no melanoma","14.0":"Vejiga/Vías urinarias","15.0":"Renal","16.0":"Próstata",
    "17.0":"Útero/Cérvix","18.0":"Linfoma","19.0":"Leucemia","20.0":"Pulmón","21.0":"Otros","nan":"Desconocido",
          "22.0":'COD(origen desconocido)',"23.0":"Otros orgfam"}
otroorgfam = {"nan":"No otro órgano fam afectado","NoNan":"Texto"}

# caracteristicas_Personales = {"sexo":sexo,"habitotab":habitotab,"indante":indante, "paqanio":paqanio,"cigdia":'cigdia', "numfampul":numfampul,"numfamotro":numfamotro,"orgfam":orgfam}
caracteristicas_Personales = {"sexo":sexo,"habitotab":habitotab,"indante":indante,"orgfam":orgfam}

# Diccionario que traduce los valores obtenidos para las claves de caracteristicas diagnostico

histologia_dict = {"-2":"Error","-1":"-","0":"Adenocarcinoma",
                "1":"Adenoescamoso","2":"Escamoso","3":"Carcinoma de células grandes","4":"Sarcomatoide","5":"NOS/Indiferenciado","6":"Carcinoma de célula pequeña (microcítico)",
                "7":"Carcinoma neuroendocrino de célula grande","8":"Tumor carcinoide","9":"Mesotelioma","10":"Timoma","11":"Carcinoma tímico","12":"Otros"}
marmol_dict = {"-2":"Error","0":"No","1":"Sí"}
marmolre_dict = {"1":"EGFR","2":"ALK","3":"PDL1"}
egfrresultado_dict = {"0":"Negativo","1":"T790M +","2":"T790M -","3":"Exón 19","4":"Exón 21","5":"NOS","6":"Otros"}
indcomor_dict = {"0":"No existen comorbilidades","1":"Asma","2":"Cardiopatía","3":"Diabetes Mellitus (DM)","4":"Dislipemia","5":"EPOC","6":"Alcoholismo/Ex_Alcoholis","7":"Hepatitis","8":"Hipercolesterolemia","9":"Hipertensión (HTA)","10":"Nefropatía",
            "11":"Obesidad","12":"Síndrome depresivo/Ansiedad","13":"Tuberculosis","14":"Vasculopatía","15":"Otra","16":"Hepatopatía","17":"Enfermedad Gastrointest","18":"Enfermedad Neurodegenerativa","19":"Hiperplasia Benigna de Próstata (HBP)","20":"Síndrome de Apnea Obstructiva del Sueño", "21":"Otra comorbilidad","22":"Enfermedad Gastrointestinal", "23":"Alcoholismo/Ex_Alcoholismo"}
otrascomor_dict = {"nan":"No-info otrascomor","NoNan":"Texto"}
alkresultado_dict = {"1":"IHQ negativo","2":"IHQ positivo","3":"FISH traslocado","4":"FISH no traslocado","5":"RNA se detecta","6":"RNA no se detecta"}
pdl1resultado_dict = {"nan":"Error","-1.0":"Desconocido","0.0":"Negativo","1.0":"Positivo"}
positividad_dict = {"nan":"No-info Positividad","NoNan":"Texto"}

caracteristicas_Diagnostico = {"estadioini":estadioini,"histologia":histologia_dict,"marmol":marmol_dict,
"marmolre": marmolre_dict,"egfrresultado":egfrresultado_dict,"indcomor":indcomor_dict,"alkresultado":alkresultado_dict,
"pdl1resultado":pdl1resultado_dict,"positividad":positividad_dict}

caracteristicas_Diagnostico_v2 = {"estadioini":["estadioini"],"marmol":["marmol"], "histologia":histologia_dict,"comorbilidad":["comorbilidad"]}

for i in range(1, 13):
    caracteristicas_Diagnostico_v2["marmolre___"+str(i)] = "marmolre___"+str(i)
    # caracteristicas_Diagnostico_v2["marmolre___" + str(i)+"_CUI"] = "marmolre___" + str(i) +"_CUI"
    caracteristicas_Diagnostico_v2["result___" + str(i)] = "result___" + str(i)
    # caracteristicas_Diagnostico_v2["result___" + str(i)+"_CUI"] = "result___" + str(i)+"_CUI"

# Diccionario que traduce los valores obtenidos para las claves de caracteristicas Prog/Rec

recaida_dict = {"0":"No tiene prog-rec","-1.0":"No-Info Recaida","0.0":"No Progresión","1.0":"Progresión","2.0":"Recaída"}
tipoprog_dict = {"nan":"No-Info tipoprog","1.0":"A distancia","2.0":"Local","3.0":"Local y a distancia","4.0":"Progresión clínica",'0.0':'None'}
locprogresion_dict = {"1":"Adenopatías extratorácicas","2":"Adenopatías torácicas","3":"Derrame pleural","4":"Hígado","5":"Hueso","6":"Linfangitis bilateral","7":"Nódulos pleurales","8":"Páncreas","9":"Peritoneales","10":"Pulmón","11":"SNC","12":"Subcutáneas","13":"Suprarrenal","14":"Tejidos blandos","15":"Otras","16":"Derrame pericárdico","17":"Carcinomatosis meníngea"}
terapiar_dict = {"0.0":"None","1.0":"Activa","2.0":"Pasiva","3.0":"Cuidados paliativos"}

caracteristicas_ProgRec = {"recaida":recaida_dict,"tipoprog":tipoprog_dict,"terapiar":terapiar_dict}

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
                          "Prog durante primer trat con varios":[0,[]],"Prog entre primer y segundo trat":[0,[]],"Prog posterior a primer trat":[0,[]],}

dictFirstTreat = {"['SUR_Curativa']": 0, "['CT_Quimioterapia intravenosa']": 1, "['CT_Quimioterapia neoadyuvante']": 2,
                  "['CT_Quimioterapia intravenosa y oral']": 3, "['RT_Paliativa']": 4, "['SUR_Diagnóstica']": 5,
                  "['CT_Terapia oral dirigida']": 6, "['CT_Quimioterapia-Radioterapia secuencial']": 7, "['RT_Radical']": 8,
                  "['CT_Inmunoterapia']": 9, "['CT_Quimioterapia intravenosa + inmunoterapia']": 10,
                  "['RT_Radical', 'CT_Quimioterapia-Radioterapia concomitante']": 11,
                  "['CT_Quimioterapia intravenosa', 'RT_Paliativa']": 12, "['CT_Terapia oral dirigida', 'RT_Paliativa']": 13,
                  "['CT_Quimioterapia-Radioterapia concomitante']": 14, "['SUR_Paliativa']": 15,
                  "['CT_Quimioterapia intravenosa y oral', 'RT_Paliativa']": 16, "['CT_Quimioterapia oral']": 17, "['CT_Otros']": 18,
                  "['RT_Adyuvante']": 19, "['CT_Quimioterapia-Radioterapia neoadyuvante']": 20,
                  "['CT_Quimioterapia-Radioterapia adyuvante']": 21,
                  "['RT_Adyuvante', 'CT_Quimioterapia-Radioterapia concomitante']": 22, "['RT_Paliativa', 'CT_Inmunoterapia']": 23,
                  "['RT_Paliativa', 'RT_Paliativa', 'CT_Inmunoterapia']": 24,
                  "['CT_Otros', 'CT_Terapia oral dirigida', 'RT_Paliativa', 'RT_Paliativa']": 25,
                  "['RT_Radical', 'CT_Quimioterapia intravenosa']": 26,
                  "['CT_Quimioterapia intravenosa y oral', 'CT_Quimioterapia intravenosa']": 27,
                  "['CT_Quimioterapia intravenosa + inmunoterapia', 'RT_Paliativa']": 28, "['SUR_-']": 29,
                  "['CT_Quimioterapia adyuvante']": 30, "['SUR_Diagnóstica', 'CT_Quimioterapia adyuvante']": 31,
                  "['CT_Quimioterapia-Radioterapia concomitante', 'RT_Paliativa']": 32,
                  "['SUR_Paliativa', 'CT_Quimioterapia intravenosa', 'RT_Paliativa', 'RT_Paliativa']": 33,
                  "['CT_Quimioterapia-Radioterapia neoadyuvante', 'RT_Neoadyuvante']": 34, 'No TratCon': -1}

dictFirstTreat_Reduced = {'SUR_Curativa': '0', 'CT_Quimioterapia intravenosa y oral': '1',
                           'CT_Quimioterapia-Radioterapia secuencial': '2', 'CT_Quimioterapia neoadyuvante': '3',
                           'CT_Quimioterapia intravenosa': '4', 'CT_Terapia oral dirigida': '5',
                           'CT_Quimioterapia-Radioterapia concomitante': '6', ' RT_Adyuvante': '7', 'RT_Paliativa': '8',
                           'CT_Inmunoterapia': '9', 'RT_Radical': '10', 'SUR_Diagnóstica': '11', 'CT_Quimioterapia adyuvante': '12',
                           ' RT_Paliativa': '13', 'CT_Quimioterapia intravenosa + inmunoterapia': '14',
                           'CT_Quimioterapia-Radioterapia neoadyuvante': '15', 'CT_Otros': '16', ' CT_Quimioterapia intravenosa': '17',
                           ' SUR_Paliativa': '18', 'CT_Quimioterapia-Radioterapia adyuvante': '19',
                           ' CT_Quimioterapia-Radioterapia concomitante': '20', 'RT_Adyuvante': '21', ' RT_Radical': '22',
                           'SUR_Paliativa': '23', 'SUR_-': '24', ' CT_Otros': '25', ' CT_Terapia oral dirigida': '26',
                           'RT_Neoadyuvante': '27', ' CT_Quimioterapia-Radioterapia neoadyuvante': '28', ' SUR_Diagnóstica': '29',
                           'CT_Quimioterapia oral': '30'}

dictFirstResp = {"['No respuesta Cirugía']": 0, "['RP']": 1, "['PR']": 2, "['EE']": 3, "['NE']": 4, "['No respuesta CT']": 5,
                 "['No respuesta RT']": 6, "['NR']": 7, "['RC']": 8, "['RP', 'RP']": 9, "['EE', 'EE']": 10,
                 "['PR', 'No respuesta RT']": 11, "['RP', 'No respuesta RT']": 12, "['PR', 'EE']": 13, "['EE', 'NE']": 14,
                 "['PR', 'NE']": 15, "['No respuesta CT', 'No respuesta RT']": 16, "['PR', 'PR']": 17, "['No respuesta CT', 'EE']": 18,
                 "['NE', 'No respuesta RT']": 19, "['RP', 'EE']": 20, "['RP', 'NE']": 21, "['RP', 'No respuesta Cirugía']": 22,
                 "['RP', 'No respuesta RT', 'No respuesta Cirugía', 'No respuesta RT']": 23, "['NE', 'NE']": 24,
                 "['RP', 'RP', 'RP', 'No respuesta CT']": 25, "['EE', 'EE', 'NE']": 26}


dictMarmolre =  {'No marmolre': 0, 'EGFR_Negativo': 1, 'EGFR_Exón 19': 2, 'EGFR_Exón 21': 3, 'PDL1_Positivo': 4, 'PDL1_Negativo': 5,
                 'EGFR_Otros': 6, 'ALK_FISH no traslocado': 7, 'EGFR_T790M +': 8, 'Otros_No resultado asociado': 9,
                 'EGFR_T790M -': 10, 'BRAF_No se detecta': 11, 'HER2_FISH no amplificado': 12, 'ROS1_No resultado asociado': 13,
                 'ALK_IHQ negativo':14,'ALK_FISH traslocado':15,'RET_No resultado asociado':16,'ALK_IHQ positivo':17,
                 'KRAS_No se detecta':18, 'BRAF_Se detecta':19,'PDL1_Desconocido':20,'KRAS_Se detecta':21,'MET_No resultado asociado':22,
                 'BRAF_No resultado asociado':23,'PDL1_No resultado asociado':24}
dict_comor_reduced = {'Cardiopatía': 0, 'No existen comorbilidades': 1, 'Diabetes Mellitus (DM)': 2, 'Dislipemia': 3,
                      'EPOC': 4, 'Alcoholismo/Ex_Alcoholismo': 5, 'Hipertensión (HTA)': 6, 'Enfermedad Gastrointestinal': 7,
                      'Asma': 8, 'Hipercolesterolemia': 9, 'Hiperplasia Benigna de Próstata (HBP)': 10, 'Hepatitis': 11,
                      'Síndrome depresivo/Ansiedad': 12, 'Nefropatía': 13, 'Hipotiroidismo': 14, 'Artritis reumatoide': 15,
                      'Enfermedad Neurodegenerativa': 16, 'Pulmonar': 17, 'Osteoporosis': 18, 'Vasculopatía': 19, 'Psoriasis': 20,
                      'Púrpura trombopénica idiopática  TVP  Filtro en VCI': 21, 'Pólipos en cuerda vocal.': 22, 'Rinitis alergica': 23,
                      'Serología compatible con VHB pasado': 24,
                      ' Neumonías de repetición.   Retraso mental leve.   Epilepsia-crisis parciales complejas.  Cerebral': 25, 'Sinus pilonidal ': 26,
                      'Prostatitis': 27, 'Poliartrosis.  Probable fibromialgia.       ': 28, 'Poliartritis ANA +  ': 29, 'Pancreatitis aguda  Colelitiasis': 30,
                      'Osteorporosis    SIADH   Anemia': 31, 'Osteoporosis  Degeneración macular': 32, 'Osteopenia': 33,
                      'Osteoartropatía hipertrófica.  - Migrañas  - VPH a los 30 años. Conización del cérvix  - Hirsutismo  ': 34,
                      'Obstrucción carotídea': 35, 'Obesidad': 36, 'Sialoadenitis parotídea izquierda crónica  - Glaucoma crónico simple': 37,
                      'Talasemia minor': 38, 'Síndrome de Sjogren  Hipotiroidismo  ': 39, 'esclerosis sistmica  Hipotiroidismo subclínico.': 40,
                      'trastorno delirante': 41, 'timpanoplastia': 42, 'psoriasis': 43, 'protrusion discal': 44, 'polimialgia reumatica.Pulmonar': 45,
                      'migrañas  Hipertiroidismo ': 46, 'leucoplasia cuerda vocal': 47, 'hernias discales  ': 48,
                      'hernia discal  Bebedor de 4 bebidas de alta graduación al día': 49, 'hernia': 50, 'endometriosis': 51,
                      'Síndrome del túnel carpiano bilateral de predominio izquierdo': 52, 'coxartrosis izquierda': 53,
                      'colocación válvula derivación ventriculoperitoneal': 54, 'cataratas congénitas': 55,
                      'bronquitis crónica. Delirio': 56, 'bronquitis crónica': 57, 'bloqueo de rama derecha': 58,
                      'artritis psoriasica. Polineuropatía.': 59, 'Transplantado pulmonar.Pulmonar': 60, 'TEP bilateral ': 61,
                      'TEP': 62, 'Nódulos tiroideos.': 63, 'Meningioma lóbulo temporal derecho Pólipos lar�ngeos en 2011.': 64,
                      'Neumotorax izq con DET': 65, 'Fibroadenoma': 66, 'Estenosis valvular ': 67,
                      'Espondilitis anquilopoyética. Fx aplastamiento de L1. Lumbalgia crónica': 68,
                      'Esofagitis segmentaria proximal  ': 69, 'EICH (ENFERMEDAD INJERTO CRONTA HUESPED)crónico con afectación pulmonar    ': 70,
                      'DORSALGIA': 71, 'DLPC  Claudicación intermitente.   Isquemia crónica grado IIB': 72, 'Corea de Huntington': 73,
                      'Cirrosis biliar primaria': 74, 'Bronconeumonía ': 75,
                      'Bocio normofuncionante  Síndrome de Horner  Leiomioma esofágico. operado 2000.  Artrosis cervical  ': 76,
                      'Bocio': 77, 'BMN  VPH16+': 78, 'BEBEDOR OCASIONAL': 79, 'Artrosis': 80, 'Anorexia nerviosa  Talasemia minor': 81, 'Angioma hepático': 82, 'Aneurisma aorta ascendente': 83, 'Amebiasis en ojo derecho en 2008': 84, 'ALERGIA AL POLEN ': 85, '- Fiebre reumática': 86, ' T.Warthin.  Factor V Leiden.  ': 87, 'Factor V Leyden': 88, 'Fibrosis pulmonar idiopática.  Talasemia.  ': 89, 'Neumonías de repetición.   Polimialgia reumática.': 90, 'Fiebre botonosa mediterránea .Pulmonar': 91, 'Neumonía': 92, 'Miomas uterinos y calcificaciones mamarias en seguimiento.  Artrosis': 93, 'Miomas': 94, 'Mioma uterino  Hernia discal': 95, ' Neumonías de repetición. Absceso pulmonar cavitado en segm 6 izquierdo ': 96, 'Infección pasada VHB': 97, 'Histerectomía subtotal por miomas': 98, 'Hipotiroidismo primario': 99, 'Hipoacusia leve derecha': 100, 'Hipoacusia   Xantomas palpebrales  Infartos lacunares ': 101, 'Hiperuricemia   Tuberculosis pulmonar': 102, 'Hipertiroidismo tratado con yodo radioactivo con hipotiroidismo secundario en tratamiento con eutirox.  Fiebre tifoidea en la infancia.  ': 103, 'Hipertiroidismo ': 104, 'Hiperhomocisteinemia   ': 105, 'Herpes Zoster': 106, 'Hepatopatía': 107, 'Hemocromatosis con H63D heterozigoto': 108, 'Hamartoma condroide en segmento 6 izquierdo pulmonar extirpado en enero de 2010. AP Adenopatía ligamento pulmonar inferior: 2 ganglios linfáticos con antracosis e histiocitosis sinusoidal reactiva.  ccr tto con hemicolectomia izquierda 2008  julio2010 dx ca ductal infiltrante   divertículos sigma': 109, 'HIPOTIROIDISMO': 110, 'Guillain Barré en 2014': 111, 'Glaucoma congénito AO  Útero polimiomatoso (alta de Ginecología Nov 2.017)  Vértigo posicional benigno estudiada en ORL hace 2 años  Hipertiroidismo tras la gestación  ': 112, 'varices  TVP ': 113}


dict_tox_reduced = {'Neutropenia':1,'Neutropenia febril':2,
                    'Anemia_trombopenia':3,'Anemiatrombopenia':3,
                  'Neurotoxicidad':4,'Nefrotoxicidad':5,
                  'Hepatotoxicidad':6,
                  'Mucositis':7,
                  'Emesis':8,
                  'Astenia':9,
                  'Neumonitis':10,
                 'Obstrucción intestinal':11,
                  'Otra toxicidad':12, 'Empty value':-2,'Desconocido':0,'No presenta toxicidad':-1}

dict_tox = {"['No presenta toxicidad']": 0, "['Empty value']": 1, "['No presenta toxicidad', 'Otra toxicidad']": 2,
            "['Otra toxicidad']": 3, "['Desconocido']": 4, "['Astenia']": 5, "['Anemiatrombopenia']": 6,
            "['Empty value', 'No presenta toxicidad', 'Otra toxicidad']": 7, "['Neutropenia']": 8, "['Emesis']": 9, "['Mucositis']": 10,
            "['Neurotoxicidad']": 11, "['Nefrotoxicidad']": 12, "['Neumonitis']": 13, "['Neutropenia febril']": 14, "['Empty value', 'Desconocido']": 15,
            "['Empty value', 'No presenta toxicidad']": 16, "['Hepatotoxicidad']": 17, "['Empty value', 'No presenta toxicidad', 'Emesis']": 18,
            "['Empty value', 'No presenta toxicidad', 'Desconocido', 'Otra toxicidad']": 19, "['No presenta toxicidad', 'Anemiatrombopenia', 'Otra toxicidad']": 20,
            "['No presenta toxicidad', 'Astenia', 'Otra toxicidad']": 21, "['No presenta toxicidad', 'Desconocido', 'Otra toxicidad']": 22,
            "['No presenta toxicidad', 'Desconocido']": 23, "['No presenta toxicidad', 'Mucositis', 'Otra toxicidad']": 24, "['Desconocido', 'Otra toxicidad']": 25,
            "['Empty value', 'No presenta toxicidad', 'Desconocido']": 26}

dict_tox_otra = {'afagia': 58, 'agudización de epoc': 30, 'anemiatrombopenia': 6, 'artritis': 27, 'astenia': 7, 'aumento de las transaminasas,diarrea,disfagia': 53,
                 'cutánea y digestiva': 4, 'dermatitis': 52, 'desconocido': 13, 'diarrea': 17, 'disfagia': 28, 'disfonía, disfagia': 54, 'disnea': 51, 'emesis': 10,
                 'empty value': 1, 'esofagitis': 15, 'estomatitis': 39, 'estreñimiento': 57, 'gastrointestinal': 25, 'hematológica': 29, 'hepatotoxicidad': 56,
                 'hipertransaminasemia g3': 55, 'hipoestsia': 43, 'hipofenesis': 59, 'hipofisitis': 48, 'hiponatremia': 32, 'hipotiroidismo': 47,
                 'inestabilidad en la marcha': 22, 'infeccion respiratoria': 20, 'infecciones respiratorias': 8, 'lengua geográfica': 40,
                 'lesiones cutáneas sugerentes de vasculitis leucocitoclástica y aceniformes': 14, 'mucositis': 18, 'nauseas': 12, 'nefrotoxicidad': 19,
                 'neumonitis': 33, 'neumonitis y disnea': 35, 'neurotoxicidad': 11, 'neutropenia': 3, 'neutropenia febril': 31, 'no presenta toxicidad': 0,
                 'náuseas y vómitos.': 23, 'ototoxicidad': 26, 'otra toxicidad': 5, 'parálitico postcolitis toxica': 21, 'presbifonia, toxicidad cutánea': 46,
                 'prurito': 9, 'prurito y dolor lumbar': 49, 'rash': 16, 'rash acneiforme': 41, 'reaccion acneiforme, diarrea': 24, 'reacción acneiforme': 37,
                 'taquicardia': 34, 'tinitus': 45, 'toxicidad cutánea': 38, 'toxicidad cutánea y diarea': 50,
                 'toxicidad tipo: insuficiencia suprarrenal por tratamiento corticoideo de larga evolución tras la rt': 36, 'trombopenia': 44, 'vómitos': 42}

dtrat_cambios = {121704: "Quimioterapia-Radioterapia Radical", 545425: "Terapia oral dirigida",
                 612028: "Quimioterapia-Radioterapia Radical",
                 651078: "Quimioterapia paliativa", 1089307: "Terapia oral dirigida",
                 2714174: "Quimioterapia paliativa"}