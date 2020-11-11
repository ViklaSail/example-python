import requests
import urllib.request
import time
from bs4 import BeautifulSoup
# INSTRUCTIONS 
# Mocking https://docs.python.org/3/library/unittest.mock-examples.html
# google: python unittest mock tutorial
# https://www.youtube.com/watch?v=NnodfeQCmPQ mocking request.get
# 
# configure VSCode: shift+ctrl+p. Following you should configure: 
#    python: configure tests. python: select interpreter  
#
# example getData  https://datacatalog.worldbank.org/dataset/world-development-indicators
# https://datahelpdesk.worldbank.org/knowledgebase/articles/898581-api-basic-call-structures
# creating conda envs in vscode https://code.visualstudio.com/docs/python/environments#_conda-environments, https://github.com/microsoft/vscode-python/issues/3732
# example: conda create -n env-01 python=3.8.2 

def getData():
    # url = 'http://web.mta.info/developers/turnstile.html'
    url = 'http://api.worldbank.org/v2/country/all/indicator/SP.POP.TOTL?format=json'
    response = requests.get(url) # task: mock this function. if applicable use with your own data source (URL)
    return response
  

if __name__ == '__main__':
    data = getData()