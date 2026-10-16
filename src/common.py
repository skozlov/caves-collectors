import requests
from bs4 import BeautifulSoup


class HtmlPageLoader:
    def __init__(self, url: str, timeout_sec: int = 10):
        self.url = url
        self.timeout_sec = timeout_sec

    def load(self) -> BeautifulSoup:
        response = requests.get(
            url=self.url,
            timeout=self.timeout_sec,
            headers={'User-Agent': 'Crawler'},
        )
        response.raise_for_status()
        return BeautifulSoup(response.content, 'lxml')
