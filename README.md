# twunnel-app

## install

```
git clone https://github.com/jvansteirteghem/twunnel-app.git
cd twunnel-app
pip install -r requirements.txt
# or: pip install --use-wheel --no-index --find-links=pip -r requirements.txt
# configure: <LOCAL/REMOTE.TAC-FILE>
```

## start

```
twistd -n -y <LOCAL/REMOTE.TAC-FILE>
# or: python <PYTHON-DIRECTORY>/Scripts/twistd.py -n -y <LOCAL/REMOTE.TAC-FILE>
```

## stop

```
<CTRL+C>
```