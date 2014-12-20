from flask import Flask, request
from flask import render_template

import json

app = Flask(__name__)
with open(r'/home/lotso/PycharmProjects/tog/tog/togspider_items.json') as json_data :
        data = json.load(json_data)

@app.route('/')
def index():
    eplist = [d['chaptertitle'][0] for d in data]
    cleanEpList = sorted(set([int(ep) for ep in eplist]))
    return render_template('index.html', title='Index of episodes', cleanEpList=cleanEpList)

@app.route('/viewer/<int:episodeNo>')
def viewer(episodeNo):


    cccc = {d['pagenumber'][0]:d['images'][0]['path'] for d in data if d['chaptertitle'] == [str(episodeNo)]}
    sorted_cccc = sorted(cccc.items(), key=lambda x: x[0])

    episode = [episodeNo-1,episodeNo, episodeNo+1]

    return render_template('viewer.html', title='Viewing episodes', sorted_cccc=sorted_cccc, episode=episode)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
