# Unit 12 Homework: Mission to Mars

In this assignment, a web application was built that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page. The following information outlines what was done in this assignment.

## Overall Summary 

The overall summary of the steps taken to do complete this assignment are divided into three parts: 

1. Scraping 

2. MongoDB and Flask Application

3. Submission 

## Part 1: Scraping

Initial scraping was completed using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.

### NASA Mars News

* The [Mars News Site](https://redplanetscience.com/) was scraped and the latest News Title and Paragraph Text were collected.

```python
# Example:
news_title = "NASA's Next Mars Mission to Investigate Interior of Red Planet"

news_paragraph = "Preparation of NASA's next spacecraft to Mars, InSight, has ramped up this summer, on course for launch next May from Vandenberg Air Force Base in central California -- the first interplanetary launch in history from America's West Coast."
```

### JPL Mars Space Images—Featured Image

* The URL for the Featured Space Image site [here](https://spaceimages-mars.com) was visited.

* Splinter was used to navigate the site and find the image URL for the current Featured Mars Image.

```python
# Example:
featured_image_url = 'https://spaceimages-mars.com/image/featured/mars2.jpg'
```

### Mars Facts

* The [Mars Facts webpage](https://galaxyfacts-mars.com) was visited and Pandas ws used to scrape the table containing facts about the planet including diameter, mass, etc.

* Pandas was used to convert the data to a HTML table string.

### Mars Hemispheres

* The [astrogeology site](https://marshemispheres.com/) was visited to obtain high-resolution images for each hemisphere of Mars.

```python
# Example:
hemisphere_image_urls = [
    {"title": "Valles Marineris Hemisphere", "img_url": "..."},
    {"title": "Cerberus Hemisphere", "img_url": "..."},
    {"title": "Schiaparelli Hemisphere", "img_url": "..."},
    {"title": "Syrtis Major Hemisphere", "img_url": "..."},
]
```

- - -

## Part 2: MongoDB and Flask Application

MongoDB with Flask templating were used together to create a new HTML page that displays all the information that was scraped from the URLs above.

* The Jupyter notebook was converted into a Python script by using a function called `scrape`. This function executed all the scraping code and returned one Python dictionary containing all the scraped data.

* A route called `/scrape` was created to import the python script and the `scrape` function was called.

  * The return value was stored in Mongo as a Python dictionary.

* A root route `/` was created which would query the Mongo database and pass the Mars data into an HTML template for displaying the data.

* A template HTML file called `index.html` was created that would take the Mars data dictionary and display all the data in the appropriate HTML elements. 

- - -

© 2022 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
