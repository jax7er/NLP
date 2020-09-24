from typing import Generator
from urllib.request import urlopen

from bs4 import BeautifulSoup as bs


def get(url: str) -> Generator:
    html = urlopen(url).read()

    text = bs(html, "html.parser").get_text(separator=" ", strip=True).lower()

    yield from map(str.strip, text.split())