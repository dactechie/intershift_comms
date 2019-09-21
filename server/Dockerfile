# VERSION 1.0
# AUTHOR: Aftab Jalal
# SOURCE: https://github.com/nethacker/ubuntu-flask-gunicorn-docker

FROM nethacker/ubuntu-18-04-python-3:python-3.7.3

RUN apt-get update
RUN apt-get install apt-transport-https

RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN curl https://packages.microsoft.com/config/ubuntu/18.04/prod.list > /etc/apt/sources.list.d/mssql-release.list
RUN exit
RUN apt-get update
RUN ACCEPT_EULA=Y apt-get install -y msodbcsql17
RUN ACCEPT_EULA=Y apt-get install -y mssql-tools
RUN apt-get install unixodbc-dev


ENV SSH_PASSWD "root:Docker!"
USER root

RUN echo exit 0 > /usr/sbin/policy-rc.d

# enable ssh logins
# https://docs.microsoft.com/en-us/azure/app-service/containers/tutorial-custom-docker-image#build-the-image-from-the-docker-file

RUN apt-get update \
        && apt-get install -y --no-install-recommends dialog \
        && apt-get update \
  && apt-get install -y --no-install-recommends openssh-server \
  && echo "$SSH_PASSWD" | chpasswd 

COPY sshd_config /etc/ssh/
EXPOSE 2222
RUN service ssh start

COPY requirements.txt /root/
RUN pip install -r /root/requirements.txt && useradd -m ubuntu
ENV HOME=/home/ubuntu
USER ubuntu
COPY app.py logging.conf settings.py extensions.py /usr/src/
COPY apis /usr/src/apis

WORKDIR /usr/src
EXPOSE 5000
#ENV GUNICORN_CMD_ARGS="--bind=0.0.0.0:5000 --workers=3 --log-config=logging.conf --access-logfile=/var/log/gunicorn_access.log --error-logfile=/var/log/gunicorn_error.log"
ENV GUNICORN_CMD_ARGS="--bind=0.0.0.0:5000 --workers=3 --log-file=- --preload --access-logfile=/var/log/gunicorn_access.log --error-logfile=/var/log/gunicorn_error.log"

USER root
RUN chmod -R 777  /var/log/
RUN PYTHONPATH=/usr/src

CMD ["gunicorn", "app:app"]


