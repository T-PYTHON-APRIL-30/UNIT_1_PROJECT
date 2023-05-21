import scrapy


class ExtraspiderSpider(scrapy.Spider):
    name = "extraspider"
    allowed_domains = ["www.extra.com/en-sa"]
    start_urls = ["https://www.extra.com/en-sa"]

    def parse(self, response):
        pass
