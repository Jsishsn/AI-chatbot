import json
import requests



def donations_list(month='', year=''):
    #fetch data from api 
    url='https://apis.stmorg.in/logs/donations?month='+month+'&year='+year
    response = requests.get(url)
    data = response.json()
    # catch errors 
    return json.dumps(data)
