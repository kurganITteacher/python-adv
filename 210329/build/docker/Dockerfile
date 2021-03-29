FROM alpine:3.12

ARG workdir='/home/kpk'

ENV LANG='en_US.UTF-8' \
    LANGUAGE='en_US:en' \
    LC_ALL='en_US.UTF-8' \
    PYTHONUNBUFFERED=1

ENV KPK_BIN="${workdir}/bin" \
    KPK_DATA="${workdir}/data"

RUN apk update && \
    apk add --no-cache \
        sudo \
        python3 \
        py3-pip && \
    rm -rf /var/cache/apk/* /var/tmp/* /tmp/*

RUN pip3 install django==2.2

RUN mkdir -p "$KPK_BIN" \
    "$KPK_DATA"

ADD ./sbin /usr/local/bin

WORKDIR ${workdir}

VOLUME $KPK_DATA

EXPOSE 8000/tcp

CMD "run.sh"
