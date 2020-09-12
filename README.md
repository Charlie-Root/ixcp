# IX Control Panel

## Table of Contents

- [What is "IXCP"?](#what-is-ixcp)
- [Command line usage?](#command-line-usage)

## What is "IXCP"?

Will come soon.

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

## About

### Contributing

Pull requests and stars are always welcome. For bugs and feature requests, [please create an issue](../../issues/new).

### Author

**Wieger Bontekoe**
* [github/Charlie-Root](https://github.com/Charlie-Root)
* [linkedin/wbontekoe](https://www.linkedin.com/in/wbontekoe/)