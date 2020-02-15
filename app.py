from flask import Flask, jsonify, json
from config import BaseConfig
from document_insights.auth.validateAuthToken import authorize
from document_insights.auth.getAuthToken import get_auth_token

app = Flask(__name__)

#TODO: Remove/Modify this api to get token if requred. Adding temporarily to test authentication.
@app.route('/getToken')
def getToken():
    return get_auth_token()


@app.route('/api/v1/documentInsights/classifyDocs', methods = ["POST"])
@authorize
def classify_document():
    # TODO: Api calls to AWS and Logic.
    return jsonify({})

@app.route('/api/v1/documentInsights/extractFields', methods = ["POST"])
@authorize
def extract_document_fields():
    # TODO: Api calls to AWS and Logic.
    return jsonify({})

@app.route('/api/v1/documentInsights/validateUserProfile', methods = ["POST"])
@authorize
def validate_user_profile():
    # TODO: Api calls to AWS and Logic.
    return jsonify({})

app.run(port=8000)
