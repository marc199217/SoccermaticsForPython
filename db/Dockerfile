FROM postgres:latest

COPY install-packages-postgres.sh .
RUN ./install-packages-postgres.sh

COPY requirements-postgres.txt /tmp/
RUN pip3 install -r /tmp/requirements-postgres.txt

#RUN useradd --create-home marcnordbruch
#WORKDIR /home/marcnordbruch
#USER marcnordbruch

CMD ["postgres"]