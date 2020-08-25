import scrapy
from scrapy.crawler import CrawlerProcess


class ChaptersSpider(scrapy.Spider):
    name = 'chapters'

    def start_requests(self):
        url = "https://www.datacamp.com/courses/tech:python"
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        c_link = response.css("div.course-block>a::attr(href)").getall()
        for link in c_link:
            yield response.follow(url=link, callback=self.parse1)

    def parse1(self, response):
        c_titles = response.css("h1.header-hero__title::text").extract()
        ch_titles = set(response.css("h4.chapter__title::text").extract())
        with open("Chapters.txt", "a") as f:
            for title in c_titles:
                f.write(title + ':\n')
            for chapter in ch_titles:
                f.write(chapter)
            f.write('\n\n')


process = CrawlerProcess()
process.crawl(ChaptersSpider)
process.start()
