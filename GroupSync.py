import logging
from GitLab.GitLabHelper import GitLabHelper
from LDAP.LDAPHelper import LDAPHelper
from configuration.ConfigFile import ConfigFile

if __name__ == '__main__':
    settings = ConfigFile("settings.conf").settings
    log = logging.getLogger(__name__)
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(levelname)-8s %(message)s',
                        datefmt='%a, %d %b %Y %H:%M:%S')

    ldaphelper = LDAPHelper(settings.ldap_bind_user, settings.ldap_bind_password)
    gitlabhelper = GitLabHelper(settings.gitlab_address, settings.gitlab_apikey)

    gitlab_to_be_synced_groups = ["Engineers"]
    itpp = "itpp"
    ignored_users = ["root", "etckeeper"]

    git_users = [user for user in gitlabhelper.get_gitlab_users() if user not in ignored_users]
    for user in git_users:
        ldap_groups = ldaphelper.get_groups_by_username(user.get("username"))
        for group in gitlab_to_be_synced_groups:
            gitlabhelper.add_user_to_group(itpp, user.get("id"))
            if group in ldap_groups:
                log.info("Adding user " + str(user.get("name")) + " to group " + group)
                gitlabhelper.add_user_to_group(group, user.get("id"))
            else:
                log.info("Removing user " + str(user.get("name")) + " from group " + group)
                gitlabhelper.remove_user_from_group(group, user.get("id"))
