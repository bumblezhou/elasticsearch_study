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

## Enable port:
```bash
sudo ufw allow 9200
sudo ufw enable
```

## Test elasticsearch:
```bash
curl -X GET 'http://localhost:9200'
```

## Install python client:
```bash
python -m pip install elasticsearch
```