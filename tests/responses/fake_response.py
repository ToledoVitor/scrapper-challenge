from scrapy.http import HtmlResponse, Request


def fake_response_from_file(file_name, url=None) -> HtmlResponse:
    """
    To avoid calling the real page and making a call every time a test is run
    this creates a Scrapy fake HTTP response from a HTML file.

    There are few real HTML responses thas was copied and saved as samples.
    They can became out of date at some point, that`s when you should update the samples
    """

    if not url:
        url = 'http://www.example.com'

    request = Request(url=url)
    file_path = file_name
    file_content = open(file_path, 'r').read()

    response = HtmlResponse(
        url=url,
        body=file_content,
        request=request,
        encoding="utf-8",
    )
    return response
