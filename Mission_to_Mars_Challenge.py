# %%
# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

# %%
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

# %%
# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)

# %%
html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')

# %%
slide_elem.find('div', class_='content_title')

# %%
# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# %%
# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p

# %% [markdown]
# ### Featured Images

# %%
# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)

# %%
# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()

# %%
# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')

# %%
# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel

# %%
# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url

# %%
df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df

# %%
df.to_html()

# %%
browser.quit()

# %%
# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager

# %%
# Set the executable path and initialize Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

# %% [markdown]
# ### Visit the NASA Mars News Site

# %%
# Visit the mars nasa news site
url = 'https://redplanetscience.com/'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)

# %%
# Convert the browser html to a soup object and then quit the browser
html = browser.html
news_soup = soup(html, 'html.parser')

slide_elem = news_soup.select_one('div.list_text')

# %%
slide_elem.find('div', class_='content_title')

# %%
# Use the parent element to find the first a tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title

# %%
# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p

# %% [markdown]
# ### JPL Space Images Featured Image

# %%
# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)

# %%
# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()

# %%
# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')
img_soup

# %%
# find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel

# %%
# Use the base url to create an absolute url
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url

# %% [markdown]
# ### Mars Facts

# %%
df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.head()

# %%
df.columns=['Description', 'Mars', 'Earth']
df.set_index('Description', inplace=True)
df

# %%
df.to_html()

# %% [markdown]
# # D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

# %% [markdown]
# ### Begin Module 10 Challenge

# %%
# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'

browser.visit(url)

# %%
# 2. Create a list to hold the images and titles.

hemisphere_image_urls = []
hemisphere_image_urls.append({"title":"hemi_1", "url":"url_1"})
hemisphere_image_urls


# %%
# 3. Write code to retrieve the image urls and titles for each hemisphere.

html = browser.html
img_soup = soup(html, 'html.parser')
images = img_soup.find_all('a', class_="itemLink product-item")
img_soup

# %%
title = img_soup.find_all('h3')

titles_list = []
for title in title:
    title = title.text.strip()
    titles_list.append(title)
del titles_list[4]
titles_list

# %%
images

# %%
image_link = img_soup.find_all('img', class_="thumb")
print(image_link)

# %%
image_link = img_soup.find('img', class_="thumb")
print(image_link)

# %%

for image in image_link:
    hemispheres = {}
    browser.find_by_tag(image_link).click()
    browser.visit(url)
    html = browser.html
    img_soup_1 = soup(html, 'html.parser')
    thread = img_soup_1.find('div', class_='downloads')
    link = thread.a['href']
    print(link)



# %%

url_1 = 'https://marshemispheres.com/cerberus.html'
browser.visit(url_1)
html = browser.html
img_soup_1 = soup(html, 'html.parser')
thread = img_soup_1.find('div', class_='downloads')
link_1 = thread.a['href']
link_1 = f'{url_1}/{link_1}'
print(link_1)

  

# %%
url_2 = 'https://marshemispheres.com/schiaparelli.html'
browser.visit(url_2)
html = browser.html
img_soup_1 = soup(html, 'html.parser')
thread = img_soup_1.find('div', class_='downloads')
link_2 = thread.a['href']
link_2 = f'{url_2}/{link_2}'
print(link_2)

# %%
url_3 = 'https://marshemispheres.com/syrtis.html'
browser.visit(url_3)
html = browser.html
img_soup_1 = soup(html, 'html.parser')
thread = img_soup_1.find('div', class_='downloads')
link_3 = thread.a['href']
link_3 = f'{url_3}/{link_3}'
print(link_3)

# %%
url_4 = 'https://marshemispheres.com/valles.html'
browser.visit(url_4)
html = browser.html
img_soup_1 = soup(html, 'html.parser')
thread = img_soup_1.find('div', class_='downloads')
link_4 = thread.a['href']
link_4 = f'{url_4}/{link_4}'
print(link_4)

# %%
# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'

browser.visit(url)


# %%
# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []


# %%
# 3. Write code to retrieve the image urls and titles for each hemisphere.

html = browser.html
img_soup = soup(html, 'html.parser')
images = img_soup.find_all('a', class_="itemLink product-item")

# %%
urls = []
for x in img_soup.find_all('a', href=True):
    urls.append(x['href'])
urls_ = []
[urls_.append(x) for x in urls if x not in urls_]
urls_df = pd.DataFrame(urls_)
urls_df = urls_df.drop([0,1]).reset_index()
urls_df = urls_df.drop(['index'],axis=1)
urls_df.columns = ['html']

# %%

for html in urls_df.html:
     urls_df['main'] = ("https://marshemispheres.com/")
urls_df['url'] = urls_df['main'] + urls_df['html']
urls_df = urls_df.drop(['html'], axis=1)
urls_df = urls_df.drop(['main'], axis=1)
urls_df


# %%
titles = img_soup.find_all('h3')
titles_df = pd.DataFrame(titles)
titles_df =titles_df.drop(4)
titles_df.columns = ['title']
titles_df

# %%
mars_hemispheres_df = pd.merge(titles_df, urls_df, left_index=True, right_index=True)
mars_hemispheres_df

# %%
hemisphere_image_urls = mars_hemispheres_df.values.tolist()
hemisphere_titles = titles_df.values.tolist()
hemisphere_urls = urls_df.values.tolist()
hemisphere_image_urls = mars_hemispheres_df.values.tolist()
hemisphere_image_urls = mars_hemispheres_df.to_dict()

# %%
hemisphere_titles

# %%
hemisphere_urls

# %%
# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls

# %%
# 5. Quit the browser
browser.quit()


