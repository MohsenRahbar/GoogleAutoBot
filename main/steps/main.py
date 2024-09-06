"""
    about test auto Search with google
"""
from behave import given , when , then
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# First step:
@given(u'Launch browser')
def Launch_browser(context):
    """
        This function for Launch browser 
    """
    # lunch to browser:
    context.driver=webdriver.Chrome()
    time.sleep(5)

# Second step:
@when(u'Open Google page')
def Page(context):
    """
        This function for Open Google index page 
    """
    # Open goole page:
    context.driver.get("https://www.google.com")    
    time.sleep(5)

# Third step:
@then(u'Search about toy')
def Search(context):
    """
        This function for Searching 
    """
    text="toy"
    # Find elment and writ text search:
    elment = context.driver.find_element(By.NAME, "q").send_keys(text)
    # Save search box text
    current_value = context.search_box.get_attribute(text)
    time.sleep(5)
    # Check text elment:
    assert current_value == text
    time.sleep(5)
    # Send text:
    elment.submit()
    time.sleep(5)

# Fourth step:
@then(u'close page')
def close_page(context):
    """
        This function for close browser driver
    """
    # Close driver:
    context.driver.quit()
    context.driver.close()
