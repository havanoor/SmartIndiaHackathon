import requests,json
loc_base_url="https://maps.googleapis.com/maps/api/place/findplacefromtext/json?"
place=input('Enter city name')

loc_api_key='AIzaSyD2OfkmLHKOjsBSn7caMmvFijLz4CC45Us'
loc_final_url=loc_base_url+"input="+place+"&inputtype=textquery&fields=photos,formatted_address,name,rating,opening_hours,geometry&key="+loc_api_key

response1=requests.get(loc_final_url)
val=response1.json()

val2=val['candidates'][0]
req=val2['geometry']['location']
lat=req['lat']
longi=req['lng']
    
    
base_url='https://api.darksky.net/forecast/'
API_KEY='fc5e98a1edc97881879adb0e2a793604/'

final=base_url+API_KEY+str(lat)+","+str(longi)+"?"+"units=si"
response2=requests.get(final)
val2=response2.json()
dataset=val2['currently']['temperature']
print(dataset)
#for i in dataset:
 ##  print("-----------------------------")
