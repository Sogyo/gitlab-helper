from GitLab.Events.EventEqualityMixin import EqualityMixin
import logging

class GitLabCreateUserEvent(EqualityMixin):

    def __init__(self, json):
        self.__log = logging.getLogger(__name__)
        self.json = json

    def execute(self, ldaphelper, gitlabhelper):
        ldap_groups = ldaphelper.groups_of_username(self.get_username())
        self.__log.debug("LDAP groups: " + str(ldap_groups))
        gitlab_groups = gitlabhelper.get_gitlab_group_names()
        self.__log.debug("GitLab groups: " + str(gitlab_groups))

        for group in ldap_groups:
            if group in gitlab_groups:
                self.__log.debug("Adding user " + self.get_user_email() + " to group " + group)
                gitlabhelper.add_user_to_group(group, self.get_user_id())

    def get_username(self):
        return self.get_user_email().split("@")[0]

    def get_user_id(self):
        return self.json.get("user_id")

    def get_user_email(self):
        return self.json.get("email")