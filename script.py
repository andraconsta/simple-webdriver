from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.microsoft import EdgeChromiumDriverManager

# Setup Edge WebDriver with WebDriver Manager
driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

try:
    # Navigate to Bing
    driver.get("https://www.bing.com")

    # Wait for the search box to be present
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "q"))
    )
    
    # Type a query into the search box and press Enter
    search_box.send_keys("Hello World")
    search_box.send_keys(Keys.RETURN)
    
    # Wait for the search results to load
    first_result = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "li.b_algo h2 a"))
    )
    
    # Click on the first search result link
    first_result.click()
    
    print("Clicked on the first link successfully")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Keep the browser open until the user decides to close it
    input("Press Enter to close the browser...")
    driver.quit()
