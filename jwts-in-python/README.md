# Creation Python environment

``` 
mkdir jwts-in-python
cd jwts-in-python
```

## Create an environment named  *_env_*:
``` 
python -m venv env
```

## I can activate it and install the latest version of *_pip_*:
```
D:\Python\jwts-in-python>env\Scripts\activate
pip install -U pip
```

## Generating an RSA key pair 
```
mkdir ~/jwts-in-python/.ssh
ssh-keygen -t rsa
```

## Instal rquirements

``` 
pip install pyjwt[crypto]
pip install ipython
``` 