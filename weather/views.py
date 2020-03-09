from django.shortcuts import render
import requests,json
from farmers.models import *

def weather_display(request):
    li=[]
    dis=Farmer.objects.get(fidentity=request.user)
    print(dis.fdis.dname)
    if request.method=='POST':
        place=request.POST['name']
        dis=Farmer.objects.get(fidentity=request.user)
        print(dis.fdis.dname)

        loc_final_url="https://api.opencagedata.com/geocode/v1/json?q={}&key=260699c0c06c46839d815f10c75c0039".format(place)

        response1=requests.get(loc_final_url)
        val=response1.json()

        val2=val['results'][0]['geometry']
    
        lat=val2['lat']
        longi=val2['lng']
        
        
        base_url='https://api.darksky.net/forecast/'
        API_KEY='fc5e98a1edc97881879adb0e2a793604/'

        final=base_url+API_KEY+str(lat)+","+str(longi)+"?"+"units=si"
        response2=requests.get(final)
        val2=response2.json()
        dataset=val2['daily']['data']
        
        for i in dataset:
            print(i['temperatureHigh'])
            li.append(i['temperatureHigh'])

    return render(request,"weatherHome.html",{'data':li,'val':dis.fdis.dname})
        
