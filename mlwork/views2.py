
import requests,json
import pandas as pd
import joblib

def weath(place_input):
    place=str(place_input)

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
    dataset1=val2['currently']['temperature']
    dataset2=val2['currently']['humidity']
    dataset=[dataset1,dataset2]

    return dataset

def yield_calculate(vals):
    i=0
    resultset=[]
    cropnames=[]
    final=[]
    for eachfile in [ 'Jowar', 'Maize','Bajra','Cotton(lint)',
        'Groundnut', 'Moong(Green Gram)', 'Soyabean', 'Gram',
        'Wheat',  'Rice', 'Castor seed',
        'Sugarcane',   'Ragi', 'Niger seed',
        'Sunflower'] :
        a=joblib.load('model{}.pkl'.format(i))
    #  b=pd.read_csv("{}X_test.csv".format(eachfile))
    #  d=pd.read_csv("{}Y_test.csv".format(eachfile),header=None)
    #  b=b.drop("Unnamed: 0",axis=1)
    #  d=d.drop(d.columns[0],axis=1)
        b=[vals]
        c=a.predict(b)
        resultset.append(c)

        print(eachfile)
        cropnames.append(eachfile)
        print(c)
        final=[cropnames,resultset]
        
        print("#############")
    #    print(d[:][1])
    #   z=d[:][1]
    #  print("####################")
    
    
    #  print(mean_absolute_error(z,c))

        i=i+1
    return final