import scrapy
from scrapy.crawler import CrawlerProcess 


class DescriptionSpider(scrapy.Spider):
    name = "description"

    def start_requests(self):
        url = "https://www.datacamp.com/courses/tech:python"
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        c_link = response.css("div.course-block>a::attr(href)").getall()
        for url in c_link:
            yield response.follow(url=url, callback=self.parse1)
    def parse1(self, response):
        c_name = response.css('h1.header-hero__title::text').getall()
        c_description = response.css('p.course__description::text').getall()
        with open("Courses.txt", "a") as f:
            for name in c_name:
                f.write(name+"\t:\n")
            for des in c_description:
                f.write(des)
            f.write('\n\n\n\n')
                
            
        


process = CrawlerProcess()
process.crawl(DescriptionSpider)
process.start()
