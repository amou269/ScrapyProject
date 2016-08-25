import scrapy


class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["stats.nba.com"]
    start_urls = [
        "http://stats.nba.com/stats/boxscoretraditionalv2?EndPeriod=10&EndRange=28800&GameID=0021500107&RangeType=0&Season=2015-16&SeasonType=Regular%20Season&StartPeriod=1&StartRange=0"
    ]

    def parse(self, response):
        print response.body

