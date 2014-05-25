from distutils.core import setup

setup(
    name='gitlab-helper',
    version='0.1',
    packages=['GitLab', 'GitLab.Events'],
    install_requires=['pyapi-gitlab==6.2.3', 'python-ldap'],
    url='',
    license='',
    author='Kevin van der Vlist',
    author_email='kvdvlist@sogyo.nl',
    description='GitLab / AD integration, tailored for Sogyo'
)
