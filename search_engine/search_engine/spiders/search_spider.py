import scrapy


class SearchSpider(scrapy.Spider):
    name = "search"

    allowed_domains = [
        'https://bk.rw/',
        'https://rwanda.accessbankplc.com/',
        'https://www.ecobank.com/'
    ]

    start_urls = [
        'https://bk.rw/',
        'https://www.ecobank.com/'
        ''
    ]

    def parse(self, response):

        # start_urls = [
        #     'https://bk.rw/',
        #     'https://rwanda.accessbankplc.com/',
        #     'https://www.ecobank.com/'
        # ]

        # for link in start_urls:
        print('============================================',
              response.xpath(
                  "//*[contains(text(), 'savings')]").getall(),
              '============================================',
              response.url
              )
