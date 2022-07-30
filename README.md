# jupyterlab-project
cookiecutter project for data science env

create python env
```bash
python3 -m venv venv
source venv/bin/activate
```
install cookiecutter module
```bash
pip --no-cache install --upgrade pip setuptools
pip install cookiecutter
```

download docker image
```bash
cookiecutter https://github.com/sebkaz/jupyterlab-project
```

choose with env You need and run docker 
```bash
docker-compose up -d --build
```

You have full JupyterLab env for data science 

STOP: 
```bash
docker-compose down
```
