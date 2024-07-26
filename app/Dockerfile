# Set base image
FROM python:3.11.4-slim-buster

# Se Environment Variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV HOME=/home/app
ENV APP_HOME=${HOME}/web

# Creates a user and necessary directories
RUN mkdir -p $HOME && \
    addgroup --system app && \
    adduser --system --group app && \
    mkdir $APP_HOME ${APP_HOME}/static ${APP_HOME}/media

# Sets the working directory 
WORKDIR $APP_HOME

# Copies the application requirements and installs Python dependencies
COPY ./requirements.txt $APP_HOME
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Installs additional system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends netcat && rm -rf /var/lib/apt/lists/*

# Copies an entrypoint script used to initialize the application
COPY ./entrypoint.sh $APP_HOME

# Sets ownership and permissions for the app user
RUN chown -R app:app $APP_HOME && chmod -R 777 $APP_HOME

# Switches to app user
USER app

# Collect Static Files
RUN python manage.py collectstatic --no-input --clear

# Exposes port 8000 for the application
EXPOSE 8000

# Configures a health check using curl
HEALTHCHECK --interval=5s \
            --timeout=3s \
            CMD curl --fail http://localhost:8000/health-check || exit 1

# Sets the entrypoint script and the default command to run the Gunicorn
ENTRYPOINT ["/home/app/web/entrypoint.sh"]
CMD ["gunicorn", "--workers", "3", "--bind", "0.0.0.0:8000", "--timeout", "90", "--access-logfile", "/home/app/web/access.log", "--error-logfile", "/home/app/web/error.log", "myproject.wsgi:application"]

