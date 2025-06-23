ARG VERSION=0.7.0
FROM us-central1-docker.pkg.dev/database-toolbox/toolbox/toolbox:${VERSION}

WORKDIR /app
COPY tools.yaml /app/tools.yaml

EXPOSE 5000

CMD ["/workspace/toolbox", "--tools-file", "/app/tools.yaml", "--address", "0.0.0.0", "--port", "5000"]
