# twunnel-app

## install

```
git clone https://github.com/jvansteirteghem/twunnel-app.git
cd twunnel-app
# configure <LOCAL/REMOTE.TAC-FILE>
pip install -r requirements.txt
```

## start

```
twistd -n -y <LOCAL/REMOTE.TAC-FILE>
```

or

```
python <PYTHON-DIRECTORY>/Scripts/twistd.py -n -y <LOCAL/REMOTE.TAC-FILE>
```

## stop

```
<CTRL+C>
```