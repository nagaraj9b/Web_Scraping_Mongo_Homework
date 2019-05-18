
from splinter import Browser
from bs4 import BeautifulSoup
import requests
import pandas as pd


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "chromedriver"}
    return Browser("chrome", **executable_path, headless=False)

def scrapes():
        ## NASA Mars News
        browser = init_browser()
        url = 'https://mars.nasa.gov/news/'
        browser.visit(url)
        scraped = {}
        html = browser.html
        soup = BeautifulSoup(html,'html.parser')
        # print(soup.prettify())
        news_title = soup.find('div', class_='content_title').find('a').text
        news_p = soup.find('div', class_= 'rollover_description_inner').text.strip()
        # print(f"news_title: {news_title}")
        # print(f"news_p: {news_p}")
        scraped['News_Title'] = news_title
        scraped['News'] = news_p
        
        browser.quit()

        # ### JPL Mars Space Images - Featured Image

# def scrape_images():
        browser = init_browser()
        url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
        browser.visit(url)
        # scraped = {}
        html = browser.html
        soup = BeautifulSoup(html,'html.parser')


        # for a in soup.find_all('div', class_='img'):
        #         if a.img:
        #                 # print(a.img['src'])
        #                 image = a.img['src']
        #                 imagesplit = image.split('/')
        #                 moresplit = imagesplit[4].split('-')
        #                 # print(moresplit)
        #                 featured_image_url= 'https://photojournal.jpl.nasa.gov/jpeg/' + moresplit[0]+'.jpg'
          
        a = soup.find('div', class_='img')
        image = a.img['src']
        imagesplit = image.split('/')
        moresplit = imagesplit[4].split('-')
        # print(moresplit)
        featured_image_url= 'https://photojournal.jpl.nasa.gov/jpeg/' + moresplit[0]+'.jpg'
        # print(featured_image_url)
        scraped ['Featured_image_url'] = featured_image_url
        
        browser.quit()



        # ### Mars Weather

        browser = init_browser()
        url = 'https://twitter.com/marswxreport?lang=en'
        browser.visit(url)
        html = browser.html
        soup = BeautifulSoup(html,'html.parser')
        mars_weather1 = soup.find('div','js-tweet-text-container').p.text
        mars_weather = mars_weather1.split('hP')[0]
        mars_weather
        # print(f"mars_weather = {mars_weather}")
        scraped['Mars_Weather'] = mars_weather
        browser.quit()


        # ### Mars Facts


        browser = init_browser()       
        url = 'http://space-facts.com/mars/'
        table = pd.read_html(url)
        Table_df = table[0]
        Table_df.head()
        Table_df.columns = ['Desc', 'Values']
        New_df= Table_df.set_index('Desc')
        New_df.head()
        htmldata = New_df.to_html()
        scraped['Mars_facts'] = htmldata
        browser.quit()


        # ### Mars Hemispheres


        browser = init_browser()       
        url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
        browser.visit(url)
        html = browser.html
        soup = BeautifulSoup(html,'html.parser')
        # print(soup.prettify())
        html_item = soup.find_all('div', class_='item')
        image_urls = []
        base_url = 'https://astrogeology.usgs.gov/'
        for row in html_item:
                title = row.find('h3').text
                first_imgurl = row.find('a', class_= 'itemLink product-item')['href']
                dest_url = base_url + first_imgurl
                browser = init_browser() 
                # executable_path = {'executable_path': 'chromedriver.exe'}
                # browser = Browser('chrome', **executable_path, headless=False)
                browser.visit(dest_url)
                resolution_html = browser.html
                soup = BeautifulSoup( resolution_html, 'html.parser')

                # Retrieve full image source 
                img_url = base_url + soup.find('img', class_='wide-image')['src']
              
                image_urls.append({"title" : title, "img_url" : img_url})
                browser.quit()

                # Display hemisphere_image_urls
        image_urls
        scraped['Hemispher_img'] = image_urls
        return scraped
        


        


      



