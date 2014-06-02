class Settings(object):
    def __init__(self,
                 listen_to=None,
                 bind_port=None,
                 ldap_user=None,
                 ldap_pw=None,
                 gitlab_address=None,
                 gitlab_apikey=None):
        self.__listen_to = listen_to
        self.__bind_port = bind_port
        self.__ldap_bind_user = ldap_user
        self.__ldap_bind_password = ldap_pw
        self.__gitlab_address = gitlab_address
        self.__gitlab_apikey = gitlab_apikey

    @property
    def listen_to(self):
        return self.__listen_to

    @property
    def bind_port(self):
        return self.__bind_port

    @property
    def ldap_bind_user(self):
        return self.__ldap_bind_user

    @property
    def ldap_bind_password(self):
        return self.__ldap_bind_password

    @property
    def gitlab_address(self):
        return self.__gitlab_address

    @property
    def gitlab_apikey(self):
        return self.__gitlab_apikey


class SettingsBuilder(object):
    def __init__(self):
        self.__ldap_bind_user = None
        self.__ldap_bind_pw = None
        self.__gitlab_address = None
        self.__gitlab_apikey = None
        self.__bind_port = None
        self.__listen_to = None

    def build(self):
        return Settings(
            listen_to=self.__listen_to,
            bind_port=self.__bind_port,
            ldap_user=self.__ldap_bind_user,
            ldap_pw=self.__ldap_bind_pw,
            gitlab_address=self.__gitlab_address,
            gitlab_apikey=self.__gitlab_apikey
        )

    def with_key_value(self, key, value):
        if key == "ldap_user":
            self.with_ldap_bind_user(value)
        elif key == "ldap_pass":
            self.with_ldap_bind_password(value)
        elif key == "gitlab_address":
            self.with_gitlab_address(value)
        elif key == "gitlab_apikey":
            self.with_gitlab_apikey(value)
        elif key == "listen_to":
            self.with_listen_to(value)
        elif key == "bind_port":
            self.with_bind_port(value)

    def with_ldap_bind_user(self, ldap_user):
        self.__ldap_bind_user = ldap_user

    def with_ldap_bind_password(self, ldap_pw):
        self.__ldap_bind_pw = ldap_pw

    def with_gitlab_address(self, gitlab_address):
        self.__gitlab_address = gitlab_address

    def with_gitlab_apikey(self, gitlab_apikey):
        self.__gitlab_apikey = gitlab_apikey

    def with_listen_to(self, listen_to):
        self.__listen_to = listen_to

    def with_bind_port(self, port):
        self.__bind_port = int(port)