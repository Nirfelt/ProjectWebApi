import json
from urllib import urlopen, quote_plus as urlencode

class Profile(object):
	def __init__(self, json):
		self.name = json['name']
		self.email = json['email']

def get_profile(query, as_dict = False):
	profile = None

	j = urlopen('https://api.github.com/users/' + urlencode(query))

	profile_data = json.load(j)

	profile = Profile(profile_data)

	if as_dict:
		return profile.__dict__
	else:
		return profile