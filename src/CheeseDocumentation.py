#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import time

from cheese.cheese import Cheese
from cheese.appSettings import Settings

"""
File generated by Cheese Framework

main file of Cheese Application
"""

if __name__ == "__main__":
    Cheese.init()

    while True:
        try:
            requests.post(f"http://localhost/services/doYouKnowMe?name=Cheese_Documentations&icon=frogieCloudBlack.png&port={Settings.port}&color=85FF77", data='{"TOKEN":"serviceToken"}')
            break
        except:
            time.sleep(1)

    Cheese.serveForever()