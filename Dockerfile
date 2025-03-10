FROM python:3.11

WORKDIR /app

ENV PYDEVD_DISABLE_FILE_VALIDATION=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .


CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]

