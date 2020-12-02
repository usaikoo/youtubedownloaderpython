
FROM ubuntu:20.04
RUN apt-get update && apt-get install -y python3 python3-pip python3-dev 
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip3 install -r requirements.txt
COPY . /app
RUN ls -l
VOLUME [ "/app/Videos" ]
ENTRYPOINT [ "python3" ]
CMD [ "main.py" ]