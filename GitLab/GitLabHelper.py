import gitlab
import logging

class GitLabHelper():
    def __init__(self, host, token):
        self.host = host
        self.token = token
        self.__log = logging.getLogger(__name__)
        self.__log.debug("Making a connection to GitLab at " + host)
        self.gitlab = gitlab.Gitlab(host, token=token)

    def get_gitlab_group_names(self):
        raw_groups = self.gitlab.getgroups()
        return [group.get("name") for group in raw_groups]

    def add_user_to_group(self, groupname, user_id):
        group = self.__get_group(groupname)
        if group is None:
            self.__log.debug("Groupname " + groupname + " does not exist in GitLab")
            return
        gid = group.get("id")
        access_level = "developer"
        self.__add_user_to_group(gid, user_id, access_level)

    def __add_user_to_group(self, group_id, user_id, access_level):
        self.__log.debug("Adding user id " + str(user_id) + " to group id " + str(group_id) + " with level " + access_level)
        self.gitlab.addgroupmember(group_id, user_id, access_level, sudo="")

    def __get_group(self, key):
        groups = self.gitlab.getgroups()
        for g in groups:
            if g.get("name") == key:
                return g
        return None