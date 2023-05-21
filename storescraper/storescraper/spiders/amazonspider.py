import scrapy


class AmazonspiderSpider(scrapy.Spider):
    name = "amazonspider"
    allowed_domains = ["www.amazon.sa"]
    start_urls = ["https://www.amazon.sa/s?rh=n%3A12463162031"]

    def parse(self, response):
        pass
