# coding: utf-8
from flask import Flask, request, jsonify, render_template

from api_tools import get_profile, get_search_github, get_github_user, get_stackoverflow_user, get_combined_profile

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('RateYourself.html')

@app.route('/levels')
def levels():
	return render_template('levels_template.html')

@app.route('/api')
def api():
	return render_template('api_template.html', test="Hejsan Annika")

#API
@app.route('/api/v1/search')
def search_api():
	query = request.args.get('q')
	search = get_search_github(query, as_dict = True)
	return jsonify(search = search)

@app.route('/api/v1/login_github')
def login_github_api():
	query = request.args.get('q')
	profile = get_profile(query)
	return jsonify(profile = profile.__dict__)

@app.route('/api/v1/user_github')
def user_github_api():
	query = request.args.get('q')
	profile = get_github_user(query)
	return jsonify(profile = profile.__dict__)

@app.route('/api/v1/user_stackoverflow')
def user_stackoverflow_api():
	query = request.args.get('q')
	profile = get_stackoverflow_user(query)
	return jsonify(profile = profile.__dict__)

@app.route('/api/v1/profile')
def profile_combined_api():
	gquery = request.args.get('email')
	squery = request.args.get('stackid')
	# No query was provided
	if not gquery:
	# Return an error and set an appropriate status code
		return jsonify({'error': 'Bad Request', 'code': 400, 'message': 'No email parameter was provided'}), 400
	if not squery:
	# Return an error and set an appropriate status code
		return jsonify({'error': 'Bad Request', 'code': 400, 'message': 'No stackoverflow id parameter was provided'}), 400
	profile = get_combined_profile(gquery, squery)
	return jsonify(profile = profile.__dict__)

@app.route('/profile')
def rate_page():
	profile = get_combined_profile(
		request.args.get('email'),
		request.args.get('stackid'))

	return render_template(
		'rated.html',
		email=profile.email,
		name=profile.name,
		picture=profile.picture,
		bio=profile.gbio,
		level=profile.level)

if __name__ == "__main__":
	app.debug = True
	app.run()