from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time


class Commands:
    def __init__(self) -> None:
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()), options=options
        )

    # Searches for data on Wikipedia
    def get_info(self, query):
        driver = self.driver
        driver.get("https://www.wikipedia.com")
        search = driver.find_element("xpath", '//*[@id="searchInput"]')
        search.click()
        search.send_keys(query)
        btn = driver.find_element("xpath", '//*[@id="search-form"]/fieldset/button/i')
        btn.click()

    # Plays a video or song on YouTube
    def get_vid(self, query):
        self.driver.get("https://www.youtube.com/results?search_query=" + query)
        terms = self.driver.find_element(
            "xpath",
            '//*[@id="content"]/div[2]/div[6]/div[1]/ytd-button-renderer[2]/yt-button-shape/button/yt-touch-feedback-shape/div/div[2]',
        )
        terms.click()
        time.sleep(0.5)
        vid = self.driver.find_element(
            "xpath", '//*[@id="video-title"]/yt-formatted-string'
        )
        vid.click()
