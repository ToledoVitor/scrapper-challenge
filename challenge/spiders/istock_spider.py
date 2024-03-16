import logging

import scrapy
from scrapy.http.response.html import HtmlResponse

from challenge.infra.storage import ScrapperStorage


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

    @property
    def missing_images(self) -> bool:
        return self.images_to_fetch > 0

    def parse(self, response: HtmlResponse):
        """
        This function is the main responsible for crawling and retrieving data.

        It will start getting images at the first image, and will stop either when
        there`s no more images to get, or there already fetch de desired number of images

        On the first page, theres a little diference from the subsequently pages.
        On first page the next results button are different, it shows a "See More".
        In second+ pages the buttons show "previous" and "next" texts.
        """

        if self.missing_images:
            pictures = response.xpath(
                '//div[contains(@class,"grid-container")]//picture//img/@src'
            ).re(r"https://\s*(.*)")

            for picture in pictures:
                to_save = (picture,)  # More fields can be added here
                self.images_to_fetch -= 1
                self.images.append(to_save)

            next_page = response.css("a.border-search-bar-border ::attr(href)").get()
            if next_page is None:
                next_page = response.css("a.next-page-link ::attr(href)").get()

            if next_page is None and self.missing_images:
                logging.error(
                    f"Missing results: Last page searched, {self.images_to_fetch} images still missing"
                )
            else:
                return scrapy.Request(
                    f"{self.base_url}{next_page}", callback=self.parse
                )

    def close(self, reason):
        ScrapperStorage().save_images(images=self.images)
        return super().close(self, reason=reason)
