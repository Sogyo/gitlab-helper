from GitLab.Events.GitLabCreateUserEvent import GitLabCreateUserEvent
from GitLab.Events.GitLabAddUserToTeamEvent import GitLabUserAddToTeamEvent
import logging


class GitLabResponseHandler():

    def __init__(self):
        self.__log = logging.getLogger(__name__)

    def handle(self, json, ldaphelper, gitlabhelper):
        event = self.parse_response_as_event(json)
        if event is not None:
            event.execute(ldaphelper, gitlabhelper)

    def parse_response_as_event(self, json):
        if json.get('event_name') == "user_create":
            self.__log.info("Response is user_create")
            return GitLabCreateUserEvent(json)
        elif json.get('event_name') == "user_add_to_team":
            self.__log.info("Response is user_add_to_team")
            return GitLabUserAddToTeamEvent(json)
        else:
            self.__log.debug("Unknown: ignoring response")
            pass