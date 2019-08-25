import scrapy


class JobItem(scrapy.Item):
    site = scrapy.Field()
    href = scrapy.Field()
    title = scrapy.Field()
    description = scrapy.Field()
    company = scrapy.Field()
    image = scrapy.Field()
    city = scrapy.Field()
    days_left = scrapy.Field()
    created = scrapy.Field()
