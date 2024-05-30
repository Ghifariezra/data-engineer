# How is work ?

1. Run scripts
```
docker build -t <API-IMAGE-NAME> -f ./images/Dockerfile.api .
```

2. Create Api Container based on Api Image
```
docker run -d -p 8000:8000 --name {CONTAINER-NAME} {API-IMAGE-NAME}
```