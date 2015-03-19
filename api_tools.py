import json
import urllib2
from urllib import urlopen, quote_plus as urlencode
import gzip
import io

class GithubProfile(object):
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

class StackoverflowProfile(object):
	def __init__(self, json):
		self.name = json['items'][0]['display_name']
		self.bronze_badge = json['items'][0]['badge_counts']['bronze']
		self.silver_badge = json['items'][0]['badge_counts']['silver']
		self.gold_badge = json['items'][0]['badge_counts']['gold']
		self.reputation = json['items'][0]['reputation']
		self.stackoverflow_link = json['items'][0]['link']
		
class UserGithub(object):
	def __init__(self, json):
		self.login = json['login']
		self.profile = json['url']

class Profile(object):
	def __init__(self, json):
		self.name = json['name']
		self.sbronze_badge = json['bronze']
		self.ssilver_badge = json['silver']
		self.sgold_badge = json['gold']
		self.sreputation = json['reputation']
		self.stackoverflow_link = json['slink']
		self.email = json['email']
		self.picture = json['avatar_url']
		self.gfollowers = json['followers']
		self.gpublic_repos = json['public_repos']
		self.gcreated = json['created_at']
		self.gupdated = json['updated_at']
		self.gbio = json['bio']
		self.hireable = json['hireable']
		self.location = json['location']
		self.score = json['score']
		self.level = json['level']

def get_profile(query, as_dict = False):
	profile = None

	j = urlopen('https://api.github.com/users/' + urlencode(query))

	profile_data = json.load(j)

	profile = GithubProfile(profile_data)

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
				search.append(UserGithub(item).__dict__)
			else:
				search.append(UserGithub(item))
	return search

def get_github_user(query, as_dict = False):
	profile = None
	search = get_search_github(query)
	j = urlopen('https://api.github.com/users/' + urlencode(search[0].login))
	user_data = json.load(j)

	profile = GithubProfile(user_data)

	if as_dict:
		return profile.__dict__
	else:
		return user_data

def get_stackoverflow_user(query, as_dict=False):
	profile = None

	j = urlopen('https://api.stackexchange.com/2.2/users/' + urlencode(query) + '?order=desc&sort=reputation&site=stackoverflow')
	
	compressed_file = io.BytesIO(j.read())
	d = gzip.GzipFile(fileobj=compressed_file)

	user_data = json.load(d)
	
	profile = StackoverflowProfile(user_data)

	if as_dict:
		return profile.__dict__
	else:
		return user_data

def get_combined_profile(gquery, squery, as_dict=False):
	combined_profile = {}
	if gquery != "":
		gprofile = get_github_user(gquery)
		combined_profile['name'] = gprofile['name']
		combined_profile['email'] = gprofile['email']
		combined_profile['avatar_url'] = gprofile['avatar_url']
		combined_profile['followers'] = gprofile['followers']
		combined_profile['public_repos'] = gprofile['public_repos']
		combined_profile['created_at'] = gprofile['created_at']
		combined_profile['updated_at'] = gprofile['updated_at']
		combined_profile['bio'] = gprofile['bio']
		combined_profile['hireable'] = gprofile['hireable']
		combined_profile['location'] = gprofile['location']
	else:
		combined_profile['name'] = ""
		combined_profile['email'] = ""
		combined_profile['avatar_url'] = ""
		combined_profile['followers'] = ""
		combined_profile['public_repos'] = ""
		combined_profile['created_at'] = ""
		combined_profile['updated_at'] = ""
		combined_profile['bio'] = ""
		combined_profile['hireable'] = ""
		combined_profile['location'] = ""
	if squery != "":
		sprofile = get_stackoverflow_user(squery)
		combined_profile['bronze'] = sprofile['items'][0]['badge_counts']['bronze']
		combined_profile['silver'] = sprofile['items'][0]['badge_counts']['silver']
		combined_profile['gold'] = sprofile['items'][0]['badge_counts']['gold']
		combined_profile['reputation'] = sprofile['items'][0]['reputation']
		combined_profile['slink'] = sprofile['items'][0]['link']
	else:
		combined_profile['bronze'] = ""
		combined_profile['silver'] = ""
		combined_profile['gold'] = ""
		combined_profile['reputation'] = ""
		combined_profile['slink'] = ""

	combined_profile['score'] = calculate_score(combined_profile['bronze'], combined_profile['silver'], combined_profile['gold'], combined_profile['reputation'], combined_profile['public_repos'], combined_profile['followers'])
	combined_profile['level'] = calculate_level(combined_profile['score'])

	json_data = combined_profile

	profile = Profile(json_data)

	if as_dict:
		return profile.__dict__
	else:
		return profile

def calculate_score(b, s, g, rep, repos, follow):
	score = b + (2*s) + (3*g) + repos + follow + rep/100
	return score

def calculate_level(s):
	if s<10:
		return 1
	elif s>10 and s<30:
		return 2
	elif s>30 and s<50:
		return 3
	elif s>50 and s<70:
		return 4
	elif s>70 and s<100:
		return 5
	elif s>100 and s<130:
		return 6
	elif s>130 and s<160:
		return 7
	elif s>160 and s<200:
		return 8
	elif s>200 and s<240:
		return 9
	elif s>240 and s<280:
		return 10
	elif s>280 and s<320:
		return 11
	elif s>320:
		return 12
