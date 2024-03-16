import logging

import scrapy
from scrapy.http.response.html import HtmlResponse


class IStockSpider(scrapy.Spider):
    name = "IStock-dogs"
    allowed_domaings = [
        "freeimages.com",
    ]
    base_url = "https://www.freeimages.com"
    start_urls = [
        "https://www.freeimages.com/search/dogs",
    ]

    images_to_fetch = 1000
    images = []

    def __init__(self):
        self.images_to_fetch = 1000
        self.images = []

    def parse(self, response: HtmlResponse):
        if self.images_to_fetch > 0:
            pictures = response.xpath(
                '//div[contains(@class,"grid-container")]//picture//img/@src'
            ).re(r"https://\s*(.*)")

            for picture in pictures:
                logging.info(f"{picture}")
                self.images_to_fetch -= 1
                self.images.append(picture)

            # The next results button are different in first page and other pages
            # At first page, it shows a button with "See More"
            # In second+ pages shows buttons with "previous" and "next" pages
            next_page = response.css("a.border-search-bar-border ::attr(href)").get()
            if next_page is None:
                next_page = response.css("a.next-page-link ::attr(href)").get()

            if next_page is not None:
                return scrapy.Request(
                    f"{self.base_url}{next_page}", callback=self.parse
                )
