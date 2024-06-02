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