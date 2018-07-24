# importing the requests library
import requests
from base64 import b64encode
userAndPass = b64encode(b"pub_f659688b2a9b357a239437326f3cd282:7fdf6a74e8050761064cd92bf756817fb5a182a6").decode("ascii")
headers = { 'Authorization' : 'Basic %s' %  userAndPass }

# api-endpoint
URL = "https://api.slicktext.com/v1/contacts?limit=40&offset=0"
URL_DELETE = "https://api.slicktext.com/v1/contacts/"
r = requests.get(url = URL, headers=headers)
 
# extracting data in json format
data = r.json()
for users in data["contacts"]:
    user_id = str(users['id'])
    print "Each User: " + str(users)
    print "\n Users: " +user_id
    deleteData = {'action': "DELETE"}
    URL_USER = URL_DELETE+user_id
    print "URL User: " + URL_USER 
    delete = requests.post(url = URL_USER, headers=headers, data=deleteData)
    print "Delete API: "+ str(delete)
    response_delete = delete.text
    print "\n Response: "+ str(response_delete)
# printing the output




