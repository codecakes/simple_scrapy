import unicodedata
import scrapy
from scrapy.loader import ItemLoader
from tutorial.items import TutorialItem

# convert unicode from html to string
fn = lambda t: unicodedata.normalize('NFKD', t).encode('ascii', 'ignore')

class ExtractQoutes(scrapy.Spider):
    name = "qoutes"
    
    # get the starting link
    start_urls = ["http://quotes.toscrape.com/"]
    allowed_domains = ["toscrape.com"]

    def parse(self, res):
        # item_loader = res.meta.get('item_loader', None) or ItemLoader(item=TutorialItem(), response=res)
        # extract the elements from parsed list
        # div_quote_loader = res.meta.get('div_quote_loader', None) or item_loader.nested_css("div.quote")
        # div_quote_loader.add_css("quote", "span.text")
        # div_quote_loader.add_css("author", "span small.author")
        # div_quote_loader.add_css("tags", "div.tags a.tag")
        for q in res.css("div.quote"):
            yield {
            "quote": fn(q.css("span.text::text").extract_first()),
            "author": fn(q.css("span small.author::text").extract_first()),
            "tags":  q.css("div.tags a.tag::text").extract()
            }
        # prev_result = res.meta.get('result', [])
        # result = [item_loader.load_item()] + prev_result
        # yield item_loader.load_item()
        # print "result is >>>>>>>", result
        # get the next page link
        next_link = res.css('.next > a:nth-child(1)::attr(href)').extract_first()
        # # print ">>>>>>>>>>>> Going to page %s <<<<<<<<<<<<<< " %(next_link)
        if next_link:
            next_link = res.urljoin(next_link)
            yield scrapy.Request(next_link, self.parse, meta = {
                # 'item_loader': item_loader,
                # 'div_quote_loader': div_quote_loader,
                # 'result': result
                })
        # else:
        #     # yield item_loader.load_item()
        #     yield {'result': result}