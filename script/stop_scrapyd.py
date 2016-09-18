import urllib2
import urllib
import json

cancel_url = "http://localhost:6800/cancel.json"
listjobs_url = "http://localhost:6800/listjobs.json"


values = {'project': 'bookspider'}
url_params = urllib.urlencode(values)
req = urllib2.Request(listjobs_url + "?" + url_params)
response = urllib2.urlopen(req)
json_response = response.read()
json_response = json.loads(json_response)
print json_response
for item in json_response['running']:
    id = item['id']
    values = {'project': 'bookspider', 'job': id}
    print 'stop:', values
    url_params = urllib.urlencode(values)
    req = urllib2.Request(cancel_url, url_params)
    response = urllib2.urlopen(req)
    json_response = response.read()
    print json_response
