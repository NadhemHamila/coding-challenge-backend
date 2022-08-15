# syntax=docker/dockerfile:1

# Using python image image as a base image
FROM python:3.8-slim-buster

# set the working directory in the container
WORKDIR /python-docker

# copy the dependencies file to the working directory
COPY Docker/requirements.txt .

#Install dependencies
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

#copy the remainder of the files in our local working directory to the directory in the docker image
COPY . .

# CMD [ "cd", ".."]
CMD [ "python3", "-m" , "flask", "--app", "src", "--debug", "run", "--host=0.0.0.0"]