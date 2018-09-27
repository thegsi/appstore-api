import urllib2
import json

url = 'https://itunes.apple.com/search?term=xxx&country=gb&entity=software&genreId=6018&offset=0&limit=200'

apps = {"results": []}
offset = 450

def getApps():

    def getRequest ():
        global offset

        offsetUrl = 'https://itunes.apple.com/search?term=xxx&country=gb&entity=software&genreId=6018&offset=%d&limit=150' % offset
        appContent = json.loads(urllib2.urlopen(offsetUrl).read())
        # print(len(appContent['results']))
        if len(appContent['results']) > 0 and offset < 500:
            apps['results'].extend(appContent['results'])
            offset += 1
            print('total' + str(len(apps['results'])))
            getRequest()
    # print appContent['results']
    getRequest()

getApps()

filename = 'appstore_books%d.json' % offset

with open(filename, 'w') as outfile:
    json.dump(apps, outfile)
