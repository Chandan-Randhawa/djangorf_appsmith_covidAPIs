from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import psycopg2
from rest_framework.parsers import JSONParser
import math
import json
import pandas as pd
import plotly.express as px
import random
from django.http import FileResponse

# Create your views here.

@api_view(['GET', 'POST'])
def redundant_icmr_all(request):
    conn = psycopg2.connect(
    database="icmr_covid_db", user = "postgres", password = "veryvery" , host = "127.0.0.1",port=5433)

    cursor = conn.cursor()

    cursor.execute('''select * from redundant_icmr_all''')
    result = cursor.fetchall()

    data_dict = {}
    
    for k,v in result:
        data_dict[str(k)]=[round(math.log(v),2) , v]  
        

    cursor.execute('''select * from redundant_icmr_pc_all''')
    result1 = cursor.fetchall()
    for k,v in result1:
        if str(k) in data_dict:
            data_dict[str(k)].extend([round(math.log(v),2) , v]) 
        else:
            data_dict[str(k)]=[0 , 0 , round(math.log(v),2) , v]  
    ord_list=[]
    for k,v in data_dict.items():
        ord_dict={}
        if len(v)<3:
            v.extend([0,0])
        ord_dict['key'] = k
        ord_dict['value'] = v
        ord_list.append(ord_dict)

    sum_of_overall = 0
    for element in ord_list:
        sum_of_overall += (element["value"][1]*int(element["key"]))
    formatted_overall = "{:,}".format(sum_of_overall)

    sum_of_voluntary = 0
    for element in ord_list:
        sum_of_voluntary += (element["value"][3]*int(element["key"]))
    formatted_voluntary = "{:,}".format(sum_of_voluntary)
    if request.method == 'GET':
        return Response(ord_list)
    if request.method == 'POST':    
        return Response({'overall':formatted_overall , 'voluntary':formatted_voluntary})

@api_view(['GET', 'POST'])
def redundant_lab_id(request):
    conn = psycopg2.connect(
    database="icmr_covid_db", user = "postgres", password = "veryvery" , host = "127.0.0.1",port=5433)
    # df = pd.read_sql_query('select * from icmr2 limit 100000', conn)
    cursor = conn.cursor()

    if request.method == 'GET':
        cursor.execute('''select * from redundant_lab_id where count > 50''')
        result = cursor.fetchall()

        ord_list=[]
        
        for k,v,w in result:
            data_dict = {}

            data_dict["rowid"]=str(k)
            data_dict["columnid"]=str(v)
            data_dict["value"]=str(w)
       
            ord_list.append(data_dict)
        return Response(ord_list)


@api_view(['GET', 'POST'])
def redundant_icmr_s_all(request):
    
    conn = psycopg2.connect(
    database="icmr_covid_db", user = "postgres", password = "veryvery" , host = "127.0.0.1",port=5433)
    # df = pd.read_sql_query('select * from icmr2 limit 100000', conn)
    cursor = conn.cursor()

    cursor.execute('''select * from redundant_icmr_s_all''')
    result = cursor.fetchall()
    ord_list=[]
    for k,v in result:
        data_dict = {}
        data_dict['key']=str(k)
        data_dict['value']=[round(math.log(v),2) , v]  
        ord_list.append(data_dict)


    sum_of_values = 0

    for element in ord_list:
        sum_of_values += (element["value"][1]*int(element["key"]))

    formatted_value = "{:,}".format(sum_of_values)

    if request.method == 'GET':
        return Response(ord_list)
    if request.method == 'POST':    
        return Response({'sum':formatted_value})

        

@api_view(['GET', 'POST'])
def redundant_icmr_umc_all(request):

    conn = psycopg2.connect(
    database="icmr_covid_db", user = "postgres", password = "veryvery" , host = "127.0.0.1",port=5433)
    # df = pd.read_sql_query('select * from icmr2 limit 100000', conn)
    cursor = conn.cursor()

    cursor.execute('''select * from redundant_icmr_umc_all''')
    result = cursor.fetchall()
    ord_list=[]
    for k,v in result:
        data_dict = {}
        data_dict['key']=str(k)
        data_dict['value']=[round(math.log(v),2) , v]  
        ord_list.append(data_dict)
    
    sum_of_values = 0

    for element in ord_list:
        sum_of_values += (element["value"][1]*int(element["key"]))

    formatted_value = "{:,}".format(sum_of_values)

    if request.method == 'GET':
        return Response(ord_list)
    if request.method == 'POST':    
        return Response({'sum':formatted_value})

