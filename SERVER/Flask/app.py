from flask import Flask, request, make_response, jsonify
from flask_restx import Api, Resource, fields
from werkzeug.middleware.proxy_fix import ProxyFix
import os, sys, json
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from Common import dictVars as dv
from functions import *
from functools import wraps
from waitress import serve
import AES, base64


app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)
api = Api(app, version='4.0', title='API P4-LUCAT UPM',
    description='REST API methods from UPM'
)

app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['RESTX_MASK_SWAGGER'] = False



perfil = api.model('Profile',{
    'Gender':fields.String(required=True,description="Genre of patient",enum=dv.sexo_f,example="Male"),
    'Smoking habit':fields.String(required=True,description="Specify de smoking habit of the patient",enum = dv.habitotab_f,example="Ex smoker(>1 year)"),
    'Organ affected by the cancer of a familiar':fields.List(fields.String(description="specify organs affected by cancer in relatives",enum=dv.indante_f,example = "Malignant neoplasm of pancreas")),
    'Cancer stage':fields.String(required=True,description="Stage of cancer of patient",enum=dv.estadio_list_f,example="IV"),
    'Histology':fields.String(required=True,description="Type of cancer",enum=dv.histologia_f,example="Adenocarcinoma"),
    'Molecular markers and associated result':fields.String(required=True,description="Specify molecular marker associated with patient",enum=dv.marmol_f,example="ALK gene/Immunohistochemistry/Positive"),
    'PDL1 result':fields.String(required=True,description="Specify pdl1 result associated with patient",enum=dv.pdl1_f,example="PDL1_Unknown")
})

perfil_multiple = api.model('Profiles_description',{
    'Gender':fields.List(fields.String(description="Genres which matched with input information ![alt text](static/img/f1.png)",enum=dv.sexo_f,example = "Male")),
    'Smoking habit':fields.List(fields.String(description="Smoking habits which matched with input information",enum=dv.habitotab_f,example = "Ex smoker(>1 year)")),
    'Organ affected by the cancer of a familiar':fields.List(fields.String(description="Organs affected by cancer in relatives which matched with input information",enum=dv.indante_f,example = "Malignant neoplasm of pancreas")),
    'Cancer stage':fields.List(fields.String(description="Stage of cancer which matched with input information",enum=dv.estadio_list_f,example = "IV")),
    'Histology':fields.List(fields.String(description="Type of cancers which matched with input information",enum=dv.histologia_f,example = "Adenocarcinoma")),
    'Molecular markers and associated result':fields.List(fields.String(description="Molecular markers which matched with input information",enum=dv.marmol_f,example = 'ALK gene/Immunohistochemistry/Positive')),
    'PDL1 result':fields.List(fields.String(description="PDL1 results which matched with input information",enum=dv.pdl1_f,example = "PDL1_Unknown"))
})

###### BUILDING DICT FORMATS FOR RESPONSE ###########
profile_graph_response = api.model('Profiles_to_graph',{
    'Gender':fields.String(required=True,description="Genre of patient",enum=dv.sexo_f,example="Male"),
    'Smoking habit':fields.String(required=True,description="Specify de smoking habit of the patient",enum = dv.habitotab_f,example="Ex smoker(>1 year)"),
    'Organ affected by the cancer of a familiar':fields.String(required=True,description="Specifies whether or not familiars have developed cancer",enum=['Yes','No'],example="Yes"),
    'Cancer stage':fields.String(required=True,description="Stage of cancer of patient",enum=dv.estadio_list_f,example="IV"),
    'Histology':fields.String(required=True,description="Type of cancer",enum=dv.histologia_f,example="Adenocarcinoma"),
    'Molecular markers and associated result':fields.String(required=True,description="Specifies whether or not it has tested positive in the marker study",enum=['Yes','No'],example="Yes"),
    'PDL1 result':fields.String(required=True,description="Specifies pdl1 result associated with patient",enum=dv.pdl1_f,example="PDL1_Unknown")
})

graph_profile = api.model('Details', {
    "Profiles":fields.List(fields.Nested(profile_graph_response),description="List containing the 20 profiles with highest appearance in the database considering the cancer stage specified in the input form. This set of 20 profiles includes the profile given in the inpur form",example=[('Male', 'Ex smoker(>1 year)', 'Yes', 'Adenocarcinoma', 'Yes', 'PDL1_Unknown'), ('Male', 'Active smoker', 'Yes', 'Adenocarcinoma', 'Yes', 'PDL1_Unknown')]),
    "Count": fields.List(fields.Integer(),description="Specifies count of each profile in Profiles key",example=[21, 11]),
    "Index_to_color":fields.Integer(description="Specifies the index of Profiles list which has to be resalted in graph because it is the profile with the highest count value", example=0)
})

