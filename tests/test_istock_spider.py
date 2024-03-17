import unittest

from src.spiders.istock import IStockSpider
from tests.responses.fake_response import fake_response_from_file


class OsdirSpiderTest(unittest.TestCase):
    BASE_PATH = "tests/responses/samples"

    def test_parse_first_page(self):
        spider = IStockSpider(save_on_db=False)
        spider.parse(
            fake_response_from_file(
                f"{self.BASE_PATH}/first_page.html", url="https://www.example.com"
            )
        )

        assert spider.images is not None
        assert len(spider.images) == 60

    def test_parse_second_page(self):
        spider = IStockSpider(save_on_db=False)
        spider.parse(
            fake_response_from_file(
                f"{self.BASE_PATH}/second_page.html", url="https://www.example.com"
            )
        )

        assert spider.images is not None
        assert len(spider.images) == 60

    def test_parse_last_page(self):
        spider = IStockSpider(save_on_db=False)
        spider.parse(
            fake_response_from_file(
                f"{self.BASE_PATH}/last_page.html", url="https://www.example.com"
            )
        )

        assert spider.images is not None
        assert len(spider.images) == 25