@api_view(['GET', 'POST'])
def redundant_icmr_pn_all(request):

    conn = psycopg2.connect(
    database="icmr_covid_db", user = "postgres", password = "veryvery" , host = "127.0.0.1",port=5433)
    # df = pd.read_sql_query('select * from icmr2 limit 100000', conn)
    cursor = conn.cursor()

    cursor.execute('''select * from redundant_icmr_pn_all''')
    result = cursor.fetchall()
    ord_list=[]
    for k,v in result:
        data_dict = {}
        data_dict['key']=str(k)
        data_dict['value']=[round(math.log(v),2) , v]  
        ord_list.append(data_dict)
    
    sum_of_values = 0

    for element in ord_list:
        sum_of_values += (element["value"][1]*int(element["key"]))

    formatted_value = "{:,}".format(sum_of_values)

    if request.method == 'GET':
        return Response(ord_list)
    if request.method == 'POST':    
        return Response({'sum':formatted_value})
    

@api_view(['GET', 'POST'])
def diff_res_jn(request):
    if request.method == 'GET':
        conn = psycopg2.connect(
        database="icmr_covid_db", user = "postgres", password = "veryvery" , host = "127.0.0.1",port=5433)
        # df = pd.read_sql_query('select * from icmr2 limit 100000', conn)
        cursor = conn.cursor()

        cursor.execute('''select * from diff_res_jn''')
        result = cursor.fetchall()
        ord_list=[]
        for k,v in result:
            data_dict = {}
            data_dict['key']=str(k)[23:30]
            data_dict['value']=[round(math.log(v),2) , v]  
            ord_list.append(data_dict)
    
        return Response(ord_list)

@api_view(['GET', 'POST'])
def diff_res_jn_pcr(request):
    if request.method == 'GET':

        conn = psycopg2.connect(
        database="icmr_covid_db", user = "postgres", password = "veryvery" , host = "127.0.0.1",port=5433)
        # df = pd.read_sql_query('select * from icmr2 limit 100000', conn)
        cursor = conn.cursor()

        cursor.execute('''select * from diff_res_jn_pcr''')
        result = cursor.fetchall()
        ord_list=[]
        for k,v in result[1:]:
            data_dict = {}
            data_dict['key']=str(k)[23:30]
            data_dict['value']=[round(math.log(v),2) , v]  
            ord_list.append(data_dict)
    
        return Response(ord_list)


