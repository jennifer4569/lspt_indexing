import flask
from flask import request, jsonify
import processing

app = flask.Flask(__name__)
app.config["DEBUG"] = True


""" {
    "uid": <uid>,
    "numwords": <numwords>,
    "words": 
    {"dog":
        {
            "title": 1, 
            "headers": 2, 
            "links": 0,
            "other": 2
        }
}

} """
@app.route('/insert', methods=['POST'])
# Recieve a JSON object of form:
def insert():
    #TODO: add if statements to check if data exists (if we don't want the request to fail upon missing fields)
    request_data = request.get_json()
    docId = request_data['uid']
    numWords = request_data['num_words']
    wordDict = request_data['words']
    processing.processIncomingData(docId, numWords, wordDict)
    return '''
        Index successfully recieved document {} and its metadata
        '''.format(docId)


@app.route('/docs/or', methods=['GET'])
def retrieveDocumentsOr():
    tokens = request.args.getlist('tokens')
    start = request.args.get('start')
    num_docs = request.args.get('numDocs')
    result = processing.getDocsOr(tokens, start, num_docs)
    return jsonify(result)

@app.route('/docs/and', methods=['GET'])
def retrieveDocumentsAnd():
    tokens = request.args.getlist('tokens')
    start = request.args.get('start')
    num_docs = request.args.get('numDocs')
    result = processing.getDocsAnd(tokens, start, num_docs)
    return jsonify(result)

app.run()