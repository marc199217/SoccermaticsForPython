FROM python:3.8-slim-buster

COPY install-packages.sh .
RUN ./install-packages.sh

COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt

#RUN groupadd --gid 5000 marcnordbruch \
#    && useradd --home-dir /home/marcnordbruch --create-home --uid 5000 \
#    --gid 5000 --shell /bin/bash --skel /dev/null marcnordbruch \
#    && echo "marcnordbruch:giga//games" | chpasswd
#USER marcnordbruch

CMD ["python"]