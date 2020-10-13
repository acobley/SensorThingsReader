import requests, json, sys

def getCords(Location):
    cords=Location["coordinates"]
    return cords

def getLocation(Loc):
   response = requests.get(Loc)
   if response.status_code != 200:
     print("Unexpected response: {0}. Status: {1}. Message: {2}".format(response.reason, response.status, jResp['Exception']['Message']))
     sys.exit()
   jResp = response.json()
   #print (json.dumps(jResp,indent=4,sort_keys=True))
   for key,val in jResp.items():
       for val2 in val:
          #print ("Location", val2["location"])
          cords=getCords(val2["location"])
          print ("Longitude",cords[0])
          print ("Latitude",cords[1])

def getThing(Thing):
    response = requests.get(Thing)
    if response.status_code != 200:
      print("Unexpected response: {0}. Status: {1}. Message: {2}".format(response.reason, response.status, jResp['Exception']['Message']))
      sys.exit()
    jResp = response.json()
    #print ("Thing",json.dumps(jResp,indent=4,sort_keys=True))
    dataStream=jResp["Datastreams@iot.navigationLink"]
    #print ("Datastream",dataStream)


def getLocations(Loc):
   response = requests.get(Loc)
   if response.status_code != 200:
     print("Unexpected response: {0}. Status: {1}. Message: {2}".format(response.reason, response.status, jResp['Exception']['Message']))
     sys.exit()
   jResp = response.json()
   #print (json.dumps(jResp,indent=4,sort_keys=True))
   for key,val in jResp.items():
       for val2 in val:
          #print ("Locations Link", val2["Locations@iot.navigationLink"])

          getLocation(val2["Locations@iot.navigationLink"])
          getThing(val2["Thing@iot.navigationLink"])

def getObservation(Obs,out):
    out=out+","+str(Obs["phenomenonTime"])+","+str(Obs["resultTime"])+","+str(Obs["result"])
    #print (Obs)
    #print (Obs["phenomenonTime"])
    #print (Obs["resultTime"])
    #print (Obs["result"])
    return out
    #print (getObservervedArea(Obs["observedArea"]))


def getObservations(Obs,out):
   inVal=out
   response = requests.get(Obs)
   if response.status_code != 200:
     print("Unexpected response: {0}. Status: {1}. Message: {2}".format(response.reason, response.status, jResp['Exception']['Message']))
     sys.exit()
   jResp = response.json()
   #print ("Observations --------------------")
   #print ("Observations",json.dumps(jResp,indent=4,sort_keys=True))
   for key,val in jResp.items():
      for val2 in val:
          #print (val2)
          out=getObservation(val2,out)
          print (out)
          out=inVal
def getObservervedArea(Obs,out):
    #print (Obs["type"])
    out=out+","+Obs["type"]
    coordinates=Obs["coordinates"]
    for key in coordinates:
        out=out+","+str(key)
        #print (key)
    return out

def getUnitOfmeasurment(Obs,out):
    out=out+","+Obs["name"]+","+Obs["symbol"]
    #print (Obs["name"])
    #print (Obs["symbol"])
    return out

def getDataStreams(DS,out):
   inVal=out
   response = requests.get(DS)
   if response.status_code != 200:
     print("Unexpected response: {0}. Status: {1}. Message: {2}".format(response.reason, response.status, jResp['Exception']['Message']))
     sys.exit()
   jResp = response.json()
   #print ("DataStream---------------------------------------------------")
   #print ("DataStream",json.dumps(jResp,indent=4,sort_keys=True))
   for key,val in jResp.items():
      for val2 in val:
         #print ("Val2 (DataStream)",json.dumps(val2,indent=4,sort_keys=True))
         #print ("Observations@iot.navigationLink", val2["Observations@iot.navigationLink"])
         #print (val2["name"])
         out=out+","+val2["name"]
         out = getObservervedArea(val2["observedArea"],out)
         out = getUnitOfmeasurment(val2["unitOfMeasurement"],out)
         out = getObservations(val2["Observations@iot.navigationLink"],out)
         #print out
         out=inVal
#get unit of measurement here too


url = "https://cos4cloud.demo.secure-dimensions.de/sta4cs/v1.0/Parties"
headers = {}
payload = json.dumps({ })

response = requests.get(url)
#print (response)
# exit if status code is not ok
if response.status_code != 200:
  print("Unexpected response: {0}. Status: {1}. Message: {2}".format(response.reason, response.status, jResp['Exception']['Message']))
  sys.exit()
jResp = response.json()

def getParty(Obs,out):
    #print(Obs["name"])
    #print(Obs["description"])
    out=out+Obs["name"]+","+Obs["description"]
    return out

#print (json.dumps(jResp,indent=4,sort_keys=True))
for key,val in jResp.items():
    #print ("Party ---------------------------------------------------")
    for val2 in val:
       out=""
       #print ("Parties", json.dumps(val2,indent=4,sort_keys=True))
       #print ("DataStreams", val2["Datastreams@iot.navigationLink"])
       out=getParty(val2,out)

       out=getDataStreams(val2["Datastreams@iot.navigationLink"],out)
       #print (out)
#print jResp["Locations"]
