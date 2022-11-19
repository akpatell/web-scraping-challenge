# imports
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
import requests
from bs4 import BeautifulSoup as soup
import pandas as pd

import datetime as dt 

# scrape all function 
def scrape_all():
    #print("Scrape All was reached")

    # setup splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless = False)

    # goal behind scrap all is to return json that has all of the necessary data so that it
    # can be loaded into MongoDB

    # get the information from news page
    news_title, news_paragraph = scrape_news(browser)
    
    # build dictionary using info from scrape_news(browser)
    mars_data = {
        "news_title": news_title,
        "news_paragraph": news_paragraph,
        "featured_image": scrape_featured_image(browser),
        "facts": scrape_facts(browser),
        "hemispheres": scrape_hemispheres(browser),
        "last_updated": dt.datetime.now()
    }

    # stop webdriver
    browser.quit()

    # display output in GitBash 
    return mars_data

# use scrape all function to scrape through the various pages
# scrape through mars news page
def scrape_news(browser):
    # go the Mars NASA news site
    url = 'https://redplanetscience.com/'
    browser.visit(url)

    # optional elay for loading the page
    browser.is_element_present_by_css('div.list_text', wait_time = 1)

    # convert the browser html to a soup object
    html = browser.html 
    news_soup = soup(html, 'html.parser')

    slide_elem = news_soup.select_one('div.list_text')

    # grab the title
    news_title = slide_elem.find('div', class_ = 'content_title').get_text()

    # grabs the paragraph for the headline
    news_p = slide_elem.find('div', class_ = 'article_teaser_body').get_text()

    # return the news title and the paragraph back so that we can put it into our dictionary
    return news_title, news_p

# scrape through featured image page

def scrape_featured_image(browser):
    # go to the images site
    url ='https://spaceimages-mars.com/'
    browser.visit(url)

    # visit and find the full image button in the URL
    full_image_link = browser.find_by_tag('button')[1]
    full_image_link.click()

    # parse resulting html with soup
    html = browser.html
    image_soup = soup(html, 'html.parser')

     # find the image url
    img_url_rel = image_soup.find('img', class_ = 'fancybox-image').get('src')

    # use base url to create absolute image url
    img_url = f'https://spaceimages-mars.com/{img_url_rel}'
    
    # return the image url 
    return img_url

# scrape through the facts page
def scrape_facts(browser):
    # go to the facts site
    url = 'https://galaxyfacts-mars.com/'
    browser.visit(url)

    # parse resulting html with soup
    html = browser.html
    fact_soup = soup(html, 'html.parser')

    # find the facts location
    facts_location = fact_soup.find('div', class_ = 'diagram mt-4')
    fact_table = facts_location.find('table') # grab the html code for the fact table
            
    # create an empty string
    facts = ''

    # add the text to the empty string then return 
    facts += str(fact_table)
    
    return facts 

# scrape through hemispheres page
def scrape_hemispheres(browser):
    # go to the hemispheres site
    url = 'https://marshemispheres.com/'
    browser.visit(url)

    # create a list to hold images and titles
    hemisphere_image_urls = []

    # loop through the links, click the link, find th4e sample anchor, and return the image
    for i in range(4):
        # hemisphere info dictionary 
        hemisphereInfo = {}
        
        # find the elements on each loop to avoid a stale element exception
        browser.find_by_css('a.product-item img')[i].click()
        
        # find the sample image anchor tag and extract href
        sample = browser.links.find_by_text('Sample').first
        hemisphereInfo["img_url"] = sample['href']
        
        # get the hemisphere title
        hemisphereInfo['title'] = browser.find_by_css('h2.title').text
        
        # append hemisphere object to list
        hemisphere_image_urls.append(hemisphereInfo)

        # navigate backwards
        browser.back()

    # return the hemisphere urls with the titles
    return hemisphere_image_urls

    # parse resulting html with soup
    html = browser.html
    fact_soup = soup(html, 'html.parser')


# set up as a flask app
if __name__ == "__main__":
    print(scrape_all()) 