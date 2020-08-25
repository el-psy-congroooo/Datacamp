# Datacamp-Scraper
It's a web scraping model created using Scrapy. Using Scrapy i made spiders to crawl the Datacamp website.



Web Scraping:-
Web Scraping (also termed Screen Scraping, Web Data Extraction, Web Harvesting etc.) is a technique employed to extract large amounts of data from websites whereby the data is extracted and saved to a local file in your computer or to a database in table (spreadsheet) format. Web Scraping is a technique in which we scrape or extract data from the websites according to our requirments.



Scrapy:- 
Scrapy is a free and open-source web-crawling framework written in Python. Originally designed for web scraping, it can also be used to extract data using APIs or as a general-purpose web crawler. It is currently maintained by Scrapinghub Ltd., a web-scraping development and services company.



About model:-
In this model I used python and scrapy which is a python module to buil the model. Using scrapy I created two spiders using scrapy which crawled through the datacamp's website and extracted data like the name of the courses, their description and the name of the chapters included in that course.



How to use:-
To use this model you just have to download the saurce code and then run the python script in your preferred IDE and it will extract the data and store it in a text file which it will create itself. If you want to extract the dats of different technologies courses as in this model i have scraped the data for python courses then you just have to change the start url with the preferred one i.e the url of some other programming language courses.

It conatains two spiders one named "Chapters" which extracts the name of the courses and the chapters included in it and the other named "Description" which extracts name of the courses and thier description, So you can use whichever you  want or need.
