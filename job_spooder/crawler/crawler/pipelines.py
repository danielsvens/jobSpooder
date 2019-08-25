from job_spooder import db
from job_spooder.models import StepStone, Monster
from sqlalchemy.exc import DataError, InvalidRequestError, IntegrityError
from datetime import datetime


class CrawlerPipeline(object):

    def process_item(self, item, spider):

        if item['site'] == 'StepStone':

            job_item = StepStone(
                href=item['href'],
                title=item['title'],
                description=item['description'],
                company=item['company'],
                image=item['image'],
                city=item['city'],
                days_left=item['days_left'].strip() if not None else None,
                created=datetime.now()
            )

        else:

            job_item = Monster(
                href=item['href'],
                title=item['title'],
                company=item['company'],
                image=item['image'],
                city=item['city'],
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