toxicites_graph_response = api.model('Profile_Tox_to_graph',{
    'Treatments':fields.List(fields.String(),description="List of treatments applied to the profile given as input",example=['Palliative chemotherapy', 'Immunotherapy']),
    'YesTox_count':fields.List(fields.Integer(),description="Specifies how many times each treatment has developed toxicity",example=[0,1]),
    'NoTox_count':fields.List(fields.Integer(),description="Specifies how many times each treatment has not developed toxicity",example=[3,1]),
    'Unknown_count':fields.List(fields.Integer(),description="Specifies how many times each treatment has not documented toxicity information",example=[14,0]),
})

progression_graph_response = api.model('Profile_Progression_to_graph',{
    'Treatments':fields.List(fields.String(),description="List of treatments applied to the profile given as input",example=['Palliative chemotherapy', 'Immunotherapy']),
    'Progression_count':fields.List(fields.Integer(),description="Specifies how many times each treatment has developed progression",example=[0,1]),
    'Relapse_count':fields.List(fields.Integer(),description="Specifies how many times each treatment has produced a relapse",example=[3,1]),
    'No progression/relapse_count':fields.List(fields.Integer(),description="Specifies how many times each treatment has not developed progression/relapse",example=[14,0]),
})

toxicites_more_info_graph_response = api.model('Toxicities_info_to_graph',{
    'Treatment':fields.String(description="Specifies the treatment for which we want to know the toxicity details",example="Immunotherapy"),
    'Treatment_Count':fields.Integer("Number of times the treatment has developed toxicities"),
    'Toxicities_list':fields.List(fields.String(),description="Specifies all the toxicities names developed in the treatment",example=['Hepatotoxicity']),
    'Toxicities_list_count':fields.List(fields.Integer(),description="Specifies how many times each toxicity has been developed in treatment",example=[1]),
})
progressionType = api.model('ProgressionType',{
    "ProgressionTypeX":fields.String(description="Specifies a Progression type for a Progression or Relapse",enum=dv.tipo_prog_english,example="Remote")
})
progressionTherapy = api.model('ProgressionTherapy',{
    "ProgressionTypeXTherapyN":fields.String(description="Specifies a therapy for a specific Progression type",enum=dv.terapia_prog,example="Active")
})

progression_more_info_graph_response = api.model('Progression_info_to_graph',{
    'Treatment':fields.String(description="Specifies the treatment for which we want to know the progression/relapse details",example="Palliative chemotherapy"),
    'Category_list':fields.List(fields.String(),description="Specifies if the treatment has developed progression and/or relapse",example=["Progression"]),
    'Category_list_count':fields.List(fields.Integer(),description="Specifies how many times progression and/or relapse has been developed in treatment",example=[7]),
    'Progression_type_list':fields.List(fields.Nested(progressionType),description="Specifies all the progression types for each progression/relapse. Each type is indexed, thus if a progression has two progression types, the format is -> ProgressionType1: xxxxx, ProgressionType2: xxxxx",example=['ProgressionType1: Remote', 'ProgressionType2: Local and remote']),
    'Progression_type_list_count':fields.List(fields.Integer(),description="Specifies how many times each progression type has been developed in treatment",example=[3,4]),
    'Progression_therapy_list':fields.List(fields.Nested(progressionTherapy),description="Specifies all the therapies for each progression type. Each type is indexed, thus if a progression type has two therapies, the format is -> ProgressionType1Therapy1: xxxxx, ProgressionType1Therapy2: xxxxx",example=['ProgressionType1Therapy1: Active', 'ProgressionType1Therapy2: Palliative care','ProgressionType2Therapy1: Active']),
    'Progression_therapy_list_count':fields.List(fields.Integer(),description="Specifies how many times each therapy has been developed in each progression type",example=[2,1,4]),
})

sankey_response = api.model('Sankey',{
    'Source_Id':fields.Integer(description="ID source",example=3),
    'Source':fields.String(description="Label source",example='Item 1'),
    'Target_Id':fields.Integer(description="ID target",example=3),
    'Target':fields.String(description="Label target",example='Item 2'),
    'Count':fields.Integer(description="Number of transactions with label source X and label target Y ",example=5),
    'Color':fields.Integer(description="Index which establish if the color join between source and target has to be same or not",example=0)
})

