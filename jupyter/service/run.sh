docker build -t aktur/lp-service . ||  exit 666
docker run --rm --name service -p 8000:8000 aktur/lp-service
