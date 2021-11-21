FROM ubuntu:18.04

COPY ["requirements.txt", "app.py", "model.pkl", "README.md", "./"]

RUN mkdir ./templates
COPY ./templates/form.html ./templates
 
RUN apt-get update 
RUN apt-get install -y wget python3.9 python3-pip 
RUN pip3 install -r requirements.txt

ENTRYPOINT ["app.py"]