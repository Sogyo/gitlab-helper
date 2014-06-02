import SimpleHTTPServer
import SocketServer
import cgi
import json
import logging

from GitLab.GitLabHelper import GitLabHelper
from GitLab.GitLabResponseHandler import GitLabResponseHandler
from LDAP.LDAPHelper import LDAPHelper
from configuration.ConfigFile import ConfigFile


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
    settings = ConfigFile("settings.conf").settings
    log = logging.getLogger(__name__)
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(levelname)-8s %(message)s',
                        datefmt='%a, %d %b %Y %H:%M:%S')

    ldaphelper = LDAPHelper(settings.ldap_bind_user, settings.ldap_bind_password)
    gitlabhelper = GitLabHelper(settings.gitlab_address, settings.gitlab_apikey)
    handler = GitLabResponseHandler()

    Handler = ServerHandler

    httpd = SocketServer.TCPServer(("", settings.bind_port), Handler)

    print "Serving at: http://%(interface)s:%(port)s" % dict(interface=settings.listen_to or "localhost", port=settings.bind_port)
    httpd.serve_forever()