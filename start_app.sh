APP_CONFIG_FILE="/pybo/config/${RUN_ENV}.py"
export APP_CONFIG_FILE
chmod +x db_run.sh
./db_run.sh
echo "Environment: ${RUN_ENV} / APP_CONFIG_FILE: ${APP_CONFIG_FILE}"
gunicorn --bind 0:5000 "app:create_app()"