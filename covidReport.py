#!/usr/bin/env python

from selenium import webdriver
import time, requests, bs4

def findAndClick(cssSelector):
	elem = browser.find_element_by_css_selector(cssSelector)
	elem.click()

def addDataPoint(cssSelector):
	covidData.append(browser.find_element_by_css_selector(cssSelector).text)

#Open Firefox and navigate to IN coronavirus portal
browser = webdriver.Firefox()
browser.get('https://www.coronavirus.in.gov/map/test.htm#')

#Click link to show school data
findAndClick('#left-tabs-example-tab-third')

#Search for White Lick Elementary
searchField = browser.find_element_by_css_selector('div.rbt:nth-child(2) > div:nth-child(1) > input:nth-child(1)')
searchField.send_keys('white lick')

#Select White Lick
findAndClick('#school-typeahead-item-0')

#Scrape page data
covidData = []
#Results as of:
addDataPoint('.header > div:nth-child(1) > b:nth-child(1)')
#Updated on:
addDataPoint('.header > div:nth-child(1) > b:nth-child(2)')

#New Student Positive Cases Title
addDataPoint('#left-tabs-example-tabpane-third > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(4) > div:nth-child(2) > div:nth-child(1) > p:nth-child(2)')
#New Student Positive Cases Amount
addDataPoint('#left-tabs-example-tabpane-third > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(4) > div:nth-child(2) > div:nth-child(1) > div:nth-child(3) > span:nth-child(1)')
#New Teacher Positive Cases Title
addDataPoint('div.col-md-4:nth-child(3) > div:nth-child(1) > p:nth-child(2)')
#New Teacher Positive Cases Amount
addDataPoint('div.col-md-4:nth-child(3) > div:nth-child(1) > div:nth-child(3) > span:nth-child(1)')
#New Staff Positive Cases Title
addDataPoint('div.col-md-4:nth-child(4) > div:nth-child(1) > p:nth-child(2)')
#New Staff Positive Cases Amount
addDataPoint('div.col-md-4:nth-child(4) > div:nth-child(1) > div:nth-child(3) > span:nth-child(1)')

#Total Student Positive Cases Title
addDataPoint('div.m-stats-cards-card-wrapper:nth-child(6) > div:nth-child(1) > p:nth-child(2)')
#Total Student Positive Cases Amount
addDataPoint('div.m-stats-cards-card-wrapper:nth-child(6) > div:nth-child(1) > div:nth-child(3) > span:nth-child(1)')
#Total Teacher Positive Cases Title
addDataPoint('div.col-md-4:nth-child(7) > div:nth-child(1) > p:nth-child(2)')
#Total Teacher Positive Cases Amount
addDataPoint('div.col-md-4:nth-child(7) > div:nth-child(1) > div:nth-child(3) > span:nth-child(1)')
#Total Staff Positive Cases Title
addDataPoint('div.col-md-4:nth-child(8) > div:nth-child(1) > p:nth-child(2)')
#Total Staff Positive Cases Amount
addDataPoint('div.col-md-4:nth-child(8) > div:nth-child(1) > div:nth-child(3) > span:nth-child(1)')

#Quit Firefox
browser.quit()

#Issue Tweet using scraped data
for i in covidData:
	print(i)

