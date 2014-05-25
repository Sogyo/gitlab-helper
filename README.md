GitLab-helper
=======

A service that automatically enrolls users in GitLab groups based on their AD / LDAP group membership. It will only try to enroll a user if a corresponding GitLab group exists. 

This works by registering this service as a GitLab system hook. GitLab will then notify the helper on important events. The event on which this listener will act is the 'user_create' event.

For example: A user has AD group membership 'Foo' and 'Bar'. GitLab is configured with group 'Foo' as well, but lacks 'Bar'. As soon as the user creates an account on GitLab (by logging in with their AD credentials), this service will be notified. The user will then be placed in the 'Foo' group, because it exists on both sides, but its membership of 'Bar' will be ignored.
