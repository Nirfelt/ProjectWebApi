# coding: utf-8
from flask import Flask, render_template, request, jsonify

from api_tools import get_profile, get_search_github, get_github_user, get_stackoverflow_user

app = Flask(__name__)

@app.route('/')
def index():
	return 'Hello World!'

#API
@app.route('/api/v1/search')
def search_api():
	query = request.args.get('q')
	search = get_search_github(query, as_dict = True)
	return jsonify(search = search)

@app.route('/api/v1/login_github')
def login_github__api():
	query = request.args.get('q')
	profile = get_profile(query)
	return jsonify(profile = profile.__dict__)

@app.route('/api/v1/user_github')
def user_github__api():
	query = request.args.get('q')
	profile = get_github_user(query)
	return jsonify(profile = profile.__dict__)

@app.route('/api/v1/user_stackoverflow')
def user_stackoverflow__api():
	query = request.args.get('q')
	profile = get_stackoverflow_user(query)
	return jsonify(profile = profile.__dict__)

if __name__ == "__main__":
	app.debug = True
	app.run()