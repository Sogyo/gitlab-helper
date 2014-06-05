import gitlab
import logging

class GitLabHelper():
    def __init__(self, host, token):
        self.host = host
        self.token = token
        self.__log = logging.getLogger(__name__)
        self.__log.debug("Making a connection to GitLab at " + host)
        self.gitlab = gitlab.Gitlab(host, token=token)

    def get_groups(self):
        return self.gitlab.getgroups(page=1, per_page=200)

    def get_group_by_name(self, name):
        raw_groups = self.get_groups()
        return [group for group in raw_groups if group.get("name") == name]

    def get_gitlab_group_names(self):
        raw_groups = self.get_groups()
        return [group.get("name") for group in raw_groups]

    def add_user_to_group(self, groupname, user_id):
        group = self.__get_group(groupname)
        if group is None:
            self.__log.debug("Groupname " + groupname + " does not exist in GitLab")
            return
        gid = group.get("id")
        access_level = "owner"
        self.__add_user_to_group(gid, user_id, access_level)

    def remove_user_from_group(self, group_name, user_id):
        group = self.__get_group(group_name)
        if group is None:
            self.__log.debug("Groupname " + group_name + " does not exist in GitLab")
            return
        gid = group.get("id")
        self.__remove_user_from_group(gid, user_id)

    def get_gitlab_users(self):
        return self.gitlab.getusers(page=1, per_page=200)

    def __add_user_to_group(self, group_id, user_id, access_level):
        self.__log.debug("Adding user id " + str(user_id) + " to group id " + str(group_id) + " with level " + access_level)
        self.gitlab.addgroupmember(group_id, user_id, access_level, sudo="")

    def __remove_user_from_group(self, group_id, user_id):
        self.__log.debug("Removing user id " + str(user_id) + " from group id " + str(group_id))
        self.gitlab.deletegroupmember(group_id, user_id)

    def __get_group(self, key):
        groups = self.get_groups()
        for g in groups:
            if g.get("name") == key:
                return g
        return None
