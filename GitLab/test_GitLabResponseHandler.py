import unittest
import json
from GitLab.Events.GitLabCreateUserEvent import GitLabCreateUserEvent
from GitLab.Events.GitLabAddUserToTeamEvent import GitLabUserAddToTeamEvent

from GitLab.GitLabResponseHandler import GitLabResponseHandler


class EchoHandlerTest(unittest.TestCase):

    def setUp(self):
        self.user_create_raw = '{"event_name":"user_create","created_at":"2014-05-23T08:30:32.558Z","name":"Kevin van der Vlist","email":"kvdvlist@sogyo.nl","user_id":3}'
        self.user_add_to_team_raw = '{"event_name":"user_add_to_team","created_at":"2014-05-23T13:23:47.825Z","project_name":"HapOldscool","project_path":"hapoldscool","project_id":6,"user_name":"Arno den Uijl","user_email":"aduijl@sogyo.nl","project_access":"Master"}'

        self.user_create = json.loads(self.user_create_raw)
        self.user_add_to_team = json.loads(self.user_add_to_team_raw)

    def test_user_create(self):
        rh = GitLabResponseHandler()
        event = rh.parse_response_as_event(self.user_create)
        self.assertEqual(event, GitLabCreateUserEvent(self.user_create))
        self.assertEqual(event.get_username(), "kvdvlist")
        self.assertEqual(event.get_user_id(), 3)
        self.assertEqual(event.get_user_email(), "kvdvlist@sogyo.nl")

    def test_user_add_to_team(self):
        rh = GitLabResponseHandler()
        event = rh.parse_response_as_event(self.user_add_to_team)
        self.assertEqual(event, GitLabUserAddToTeamEvent(self.user_add_to_team))