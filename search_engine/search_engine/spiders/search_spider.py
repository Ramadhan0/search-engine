import scrapy


class SearchSpider(scrapy.Spider):
    name = "search"

    start_urls = [
        'https://bk.rw/',
        'https://rwanda.accessbankplc.com/',
        'https://www.ecobank.com/rw/personal-banking/countries'
    ]

    def parse(self, response):
        page = response.url
