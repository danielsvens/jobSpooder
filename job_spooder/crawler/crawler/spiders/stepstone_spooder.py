import scrapy

from job_spooder.crawler.crawler.items import JobItem


class StepstoneSpooder(scrapy.Spider):
    name = 'stepstone'
    max_pages = 200

    def start_requests(self):
        for i in range(1, self.max_pages):
            yield scrapy.Request(f'https://www.stepstone.se/lediga-jobb-i-hela-sverige/sida{i}/', callback=self.parse)

    def parse(self, response):
        self.logger.info('Getting item from StepStone.se')
        list_of_jobs = response.xpath("//*[@id='list-style-foongus']")
        for item in list_of_jobs:
            for i in range(1, 14):
                if item.xpath(f".//article[{i}]/div[2]/div/h5/a/text()").get() is not None:
                    yield JobItem(
                        site='StepStone',
                        image=item.xpath(f".//article[{i}]/div/div/div/a/img/@src").get(),
                        company=item.xpath(f".//article[{i}]/div[2]/div/span[1]/a/text()").get(),
                        title=item.xpath(f".//article[{i}]/div[2]/div/h5/a/text()").get(),
                        description=item.xpath(f".//article[{i}]/div[2]/div/p/text()").get(),
                        created=item.xpath(f".//article[{i}]/div[2]/div/span[2]/span[1]/text()").get(),
                        city=item.xpath(f".//article[{i}]/div[2]/div/span[2]/span[2]/text()").get(),
                        days_left=item.xpath(f".//article[{i}]/div[2]/div/span[2]/span[3]/span/text()").get(),
                        href=item.xpath(f".//article[{i}]/div[2]/div/span[1]/a/@href").get()
                    )
