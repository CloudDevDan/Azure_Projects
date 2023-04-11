import requests
from creds import *

# CLIENT_ID, SECRET_TOKEN, USERNAME + PASSWORD saved to creds.py - ignored from commit

# started this script following: https://towardsdatascience.com/how-to-use-the-reddit-api-in-python-5e05ddfd1e5c

# populate readme.md
r = open("../readme.md", "w")
r.write("# AZURE PROJECTS\n")
r.write("\n![AZURE PROJECTS](banner.png 'AZURE PROJECTS')")
r.write("""

Following on from the success of [Azure Pirate](https://clouddevdan.co.uk/azure-pirate), I've been busy working behind the scenes to launch a new Azure community initiative, called AZURE PROJECTS!

## What is it?

Azure Projects is a community initiative to facilitate a "learn by doing" approach to Microsoft Azure and related technologies.

Here's the concept: you've been upskilling in an area of Azure and are ready to have a go yourself, but need a little inspiration on what to try.

This is where Azure Projects comes in!

For more information, please view my blog post, [here](https://clouddevdan.co.uk/azure-projects).

**Note that this GitHub repository has replaced the subreddit.**

**The project has been archived as of April 2023.**

## Projects:

| Title         | Author     | Tag |
|--------------|-----------|------------|""")

# note that CLIENT_ID refers to 'personal use script' and SECRET_TOKEN to 'token'
auth = requests.auth.HTTPBasicAuth(CLIENT_ID, SECRET_TOKEN)

# here we pass our login method (password), username, and password
# had too disable mfa on my reddit account for the below to work
data = {'grant_type': 'password',
        'username': USERNAME,
        'password': PASSWORD}

# setup our header info, which gives reddit a brief description of our app
headers = {'User-Agent': 'az_proj_archive/0.0.1'}

# send our request for an OAuth token
res = requests.post('https://www.reddit.com/api/v1/access_token',
                    auth=auth, data=data, headers=headers)

# convert response to JSON and pull access_token value
TOKEN = res.json()['access_token']

# add authorization to our headers dictionary
headers = {**headers, **{'Authorization': f"bearer {TOKEN}"}}

# while the token is valid (~2 hours) we just add headers=headers to our requests
requests.get('https://oauth.reddit.com/api/v1/me', headers=headers)

################

res = requests.get("https://oauth.reddit.com/r/azureprojects",
                   headers=headers)

for post in res.json()['data']['children']:
    if post['data']['title']=='r/azureprojects Lounge':
        continue
    
    print(f"Archiving: {post['data']['title']}")

    # post meta and content to markdown file
    filename = f"{post['data']['title'].lower().replace(' ', '_')}.md"
    f = open(f"../posts/{filename}", "w")
    f.write(f"# {post['data']['title']}\n\n")
    f.write(f"- Author: [{post['data']['author']}](https://www.reddit.com/user/{post['data']['author']})\n")
    f.write(f"- Category: {post['data']['link_flair_text'].replace('&amp;', '&')}\n")
    f.write("\n---\n")
    f.write("\n")
    f.write(post['data']['selftext'])
    f.close()

    # update readme.md with info
    r.write(f"\n| [{post['data']['title']}](posts/{filename}) | [{post['data']['author']}](https://www.reddit.com/user/{post['data']['author']}) | {post['data']['link_flair_text'].replace('&amp;', '&')} |")

# close readme.md
r.close()