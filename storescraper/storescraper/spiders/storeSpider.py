import scrapy


class StorespiderSpider(scrapy.Spider):
    name = "storespider"
    allowed_domains = ["www.jarir.com"]
    start_urls = ["https://www.jarir.com"]

    def parse(self, response):
        pass