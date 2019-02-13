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

# [START gae_python37_app]
from flask import Flask

# [imports]
import json as JSON
import requests
import numpy as np
import gc
# from tensorflow.keras.models import Model
# from tensorflow.keras.layers import Dense, Input
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score, normalized_mutual_info_score

# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)

VERSION = "0.0.1" # Analyser version
INDEX_SIZE = 4    # 

@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'This is our WebService!'

@app.route('/analyse/<track_uri>/<auth_token>')
def serve_analysed_data(track_uri, auth_token):
    
    if track_uri == "1NeLwFETswx8Fzxl2AFl91":
        return "{'analyser_version': '0.0.1', 'index_size': 4, 'item_size': 957, 'items': [{'start': 2.76186, 'index': 0}, {'start': 2.76186, 'index': 0}, {'start': 2.76186, 'index': 0}, {'start': 5.17456, 'index': 3}, {'start': 5.17456, 'index': 3}, {'start': 5.17456, 'index': 3}, {'start': 5.17456, 'index': 3}, {'start': 7.56952, 'index': 0}, {'start': 7.56952, 'index': 0}, {'start': 7.56952, 'index': 0}, {'start': 7.56952, 'index': 0}, {'start': 9.97937, 'index': 2}, {'start': 9.97937, 'index': 2}, {'start': 9.97937, 'index': 2}, {'start': 9.97937, 'index': 2}, {'start': 12.3722, 'index': 3}, {'start': 12.3722, 'index': 3}, {'start': 12.3722, 'index': 3}, {'start': 12.3722, 'index': 3}, {'start': 14.77429, 'index': 1}, {'start': 14.77429, 'index': 1}, {'start': 14.77429, 'index': 1}, {'start': 14.77429, 'index': 1}, {'start': 17.18018, 'index': 1}, {'start': 17.18018, 'index': 1}, {'start': 17.18018, 'index': 1}, {'start': 17.18018, 'index': 1}, {'start': 19.52925, 'index': 0}, {'start': 19.52925, 'index': 0}, {'start': 19.52925, 'index': 0}, {'start': 19.52925, 'index': 0}, {'start': 19.78104, 'index': 0}, {'start': 20.32485, 'index': 3}, {'start': 20.98971, 'index': 3}, {'start': 21.61175, 'index': 1}, {'start': 22.2327, 'index': 0}, {'start': 22.86535, 'index': 2}, {'start': 23.36082, 'index': 1}, {'start': 23.98653, 'index': 3}, {'start': 24.37515, 'index': 1}, {'start': 25.11787, 'index': 3}, {'start': 25.72136, 'index': 0}, {'start': 26.401, 'index': 1}, {'start': 26.77959, 'index': 0}, {'start': 27.67134, 'index': 0}, {'start': 28.13778, 'index': 3}, {'start': 28.86249, 'index': 0}, {'start': 29.36449, 'index': 0}, {'start': 29.92458, 'index': 1}, {'start': 30.58073, 'index': 3}, {'start': 31.13252, 'index': 1}, {'start': 31.76512, 'index': 1}, {'start': 32.30045, 'index': 2}, {'start': 32.92703, 'index': 1}, {'start': 33.60018, 'index': 0}, {'start': 34.16871, 'index': 3}, {'start': 34.7195, 'index': 3}, {'start': 35.32372, 'index': 2}, {'start': 36.0727, 'index': 1}, {'start': 36.641, 'index': 2}, {'start': 37.2737, 'index': 1}, {'start': 37.77374, 'index': 0}, {'start': 38.39383, 'index': 2}, {'start': 38.97206, 'index': 1}, {'start': 39.52585, 'index': 1}, {'start': 40.14259, 'index': 1}, {'start': 40.73959, 'index': 0}, {'start': 41.44617, 'index': 3}, {'start': 41.91161, 'index': 1}, {'start': 42.55633, 'index': 1}, {'start': 43.19469, 'index': 1}, {'start': 43.80376, 'index': 0}, {'start': 44.33288, 'index': 3}, {'start': 44.92485, 'index': 1}, {'start': 45.52771, 'index': 1}, {'start': 46.25488, 'index': 0}, {'start': 46.71365, 'index': 0}, {'start': 47.37002, 'index': 0}, {'start': 48.002, 'index': 3}, {'start': 48.64109, 'index': 0}, {'start': 49.1327, 'index': 2}, {'start': 49.80154, 'index': 2}, {'start': 50.40966, 'index': 2}, {'start': 50.98839, 'index': 3}, {'start': 51.6698, 'index': 2}, {'start': 52.16912, 'index': 0}, {'start': 52.7961, 'index': 1}, {'start': 53.42989, 'index': 0}, {'start': 53.9224, 'index': 2}, {'start': 54.52603, 'index': 3}, {'start': 55.27515, 'index': 1}, {'start': 55.84177, 'index': 0}, {'start': 56.47728, 'index': 1}, {'start': 56.97084, 'index': 0}, {'start': 57.67946, 'index': 3}, {'start': 58.23628, 'index': 2}, {'start': 58.72943, 'index': 3}, {'start': 59.37995, 'index': 2}, {'start': 59.94308, 'index': 1}, {'start': 60.65066, 'index': 3}, {'start': 61.27147, 'index': 1}, {'start': 61.73134, 'index': 1}, {'start': 62.40336, 'index': 1}, {'start': 63.03098, 'index': 1}, {'start': 63.5302, 'index': 3}, {'start': 64.12812, 'index': 1}, {'start': 64.88313, 'index': 1}, {'start': 65.32952, 'index': 2}, {'start': 65.90975, 'index': 3}, {'start': 66.67025, 'index': 0}, {'start': 67.28145, 'index': 0}, {'start': 67.82526, 'index': 0}, {'start': 68.33048, 'index': 2}, {'start': 68.99846, 'index': 1}, {'start': 69.53819, 'index': 0}, {'start': 70.2517, 'index': 1}, {'start': 70.86785, 'index': 1}, {'start': 71.3366, 'index': 0}, {'start': 71.99705, 'index': 0}, {'start': 72.65542, 'index': 3}, {'start': 73.14263, 'index': 1}, {'start': 73.72989, 'index': 3}, {'start': 74.33297, 'index': 1}, {'start': 74.9249, 'index': 1}, {'start': 75.51787, 'index': 1}, {'start': 76.50971, 'index': 1}, {'start': 76.87578, 'index': 2}, {'start': 77.4058, 'index': 3}, {'start': 77.94952, 'index': 0}, {'start': 78.97116, 'index': 3}, {'start': 79.27864, 'index': 1}, {'start': 79.74308, 'index': 2}, {'start': 80.46263, 'index': 0}, {'start': 81.07814, 'index': 1}, {'start': 81.67615, 'index': 1}, {'start': 82.28136, 'index': 2}, {'start': 82.90127, 'index': 1}, {'start': 83.30172, 'index': 1}, {'start': 84.06803, 'index': 3}, {'start': 84.51778, 'index': 2}, {'start': 85.25787, 'index': 2}, {'start': 85.87293, 'index': 0}, {'start': 86.44748, 'index': 1}, {'start': 87.0634, 'index': 2}, {'start': 87.64921, 'index': 0}, {'start': 88.25914, 'index': 1}, {'start': 88.88014, 'index': 0}, {'start': 89.28744, 'index': 2}, {'start': 90.08177, 'index': 2}, {'start': 90.67964, 'index': 2}, {'start': 91.25433, 'index': 2}, {'start': 91.8176, 'index': 0}, {'start': 92.35732, 'index': 3}, {'start': 93.07143, 'index': 1}, {'start': 93.66889, 'index': 1}, {'start': 94.28444, 'index': 0}, {'start': 94.88331, 'index': 2}, {'start': 95.48617, 'index': 0}, {'start': 96.0781, 'index': 0}, {'start': 96.67107, 'index': 3}, {'start': 97.28032, 'index': 0}, {'start': 98.16132, 'index': 1}, {'start': 98.48186, 'index': 2}, {'start': 98.98644, 'index': 1}, {'start': 99.53243, 'index': 2}, {'start': 101.19605, 'index': 0}, {'start': 101.19605, 'index': 0}, {'start': 101.46517, 'index': 1}, {'start': 102.08639, 'index': 2}, {'start': 103.27646, 'index': 1}, {'start': 103.27646, 'index': 1}, {'start': 104.11338, 'index': 3}, {'start': 105.38268, 'index': 2}, {'start': 105.38268, 'index': 2}, {'start': 105.64254, 'index': 1}, {'start': 106.23741, 'index': 1}, {'start': 106.83438, 'index': 0}, {'start': 107.47365, 'index': 1}, {'start': 108.08227, 'index': 2}, {'start': 108.61601, 'index': 3}, {'start': 109.29052, 'index': 0}, {'start': 109.86671, 'index': 1}, {'start': 110.48077, 'index': 1}, {'start': 110.92844, 'index': 0}, {'start': 111.63497, 'index': 1}, {'start': 112.13583, 'index': 2}, {'start': 112.86005, 'index': 3}, {'start': 113.47583, 'index': 1}, {'start': 114.09029, 'index': 1}, {'start': 114.68272, 'index': 2}, {'start': 115.27968, 'index': 0}, {'start': 115.80172, 'index': 1}, {'start': 116.43057, 'index': 1}, {'start': 116.95243, 'index': 1}, {'start': 117.6717, 'index': 1}, {'start': 118.26395, 'index': 3}, {'start': 118.82816, 'index': 3}, {'start': 119.37324, 'index': 0}, {'start': 120.07846, 'index': 0}, {'start': 120.66168, 'index': 1}, {'start': 121.26608, 'index': 3}, {'start': 121.77755, 'index': 0}, {'start': 122.4858, 'index': 2}, {'start': 122.90336, 'index': 3}, {'start': 123.65819, 'index': 3}, {'start': 124.11646, 'index': 0}, {'start': 124.88322, 'index': 0}, {'start': 125.398, 'index': 2}, {'start': 126.0898, 'index': 0}, {'start': 126.53061, 'index': 1}, {'start': 127.2742, 'index': 2}, {'start': 127.67787, 'index': 0}, {'start': 128.44862, 'index': 3}, {'start': 129.09138, 'index': 1}, {'start': 129.6849, 'index': 1}, {'start': 130.24177, 'index': 0}, {'start': 130.86095, 'index': 1}, {'start': 131.42018, 'index': 0}, {'start': 132.0746, 'index': 0}, {'start': 132.47764, 'index': 1}, {'start': 133.26005, 'index': 3}, {'start': 133.87524, 'index': 3}, {'start': 134.49696, 'index': 1}, {'start': 135.04653, 'index': 0}, {'start': 135.6751, 'index': 3}, {'start': 136.29052, 'index': 0}, {'start': 136.74181, 'index': 0}, {'start': 137.43388, 'index': 3}, {'start': 138.09483, 'index': 1}, {'start': 138.69401, 'index': 2}, {'start': 139.24966, 'index': 1}, {'start': 139.8527, 'index': 0}, {'start': 140.49243, 'index': 0}, {'start': 141.09483, 'index': 0}, {'start': 141.68957, 'index': 2}, {'start': 142.16367, 'index': 0}, {'start': 142.90045, 'index': 1}, {'start': 143.35365, 'index': 0}, {'start': 144.09166, 'index': 3}, {'start': 144.6551, 'index': 1}, {'start': 145.28141, 'index': 2}, {'start': 145.88408, 'index': 1}, {'start': 146.34798, 'index': 3}, {'start': 147.06943, 'index': 1}, {'start': 147.68426, 'index': 1}, {'start': 148.161, 'index': 2}, {'start': 148.8741, 'index': 2}, {'start': 149.43501, 'index': 3}, {'start': 150.08825, 'index': 0}, {'start': 150.6854, 'index': 1}, {'start': 151.16689, 'index': 0}, {'start': 151.89283, 'index': 0}, {'start': 152.35791, 'index': 2}, {'start': 153.07637, 'index': 0}, {'start': 153.6868, 'index': 0}, {'start': 154.25084, 'index': 0}, {'start': 154.8839, 'index': 0}, {'start': 155.48576, 'index': 0}, {'start': 155.939, 'index': 3}, {'start': 156.84, 'index': 1}, {'start': 157.28553, 'index': 0}, {'start': 157.80422, 'index': 1}, {'start': 158.43569, 'index': 2}, {'start': 159.04998, 'index': 0}, {'start': 159.68952, 'index': 3}, {'start': 160.21787, 'index': 2}, {'start': 160.89107, 'index': 1}, {'start': 161.3463, 'index': 2}, {'start': 161.94807, 'index': 1}, {'start': 162.69107, 'index': 2}, {'start': 163.29351, 'index': 1}, {'start': 163.8507, 'index': 3}, {'start': 164.49039, 'index': 1}, {'start': 165.0946, 'index': 0}, {'start': 165.55959, 'index': 2}, {'start': 166.3015, 'index': 0}, {'start': 166.88785, 'index': 0}, {'start': 167.32848, 'index': 0}, {'start': 168.04766, 'index': 1}, {'start': 168.70399, 'index': 3}, {'start': 169.29039, 'index': 1}, {'start': 169.74463, 'index': 0}, {'start': 170.37274, 'index': 0}, {'start': 171.2478, 'index': 1}, {'start': 171.54898, 'index': 2}, {'start': 172.29197, 'index': 3}, {'start': 172.90132, 'index': 0}, {'start': 173.27351, 'index': 0}, {'start': 173.95279, 'index': 1}, {'start': 174.59755, 'index': 0}, {'start': 175.1468, 'index': 0}, {'start': 175.67111, 'index': 1}, {'start': 176.49456, 'index': 2}, {'start': 176.99406, 'index': 1}, {'start': 177.62059, 'index': 1}, {'start': 178.25415, 'index': 3}, {'start': 178.75401, 'index': 0}, {'start': 179.35147, 'index': 0}, {'start': 180.09937, 'index': 0}, {'start': 180.54866, 'index': 1}, {'start': 181.12639, 'index': 0}, {'start': 182.14857, 'index': 0}, {'start': 182.36444, 'index': 1}, {'start': 183.05329, 'index': 2}, {'start': 183.54803, 'index': 0}, {'start': 184.20399, 'index': 2}, {'start': 184.76227, 'index': 0}, {'start': 185.48063, 'index': 1}, {'start': 186.09057, 'index': 3}, {'start': 186.57293, 'index': 3}, {'start': 187.2815, 'index': 2}, {'start': 187.85537, 'index': 3}, {'start': 188.3658, 'index': 0}, {'start': 188.94726, 'index': 0}, {'start': 189.55628, 'index': 3}, {'start': 190.45016, 'index': 0}, {'start': 190.74014, 'index': 2}, {'start': 191.50068, 'index': 3}, {'start': 192.23306, 'index': 0}, {'start': 192.65619, 'index': 0}, {'start': 193.16667, 'index': 0}, {'start': 193.82753, 'index': 0}, {'start': 194.34971, 'index': 0}, {'start': 194.87941, 'index': 2}, {'start': 195.69701, 'index': 3}, {'start': 196.19732, 'index': 1}, {'start': 196.82372, 'index': 3}, {'start': 197.4571, 'index': 2}, {'start': 197.95519, 'index': 0}, {'start': 198.54893, 'index': 3}, {'start': 199.30272, 'index': 0}, {'start': 199.75565, 'index': 2}, {'start': 200.33016, 'index': 2}, {'start': 200.96943, 'index': 1}, {'start': 201.70118, 'index': 0}, {'start': 202.2512, 'index': 2}, {'start': 202.75701, 'index': 1}, {'start': 203.41819, 'index': 0}, {'start': 203.96567, 'index': 0}, {'start': 204.67887, 'index': 0}, {'start': 205.29315, 'index': 0}, {'start': 205.77483, 'index': 0}, {'start': 206.48948, 'index': 1}, {'start': 207.05791, 'index': 0}, {'start': 207.56413, 'index': 0}, {'start': 208.15624, 'index': 1}, {'start': 208.75864, 'index': 3}, {'start': 209.65288, 'index': 3}, {'start': 209.93633, 'index': 1}, {'start': 210.6981, 'index': 0}, {'start': 211.30798, 'index': 3}, {'start': 211.85973, 'index': 1}, {'start': 212.35882, 'index': 0}, {'start': 213.02649, 'index': 0}, {'start': 213.54866, 'index': 2}, {'start': 214.28621, 'index': 3}, {'start': 214.89986, 'index': 1}, {'start': 215.41624, 'index': 2}, {'start': 216.03143, 'index': 0}, {'start': 216.67116, 'index': 2}, {'start': 217.17596, 'index': 3}, {'start': 217.7556, 'index': 1}, {'start': 218.35937, 'index': 2}, {'start': 218.95814, 'index': 0}, {'start': 219.55043, 'index': 2}, {'start': 220.4678, 'index': 3}, {'start': 220.91506, 'index': 0}, {'start': 221.46612, 'index': 2}, {'start': 221.97678, 'index': 2}, {'start': 222.70794, 'index': 1}, {'start': 223.16757, 'index': 0}, {'start': 223.87492, 'index': 0}, {'start': 224.49592, 'index': 0}, {'start': 224.97224, 'index': 1}, {'start': 225.55891, 'index': 2}, {'start': 226.26694, 'index': 1}, {'start': 226.91737, 'index': 2}, {'start': 227.36345, 'index': 1}, {'start': 228.26902, 'index': 1}]}"

    # Our headers
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json', 'Authorization': 'Bearer ' + str(auth_token)}

    # Getting content of spesific track
    r = requests.get("https://api.spotify.com/v1/audio-analysis/" + str(track_uri), headers=headers)
    
    # print(str(r.content))
    analysis_data = JSON.loads(str(r.content.decode('utf8')))

    if 'error' in analysis_data:
        return str("Error happened! "+ str(analysis_data['error']))

    pitches = []
    for segment in analysis_data['segments']:
        pitches.append(np.asarray(segment['pitches']))

    pitches = np.asarray(pitches)

    predictions = []

    ran = 150
    chunk = len(pitches) / ran

    for i in range(ran):
        val_x = pitches[int(i * chunk): int((i+1) * chunk)]

        km = KMeans(n_jobs = 4, n_clusters = INDEX_SIZE, n_init = 1)
        km.fit(val_x)
        predictions.append(list(km.predict(val_x)))

    pred = []

    for pre in predictions:
        for p in pre:
            pred.append(p)
    
    response = {}
    response["analyser_version"] = VERSION
    response["index_size"] = INDEX_SIZE
    response["item_size"] = len(pred)
    response["items"] = []
    
    a_d = {}
    b = {}
    a_d["segments"] = analysis_data['segments']
    b["beats"] = analysis_data["beats"]

    gc.collect()

    for b in b["beats"]:
        beat = float(b["start"])
        
        i = 0
        while True:
            if i == len(a_d['segments']) - 1:
                segm = 0
                break
            segm = float(a_d['segments'][i]["start"])
            if beat <= segm:
                break
            i = i + 1

        if segm > 0:
            response["items"].append({"start" : a_d['segments'][i]["start"],
                                      "index" : pred[i]})

    gc.collect()
    return str(response)

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_python37_app]
