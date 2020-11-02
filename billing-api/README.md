# Billing API

## Requirements
* Python3.9 & pip
* MySQL development libraries
* Virtualenv
* Docker

## Building / Running
(Graphite instructions are work in progress)
```bash
docker pull sitespeedio/graphite
docker run -itd --name graphite --restart=always --expose 8080 -p 8080:80 -p 2003:2003 -v ~/.htpasswd:/etc/nginx/.htpasswd -v ~/sajter/billing/graphite/whisper:/opt/graphite/storage/whisper -v ~/sajter/billing/graphite/storage-schemas.conf:/opt/graphite/conf/storage-schemas.conf sitespeedio/graphite

virtualenv -p python3.9 env
source env/bin/activate
pip install -r requirements.txt
python run.py
```

## Testing
To run the automated tests, run `pytest` on any of the test___.py files in `billing_server/tests/`

For example run `pytest test_usage_queries.py`

## Developing on a Mac
Getting lib files for MySQL is a little tricky for the mysql-python dependency when using a mac.

Download MySQL: http://dev.mysql.com/downloads/mysql/

Add the following to your `~/.profile`:
```bash
export PATH=/usr/local/mysql/bin:$PATH
export DYLD_LIBRARY_PATH=/usr/local/mysql/lib/
```
