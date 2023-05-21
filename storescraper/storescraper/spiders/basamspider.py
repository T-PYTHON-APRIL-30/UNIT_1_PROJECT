import scrapy


class BasamspiderSpider(scrapy.Spider):
    name = "basamspider"
    allowed_domains = ["alajlanonline.com"]
    start_urls = ["https://alajlanonline.com"]

    

    def parse(self, response):
        pass
