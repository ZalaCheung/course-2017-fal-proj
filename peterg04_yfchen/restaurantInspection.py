import urllib.request
import json
import dml
import prov.model
import datetime
import uuid
from builtins import staticmethod

class restaurantInspection(dml.Algorithm):
    contributor = 'peterg04_yfchen'
    reads = []
    writes = ['peterg04_yfchen.restaurants']
    
    @staticmethod
    def execute(trial = False):
        startTime = datetime.datetime.now()
        
        # Set up the db connection
        client = dml.pymongo.MongoClient()
        repo = client.repo
        repo.authenticate('peterg04_yfchen', 'peterg04_yfchen')
        
        url = 'https://data.cityofboston.gov/resource/427a-3cn5.json'
        response = urllib.request.urlopen(url).decode("utf-8")
        r = json.loads(response)
        s = json.dumps(r, sort_keys=True, indent=2)
        repo.dropCollection("restaurants")
        repo.createCollection("restaurants")
        repo['peterg04_yfchen.restaurants'].insert_many(r)
        
        repo.logout()
        
        endTime = datetime.datetime.now()
        
        return {"start":startTime, "end":endTime}
    
#     @staticmethod
#     def provenance(doc = prov.model.ProvDocument(), startTime = None, endTime = None):
#         '''
#             Create the provenance document describing everything happening
#             in this script. Each run of the script will generate a new
#             document describing that invocation event.
#         '''
#         
#         client = dml.pymongo.MongoClient()
#         repo = client.repo
#         repo.authenticate('peterg04_yfchen', 'peterg04_yfchen')
        
        
        
    
    