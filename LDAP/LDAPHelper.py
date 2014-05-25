import ldap
import logging

class LDAPHelper():
    def __init__(self, binddn, bindpass):
        self.__log = logging.getLogger(__name__)
        self.host = "ldap://dc01.sogyo.nl:389"
        self.basedn = "DC=sogyo,DC=nl"
        self.binddn = binddn
        self.bindpass = bindpass
        self.__log.debug("Initializing LDAP connection with " + self.host)
        self.ldapcon = ldap.initialize(self.host)

    def groups_of_username(self, username):
        self.__log.info("Retrieving membership of " + username)
        attributes = ['memberOf']
        filter = "(sAMAccountName=" + username + ")"
        result = self.__do_query(filter, attributes)[0]
        groups = [x.split(',')[0].split('=')[1] for x in result.get("memberOf")]
        self.__log.debug("User" + username + " is a member of groups " + str(groups))
        return groups

    def __do_query(self, filter, attributes):
        try:
            self.ldapcon.protocol_version = ldap.VERSION3
            self.ldapcon.set_option(ldap.OPT_REFERRALS, 0)

            bind = self.ldapcon.simple_bind_s(self.binddn, self.bindpass)

            result = self.ldapcon.search_s(self.basedn, ldap.SCOPE_SUBTREE, filter, attributes)

            results = [entry for dn, entry in result if isinstance(entry, dict)]
        finally:
            self.ldapcon.unbind()
        return results