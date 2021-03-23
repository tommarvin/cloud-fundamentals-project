FROM python:3.7
WORKDIR /gwc-project
COPY . .
RUN pip install -r requirements.txt
EXPOSE 5000
ENTRYPOINT ["python", "run.py"]