from flask import Flask, request
from flask import render_template

import json

app = Flask(__name__)


@app.route('/viewer/<int:episodeNo>')
def viewer(episodeNo):

    with open(r'C:\Users\bbarthelet\PycharmProjects\tog\tog\togspider_items.json') as json_data :
        data = json.load(json_data)
    cccc = {d['pagenumber'][0]:d['images'][0]['path'] for d in data if d['chaptertitle'] == [str(episodeNo)]}
    sorted_cccc = sorted(cccc.items(), key=lambda x: x[0])

    episode = [episodeNo-1,episodeNo, episodeNo+1]

    return render_template('viewer.html', title='Viewing episodes', sorted_cccc=sorted_cccc, episode=episode)

if __name__ == '__main__':
    app.run(debug = True)
