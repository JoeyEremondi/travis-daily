#Based on https://github.com/FiloSottile/travis-cron
import urllib2
import json
import sys

def api_call(url, token=None, data=None):
    print url
    if data:
        data = json.dumps(data)
    req = urllib2.Request(url, data)
    if data:
        req.add_header('Content-Type', 'application/json; charset=UTF-8')
    if token:
        req.add_header('Authorization', 'token ' + token)
        req.add_header("Accept" , 'application/vnd.travis-ci.2+json')
    p = urllib2.urlopen(req)
    return json.loads(p.read())

def travis_ping(travis_token, repository):
    last_build_id = api_call('https://api.travis-ci.org/repos/{}/builds'.format(repository))[0]['id']
    print "Got build ID", last_build_id
    return api_call('https://api.travis-ci.org/builds/{}/restart'.format(last_build_id), travis_token, { 'build_id': last_build_id })['result']
    
def main():
    #print sys.argv[1][0]
    #print sys.argv[2][0]
    travis_ping(sys.argv[1], sys.argv[2])
    
    
if __name__ == "__main__":
    main()
