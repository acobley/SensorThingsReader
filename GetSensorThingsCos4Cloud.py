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
    print ("Datastream",dataStream)


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

def getObservations(Obs):
   response = requests.get(Obs)
   if response.status_code != 200:
     print("Unexpected response: {0}. Status: {1}. Message: {2}".format(response.reason, response.status, jResp['Exception']['Message']))
     sys.exit()
   jResp = response.json()
   print ("Observations",json.dumps(jResp,indent=4,sort_keys=True))

def getDataStreams(DS):
   response = requests.get(DS)
   if response.status_code != 200:
     print("Unexpected response: {0}. Status: {1}. Message: {2}".format(response.reason, response.status, jResp['Exception']['Message']))
     sys.exit()
   jResp = response.json()
   print ("DataStream",json.dumps(jResp,indent=4,sort_keys=True))
   for key,val in jResp.items():
      for val2 in val:
         print ("Val2 (DataStream)",json.dumps(val2,indent=4,sort_keys=True))
         print ("Observations@iot.navigationLink", val2["Observations@iot.navigationLink"])
         getObservations(val2["Observations@iot.navigationLink"])
#get unit of measurement here too


url = "https://cos4cloud.demo.secure-dimensions.de/sta4cs/v1.0/Things"
headers = {}
payload = json.dumps({ })

response = requests.get(url)
#print (response)
# exit if status code is not ok
if response.status_code != 200:
  print("Unexpected response: {0}. Status: {1}. Message: {2}".format(response.reason, response.status, jResp['Exception']['Message']))
  sys.exit()
jResp = response.json()


#print (json.dumps(jResp,indent=4,sort_keys=True))
for key,val in jResp.items():
    for val2 in val:
       print ("Val2 (Things)", json.dumps(val2,indent=4,sort_keys=True))
       print ("DataStreams", val2["Datastreams@iot.navigationLink"])
       getDataStreams(val2["Datastreams@iot.navigationLink"])
#print jResp["Locations"]
