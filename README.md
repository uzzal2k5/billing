<h1 align="center">Cancer Collaboratory Billing App</h1>

<p align="center"><img alt="General Availability" title="General Availability" src="http://www.overture.bio/img/progress-horizontal-GA.svg" width="320" /></p>

[![](https://images.microbadger.com/badges/image/collaboratory/billing.svg)](https://microbadger.com/images/collaboratory/billing "Get your own image badge on microbadger.com")
[![](https://images.microbadger.com/badges/version/collaboratory/billing:1.0.0.svg)](https://microbadger.com/images/collaboratory/billing:1.0.0 "Get your own version badge on microbadger.com")  

<p align="center">
    <img alt="arch" title="Reporting by cost" src="/docs/billing_cost.png">
</p>
<p align="center">
  Reporting by cost
</p>  
<br>
<p align="center">
    <img alt="arch" title="Reporting by usage" src="/docs/billing_usage.png">
</p>
<p align="center">
  Reporting by usage
</p>    
<br>

## Modules
* [billing-api](billing-api/README.md)
* [billing-ui](billing-ui/README.md)



## Running as a Docker Container
(Graphite instructions are work in progress)
Pull the latest images:
```bash
$ docker pull sitespeedio/graphite
$ docker run --name graphite --restart=always --expose 8080 -p 8080:80 -p 2003:2003 -v <path_to_profile>/.htpasswd:/etc/nginx/.htpasswd -v <path_to_graphite_files>/whisper:/opt/graphite/storage/whisper -v <path_to_graphite_files>/storage-schemas.conf:/opt/graphite/conf/storage-schemas.conf sitespeedio/graphite

$ docker pull collaboratory/billing
```

Once ready, you can run the image. The container has nginx listening on port 8080 so you will need to expose this port. Also you should pass in your configuration file.

```bash
$ docker run --link=graphite -p <host_port>:8080 -p <api_port>:5000 --name billing -v <path_to_config>/default.py:/srv/billing-api/billing/config/default.py collaboratory/billing
```

The configuration file `default.py` takes the form of:
```python
DEBUG = False  # Debug mode for flask
SECRET_KEY = 'random, secret, super duper secret key'
AUTH_URI = 'http://<identity>/v2.0'  # Keystone/Identity API endpoint
MYSQL_URI = 'mysql://<user>:<pass>@<mysql_host>:3306'  # mysql URI
FLASK_LOG_FILE = '/srv/billing-api/logs/billing.log'
BILLING_ROLE = 'billing'
VALID_BUCKET_SIZES = ['daily', 'weekly', 'monthly', 'yearly']  # Bucketing options for query.
```

## License
* [GPLv3 License](LICENSE.md)
