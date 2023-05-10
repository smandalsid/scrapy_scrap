import scrapy
from ..items import TutorialItem
from scrapy.http import FormRequest


class quoteScraper(scrapy.Spider):
    name = 'quotes2'
    page_number = 2
    start_urls = [
        'http://quotes.toscrape.com/login',

    ]

    def parse(self, response):
        token=response.css('form input::attr(value)').get()
        return FormRequest.from_response(response, formdata={
            'csrf_token':token,
            'username':'test',
            'password':'1234',
        }, callback=self.start_scraping)
    
    def start_scraping(self, response):
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
            yield response.follow(next_page, callback=self.start_scraping)