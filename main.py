import csv
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


def validate_search_result(product_name):
    wait_timeout = 10
    driver = webdriver.Firefox(executable_path="./geckodriver")
    driver.get("https://www.supplyhouse.com/")
    driver.implicitly_wait(wait_timeout)
    import time
    time.sleep(15)
    search_box = driver.find_element_by_id("react-header-search-input")
    search_box.send_keys(product_name)
    ActionChains(driver).click(search_box).perform()
    try:
        WebDriverWait(driver, wait_timeout).until(
            lambda d: d.find_element_by_xpath('//*[@id="global-header"]/div[2]/div[3]/div[1]/form/div/div[2]'))
    except Exception as e:
        print(f"No search suggestion appear for the product name: {product_name}")
    else:
        suggestion_section = driver.find_element_by_xpath('//*[@id="global-header"]'
                                                          '/div[2]/div[3]/div[1]/form/div/div[2]/div[1]/div[1]')
        suggestion_product_names = suggestion_section.find_elements_by_tag_name("div")
        print("Number of suggestion", len(suggestion_product_names))

    finally:
        driver.quit()


def main():
    with open("test_data.csv", "r") as fp:
        test_data = csv.reader(fp)
        for product_name in test_data:
            validate_search_result(product_name)


if __name__ == "__main__":
    main()
