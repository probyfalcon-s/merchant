FROM python:3.12-slim

WORKDIR /app
# Install postgress server for tests
#RUN apt update && apt install -y postgresql

COPY ./requirements.txt ./requirements.txt

RUN apt-get update && apt-get install -y libgl1

RUN pip install virtualenv
RUN virtualenv -p python venv
RUN /bin/bash -c "source venv/bin/activate"
RUN pip install --upgrade setuptools && pip install -r /app/requirements.txt
RUN playwright install --with-deps

# Copy source code
COPY . /app/.env

ENV PYTHONPATH=/app
ENV PYTHONPATH "/app:/app/tests"

ENV DEV_USER_EMAIL=""
ENV DEV_USER_PASSWORD=""
ENV ADMIN_LOGIN=""
ENV ADMIN_PASSWORD=""
ENV WEB3_PRIVATE_KEY=""
ENV SENDER_ADDRESS=""
ENV RECIPIENT_ADDRESS=""
ENV TEST_USER_USERNAME=""
ENV TEST_USER_PASSWORD=""
ENV TCMS_USERNAME=""
ENV TCMS_PASSWORD=""

ENTRYPOINT ["/app/docker-entrypoint.sh"]
