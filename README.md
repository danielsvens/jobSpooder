# job_spooder

## populate db

set FLASK_APP=application.py

flask db migrate

flask db upgrade

## Spiders

Run the spiders via

scrapy crawl stepstone

scrapy crawl monster
