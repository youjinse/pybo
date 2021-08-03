FROM python:3.9.2
COPY . /pybo
ENV APP_COFNIG_FILE /pybo/config/dev.py
ENV APP_CONFIG_FILE=$APP_COFNIG_FILE
WORKDIR /pybo
RUN pip install --no-cache-dir -r requirements.txt
RUN chmod +x /pybo/start_app.sh
EXPOSE 5000
# CMD ["uvicorn", "app:create_app", "--host", "0.0.0.0", "--port", "8081"]
# ENTRYPOINT  ["flask", "run", "--host", "0.0.0.0"]
ENTRYPOINT ["gunicorn", "--bind", "0:5000", "app:create_app"]