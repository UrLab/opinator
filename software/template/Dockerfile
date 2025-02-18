FROM python:3.10-alpine

# folder src contains all python files
# folder logs contains all the logs
VOLUME ["/logs", "/src"]
WORKDIR "/src"

# install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# inject listener lib
COPY listener.py .
