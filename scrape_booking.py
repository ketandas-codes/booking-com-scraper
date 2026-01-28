
import time
import random
import numpy as np
import pandas as pd
from selenium_stealth import stealth
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException

class BookingScraper:
    def __init__(self, url, timeout=10):
        self.url = url
        self.data = []
        self.seen_hotels = set()
        self.driver = self._initialize_driver()
        self.wait = WebDriverWait(self.driver,timeout)


    def _initialize_driver(self):
        USER_AGENTS = [
                " Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.96 Safari/537.36",
               "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36"
            ]
        options = Options()
        options.add_argument(f"user-agent={random.choice(USER_AGENTS)}")
        options.add_argument("--window-size=1366,768")
        options.add_argument("--lang=en-GB")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-infobars")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--no-first-run")
        options.add_argument("--no-default-browser-check")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-plugins")
        options.add_argument("--disable-plugins-power-saver")
        options.add_argument("--disable-sync")
        prefs = {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.default_content_settings.popups": 0,
        }
        options.add_experimental_option("prefs", prefs)


        driver = uc.Chrome(options=options)
        driver.maximize_window()
        return driver
    
    def apply_stealth(self):
        stealth(
            self.driver,
            languages=["en-US", "en"],
            vendor="Google Inc.",
            platform="Win32",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            fix_hairline=True,
        )

        self.driver.execute_cdp_cmd(
                "Page.addScriptToEvaluateOnNewDocument",
                {
                    "source": """
                    Object.defineProperty(navigator, 'webdriver', {
                        get: () => undefined
                    });
                    """
                }
            )

    def access_website(self):
        self.driver.get(self.url)
        time.sleep(3)

    
    def enter_search_details(self,text):

        try:
            popup = self.wait.until(
                EC.element_to_be_clickable((By.XPATH,"//button[contains(@class,'de576f5064 b46cd7aad7 e26a59bb37 c295306d66 c7a901b0e7 daf5d4cb1c')]"))
            ).click()

        except ElementClickInterceptedException:
            print("element is not visible")

        try:
            city_input = self.wait.until(
                EC.presence_of_element_located((By.XPATH,"//input[contains(@class,'b915b8dc0b')]"))
            ).send_keys(text)
        except TimeoutException:
            print("no load input box")


        try:
            date = self.wait.until(
                EC.element_to_be_clickable((By.XPATH,"//button[contains(@class,'de576f5064 dc15842869 f1f96fdf10 d10abb4e59')]"))
            ).click()
            time.sleep(1)
            month = self.wait.until(
                EC.element_to_be_clickable((By.XPATH,"//button[contains(@class,'de576f5064 b46cd7aad7 e26a59bb37 c295306d66 dda427e6b5 daf5d4cb1c dd4cd5bde4 fe489d9513')]"))
            ).click()
            time.sleep(1)
        except TimeoutException:
            print("elemnsts are not clickable")

        try:
            date_num = self.wait.until(
                EC.element_to_be_clickable((By.XPATH,"//span[@data-date='2026-03-28']"))
            ).click()
            time.sleep(1)
        except TimeoutException:
            print("date number is not clickabel")

        try:
            check_out = self.wait.until(
                EC.element_to_be_clickable((By.XPATH,"//span[@data-date='2026-03-30']"))
            ).click()
            time.sleep(1)
        except TimeoutException:
            print("date number is not clickabel")


    def submit_search(self):        
        try:
            search_btn = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
            ).send_keys(Keys.ENTER)
        except TimeoutException:
            print("searc button is not clickable")
    
    def apply_filters(self):
        try:
            free_cancellation = self.wait.until(
                EC.presence_of_element_located(
                (By.XPATH, "//input[@type='checkbox' and contains(@aria-label,'Free cancellation')]")
                )
            ).click()
        except TimeoutException:
            print("free cancilaitaion si not clickable")

        try:
            private_bathroom = self.wait.until(
                EC.presence_of_element_located((By.XPATH,"//input[@type='checkbox' and @name='roomfacility=38']"))
            )
            self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});",private_bathroom)
            time.sleep(0.5)
            private_bathroom.click()
        except TimeoutException:
            print("private bathromm is not clickable")
        

    def scraping_data(self):

        dom = self.driver.find_elements(By.XPATH,"//div[@data-testid='property-card']")
        for doms in dom:
            try:
            
                name = doms.find_element(By.XPATH,".//div[contains(@class,'b87c397a13 a3e0b4ffd1')]").text
          
            except StaleElementReferenceException:
                print(" Stale element is skipping this hotel")
                continue
            except:
                name = np.nan


            try:
                price = doms.find_element(By.XPATH,".//span[contains(@class,'b87c397a13 f2f358d1de ab607752a2')]").text
           
            except StaleElementReferenceException:
                continue
            except:
                price = np.nan
            
            try:
                hotel_url = doms.find_element(By.XPATH,".//a[contains(@href,'/hotel/')]").get_attribute("href").split("?")[0]
                if hotel_url in self.seen_hotels:
                        continue   
                self.seen_hotels.add(hotel_url)
               
            except StaleElementReferenceException:
                continue
            except:
                hotel_url = np.nan
            try:
                rating = doms.find_element(By.XPATH,".//div[contains(@class,'f63b14ab7a dff2e52086')]").text
               
            except StaleElementReferenceException:
                continue
            except:
                rating = np.nan
            try:
                reviews_count = doms.find_element(By.XPATH,".//div[contains(@class,'fff1944c52 fb14de7f14 eaa8455879')]").text
                
            except StaleElementReferenceException:
                continue
            except:
                reviews_count = np.nan
            try:
                address = doms.find_element(By.XPATH,".//span[contains(@data-testid,'address')]").text
                
            except StaleElementReferenceException:
                continue
            except:
                address = np.nan


            try:
                free_cancellations = doms.find_element(By.XPATH,".//strong[normalize-space()='Free cancellation']").text
                
            except StaleElementReferenceException:
                continue
            except:
                free_cancellations = np.nan
            try:
                no_prepayment = doms.find_element(By.XPATH,".//strong[normalize-space()='No prepayment needed']").text
            
            except StaleElementReferenceException:
                continue
            except:
                no_prepayment = np.nan

            try:
                property_type = doms.find_element(By.XPATH,".//h4[contains(@class,'fff1944c52 f254df5361')]").text
               
            except StaleElementReferenceException:
                continue
            except:
                property_type = np.nan


            try:
                 stay_days= doms.find_element(By.XPATH, ".//div[@data-testid='price-for-x-nights']").text
            
            except StaleElementReferenceException:
                continue
            except:
                stay_days = np.nan
            
            hotel_Data = {
                "hotel_name":name,
                "price": price,
                "hotel_ulr": hotel_url,
                "rating":rating,
                "reviews":reviews_count,
                "address":address,
                "cancellations":free_cancellations,
                "prepayment":no_prepayment,
                "property_type":property_type,
                "stay_dayes":stay_days,  
            }
            self.data.append(hotel_Data)
            
    
        
    def scrolling_and_pagenation(self):
        page = 0
        while True:
            page += 1
            if page == 1:
                for r in range(5):
                    self.driver.execute_script("window.scrollBy(0, 4000);")
                    time.sleep(1)
            else:        
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            self.scraping_data() 
            try:
                next_button = self.driver.find_element(By.XPATH,"//button[.//span[normalize-space()='Load more results']]")
                time.sleep(0.5)
                self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", next_button)
                time.sleep(0.3)
                next_button.click()
            except NoSuchElementException:
                print("No more pages to load")
                break
        
    def save_to_csv(self):
        df = pd.DataFrame(self.data)
        df.to_csv("Booking.com_data.csv",index=False)
        print(" Scraping complete!")
    

    def script_run(self, text="New Delhi"):
        try:
            self.apply_stealth()
            self.access_website()
            self.enter_search_details(text)
            self.submit_search()
            self.apply_filters()
            self.scrolling_and_pagenation()
            self.save_to_csv()
        finally:
            self.driver.quit()


if __name__ == "__main__":
    scraper = BookingScraper(url="https://www.booking.com/")
    scraper.script_run(
        text="New Delhi"
    )

                

            
    



            





       

