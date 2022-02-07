from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv
import time


urls = [
    {
        "base_url": "https://www.rentrip.in/rent-bike/",
        "recipie": "1"
    }
]



def get_data(website, driver, city, book_at):
    time.sleep(5)
    count =  driver.find_elements_by_xpath("//div[@id='bikehadithere']/div/*")
    lines = []
    for x in count:
        bike_name = x.find_element_by_xpath(".//div[contains(@class,'title-box')]").text
        cost = x.find_element_by_xpath(".//p[contains(@class,'cost')]").text
        print("Bike Name: {} Cost {}, {}, {}, {}".format(bike_name, cost, city, book_at, website))
        lines.append([bike_name, cost, city, book_at, website])
    return lines
        

# https://www.rentrip.in/rent-bike/ahmedabad?pick=04-05-2019&pick_time=18:00&drop=18-05-2019&drop_time=16:00&book_at=hourly

def scrape(driver, urls):
    cities = [
        "ahmedabad",
        "Delhi",
        "Bangalore",
        "Ajmer",
        "aurangabad",
        "Amritsar",
        "Bhopal",
        "bhubaneswar",
        "Chandigarh",
        "Chandigarh-leh",
        "chennai",
        "Coimbatore",
        "Dehradun",
        "delhi--leh",
        "Dharamshala",
        "Ghaziabad", 
        "Goa",
        "gurgaon",
        "Guwahati",
        "Hyderabad",
        "Indore",
        "Jaipur",
        "Jammu",
        "Kolkata",
        "Leh",
        "Shimla",
        "Rishikesh",
        "Pune"

    ]
    book_at = [
        "hour",
        "weekly"
        "daily",
        "monthly"
    ]
    lines = [["bike_name", "cost", "city", "book_at", "website"]]
    for city in  cities:
        for book in book_at:
            url_params = "{}?pick={}&pick_time={}&drop={}&drop_time={}&book_at={}".format(city, "04-05-2019", "18:00", "18-05-2019", "16:00", book)
            print(url_params)
            driver.get("https://www.rentrip.in/rent-bike/" + url_params)
            lines = lines + get_data("https://www.rentrip.in/rent-bike/", driver, city, book)
    with open('renttrip.csv', 'w') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(lines)
    writeFile.close()

def main():
    driver = webdriver.Chrome()
    scrape(driver, urls)
    driver.close()

main()

# driver.get("http://www.python.org")
# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()
