from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
import time

# TODO: build class to perform operations to crawl, search, scrape data
class IMDBClass:
  def __init__(self):
    self.website = "https://www.imdb.com/"

  def set_up(self):
    self.driver = webdriver.Chrome()

  def make_search(self, title):
    driver = self.driver
    driver.get(self.website)


  def scrap_data(self, data):
    # grab data from site
    return 1

  def tear_down(self):
    self.driver.close()

def make_web_request(data):
  try:
    imdb_website = requests.get("https://www.imdb.com/")

    soup = BeautifulSoup(imdb_website.text, 'html.parser')
    search_bar = soup.find('id', class_='imdb-header-search__input')
    return 1
  except Exception as error:
        print("Fail: error accessing website - {}".format(error))


def get_movie_date(movie_title):
    movie_data = make_web_request(movie_title)

