# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from flask import Flask

from dotenv import load_dotenv
import os
import json as JSON
import requests
import NonstopAnalyzer as na
import nsmongo
import nsanalyzed as nsaobj

load_dotenv()

app = Flask(__name__)
analyzer = na.NonstopAnalyzer()
mongo = nsmongo.NSMongo(os.getenv('MONGO_DB_STRING'))

INDEX_SIZE = 4 # what is this ?

def checkAnalyzeInMongo(track_uri):
    return mongo.get({ "track_uri" : track_uri})

def requestAnalyzeFromSpotify(track_uri, auth_token):
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json', 'Authorization': 'Bearer ' + str(auth_token)}

    # Getting content of spesific track
    r = requests.get("https://api.spotify.com/v1/audio-analysis/" + str(track_uri), headers=headers)
    
    # print(str(r.content))
    analysis_data = JSON.loads(str(r.content.decode('utf8')))

    return analysis_data

def analyzeData(raw):
    if 'error' in raw:
        return str("Error happened! "+ str(raw['error']))

    analyzed = analyzer.analyze(raw)
    return analyzed

@app.route('/')
def status():
    return 'Nonstop service is online!'

@app.route('/mongo/sanity')
def sanity():
    if not mongo.areParamsSet():
        return "not sane"
    try:
        mongo.isAlive() 
        return "sane"
    except Exception as error:
        return "not sane"
        
@app.route('/mongo/connect')
def connect():
    mongo.set_db('analyze')
    mongo.set_collection(analyzer.VERSION)
    return "hope connected"

@app.route('/get/<track_uri>')
def getTrackUri(track_uri):
    mongo.set_collection("0.0.1", "analyze")
    return str(mongo.get({ "track_uri" : track_uri}))

@app.route('/analyse/<track_uri>/<auth_token>')
def serve_analysed_data(track_uri, auth_token):

    isExistInMongo = checkAnalyzeInMongo(track_uri)
    print(isExistInMongo)
    nsanalyzed = None
    if isExistInMongo:
        nsanalyzed = nsaobj.NSAnalyzed(track_uri, isExistInMongo['items'], isExistInMongo['index_size'], isExistInMongo['analyzer_version'])

    else:
        rawAnalyze = requestAnalyzeFromSpotify(track_uri, auth_token)
        analyzed = analyzeData(rawAnalyze)

        if 'error' in analyzed:
            return str("Error happened! "+ str(raw['error']))
        
        nsanalyzed = nsaobj.NSAnalyzed(track_uri, analyzed, INDEX_SIZE, analyzer.VERSION)

        d = nsanalyzed.__dict__
        mongo.insert(d)
    
    response = {}
    response["analyser_version"] = nsanalyzed.analyzer_version
    response["index_size"] = nsanalyzed.index_size
    response["item_size"] = len(nsanalyzed.items)
    response["items"] = nsanalyzed.items
    
    return str(response)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)