group_info = api.model('Group_info',{
    'Group_description':fields.String(description="Specifies the pattern description in terms of variables",example="Cancer_stage==IV AND FirstTreatment==Palliative chemotherapy AND Gender==Male"),
    'Target':fields.String(description="Specifies the target asocciated with the pattern",enum=["No Prog/Rel No Tox","No Prog/Rel Yes Tox","Yes Prog/Rel No Tox","Yes Prog/Rel Yes Tox"],example="No Prog/Rel No Tox"),
    'Confidence':fields.Float(description="Specifies the confidence value of the pattern",example=0.8),
    'Number of variables matched from input':fields.Integer(description="Specifies the number of variables with value matched from input",example=4)
})

 ################################

post_response = api.model('Response',{
    'data_chart_profiles':fields.Nested(graph_profile),
    'data_chart_toxicities':fields.Nested(toxicites_graph_response),
    'data_chart_progression':fields.Nested(progression_graph_response),
    'data_chart_toxicities_details':fields.List(fields.Nested(toxicites_more_info_graph_response,skip_none=True),description="Specifies all the toxicity information for each treatment"),
    'data_chart_progression_details':fields.List(fields.Nested(progression_more_info_graph_response, allow_null=True),description="Specifies all the progression/relapse information for each treatment"),
    'sankey_toxicity_records':fields.List(fields.Nested(sankey_response),description="Specifies all the transactions to generate the toxicity sankey"),
    'sankey_progression_records':fields.List(fields.Nested(sankey_response),description="Specifies all the transactions to generate the progression/relapse sankey"),
    'sankey_toxicity_columns':fields.List(fields.String(),description="Specifies the columns names of toxicity sankey"),
    'sankey_progression_columns':fields.List(fields.String(),description="Specifies the columns names of progression/relapse sankey"),
    'list_of_patterns_found':fields.List(fields.Nested(group_info),description="Specifies all the patterns found using the input information")
})

test_token = api.model('test_token',{
    'key':fields.String(description="Token provided"),
})


# Authentication decorator
# It will check if a token is provided in the request. After that, the token will be decoded and compare with the key (public-id).
def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        headers = request.headers
        token = headers.get("upm-token") # Get token from GET request and eliminate '"' symbol from it.
        try:
            if not token or AES.decryptCBC(token) == False:
                return make_response(jsonify({"message": "A valid token is missing!"}), 401) # 401 HTTP response in case the token provided is not accepted.
        except (UnicodeDecodeError, base64.binascii.Error, ValueError):
            return make_response(jsonify({"message": "A valid token is missing!"}), 401) # 401 HTTP response in case the token provided is not accepted.
        return f(*args, **kwargs)
    return decorator


# Main route. GET method will return main menu options. POST method will return the data to be used to generate graphs using provided data.
# Token is required to operate in the system. It will be checked in all methods. -> @token_required
@api.route('/home')
class Home(Resource):
    @api.doc('getMenuOptions',params={'upm-token': {'description': 'Token required to operate in Api', 'in': 'header', 'type': 'string','required':'true'}})
    @token_required
    @api.response(200,"Input form returned ![alt text](static/img/f1.png)",perfil_multiple) # 201 HTTP response in case all graphs are generated succesfully.
    def get(self): # Returns the main menu options
        return dv.vars_dicc_english, 200 # 200 HTTP response that also returns the input form.
    
    @api.expect(perfil)
    @token_required
    @api.response(404,"Patient not found in database",perfil_multiple) # 404 HTTP response in case given data in the input form is not presented in the database.
    @api.response(201,"Data obtained",post_response) # 201 HTTP response in case all graphs are generated succesfully.
    @api.doc('generateGraphs',params={'upm-token': {'description': 'Token required to operate in Api', 'in': 'header', 'type': 'string','required':'true'}})
    def post(self): # Generate graphs and obtain patterns based on input information. In case that there are not patients with the information given as input, a new form will be returned with custom information according to the information provided.
        d_vars,l_vars, d_vars_info = create_list_dict(api.payload) # Process input data.
        found, d = check_input(d_vars)
        if found == False: # Check if provided data are presented in database.
            return d,404 # 404 HTTP response that also returns a new form with custom information according to the information provided.
        data = json.dumps([d_vars, l_vars, d_vars_info])
        
        return createGraphs_patterns(data) # Generate graphs with given information


if __name__ == '__main__':

    with app.test_request_context():
        app.run(debug=True)
        #serve(app, host='0.0.0.0', port=8080)
