import scrapy, unicodedata

fn = lambda t: unicodedata.normalize('NFKD', t).encode('ascii', 'ignore')

class ExtractQoutes(scrapy.Spider):
    name = "qoutes"
    
    # get the starting link
    start_urls = ["http://quotes.toscrape.com/"]
    allowed_domains = ["toscrape.com"]
    
    def parse(self, res):
        # extract the elements from parsed list
        for q in res.css("div.quote"):
            yield {
            "qoute": fn(q.css("span.text::text").extract_first()),
            "author": fn(q.css("span small.author::text").extract_first()),
            "tags":  q.css("div.tags a.tag::text").extract()
            }
        # get the next page link
        next_link = res.css('.next > a:nth-child(1)::attr(href)').extract_first()
        # print ">>>>>>>>>>>> Going to page %s <<<<<<<<<<<<<< " %(next_link)
        if next_link:
            next_link = res.urljoin(next_link)
            yield scrapy.Request(next_link, self.parse)