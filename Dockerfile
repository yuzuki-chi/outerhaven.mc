FROM openjdk:17.0.1

WORKDIR /app

RUN apt update && apt install jq -y

COPY entrypoint.sh /bin/
ENTRYPOINT ["/bin/entrypoint.sh"]