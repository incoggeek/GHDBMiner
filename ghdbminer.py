from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException, TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
import designs


class GHDBMiner:

    def __init__(self):
        try:
            print(designs.banner)

            # Setup Chrome in headless mode
            chrome_options = Options()
            chrome_options.add_argument("--headless=new")
            chrome_options.add_argument("--log-level=3")
            chrome_options.add_argument("--window-size=1920,1080")
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--disable-dev-shm-usage")
            chrome_options.add_argument("--disable-gpu")
            self.driver = webdriver.Chrome(options=chrome_options)
            self.driver.get(
                "https://www.exploit-db.com/google-hacking-database/")

            print("Select search mode:")
            print("1. Keyword-based")
            print("2. Category-based")

            try:
                mode = input("Enter 1 or 2 > ").strip()

            except (ValueError, KeyboardInterrupt):
                print("Invalid value Exiting.")
                exit()

            if mode == "1":

                try:
                    self.keyword = input("Enter search operator > ").strip()
                    self.category = None

                except (ValueError, KeyboardInterrupt):
                    print("Invalid value Exiting.")
                    exit()

            elif mode == "2":
                print("\nAvailable categories:")
                for k, v in designs.category.items():
                    print(f"{k}: {v}")

                try:
                    cat_id = int(input("Enter category ID > ").strip())
                    self.category = designs.category[cat_id]
                except (ValueError, KeyError, KeyboardInterrupt):
                    print("Invalid category ID. Exiting.")
                    exit()

                self.keyword = ""

                try:
                    self.driver.execute_script(
                        "document.getElementById('showFilters').click();")

                    WebDriverWait(self.driver, 10).until(
                        EC.presence_of_element_located(
                            (By.ID, "categorySelect"))
                    )

                    self.driver.execute_script(f"""
                        var select = document.getElementById('categorySelect');
                        if (select && select.selectize) {{
                            select.selectize.setValue('{cat_id}');
                        }}
                    """)

                    time.sleep(2)

                except Exception as e:
                    print("Failed to apply category filter:", e)
                    self.driver.quit()
                    exit()

            else:
                print("Invalid selection. Exiting.")
                exit()

            self.output_file = None
            save_prompt = input(
                "\nDo you want to save the results to a file? (y/n) > ").strip().lower()
            if save_prompt == 'y':
                self.output_file = input(
                    "Enter output filename (e.g., dorks.txt) > ").strip()

        except Exception as e:
            print(f"Error during initialization: {e}")
            if hasattr(self, 'driver'):
                self.driver.quit()
            exit()

    def dork_mining(self):

        self.extracted_dorks = []

        print(f"\n{designs.FIRE} Latest Google Dorks From GHDB {designs.FIRE}\n")
        try:
            self.driver.implicitly_wait(5)

            while True:
                try:
                    # Scroll to next button (improves visibility in headless)
                    next_btn = self.driver.find_element(
                        By.CSS_SELECTOR, "#exploits-table_next a"
                    )
                    ActionChains(self.driver).scroll_to_element(
                        next_btn).perform()

                except NoSuchElementException:
                    print("Next button not found. Possibly end of pages.")
                    break

                # Extract dorks from current page
                try:
                    table_rows = self.driver.find_elements(
                        By.XPATH, "//table[@id='exploits-table']/tbody/tr"
                    )

                    for row in table_rows:
                        try:
                            link_td = row.find_element(By.XPATH, ".//td[2]")
                            links = link_td.find_elements(By.TAG_NAME, "a")

                            for link in links:
                                dork_text = link.get_attribute("innerText")
                                if not self.keyword or self.keyword.lower() in dork_text.lower():
                                    print(f"{designs.SUCCESS} {dork_text}")
                                    self.extracted_dorks.append(dork_text)

                        except Exception:
                            print("No matching found on this page")
                            continue  # Skip malformed row

                except Exception as e:
                    print(f"Failed to extract table rows: {e}")
                    break

                # Try clicking next
                try:
                    wait = WebDriverWait(self.driver, 10)
                    next_button = wait.until(
                        EC.element_to_be_clickable(
                            (By.CSS_SELECTOR, "#exploits-table_next a"))
                    )
                    self.driver.execute_script(
                        "arguments[0].scrollIntoView(true);", next_button)
                    time.sleep(0.5)
                    next_button.click()
                    time.sleep(5)
                except WebDriverException:
                    print(
                        f"No more pages or something went wrong! {designs.SAD} ")
                    break

        except KeyboardInterrupt:
            designs.red_text(f"\nKeyboard Interrupt {designs.INTE}")

        except WebDriverException:
            designs.red_text(
                f"\nSomething went wrong with web driver! {designs.SAD}")
            designs.yellow_text(
                f"\nOr please check your internet connection! {designs.GLOBE}")

        except Exception as e:
            print(f"Unexpected error: {e}")

        finally:
            if self.output_file and self.extracted_dorks:
                try:
                    with open(self.output_file, "a", encoding="utf-8") as f:
                        for dork in self.extracted_dorks:
                            f.write(dork + "\n")
                    print(
                        f"\nResults saved to {self.output_file} {designs.FILE}")
                except Exception as e:
                    print(f"\nFailed to save file: {e}")

            self.driver.quit()
            print(
                f"\n{designs.GLOBE} Done. Visit: https://www.exploit-db.com/google-hacking-database\n")


# Starts here....
if __name__ == "__main__":
    try:
        tool = GHDBMiner()
        tool.dork_mining()
    except Exception as err:
        print(f"Fatal error: {err}")
