from selenium import webdriver
from time import sleep

class TwitterBot:
    def __init__(self, username, password):
        self.driver = webdriver.Chrome()
        self.driver.get("https://twitter.com")
        sleep(2)

        logInxPath = "/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/div/a[2]"
        logIn = self.driver.find_element_by_xpath(logInxPath)
        logIn.click()

        sleep(2)
        
        uNamexPath = "/html/body/div[1]/div[2]/div/div/div[1]/form/fieldset/div[1]/input"
        uName = self.driver.find_element_by_xpath(uNamexPath)
        uName.send_keys(username)

        sleep(2)

        pWordxPath = "/html/body/div[1]/div[2]/div/div/div[1]/form/fieldset/div[2]/input"
        pWord = self.driver.find_element_by_xpath(pWordxPath)
        pWord.send_keys(password)

        sleep(2)

        logxPath = "/html/body/div[1]/div[2]/div/div/div[1]/form/div[2]/button"
        log = self.driver.find_element_by_xpath(logxPath)
        log.click()

        sleep(5)

    def retweet(self):
        driver = self.driver

        #Scroll to load tweets
        for i in range(1, 5):
            driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
            sleep(2)
            

        

bot = TwitterBot("username", "password")
bot.retweet()
