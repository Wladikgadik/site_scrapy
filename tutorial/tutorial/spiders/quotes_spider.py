import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://books.toscrape.com/catalogue/page-1.html'
    ]

    def parse(self, response):
        for quote in response.css('article.product_pod'):
            yield {
                'text': quote.css('h3 a::attr(title)').extract_first()
            }
        next_page = response.css('li.next a::attr(href)').extract_first()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
