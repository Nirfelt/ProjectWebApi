import json
import urllib2
from urllib import urlopen, quote_plus as urlencode
from flask import Flask, request
from flask_mime import Mime

class Profile(object):
	def __init__(self, json):
		self.name = json['name']
		self.email = json['email']
		self.picture = json['avatar_url']
		self.followers = json['followers']
		self.public_repos = json['public_repos']
		self.created = json['created_at']
		self.updated = json['updated_at']
		self.bio = json['bio']
		self.hireable = json['hireable']
		self.location = json['location']

class User_github(object):
	def __init__(self, json):
		self.login = json['login']
		self.profile = json['url']

def get_profile(query, as_dict = False):
	profile = None

	j = urlopen('https://api.github.com/users/' + urlencode(query))

	profile_data = json.load(j)

	profile = Profile(profile_data)

	if as_dict:
		return profile.__dict__
	else:
		return profile

def get_search_github(query, as_dict = False):
	search = []
	url = 'https://api.github.com/search/users?q=' + urlencode(query) + '&page=1&per_page=100'
	headers = {'Accept': 'application/vnd.github.v3.text-match+json'}
	req = urllib2.Request(url, None, headers=headers)
	j = urllib2.urlopen(req)
	search_data = json.load(j)

	if len(search_data['items']) > 0:

		for item in search_data['items']:

			if as_dict:
				search.append(User_github(item).__dict__)
			else:
				search.append(User_github(item))
	return search

def get_github_user(query, as_dict = False):
	profile = None
	search = get_search_github(query)
	j = urlopen('https://api.github.com/users/' + urlencode(search[0].login))
	user_data = json.load(j)

	profile = Profile(user_data)

	if as_dict:
		return profile.__dict__
	else:
		return profile