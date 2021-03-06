# Copyright 2020(c) The Ontario Institute for Cancer Research. All rights reserved.

FROM ubuntu:18.04
RUN rm /bin/sh && ln -s /bin/bash /bin/sh

# Install
RUN \
  sed -i 's/# \(.*multiverse$\)/\1/g' /etc/apt/sources.list && \
  apt-get update && \
  apt-get -y upgrade && \
  apt-get install -y build-essential libssl-dev bash-completion && \
  apt-get install -y curl git man vim wget && \
  apt-get install -y python3.7 python3.7-dev virtualenv nginx libmysqlclient-dev && \
  apt-get clean

# nvm environment variables
ENV NODE_VERSION 13.6.0
ENV NVM_DIR /root/.nvm

# NODE & NPM
RUN \
  wget -qO- https://raw.githubusercontent.com/nvm-sh/nvm/v0.35.1/install.sh | bash && \
  source $NVM_DIR/nvm.sh && \
  nvm install $NODE_VERSION && \
  nvm alias default $NODE_VERSION && \
  nvm use default && \
  npm install -g npm yarn

# add node and npm to path so the commands are available
ENV NODE_PATH $NVM_DIR/v$NODE_VERSION/lib/node_modules
ENV PATH $NVM_DIR/versions/node/v$NODE_VERSION/bin:$PATH

RUN mkdir -p /srv
ADD billing-api /srv/billing-api
ADD billing-ui /srv/billing-ui

# UI
WORKDIR /srv/billing-ui
RUN \
  yarn install && \
  # yarn add node-sass --force && \
  yarn run build

# API
WORKDIR /srv/billing-api
RUN \
  virtualenv -p python3.7 env && \
  source env/bin/activate && \
  pip install -r requirements.txt && \
  pip install gunicorn

# NGINX
RUN rm -f /etc/nginx/sites-enabled/default
ADD nginx/billing.conf /etc/nginx/sites-enabled/billing.conf

RUN mkdir -p /var/log/gunicorn && mkdir -p /srv/billing-api/logs

# RUN FLASK API
CMD ["/srv/billing-api/run.sh"]
