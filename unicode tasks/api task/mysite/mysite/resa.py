import requests

url = "https://covid-193.p.rapidapi.com/statistics"

querystring = {"country":"india"}

headers = {
    'x-rapidapi-host': "covid-193.p.rapidapi.com",
    'x-rapidapi-key': "a67fd8a650msh4ac89d6ce0cc29fp1d63a6jsnde9d1edb5282"
    }

response = requests.request("GET", url, headers=headers, params=querystring)
r_dict=response.text
jsonResponse = response.json()
print(response.text)
print(response.json)
print("Print each key-value pair from JSON response")
print(jsonResponse["response"])   
a={}
for x in jsonResponse["response"]:
    a.update(x)
    print(a)
    for key in a:
        s=str(a[key])
        print(key+":"+s)
