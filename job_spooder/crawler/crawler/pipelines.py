from sqlalchemy.dialects.postgresql import psycopg2

from job_spooder import db
from job_spooder.models import JobArticle
from sqlalchemy.exc import DataError, InvalidRequestError, IntegrityError
from datetime import datetime


class CrawlerPipeline(object):

    def process_item(self, item, spider):

        if item['city'] is not None:
            item['city'] = item['city'].strip()

        if item['days_left'] is not None:
            item['days_left'] = item['days_left'].strip()

        job_item = JobArticle(
            site=item['site'],
            href=item['href'],
            title=item['title'],
            description=item['description'],
            company=item['company'],
            image=item['image'],
            city=item['city'],
            days_left=item['days_left'],
            created=datetime.now()
        )

        try:
            db.session.add(job_item)
            db.session.commit()
        except DataError as e:
            print(str(e))
        except InvalidRequestError as i:
            print(str(i))
        except IntegrityError:
            print('Article already exist')

        return item