@api_view(['GET', 'POST'])
def redundant_ids(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        print(data)
        conn = psycopg2.connect(
        database="icmr_covid_db", user = "postgres", password = "veryvery" , host = "127.0.0.1",port=5433)
        cursor = conn.cursor()

        cursor.execute('''select icmr_id from icmr2 order by user_id asc limit 10000''')
        result= cursor.fetchall()

        from collections import Counter
        from datetime import datetime
        # initial_input =  input('Patinet with how many tests : ')
        # second_input = int(input('within how many days you want : '))
        # testing_kit_used = input('if you want PCR testing kit press 1  : ')
        d= Counter(result)
        # print(d)
        finl_li = []
        for a , b in dict(d).items():
            if b >= int(data['initial_input']):
#                         print(type(a))
                # if testing_kit_used == '1':
                #     cursor.execute(f"select date_sample_collection from icmr2 where icmr_id = '{''.join(a)}' and testing_kit_used like '%PCR%' ")
                # else:
                cursor.execute(f"select date_sample_collection from icmr2 where icmr_id = '{''.join(a)}' ")
                result_1 = cursor.fetchall()

                dates_1 = []
                for i in result_1:
                    x = (''.join(i))
#                                        --------------print('xxx :', x)
                    y = datetime.strptime(x, '%Y-%m-%d %H:%M:%S')
#                                        ----------print('yyyyy: ', y)
                    dates_1.append(y)
                dates_1.sort()
                print(dates_1)
#                         --------print(dates_1)
                n = 0
                for (i , j)  in zip(dates_1[1:], dates_1[:-1]):
                    print(i ,'----',j)
                    n +=1
                    c= i-j 
                    print(c, 'outer days')  
                    if c.days<=int(data['second_input']):
                        print(n,'first')
                        days_count=1  
                        for i in dates_1[n:]:
                            cc = i-dates_1[n-1]
                            print(cc ,'internal days')   
                            if cc.days > int(data['second_input']):
                                break
                            elif cc.days<=int(data['second_input']):
                                days_count+=1
                                print(i,'--',dates_1[n-1],'::',cc)
                                print('no. of testss.',days_count)
                            if days_count==int(data['initial_input']):
                                print(''.join(a),"::",days_count, 'tests')
                                finl_li.append(''.join(a))
                                break       
                        if days_count == int(data['initial_input']):
                            break
        fin_li = []
        for i in finl_li:
            dictss = {} 
            dictss['id'] = i
            fin_li.append(dictss)
        return Response(fin_li)        
     

@api_view(['GET', 'POST','PUT'])
def mapss(request): 
    if request.method == 'GET':
        image_path = r'E:\djangorf_appsmith_covidAPIs\map.jpeg'
        if image_path:
            return FileResponse(open(image_path, 'rb'), content_type = 'image/jpeg')

        india_states = json.load(open(r"E:\djangorf_appsmith_covidAPIs\home\states_india.geojson", "r"))
        state_id_map = {}
        for feature in india_states["features"]:
            feature["id"] = feature["properties"]["state_code"]
            state_id_map[feature["properties"]["st_nm"]] = feature["id"]
        my_dict_state = {'Karnataka': 1957, 'Maharashtra': 1059, 'West Bengal': 368, 'Tamil Nadu': 576, 'Kerala': 1253, 'Uttar Pradesh': 2662, 'Jammu & Kashmir': 104, 'NCT of Delhi': 1014, 'Haryana': 293, 'Sikkim': 73, 'Telangana': 56, 'Bihar': 177, 'Odisha': 243, 'Uttarakhand': 68, 'Madhya Pradesh': 234, 'Andhra Pradesh': 263, 'Puducherry': 41, 'Meghalaya': 30, 'Himachal Pradesh': 39, 'Punjab': 87, 'Assam': 122, 'Chhattisgarh': 42,  'Gujarat': 191, 'Chandigarh': 21, 'Rajasthan': 349, 'Nagaland': 15, 'Jharkhand': 89, 'Manipur': 25,  'Goa': 8}
        df = pd.DataFrame(list(my_dict_state.items()), columns=['State', 'Values'])
        df['id'] = df['State'].apply(lambda x:state_id_map[x])
        fig = px.choropleth(df, 
                        locations = 'id',
                        geojson = india_states,
                        color = 'Values',
                        scope = 'asia',
                        hover_name = 'State',
                        hover_data=['Values'])
        fig.update_geos(fitbounds="locations", visible=False)
        print('lllllllllll')
        fig.write_image("map.jpeg")
        print('pnggggggggggggg')
        image_path = r'E:\djangorf_appsmith_covidAPIs\map.jpeg'
        return FileResponse(open(image_path, 'rb'), content_type = 'image/jpeg')
    
    elif request.method == "POST":
        image_path = r'E:\djangorf_appsmith_covidAPIs\mappcr.jpeg'
        if image_path:
            return FileResponse(open(image_path, 'rb'), content_type = 'image/jpeg')

        india_states = json.load(open(r"E:\djangorf_appsmith_covidAPIs\home\states_india.geojson", "r"))
        state_id_map = {}
        for feature in india_states["features"]:
            feature["id"] = feature["properties"]["state_code"]
            state_id_map[feature["properties"]["st_nm"]] = feature["id"]
        my_dict_state_pcr = {'Uttar Pradesh': 2144, 'Odisha': 196, 'Gujarat': 65, 'Tamil Nadu': 404, 'NCT of Delhi': 530, 'Karnataka': 1245, 'Bihar': 52, 'West Bengal': 261, 'Rajasthan': 199, 'Maharashtra': 764, 'Haryana': 172, 'Kerala': 672, 'Chhattisgarh': 16, 'Assam': 70, 'Madhya Pradesh': 116,  'Meghalaya': 27, 'Nagaland': 11, 'Manipur': 16, 'Jammu & Kashmir': 95, 'Himachal Pradesh': 30, 'Uttarakhand': 44, 'Jharkhand': 39, 'Sikkim': 71, 'Punjab': 53, 'Andhra Pradesh': 48, 'Telangana': 40, 'Puducherry': 33, 'Goa': 8, 'Chandigarh': 17}
        df = pd.DataFrame(list(my_dict_state_pcr.items()), columns=['State', 'Values'])
        df['id'] = df['State'].apply(lambda x:state_id_map[x])
        fig = px.choropleth(df, 
                        locations = 'id',
                        geojson = india_states,
                        color = 'Values',
                        scope = 'asia',
                        hover_name = 'State',
                        hover_data=['Values'])
        fig.update_geos(fitbounds="locations", visible=False)
        print('lllllllllll')
        fig.write_image("mappcr.jpeg")
        print('pnggggggggggggg')
        image_path = r'E:\djangorf_appsmith_covidAPIs\mappcr.jpeg'
        return FileResponse(open(image_path, 'rb'), content_type = 'image/jpeg')
    elif request.method == "PUT":
        my_dict_state = {'Karnataka': 1957, 'Maharashtra': 1059, 'West Bengal': 368, 'Tamil Nadu': 576, 'Kerala': 1253, 'Uttar Pradesh': 2662, 'Jammu & Kashmir': 104, 'NCT of Delhi': 1014, 'Haryana': 293, 'Sikkim': 73, 'Telangana': 56, 'Bihar': 177, 'Odisha': 243, 'Uttarakhand': 68, 'Madhya Pradesh': 234, 'Andhra Pradesh': 263, 'Puducherry': 41, 'Meghalaya': 30, 'Himachal Pradesh': 39, 'Punjab': 87, 'Assam': 122, 'Chhattisgarh': 42,  'Gujarat': 191, 'Chandigarh': 21, 'Rajasthan': 349, 'Nagaland': 15, 'Jharkhand': 89, 'Manipur': 25,  'Goa': 8}
        my_dict_state_pcr = {'Uttar Pradesh': 2144, 'Odisha': 196, 'Gujarat': 65, 'Tamil Nadu': 404, 'NCT of Delhi': 530, 'Karnataka': 1245, 'Bihar': 52, 'West Bengal': 261, 'Rajasthan': 199, 'Maharashtra': 764, 'Haryana': 172, 'Kerala': 672, 'Chhattisgarh': 16, 'Assam': 70, 'Madhya Pradesh': 116,  'Meghalaya': 27, 'Nagaland': 11, 'Manipur': 16, 'Jammu & Kashmir': 95, 'Himachal Pradesh': 30, 'Uttarakhand': 44, 'Jharkhand': 39, 'Sikkim': 71, 'Punjab': 53, 'Andhra Pradesh': 48, 'Telangana': 40, 'Puducherry': 33, 'Goa': 8, 'Chandigarh': 17}
        merged_dict = {}

        for key in my_dict_state.keys() | my_dict_state_pcr.keys():
            merged_dict[key] =  [my_dict_state.get(key), my_dict_state_pcr.get(key)]

        ord_list = []
        for k,v in merged_dict.items():
            data_dict = {}
            data_dict['key']=str(k)
            data_dict['value']= v
            ord_list.append(data_dict)
        sorted_list = sorted(ord_list, key=lambda x: x['key'])
        return Response(sorted_list)

def mapss_html(request): 
    india_states = json.load(open(r"E:\djangorf_appsmith_covidAPIs\home\states_india.geojson", "r"))
    state_id_map = {}
    for feature in india_states["features"]:
        feature["id"] = feature["properties"]["state_code"]
        state_id_map[feature["properties"]["st_nm"]] = feature["id"]
    my_dict_state = {'Karnataka': 1957, 'Maharashtra': 1059, 'West Bengal': 368, 'Tamil Nadu': 576, 'Kerala': 1253, 'Uttar Pradesh': 2662, 'Jammu & Kashmir': 104, 'NCT of Delhi': 1014, 'Haryana': 293, 'Sikkim': 73, 'Telangana': 56, 'Bihar': 177, 'Odisha': 243, 'Uttarakhand': 68, 'Madhya Pradesh': 234, 'Andhra Pradesh': 263, 'Puducherry': 41, 'Meghalaya': 30, 'Himachal Pradesh': 39, 'Punjab': 87, 'Assam': 122, 'Chhattisgarh': 42,  'Gujarat': 191, 'Chandigarh': 21, 'Rajasthan': 349, 'Nagaland': 15, 'Jharkhand': 89, 'Manipur': 25, 'Goa': 8}
    my_dict_state_pcr = {'Uttar Pradesh': 2144, 'Odisha': 196, 'Gujarat': 65, 'Tamil Nadu': 404, 'NCT of Delhi': 530, 'Karnataka': 1245, 'Bihar': 52, 'West Bengal': 261, 'Rajasthan': 199, 'Maharashtra': 764, 'Haryana': 172, 'Kerala': 672, 'Chhattisgarh': 16, 'Assam': 70, 'Madhya Pradesh': 116,  'Meghalaya': 27, 'Nagaland': 11, 'Manipur': 16, 'Jammu & Kashmir': 95, 'Himachal Pradesh': 30, 'Uttarakhand': 44, 'Jharkhand': 39, 'Sikkim': 71, 'Punjab': 53, 'Andhra Pradesh': 48, 'Telangana': 40, 'Puducherry': 33, 'Goa': 8, 'Chandigarh': 17}
    df = pd.DataFrame(list(my_dict_state_pcr.items()), columns=['State', 'Values'])
    df['id'] = df['State'].apply(lambda x:state_id_map[x])
    fig = px.choropleth(df, 
                    locations = 'id',
                    geojson = india_states,
                    color = 'Values',
                    scope = 'asia',
                   hover_name = 'State',
                   hover_data=['Values'])
    fig.update_geos(fitbounds="locations", visible=False)
    print('lllllllllll')
    plot_data = fig.to_html(full_html=False)
    print('pnggggggggggggg')
    return render(request , 'mapss.html',{'plot_data':plot_data})

@api_view(['GET', 'POST'])
def slogans(request):
    li = [  "Stay home, stay safe, save lives."
            ,"Mask up, protect yourself and others."
            ,"Together apart, we'll overcome."
            ,"Social distance today for a better tomorrow."
            ,"Flatten the curve, break the chain."
            ,"Hand hygiene is a must, in COVID we trust."
            ,"Don't be a spreader, be a defender."
            ,"Stay informed, stay prepared."
            ,"Keep calm and stay COVID-free."
            ,"In unity, we conquer COVID."
            ,"Stay strong, we'll get through this."
            ,"Protect your loved ones, follow the guidelines."
            ,"Show you care, wear a mask everywhere."
            ,"Heroes wear masks, not capes."
            ,"COVID can't defeat our resilience."
            ,"Spread kindness, not the virus."
            ,"Stay positive, test negative."
            ,"Don't take risks, save lives."
            ,"Be a responsible citizen, stop the transmission."
            ,"Your safety, our priority."
            ,"Follow guidelines, save lives."
            ,"Keep your distance, be a hero."
            ,"Together we fight, together we win."
            ,"Be vigilant, stay healthy."
            ,"Stay home, protect the vulnerable."
            ,"We're in this together, stay united."
            ,"Health first, COVID last."
            ,"Follow protocols, break the virus."
            ,"Safety starts with you."
            ,"Don't let COVID define us, let resilience shine."
            ,"Hope, heal, and overcome."
            ,"Keep the faith, stay safe."
            ,"Prevention is the best protection."
            ,"Stay aware, stay safe."
            ,"United against COVID-19."
            ,"Spread love, not the virus."
            ,"Prioritize safety, beat the pandemic."
            ,"Stay apart, stay connected."
            ,"Care for yourself, care for others."
            ,"We'll rise again, stronger than before."
            ,"Be a superhero, wear a mask."
            ,"Your actions matter, save lives."
            ,"Distance today, embrace tomorrow."
            ,"Stay disciplined, stay healthy."
            ,"Protect yourself, protect your community."
            ,"Stay patient, stay protected."
            ,"Together, we can overcome anything."
            ,"Stay home, stay positive."
            ,"COVID won't last forever, but our unity will."
            ,"Remember: health is wealth."]
    paragraphs = [
    "COVID-19, also known as the coronavirus, is a respiratory illness caused by the novel coronavirus SARS-CoV-2. It was first identified in Wuhan, China, in late 2019 and has since become a global pandemic.",
    "The main symptoms of COVID-19 include fever, cough, and difficulty breathing. However, some individuals may be asymptomatic, meaning they show no symptoms but can still spread the virus to others.",
    "The virus primarily spreads through respiratory droplets when an infected person coughs, sneezes, talks, or breathes. It can also spread by touching contaminated surfaces and then touching the face.",
    "To prevent the spread of COVID-19, it is important to practice good hygiene, such as washing hands frequently with soap and water for at least 20 seconds, wearing masks in public places, and maintaining physical distancing.",
    "COVID-19 has had a significant impact on the global economy, leading to job losses, business closures, and financial hardships for many individuals and communities.",
    "Vaccines have been developed and are being administered worldwide to provide protection against COVID-19. Vaccination is a crucial tool in controlling the spread of the virus and preventing severe illness and death.",
    "Variants of the virus have emerged over time, some of which are more transmissible or may have different clinical outcomes. Ongoing surveillance and research are essential in understanding and addressing these variants.",
    "COVID-19 has put immense pressure on healthcare systems globally, leading to overcrowding in hospitals and shortages of medical supplies. Healthcare workers have played a critical role in caring for patients and combating the pandemic.",
    "Social distancing measures, such as lockdowns and travel restrictions, have been implemented in many countries to slow the spread of the virus and reduce the burden on healthcare systems.",
    "While progress has been made in controlling the spread of COVID-19 through public health measures and vaccinations, it is important to remain vigilant and follow guidelines to prevent further outbreaks and protect vulnerable populations."
]

    random_value = random.choice(paragraphs)
    if request.method=="GET":
        return Response({'slogan':random_value})