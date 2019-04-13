import scrapy
from tutorial.items import TutorialItem


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    start_urls = [
        'http://quotes.toscrape.com/'
    ]

    custom_settings = {
        'ITEM_PIPELINES': {
            'tutorial.pipelines.TutorialPipeline': 400
        },
        'LOG_FILE': 'tutorial.log',
        'FEED_FORMAT': 'csv',
        'JOBDIR': 'crawls\\tutorial',
        'FEED_URI': 'tutorial_resultados_2.csv'
    }

    # def parse(self, response):
    #     item = TutorialItem()
    #     quotes = response.css('span.text::text').extract()
    #     for q in quotes:
    #         item['quote'] = q.strip('\n“”\'\"')
    #         yield item

    # def parse(self, response):
    #     item = TutorialItem()
    #     for quote in response.css("div.quote"):
    #         item['quote'] = quote.css("span.text::text").get()
    #         item['autor'] = quote.css("small.author::text").get()
    #         yield item
    #
    #     next_page = response.css('li.next a::attr(href)').get()
    #     if next_page is not None:
    #         next_page = response.urljoin(next_page)
    #         yield scrapy.Request(next_page, callback=self.parse)