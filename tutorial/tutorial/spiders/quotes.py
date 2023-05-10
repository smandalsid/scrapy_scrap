import scrapy
from ..items import TutorialItem


class quoteScraper(scrapy.Spider):
    name = 'quotes'
    page_number = 2
    start_urls = [
        'https://quotes.toscrape.com/page/1/',

    ]

    def parse(self, response):
        # title=response.css('title::text').extract()
        # yield{'titletext':title}

        items=TutorialItem()

        all_divs=response.css('div.quote')

        for div in all_divs:

            title=div.css("span.text::text").extract()
            author=div.css("small.author::text").extract()
            tags=div.css("a").xpath("@href").extract()

            items['title']=title
            items['author']=author
            items['tags']=tags
            yield items
        
        # next_page = response.css('li.next a::attr(href)').get()
        next_page="https://quotes.toscrape.com/page/"+str(self.page_number)+"/"
        # if next_page!=None:
        if self.page_number<11:
            self.page_number+=1
            yield response.follow(next_page, callback=self.parse)

