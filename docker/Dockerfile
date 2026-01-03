#FROM python:3.11-slim
#WORKDIR /app
#COPY app/ /app/
#CMD ["python", "resume_engine.py"]



FROM python:3.11-slim

WORKDIR /app

RUN pip install python-docx

COPY app/ /app/
COPY templates/ /app/templates/

CMD ["python", "resume_engine.py"]

