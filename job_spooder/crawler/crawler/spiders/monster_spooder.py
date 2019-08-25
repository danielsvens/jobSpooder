import scrapy

from job_spooder.crawler.crawler.items import JobItem


class MonsterSpooder(scrapy.Spider):
    name = 'monster'
    max_pages = 100

    def start_requests(self):
        for i in range(10, self.max_pages):
            yield scrapy.Request(f'https://www.monster.se/jobb/sok/?stpage=1&page={i}', callback=self.parse)

    def parse(self, response):
        self.logger.info('Getting item from Monster.se')
        list_of_jobs = response.xpath("//*[@id='SearchResults']")

        for item in list_of_jobs:
            for i in range(1, 31):
                if item.xpath(f".//section[{i}]/div/div[2]/header/h2/a/text()").get() is not None:
                    yield JobItem(
                        site='Monster',
                        image=item.xpath(f".//section[{i}]/div/div[1]/img/@src").get(),
                        company=item.xpath(f".//section[{i}]/div/div[2]/div[1]/a/text()").get(),
                        title=item.xpath(f".//section[{i}]/div/div[2]/header/h2/a/text()").get(),
                        city=item.xpath(f".//section[{i}]/div/div[2]/div[2]/a/text()").get(),
                        created=item.xpath(f".//section[{i}]/div/div[3]/time/text()").get(),
                        href=item.xpath(f".//section[{i}]/div/div[2]/header/h2/a/@href").get()
                    )
