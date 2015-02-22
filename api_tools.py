import json
import urllib2
from urllib import urlopen, quote_plus as urlencode
from flask import Flask, request

from flask_mime import Mime

class Profile(object):
	def __init__(self, json):
		self.name = json['name']
		self.email = json['email']

class User_github(object):
	def __init__(self, json):
		self.login = json['login']
		self.test = json['text_matches'][0]['object_url']

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
