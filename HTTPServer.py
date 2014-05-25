import SimpleHTTPServer
import SocketServer
import cgi
import json
import logging

from GitLab.GitLabHelper import GitLabHelper
from GitLab.GitLabResponseHandler import GitLabResponseHandler
from LDAP.LDAPHelper import LDAPHelper

class ServerHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):

    def do_GET(self):
        return

    def do_POST(self):
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={"REQUEST_METHOD": "POST"}
        )
        raw_json = form.file.read()
        log.info("Receiving a request")
        log.debug(str(raw_json))
        parsed_json = json.loads(raw_json)
        handler.handle(parsed_json, ldaphelper, gitlabhelper)
        SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)


if __name__ == '__main__':
    log = logging.getLogger(__name__)
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(levelname)-8s %(message)s',
                        datefmt='%a, %d %b %Y %H:%M:%S')

    port = 3731
    address = "localhost"
    ldaphelper = LDAPHelper("CN=sonar,OU=Systeem Accounts,DC=sogyo,DC=nl", "secret")
    gitlabhelper = GitLabHelper("http://gittestkevin.sogyo.nl", "secret")
    handler = GitLabResponseHandler()

    Handler = ServerHandler

    httpd = SocketServer.TCPServer(("", port), Handler)

    print "Serving at: http://%(interface)s:%(port)s" % dict(interface=address or "localhost", port=port)
    httpd.serve_forever()