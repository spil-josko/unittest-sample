FROM eu.gcr.io/spil-infra-registry/image-python-service:e503c74c98

MAINTAINER BI Data <bidev@spilgames.com>

# Required to acquire credentials
ARG CREDENTIAL_URL=

# Application
COPY microservices-ext/container/ /opt/ext/
COPY container/ /opt/container/
WORKDIR /opt/container

# Install requirements
RUN /opt/ext/git-auth init && pip install -r /opt/container/requirements.txt

RUN apt-get autoremove --yes \
    && apt-get autoclean --yes \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ENV SERVICE_NAME=unittest-sample \
    SERVICE_TAGS=etl \
    LOG_LEVEL=INFO \
    GOOGLE_APPLICATION_CREDENTIALS=/opt/secrets/service-account/key.json

# Entrypoint
ENTRYPOINT ["/opt/container/"]
