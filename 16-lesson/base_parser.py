#!/usr/bin/env python3
"""
File: base_parser.py
Author: Zakhidov Beck
Email: admbeck@outlook.com
Github: https://github.com/admbeck
Description: base parser for texnomart.uz
"""
import requests
import json
from config import *

class BaseParser:
    """Main parser class"""
    def __init__(self):
        self.url = URL
        self.host = HOST

    def getHtml(self, link):
        """obtain raw html from the url"""
        return requests.get(link).text

    @staticmethod
    def saveToJson(path):
        """save given data into json file"""
        with open(f'{path}.json', mode='w', encoding='UTF-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
