# coding: utf-8
from flask import Flask, request, jsonify, render_template

from api_tools import get_combined_profile

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('RateYourself.html')

@app.route('/levels')
def levels():
	return render_template('levels_template.html')

@app.route('/api')
def api():
	return render_template('api_template.html', address='http://127.0.0.1:5000/')

@app.route('/profile')
def rate_page():
	profile = get_combined_profile(
		request.args.get('email'),
		request.args.get('stackid'))

	level = profile.level
	lvl_pic = ''
	lvl_name = ''
	width = ''
	height = ''

	if level == 1:
		lvl_pic = 'static/lvl1.png'
		lvl_name = 'Kid'
		width = '240'
		height = '300'
	elif level == 2:
		lvl_pic = 'static/lvl2.png'
		lvl_name = 'Tourist'
		width = '240'
		height = '300'
	elif level == 3:
		lvl_pic = 'static/lvl3.png'
		lvl_name = 'Student'
		width = '240'
		height = '300'
	elif level == 4:
		lvl_pic = 'static/lvl4.png'
		lvl_name = 'Pirate'
		width = '240'
		height = '300'
	elif level == 5:
		lvl_pic = 'static/lvl5.png'
		lvl_name = 'Assassin'
		width = '240'
		height = '300'
	elif level == 6:
		lvl_pic = 'static/lvl6.png'
		lvl_name = 'Ninja'
		width = '240'
		height = '300'
	elif level == 7:
		lvl_pic = '../static/lvl7.png'
		lvl_name = 'Knight'
		width = '230'
		height = '300'
	elif level == 8:
		lvl_pic = '../static/lvl8.png'
		lvl_name = 'Sumo'
		width = '240'
		height = '300'
	elif level == 9:
		lvl_pic = '../static/lvl9.png'
		lvl_name = 'Mummy'
		width = '240'
		height = '300'
	elif level == 10:
		lvl_pic = '../static/lvl10.png'
		lvl_name = 'Batman'
		width = '230'
		height = '300'
	elif level == 11:
		lvl_pic = '../static/lvl11.png'
		lvl_name = 'Devil'
		width = '240'
		height = '300'
	elif level == 12:
		lvl_pic = '../static/lvl12.png'
		lvl_name = 'Death'
		width = '300'
		height = '300'

	return render_template(
		'rated.html',
		email=profile.email,
		name=profile.name,
		picture=profile.picture,
		bio=profile.gbio,
		level=level,
		bronze=profile.sbronze_badge,
		silver=profile.ssilver_badge,
		gold=profile.sgold_badge,
		location=profile.location,
		reputation=profile.sreputation,
		followers=profile.gfollowers,
		score=profile.score,
		repos=profile.gpublic_repos,
		stars=profile.stars,
		levelpicture=lvl_pic,
		levelname=lvl_name,
		w=width,
		h=height)

#API
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

if __name__ == "__main__":
	app.debug = True
	app.run()