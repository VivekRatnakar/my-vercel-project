import json
from flask import Flask, request, jsonify

app = Flask(__name__)

# Imaginary students' marks
students = [{"name":"4bsBpu1","marks":67},{"name":"JMSfLAxv","marks":86},{"name":"gvD1X4K","marks":43},{"name":"L","marks":20},
                {"name":"zfjWxTa","marks":15},{"name":"ygk3","marks":62},{"name":"i8tpJfgSXs","marks":2},{"name":"7","marks":3},
                {"name":"loPH","marks":3},{"name":"Gi","marks":19},{"name":"VACcoBWo","marks":28},{"name":"eOY","marks":64},
                {"name":"pohA46","marks":88},{"name":"DOW","marks":60},{"name":"DDkAM","marks":74},{"name":"RmTUzI3cP","marks":70},
                {"name":"EcLQM","marks":89},{"name":"wMBZQ92d","marks":39},{"name":"cj9GxkZj2","marks":13},{"name":"xEpo3La","marks":79},
                {"name":"eH","marks":62},{"name":"lc29Lo","marks":78},{"name":"j1ZkY","marks":16},{"name":"us87j5","marks":68},
                {"name":"opZWF","marks":33},{"name":"ts","marks":48},{"name":"RxI2Buqh","marks":64},{"name":"2luDYocJhP","marks":55},
                {"name":"Tvs7K","marks":37},{"name":"yzsv","marks":86},{"name":"Wv9gSeh","marks":45},{"name":"gpcdJmo","marks":85},
                {"name":"TOE","marks":32},{"name":"HRUZUc9s","marks":69},{"name":"s01","marks":79},{"name":"QFLZc2","marks":99},
                {"name":"4SgFLc4N","marks":80},{"name":"6snFOknI","marks":27},{"name":"wbBAY","marks":4},{"name":"CywAY","marks":80},
                {"name":"RCOd","marks":34},{"name":"o5WwDOysKJ","marks":42},{"name":"wc9ERES3Xa","marks":49},{"name":"nSpY05D9","marks":18},
                {"name":"UCw0q","marks":43},{"name":"10Mp3gCb7S","marks":73},{"name":"ROYWGa","marks":53},{"name":"9","marks":83},
                {"name":"EnyC1","marks":52},{"name":"B5IHKG5","marks":55},{"name":"U","marks":98},{"name":"zYAoH","marks":29},
                {"name":"MshqC2Bw","marks":79},{"name":"S2LjQ4c9","marks":23},{"name":"pf0wq","marks":8},{"name":"3famqbM","marks":3},
                {"name":"Ki","marks":26},{"name":"v4y","marks":74},{"name":"emkJBDj","marks":7},{"name":"x71SXU","marks":43},
                {"name":"znoEhUz","marks":85},{"name":"Ls7yWh","marks":30},{"name":"RI","marks":44},{"name":"39j4M","marks":67},
                {"name":"0CD2FTcXR","marks":33},{"name":"8","marks":58},{"name":"lQcfAAtNS","marks":48},{"name":"MsZAbRYLo3","marks":79},
                {"name":"V0mRA2Nh","marks":6},{"name":"2cyCRCdV","marks":68},{"name":"rpREBWkv","marks":24},{"name":"w3b2PM","marks":15},
                {"name":"sGIzy26Tf","marks":78},{"name":"GbX","marks":84},{"name":"oq","marks":41},{"name":"ESNegxEJtY","marks":46},
                {"name":"N9A","marks":9},{"name":"6pMfcfWl","marks":73},{"name":"9kHweqtf","marks":51},{"name":"BLnh","marks":25},
                {"name":"5","marks":60},{"name":"H08H","marks":18},{"name":"u","marks":20},{"name":"z","marks":90},
                {"name":"FFdUoVnaJ","marks":14},{"name":"hM3zu","marks":24},{"name":"ET1hendevh","marks":15},
                {"name":"85","marks":37},{"name":"DIEiQulZEn","marks":1},{"name":"FuHpWHAe95","marks":49},
                {"name":"r5yokT","marks":87},{"name":"n926a6u","marks":11},{"name":"YDzj49bl","marks":24},
                {"name":"muJEw90OB","marks":70},{"name":"5DofPfrCgq","marks":55},{"name":"HAOP","marks":66},
                {"name":"lDbdjYM","marks":94},{"name":"rg0Yama","marks":58},{"name":"c3Le","marks":45},{"name":"tL6Yapy","marks":74}]

@app.route('/api')
def get_marks():
    names = request.args.getlist('name')
    marks = [students.get(name, 0) for name in names]  # Default mark is 0 if name not found
    return jsonify({"marks": marks})

if __name__ == '__main__':
    app.run(debug=True)
