# IX Control Panel

## Table of Contents

- [What is "IXCP""?](#what-is-ixcp)

## What is "IXCP"?

## Command line usage

**First time usage**

Use git `clone` to download the code. After that generate the database tables and create a superuser:

```sh
$ git clone https://github.com/Charlie-Root/ixcp.git
$ cd ixcp/
$ python3 manage.py makemigrations
$ python3 manage.py migrate
$ python3 manage.py createsuperuser
Username: admin
Email address: your.email@host.com
Password:
Password (again):
Superuser created successfully.
```
Now you can start the server using:
```sh
$ python3 manage.py runserver 0.0.0.0:8080
```