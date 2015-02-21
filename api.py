# coding: utf-8
from flask import Flask, render_template, request, jsonify

from api_tools import get_profile

app = Flask(__name__)

@app.route('/')
def index():
	return 'Hello World!'

#API
@app.route('/api/v1/search')
def search_api():
	query = request.args.get('name')
	profile = get_profile(query)
	return jsonify(profile = profile.__dict__)

if __name__ == "__main__":
	app.debug = True
	app.run()