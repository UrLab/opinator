FROM python:3.10-alpine

# folder src contains all python files
# folder logs contains all the logs
WORKDIR "/src"

# install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# inject MQTT sub lib
COPY MQTTClient.py .
COPY MQTTSettings.py .

