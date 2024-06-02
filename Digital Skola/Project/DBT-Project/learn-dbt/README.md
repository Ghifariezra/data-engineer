# learn_dbt
Source from: [Here](https://gitlab.com/farhansmg/learn_dbt.git).

## Pre-requisites
create a `virtual env` of python first :
```bash
# create the environment
python -m venv <venv-name>

# activate the environment
<venv-name>\Scripts\activate # for Windows
source <name-venv>/bin/activate # for Linux or Mac
```

### Installation
If you can run on `Linux` or `Mac`:
```bash
sudo apt-get install git libpq-dev python-dev python3-pip
sudo apt-get remove python-cffi
sudo pip install --upgrade cffi
pip install cryptography~=3.4
```

### Build and Run Postgres
You must `build` the docker image and `run` the container
1. build the postgres image
```bash
docker build -t {postgres_image_name} -f Dockerfile.postgres .
```
2. run postgres container
if you want to check the result on local (uncomment first the EXPOSE command on dockerfile postgres)
```bash
docker run -d -p 5432:5432 --name {postgres_container_name} {postgres_image_name}
```

### Run DBT
Before you run `dbt`, you must install `adapter`.
1. install dbt
```bash
python -m pip install dbt-core dbt-postgres
```
2. debug your dbt connection
```bash
dbt debug --profiles-dir ./ --project-dir dbt_dskola_project
```
3. run dbt model
```bash
dbt run --profiles-dir ./ --project-dir dbt_dskola_project
```
4. generate dbt docs
```bash
dbt docs generate --profiles-dir ./ --project-dir dbt_dskola_project
```
5. serve dbt docs
```bash
dbt docs serve --profiles-dir ./ --project-dir dbt_dskola_project
```