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
        'FEED_URI': 'tutorial_resultados.csv'
    }

    def parse(self, response):
        item = TutorialItem()
        quotes = response.css('span.text::text').extract()
        for q in quotes:
            item['quote'] = q.strip('\n“”\'\"')
            yield item
