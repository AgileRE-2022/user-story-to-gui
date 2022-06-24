from django.shortcuts import render
from django.http import HttpResponse
from plantuml import PlantUML
import random
import string
import json
import re

# Create your views here.


def index(request):
    return render(request, 'index.html')


def generate(request):

    response_data = {}
    response_data['data'] = request.POST
    response_data['status'] = 'success'

    result_data = {}
    result_data['actor'] = request.POST['role']
    result_data['feature'] = request.POST['task']
    result_data['scenarios'] = []

    iterate_scenarios = 1
    while 'initState_'+str(iterate_scenarios) in request.POST:

        scenario_data = {}
        name_scn = request.POST['scn_name_'+str(iterate_scenarios)]

        given = request.POST['initState_'+str(iterate_scenarios)]
        when = request.POST['action_'+str(iterate_scenarios)]
        then = request.POST['result_'+str(iterate_scenarios)]

        # generate salt code
        salt_scn = buildSaltCode(given, when, then)

        # generate image
        image_scn = "static/images/"+buildImageGUI(salt_scn)

        scenario_data['name'] = name_scn
        scenario_data['salt'] = salt_scn
        scenario_data['image'] = image_scn

        result_data['scenarios'].append(scenario_data)
        iterate_scenarios += 1

    return render(request, 'result.html', result_data)

    # return HttpResponse(json.dumps(result_data), cont/ent_type='application/json')
    # return HttpResponse(json.dumps(given), content_type='application/json')


def buildSaltCode(given, when, then):
    salt_scn_start = "@startsalt \n"
    salt_scn_end = "\n}  \n@endsalt"
    salt_scn_content = ""

    # algoritma untuk mengambil page title (GIVEN)
    # akan mengambil words yang berada di dalam petik, dalam konteks ini page title = checkout_page
    page_title = re.findall('"([^"]*)"', given)[0]
    salt_scn_content += "title "+page_title+" \n{+\n   "

    # algoritma untuk mengambil page component (WHEN)
    # di bagian ini bisa sangat bervariasi, tergantung sedetail apa yang diinginkan
    # untuk kondisi saat ini asumsinya, untuk 1 page terdapat 3 component, yaitu:
    # 1. form input
    # 2. resource
    # 3. button
    # jadi harap urut saat menuliskannya

    components = re.findall('"([^"]*)"', when)

    resource = components[1]
    form = '"'+resource+'"' + " \n   "    
    button = "[" +components[2] +"]" + " \n   "

    page_component = form + button
    salt_scn_content += page_component

    # algoritma untuk mengambil page result (THEN)
    page_result = page_title = re.findall('"([^"]*)"', then)[0]
    salt_scn_content += ".\n   " + page_result

    salt_scn_final = salt_scn_start + salt_scn_content + salt_scn_end

    return salt_scn_final


def buildImageGUI(salt_scn):

    plantuml = PlantUML(url='http://www.plantuml.com/plantuml/img/',
                        basic_auth={}, form_auth={}, http_opts={}, request_opts={})
    png = plantuml.processes(salt_scn)
    filename = ''.join(random.choice(string.ascii_lowercase +
                       string.digits) for _ in range(10)) + '.png'

    # save png to file .png
    with open('projectApp/static/images/'+filename, 'wb') as f:
        f.write(png)

    return filename
