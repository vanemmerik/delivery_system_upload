from dotenv import load_dotenv
import os
import requests
# Load environment variables from .env file
load_dotenv()

# test values
pub_id = os.getenv('PUB_ID')
client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')
access_token_url = "https://oauth.brightcove.com/v4/access_token"
file_path = "plugins/"
file_name = "chapter_bar/cuepoints.js"
repo_name = "plugins"

# create the access token
def get_access_token():
    access_token = None
    r = requests.post(access_token_url, params="grant_type=client_credentials", auth=(client_id, client_secret),
    verify=True)
    if r.status_code == 200:
        access_token = r.json().get('access_token')
    # print(access_token)
    return access_token


# Upload to Repo function

# Returns response from API
def upload_to_repo(file_path, file_name):
    full_file_path = os.path.join(file_path, file_name)
    access_token = get_access_token()
    headers = {'Authorization': 'Bearer ' + access_token}
    url ="https://repos.api.brightcove.com/v1/accounts/{pubid}/repos/{repname}/files/{filename}".format(
        pubid=pub_id,
        repname=repo_name,
        filename=file_name
    )
    with open(full_file_path, "rb") as f:
        file = {"contents": (file_name, f)}
        r = requests.request("PUT", url, headers=headers, files=file)
        response = r.json()
    return response

# Upload to the repo
result = upload_to_repo(file_path, file_name)
print(result)