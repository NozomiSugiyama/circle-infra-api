# circle-infra-api
Rabbit null API

## Setup

1. Create file the `.env`

```sh
```

check the `.env.sample`

2. Create virtualenv

- Not installed virtualenv

```bash
$ pip install virtualenv
$ virtualenv -p python3 virtualenv
```

- Installed virtualenv
```bash
$ virtualenv -p python3 virtualenv
```

3. Start virtualenv

```bash
$ source virtualenv/bin/activate
```

4. Install dependencies

```bash
$ pip install -U pylint
$ pip install python-dotenv
$ pip install gevent
$ pip install flask
$ pip install flake8
```

- Exit virtualenv
```bash
$ deactivate
```

## Run AppSync-test Apprication

Run main.py
```
$ python3 main.py
```

## Check source lint
```bash
$ flake8 *.py
```

## Editor Setting

https://code.visualstudio.com/docs/python/environments

## Roadmap
1. feat: Reset routing table of routers in department
