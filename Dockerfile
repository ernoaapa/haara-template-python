# Multi-stage Dockerfile: the `dev` target is what the platform runs in
# development mode (source is volume-mounted from the PVC; uvicorn --reload
# hot-restarts on file change). The final stage is the prod image.

FROM python:3.12-alpine AS dev
EXPOSE 8000
CMD ["sh", "-c", "pip install --quiet -r requirements.txt && uvicorn main:app --host 0.0.0.0 --port 8000 --reload"]

FROM python:3.12-alpine
WORKDIR /app
COPY requirements.txt .
RUN pip install --quiet --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
