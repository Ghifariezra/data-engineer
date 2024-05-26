## No.2

To run it :
1. build the postgres image
```
docker build -t {postgres_image_name} -f Dockerfile.postgres .
```
2. run postgres container
if you want to check the result on local (uncomment first the EXPOSE command on dockerfile postgres)
```
docker run -d -p 5432:5432 --name {postgres_container_name} {postgres_image_name}
```
or if you don't
```
docker run -d --name {postgres_container_name} {postgres_image_name}
```
3. build api image
```
docker build -t {api_image_name} -f Dockerfile.api .
```
4. run api container and link it with postgres container
```
docker run -d -p 8000:8000 --name {api_container_name} --link {postgres_container_}:postgres {api_image_name}
```

echo "172.20.214.105 localhost" >> /etc/hosts

netsh interface portproxy add v4tov4 listenport=5432 listenaddress=0.0.0.0 connectport=5432 connectaddress=172.20.214.105