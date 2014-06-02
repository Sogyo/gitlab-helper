import StringIO
import unittest
from configuration.ConfigFile import ConfigFile


class Test(unittest.TestCase):

    def setUp(self):
        self.example_config = StringIO.StringIO()
        self.example_config.write("# Configuration for gitlab helper: \n")
        self.example_config.write("listen_to|localhost \n")
        self.example_config.write("bind_port|3731 \n")
        self.example_config.write("ldap_user|user \n")
        self.example_config.write("ldap_pass|secret \n")
        self.example_config.write("gitlab_address|http://foo.bar \n")
        self.example_config.write("gitlab_apikey|mysecretkey \n")
        self.example_config.seek(0)

    def tearDown(self):
        pass

    def test_valid_configuration(self):
        c = ConfigFile()
        settings = c._file_reader(self.example_config)
        self.assertEqual(settings.listen_to, "localhost")
        self.assertEqual(settings.bind_port, 3731)
        self.assertEqual(settings.ldap_bind_user, "user")
        self.assertEqual(settings.ldap_bind_password, "secret")
        self.assertEqual(settings.gitlab_address, "http://foo.bar")
        self.assertEqual(settings.gitlab_apikey, "mysecretkey")
