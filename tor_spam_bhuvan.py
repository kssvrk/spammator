#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 21:28:56 2020

@author: radha krishna kavuluri , github.com/kssvrk
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 21:22:00 2020

@author: radha krishna kavuluri , github.com/kssvrk
"""
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys  # Adds chromedriver binary to path
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
fbin="/home/radhakrishna/Desktop/projects/softwares/tor-browser_en-US/Browser/firefox"
torexe = os.popen('/home/radhakrishna/Desktop/projects/softwares/tor-browser_en-US/Browser/TorBrowser/Tor/tor')
binary = FirefoxBinary(fbin)
profile = FirefoxProfile("/home/radhakrishna/Desktop/projects/softwares/tor-browser_en-US/Browser/TorBrowser/Data/Browser/profile.default")
profile.set_preference('network.proxy.type', 1)
profile.set_preference('network.proxy.socks', '127.0.0.1')
profile.set_preference('network.proxy.socks_port', 9050)
profile.set_preference("network.proxy.socks_remote_dns", False)
profile.update_preferences()

male_names='malenames.csv'
female_names='femalenames.csv'
    
def UserNamesList(iteration):
    name_list=[]
    key="prefix_"
    with open(male_names,encoding="utf8") as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        for row in csv_reader:
            name=''.join(e for e in row[0] if e.isalnum())
            if(name!="name" and name!=""):
                name_list.append(f"{key}{name}{iteration}")
        print(f'Processed Malenames.')
        
        
    with open(female_names,encoding="utf8") as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        for row in csv_reader:
            name=''.join(e for e in row[0] if e.isalnum())
            if(name!="name" and name!=""):
                name_list.append(f"{key}{name}{iteration}")
        print(f'Processed FeMalenames.')
        
    return name_list
        
    
def SpamBhuvan(user_name):
    
    
    driver = webdriver.Firefox(firefox_profile=profile,executable_path='/home/radhakrishna/Desktop/projects/python/instaspam/geckodriver')
    cdriver = webdriver.Chrome(executable_path="/home/radhakrishna/Desktop/projects/python/instaspam/chromedriver")
    
    try:
        murl="https://temp-mail.org/"
        #first open temp mail in your chrome and get an email
        cdriver.get(murl)
        cdriver.implicitly_wait(30)
        time.sleep(5)
        cdriver.maximize_window()
        
        input = cdriver.find_element_by_class_name("emailbox-input")
        temp_mail=input.get_attribute('value')
        print(temp_mail+"is the email you gat")
        
        bhuvan_signup='https://bhuvan-cas1.nrsc.gov.in/WebClientProfile.php'
        #second open bhuvan in tor browser.
        driver.get(bhuvan_signup)
        driver.implicitly_wait(30)
        driver.maximize_window()
        
        print('opening signup')
        username=driver.find_element_by_xpath("//*[@name='txtName']")
        username.send_keys(user_name)
        email=driver.find_element_by_xpath("//*[@name='txtEmail']")
        email.send_keys(temp_mail)
        firstname=driver.find_element_by_xpath("//*[@name='txtFirstName']")
        firstname.send_keys("firstname")
        lastname=driver.find_element_by_xpath("//*[@name='txtLastName']")
        lastname.send_keys("lastname")
        driver.find_element_by_xpath("//button[. = 'Submit']").click()
        #driver.quit()
        time.sleep(70)
        #now bhuvan has sent mail to temp mail...click on the temp mail and check the text
        mail_has_come=cdriver.find_element_by_xpath("//a[contains(text(),'Bhuvan')]").click()
        cdriver.implicitly_wait(10)
        #get bhuvan pwrod reset link
        link=cdriver.find_element_by_xpath("//a[contains(text(),'Click here')]").get_attribute("href")
        js=f"window.open('{link}')"
        print("executing"+js)
        driver.execute_script(js)
        WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
        driver.switch_to_window(driver.window_handles[1])
        pw=driver.find_element_by_xpath("//*[@name='txtPassword']")
        pw.send_keys("xuangzhourocks")
        cpw=driver.find_element_by_xpath("//*[@name='txtConfirmPassword']")
        cpw.send_keys("xuangzhourocks")
        driver.find_element_by_id("Button1").click()
        driver.quit()
        cdriver.quit()
    except Exception as e:
        print(f'error occured for username {user_name} as {e}')
if __name__=="__main__":
    
    random='1'
    res=UserNamesList(1)
    for username in res:
        SpamBhuvan(username+random)


    