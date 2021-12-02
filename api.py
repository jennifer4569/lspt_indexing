import flask
from flask import request, jsonify
import processing

app = flask.Flask(__name__)
app.config["DEBUG"] = True


""" {
    "uid": <uid>
    1:[
        {
            "txt": <word>
            "frequency": <freq>
            "individual": [
                {
                    "position" : <pos>
                    "meta": {<type>: <info>, }
                }
            ]
            "synonyms": <syn>
        },
    ],
    2:[
        {
            "txt": <bigram>
            "frequency": <freq>
            "individual": [
                {
                    "position" : <pos>
                    "meta": {<type>: <info>, }
                }
            ]
            "synonyms": <syn>
        },
    ]
} """
@app.route('/insert', methods=['POST'])
# Recieve a JSON object of form:
def insert():
    #TODO: add if statements to check if data exists (if we don't want the request to fail upon missing fields)
    request_data = request.get_json()
    docid = request_data['uid']
    unigrams = request_data[1]
    bigrams = request_data[2]
    processing.process_data(docid, unigrams, bigrams)
    return '''
        Index successfully recieved document {} and its metadata
        '''.format(docid)



@app.route('/docs/or', methods=['GET'])
def retrieveDocumentsOr():
    tokens = request.args.getlist('tokens')
    start = request.args.get('start')
    num_docs = request.args.get('numDocs')
    result = processing.get_docs(tokens, start, num_docs)
    return jsonify(result)

@app.route('/docs/and', methods=['GET'])
def retrieveDocumentsAnd():
    tokens = request.args.getlist('tokens')
    start = request.args.get('start')
    num_docs = request.args.get('numDocs')
    result = processing.get_docs(tokens, start, num_docs)
    return jsonify(result)

app.run()