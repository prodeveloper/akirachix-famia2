FROM ubuntu:16.04
# Commands to run to install dependencies
RUN apt-get update -y
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
run pip3 install --upgrade pip
run pip3 install flask
run pip3 install peewee
run mkdir app

WORKDIR /app

# When you pass commands to the container, what should interpret them
ENTRYPOINT ["python3"]

# Command to run when the container starts
CMD ["main.py"]

# Working directory

# Make port available
EXPOSE 8080
expose 465
