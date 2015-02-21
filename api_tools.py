import json
from urllib import urlopen, quote_plus as urlencode

class Profile(object):
	def __init__(self, json):
		self.name = json['name']
		self.email = json['email']

class User_github(object):
	def __init__(self, json):
		self.login = json['login']

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
	j = urlopen('https://api.github.com/search/users?q=' + urlencode(query))
	search_data = json.load(j)

	if len(search_data['items']) > 0:

		for item in search_data['items'][:10]:

			if as_dict:
				search.append(User_github(item).__dict__)
			else:
				search.append(User_github(item))

	return search