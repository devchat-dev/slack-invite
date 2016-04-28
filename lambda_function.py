import urllib
import urllib2

token = '<your slack token here>'
url = 'https://<your-slack-team-name-here>.slack.com/api/users.admin.invite'

def invite(email):
    values = dict(email=email, token=token)
    data = urllib.urlencode(values)
    req = urllib2.Request(url, data)
    response = urllib2.urlopen(req)
    resp  = response.read()

    return resp

def lambda_handler(event, context):
    email = event.get('email')
    
    # You can handle Slack's API response on the front end
    return invite(email)
