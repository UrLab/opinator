FROM opinator:base

WORKDIR "/src"

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY *.py .
COPY .env .

CMD ["python3", "main.py"]

