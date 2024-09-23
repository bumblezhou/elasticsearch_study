# A simple project to demo how to use elesticsearch for full-text search.

## How to install:
```bash
curl -fsSL https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo gpg --dearmor -o /usr/share/keyrings/elastic.gpg

echo "deb [signed-by=/usr/share/keyrings/elastic.gpg] https://artifacts.elastic.co/packages/7.x/apt stable main" | sudo tee -a /etc/apt/sources.list.d/elastic-7.x.list

sudo apt update

sudo apt install elasticsearch
```

## How to configure:
```bash
sudo nano /etc/elasticsearch/elasticsearch.yml

. . .
# ---------------------------------- Network -----------------------------------
#
# Set the bind address to a specific IP (IPv4 or IPv6):
#
network.host: localhost
. . .
```

## Start/Enable elasticsearch:
```bash
sudo systemctl start elasticsearch
sudo systemctl enable elasticsearch
```

## Enable basic security:
```bash
sudo nano /etc/elasticsearch/elasticsearch.yml

. . .
# ---------------------------------- Security ----------------------------------
#
#                                 *** WARNING ***
#
# Elasticsearch security features are not enabled by default.
# These features are free, but require configuration changes to enable them.
# This means that users don't have to provide credentials and can get full access
# to the cluster. Network connections are also not encrypted.
#
# To protect your data, we strongly encourage you to enable the Elasticsearch security features. 
# Refer to the following documentation for instructions.
#
# https://www.elastic.co/guide/en/elasticsearch/reference/7.16/configuring-stack-security.html

# Enable basic security
xpack.security.enabled: true

CTRL + X
y, Enter

sudo systemctl restart elasticsearch
export ES_HOME=/usr/share/elasticsearch
sudo $ES_HOME/bin/elasticsearch-setup-passwords auto
y, Enter

Changed password for user apm_system
PASSWORD apm_system = ZzrSBOln7ObEpYa283Iy

Changed password for user kibana_system
PASSWORD kibana_system = AJ2QIFkCltCn0QQq2RhO

Changed password for user kibana
PASSWORD kibana = AJ2QIFkCltCn0QQq2RhO

Changed password for user logstash_system
PASSWORD logstash_system = 2qLfH0XgAGgktFiqQPQy

Changed password for user beats_system
PASSWORD beats_system = 79Zp3CwSUAOwBm23Gkw5

Changed password for user remote_monitoring_user
PASSWORD remote_monitoring_user = cgGgK0DYjCutI0yJP2TH

Changed password for user elastic
PASSWORD elastic = usKuJ3daCL4vf98kQ0Dk
```

## Enable port:
```bash
sudo ufw allow 9200
sudo ufw enable
```

## Test elasticsearch:
```bash
curl -X GET 'http://localhost:9200'
```

## Install python and requred libs:
```bash
sudo apt install python3 -y
sudo apt install python3-pip -y
pip install -r requirements.txt
```

## How to run:
```bash
python3 ./elasticsearch_test.py
python3 ./app.py
```