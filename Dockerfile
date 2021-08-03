FROM python:3.9.2
COPY . /pybo
ENV RUN_ENV dev
# ENV APP_CONFIG_FILE=/pybo/config/$CONFIG_FILE.py
WORKDIR /pybo
RUN pip install --no-cache-dir -r requirements.txt
RUN chmod +x /pybo/start_app.sh
# RUN /bin/bash /pybo/db_run.sh
EXPOSE 5000
# CMD ["uvicorn", "app:create_app", "--host", "0.0.0.0", "--port", "8081"]
# ENTRYPOINT  ["flask", "run", "--host", "0.0.0.0"]
# ENTRYPOINT ["gunicorn", "--bind", "0:5000", "app:create_app()"]
ENTRYPOINT ["/bin/bash", "start_app.sh"]