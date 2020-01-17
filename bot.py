from selenium import webdriver
from time import sleep
import random
from secret import username, password
from tweets import duckTweets

class TwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def logIn(self, username, password):
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
        #Find tweet xpath, rt if above a certain rt count
        tweets = driver.find_elements_by_xpath("//div[@data-testid='tweet']")
        rtButtons = driver.find_elements_by_xpath("//div[@data-testid='retweet']")

        #Doesn't work yet, rtButtons not returning anything
        for rtButton in rtButtons:
            rtButton.click()
            sleep(2)
            confirm = driver.find_element_by_xpath("//div[@data-testid='retweetConfirm']")
            confirm.click()
            sleep(2)


    def findQuotes(self):
        driver = self.driver
        driver.get("https://www.brainyquote.com/topics/duck-quotes")

        quotes = driver.find_elements_by_xpath()

    def tweet(self):
        driver = self.driver

        #Select tweet button
        tweetButton = driver.find_element_by_xpath("/html/body/div/div/div/div/header/div/div/div/div/div[3]/a/div")
        tweetButton.click()
        
        #Select blank, send tweet
        blankLine = driver.find_element_by_xpath("/html/body/div/div/div/div[1]/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div[1]/div[1]/div/div/div/div[2]/div/div/div/div")
        tweet = random.choice(duckTweets)
        blankLine.send_keys(tweet)

        #Submit tweet
        submitButton = driver.find_element_by_xpath("/html/body/div/div/div/div[1]/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div[1]/div/div/div/div[2]/div[2]/div/div/div[2]/div[4]/div/span/span")
        submitButton.click()


#scrolling:
# for i in range(1, 2):
#             driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
#             sleep(2)

bot = TwitterBot()
bot.logIn(username, password)
#bot.findQuotes()
bot.retweet()
