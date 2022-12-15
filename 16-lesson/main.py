#!/usr/bin/env python3
"""
File: main.py
Author: Zakhidov Beck
Email: admbeck@outlook.com
Github: https://github.com/admbeck
Description: main file for texnomart.uz parser
"""
from bs4 import BeautifulSoup
import time
from configs import *
from base_parser import BaseParser

class CategoryParser(BaseParser):
    """Parses items by categories"""
    def __init__(self):
        super(CategoryParser, self).__init__()
        self.DATA = {}

    def categoryBlockParser(self, html):
        """docstring for categoryBlockParser"""
        soup = BeautifulSoup(html, 'html.parser')
        categoryLinks = soup.find_all('a', class_='category__link')
        for category in categoryLinks:
            categoryTitle = category.find('h2', class_='content__title').get_text(strip=True)
            print(style.BLUE + categoryTitle)
            time.sleep(5)
            self.DATA[categoryTitle] = []
            categoryLink = self.host + category.get('href')

            categoryPage = self.getHtml(categoryLink)
            self.categoryPageParser(categoryPage, categoryTitle)

    def categoryPageParser(self, categoryPage, categoryTitle):
        """docstring for categoryPageParser"""
        soup = BeautifulSoup(categoryPage, 'html.parser')
        section = soup.find('div', class_='category-content__products')
        products = section.find_all('div', class_='product-item-wrapper')
        for product in products[:3]:
            productName = product.find('a', class_='product-name').get_text(strip=True)


def startCategoryParsing():
    """Starts CategoryParser"""
    parser = CategoryParser()
    category = input("Select category: ") # telefony
    categoryLink = 'https://texnomart.uz/ru/katalog/' + category
    print(style.RED + '====== Parser started working ======' + style.RESET)
    start = time.time()

    html = parser.getHtml(categoryLink)
    print(html)

    finish = time.time()
    print(style.GREEN + f'====== Parser finished working in {round(finish - start, 2)} seconds ======' + style.RESET)


if __name__ == '__main__':
    startCategoryParsing()
