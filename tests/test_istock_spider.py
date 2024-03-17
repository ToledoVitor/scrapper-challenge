import unittest
from tests.responses.fake_response import fake_response_from_file

from src.spiders.istock import IStockSpider


class OsdirSpiderTest(unittest.TestCase):
    BASE_PATH = "tests/responses/samples"

    def setUp(self):
        self.spider = IStockSpider(save_on_db=False)

    def test_parse_first_page(self):
        self.spider.parse(fake_response_from_file(f'{self.BASE_PATH}/first_page.html'))

        assert self.spider.images is not None
        print(len(self.spider.images))
        assert len(self.spider.images) == 61

    def test_parse_second_page(self):
        self.spider.parse(fake_response_from_file(f'{self.BASE_PATH}/second_page.html'))

        assert self.spider.images is not None
        print(len(self.spider.images))
        assert len(self.spider.images) == 61

    def test_parse_last_page(self):
        self.spider.parse(fake_response_from_file(f'{self.BASE_PATH}/last_page.html'))

        assert self.spider.images is not None
        print(len(self.spider.images))
        assert len(self.spider.images) == 26
