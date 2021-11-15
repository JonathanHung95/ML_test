FROM ubuntu:18.04

COPY ["requirements.txt", "main.py", "./"]
 
RUN apt update && apt-get install -y wget python3.9 python3-pip && pip3 install -r requirements.txt

ENTRYPOINT ["bash", "./run.sh"]