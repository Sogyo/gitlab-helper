from GitLab.Events.EventEqualityMixin import EqualityMixin


class GitLabUserAddToTeamEvent(EqualityMixin):

    def __init__(self, json):
        self.json = json

    def execute(self, ldaphelper, gitlabhelper):
        pass
