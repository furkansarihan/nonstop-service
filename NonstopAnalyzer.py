import os

import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score, normalized_mutual_info_score


class NonstopAnalyzer:

    def __init__(self): 
        self.VERSION = os.getenv('ANALYZER_VERSION')

    def analyze(self, analysis_data, cluster_num = 4):
        pitches = []
        print(analysis_data)
        for segment in analysis_data['segments']:
            pitches.append(np.asarray(segment['pitches']))

        pitches = np.asarray(pitches)

        predictions = []

        ran = 150
        chunk = len(pitches) / ran

        for i in range(ran):
            val_x = pitches[int(i * chunk) : int((i+1) * chunk)]

            km = KMeans(n_jobs = 1, n_clusters = cluster_num, n_init = 5)
            km.fit(val_x)
            predictions.append(list(km.predict(val_x)))

        pred = []

        for pre in predictions:
            for p in pre:
                pred.append(p)

        a_d = {}
        b = {}
        a_d["segments"] = analysis_data['segments']
        b["beats"] = analysis_data["beats"]

        items = []
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
                items.append({"start" : a_d['segments'][i]["start"],
                                        "index" : int(pred[i])})

        return items


