import os
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as bs
from lxml import html
from selenium import webdriver
from selenium.webdriver.common.by import By
class item(db.Model):
    id = db.Column(db.Integer(),primary_keys = True)
    name = db.Column(db.String(length=30),nullable = False, unique = True)
    price = db.Column(db.Integer(),nullable = False)
    barcode = db.Column(db.String(length =12),nullable = False,unique = True)
    description = db.Column(db.String(length = 1024),nullable = False,unique = True)


username ="rajatashhpa@gmail.com"
access_key = "mUm0UaR3zImIR3Og9jyCa1NHgAVWj5rvMrIc9Y6kG0klNW0U9U"

class blogScraper:
    # Generate capabilities from here: https://www.lambdatest.com/capabilities-generator/
    def setUp(self):
        capabilities ={
		"build" : "your build name",
		"name" : "your test name",
		"platform" : "Windows 11",
		"browserName" : "Chrome",
		"version" : "97.0",
        "geoLocation": "IN",
        "headless": True
        }
        self.driver = webdriver.Remote(
            command_executor="https://{}:{}@hub.lambdatest.com/wd/hub".format(username, access_key),
            desired_capabilities=capabilities)

    def tearDown(self):
        self.driver.quit()

    def scrapTopic(self, topic):
        driver = self.driver

        # Url
        driver.get("https://www.lambdatest.com/blog/")

        searchBarXpath = "/html[1]/body[1]/section[1]/div[1]/form[1]/label[1]/input[1]"

        # searching topic
        textbox = driver.find_element(By.XPATH,searchBarXpath)
        textbox.send_keys(topic)
        textbox.send_keys(Keys.ENTER)

        source = driver.page_source
        # scraping title
        title_list = []
        soup = bs(source, "html.parser")
        for h2 in soup.findAll("h2", class_="blog-titel"):
            for a in h2.findAll("a", href=True):
                title_list.append(a.text)

        return title_list


if __name__ == "__main__":
    obj = blogScraper()
    obj.setUp()
    print(obj.scrapTopic("scrap"))
    obj.tearDown()