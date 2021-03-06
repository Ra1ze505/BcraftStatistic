# DockerSetUp
## Fast install
#### Create clone:
```
git clone https://github.com/Ra1ze505/BcraftStatistic.git
```

#### Create at the root of the project file `.env` example:

```
DEBUG=1
SECRET_KEY=change_me
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]
SQL_ENGINE=django.db.backends.postgresql
SQL_DATABASE=hello_django_prod
SQL_USER=hello_django
SQL_PASSWORD=hello_django
SQL_HOST=db
SQL_PORT=5432
DATABASE=postgres
```

#### Create at the root of the project file `.env.db` example:

``` 
POSTGRES_USER=hello_django
POSTGRES_PASSWORD=hello_django
POSTGRES_DB=hello_django_prod
```

#### Up docker-compose:

```
docker-compose up
```

# Exec container:

```
docker-compose exec --user django <container-name> sh
```
#### Activate venv in container exec:

```
source /src/venv/bin/activate
```

#### Run tests

```
python manage.py test:
```

# You may get errors:
### On windows:
```
standard_init_linux.go:228: exec user process caused: no such file or directory
```
#### you need change separotors CRLF -> LF

### On Linux:
```
ERROR: for web  Cannot start service web: OCI runtime create failed: container_linux.go:380: starting container process caused: exec: "/home/app/web/entrypoint.sh": permission denied: unknown
```
#### you need:
```
chmod +x entrypoint.sh 
```
