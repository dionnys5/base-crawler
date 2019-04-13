from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from tutorial.spiders.quotes_spider import QuotesSpider


settings = get_project_settings()
settings.set('FEED_FORMAT', 'csv')
process = CrawlerProcess(settings)
process.crawl(QuotesSpider)
process.start()
