FROM python:3.8.0-alpine

# set work directory
WORKDIR /usr/src/acidbro

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update \
    && apk add --no-cache --virtual build-dependencies \
    \
    postgresql-dev \
    git \
    autoconf \
    automake \
    \
    && apk add \
    gettext \
    gcc \
    python3-dev \
    musl-dev \
    libxml2-dev libxslt-dev libffi-dev jpeg-dev \
    \
    # cleanup
    && rm -rf /tmp/*


COPY ./requirements.txt .
RUN pip install --upgrade pip setuptools
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# add entrypoint.sh
ADD entrypoint.sh /usr/src/acidbro/
RUN chmod +x /usr/src/acidbro/entrypoint.sh

EXPOSE 8000

#ENTRYPOINT ["/usr/src/acidbro/entrypoint.sh"]

# This command removes containers with <none> Tag
# docker rmi $(docker images -q -f dangling=true)
