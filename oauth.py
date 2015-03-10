from linkedin import linkedin
#import json
#from prettytable import PrettyTable # pip install prettytable


API_KEY = '78w8gcqfrt0sbn'
API_SECRET = 'eLLAFinI25xkmtpG'
RETURN_URL = 'http://localhost:8000'
USER_TOKEN = '6a028c45-b14d-447b-b0a1-ba39044914e7'
USER_SECRET = 'a2f59d06-b091-4210-b776-0828fbbd513c'
auth = linkedin.LinkedInDeveloperAuthentication(API_KEY, API_SECRET, USER_TOKEN, USER_SECRET, RETURN_URL, permissions=linkedin.PERMISSIONS.enums.values())

# Pass it in to the app...

app = linkedin.LinkedInApplication(auth)

# Use the app...

profile = app.get_profile()

#profile_data = linkedin.get_profile('https://api.linkedin.com/v1/people/~?format=json')

print profile



