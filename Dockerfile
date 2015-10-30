FROM python:2.7

RUN apt-get update && apt-get install -y python-setuptools libldap2-dev libsasl2-dev && rm -rf /var/lib/apt/lists/*

ADD . /opt/gitlab-helper
WORKDIR /opt/gitlab-helper

RUN pip install pyapi-gitlab==6.2.3
RUN pip install python-ldap
RUN python setup.py install

EXPOSE 3731

CMD ["python", "HTTPServer.py"]
