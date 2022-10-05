
# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
import datetime as dt
from webdriver_manager.chrome import ChromeDriverManager


def scrape_all():
    # Initiate headless driver for deployment
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=True)
    # # Set up Splinter
    # executable_path = {'executable_path': ChromeDriverManager().install()}
    # browser = Browser('chrome', **executable_path, headless=False)

    news_title, news_paragraph = mars_news(browser)
    hemisphere_titles, hemisphere_urls = hemisphere(browser)

    # Run all scraping functions and store results in a dictionary
    data = {
        "news_title": news_title,
        "news_paragraph": news_paragraph,
        "featured_image": featured_image(browser),
        "facts": mars_facts(),
        "last_modified": dt.datetime.now(),
        "hemisphere title": hemisphere_titles,
        "hemisphere urls": hemisphere_urls
    }

    # Stop webdriver and return data
    browser.quit()
    return data


def mars_news(browser):

    # Scrape Mars News
    # Visit the mars nasa news site
    url = 'https://data-class-mars.s3.amazonaws.com/Mars/index.html'
    browser.visit(url)

    # Optional delay for loading the page
    browser.is_element_present_by_css('div.list_text', wait_time=1)

    # Convert the browser html to a soup object and then quit the browser
    html = browser.html
    news_soup = soup(html, 'html.parser')

    # Add try/except for error handling
    try:
        slide_elem = news_soup.select_one('div.list_text')
        # Use the parent element to find the first 'a' tag and save it as 'news_title'
        news_title = slide_elem.find('div', class_='content_title').get_text()
        # Use the parent element to find the paragraph text
        news_p = slide_elem.find('div', class_='article_teaser_body').get_text()

    except AttributeError:
        return None, None

    return news_title, news_p


def featured_image(browser):
    # Visit URL
    url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'
    browser.visit(url)

    # Find and click the full image button
    full_image_elem = browser.find_by_tag('button')[1]
    full_image_elem.click()

    # Parse the resulting html with soup
    html = browser.html
    img_soup = soup(html, 'html.parser')

    # Add try/except for error handling
    try:
        # Find the relative image url
        img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')

    except AttributeError:
        return None

    # Use the base url to create an absolute url
    img_url = f'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/{img_url_rel}'

    return img_url

def mars_facts():
    # Add try/except for error handling
    try:
        # Use 'read_html' to scrape the facts table into a dataframe
        df = pd.read_html('https://data-class-mars-facts.s3.amazonaws.com/Mars_Facts/index.html')[0]

    except BaseException:
        return None

    # Assign columns and set index of dataframe
    df.columns=['Description', 'Mars', 'Earth']
    df.set_index('Description', inplace=True)

    # Convert dataframe into HTML format, add bootstrap
    return df.to_html(classes="table table-striped")



def hemisphere(browser):
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
    title = img_soup.find_all('h3')

    titles_list = []
    for title in title:
        title = title.text.strip()
        titles_list.append(title)
    del titles_list[4]
    titles_list

# %%

    image_link_1 = img_soup.find_all("div", class_="description")
    image_link_1

    image_link_2 = img_soup.find("a", class_="itemLink product-item").get("href")
    image_link_2

    urls_hemispheres = []
    for link in image_link_1:
        #link = image_soup.find_all("a", class_="itemLink product-item")
        link2 = link.find("a", class_="itemLink product-item").get("href")
        #link = link("href")
        #print(link2)
        urls_hemispheres.append(link2)

    urls_hemispheres

    full_urls = []
    for url_hemi in urls_hemispheres:
        url_link = f'{url}{url_hemi}'
        full_urls.append(url_link)
    full_urls

    url_0 = full_urls[0]
    url_0

    browser.visit(url_0)
    html = browser.html
    img_soup_1 = soup(html, 'html.parser')
    thread = img_soup_1.find('div', class_='downloads')
    link_0 = thread.a['href']
    link_0 = f'{url}{link_0}'
    #print(link_0)


    url_1 = full_urls[1]
    url_1

    browser.visit(url_1)
    html = browser.html
    img_soup_1 = soup(html, 'html.parser')
    thread = img_soup_1.find('div', class_='downloads')
    link_1 = thread.a['href']
    link_1 = f'{url}{link_1}'
    #print(link_1)


    url_2 = full_urls[2]
    url_2

    browser.visit(url_2)
    html = browser.html
    img_soup_1 = soup(html, 'html.parser')
    thread = img_soup_1.find('div', class_='downloads')
    link_2 = thread.a['href']
    link_2 = f'{url}{link_2}'
    #print(link_2)



    url_3 = full_urls[3]
    url_3

    browser.visit(url_3)
    html = browser.html
    img_soup_1 = soup(html, 'html.parser')
    thread = img_soup_1.find('div', class_='downloads')
    link_3 = thread.a['href']
    link_3 = f'{url}{link_3}'
    print(link_3)

    full_urls = [link_0, link_1, link_2, link_3]
    full_urls

    full_urls_df = pd.DataFrame(full_urls)
    full_urls_df.columns = ['html']
    full_urls_df



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
    # %%
    hemisphere_image_urls = mars_hemispheres_df.values.tolist()
    hemisphere_titles = titles_df.values.tolist()
    hemisphere_urls = full_urls_df.values.tolist()

    
# %%
    return hemisphere_titles, hemisphere_urls

# %%
# %%
# 5. Quit the browser
    browser.quit()


