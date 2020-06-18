from selenium import webdriver
import time

url = 'https://shop.hak5.org/products/hak5-elite-field-kit'
driver = webdriver.Chrome('./chromedriver')
driver.get(url)
price = driver.find_element_by_class_name("current_price").find_element_by_class_name("money")
result = (price.get_attribute('innerHTML').strip('$'))

print ("Your item costs: $" + result +  '\nI will now watch it for changes')



class HackerBot:

    def __init__(self, hacker_url):
        self.hacker_url =  hacker_url
        self.driver = webdriver.Chrome('./chromedriver')

    def get_price(self):
        self.driver.get(self.hacker_url)
        price = self.driver.find_element_by_class_name("current_price").find_element_by_class_name("money")
        return (price.get_attribute('innerHTML').strip('$'))

def main():
    url = 'https://shop.hak5.org/products/hak5-elite-field-kit'
    bot = HackerBot(url)
    last_price = result
    while 1:
        price = bot.get_price()
        if last_price:
            if price < last_price:
                print(f"**** ALERT **** \nPrice dropped: {last_price - price}")
            elif price > last_price:
                print(f"**** ALERT **** \nPrice rose: {price - last_price}")
            else:
                print(f"Price stayed: {price}")
        last_price = price
        time.sleep(3)

if __name__ == "__main__":
    main()
