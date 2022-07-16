#import the whiskey_web_scraping class
from scrape import whiskey_web_scraping

#create an instance of the whiskey_web_scraping class/scraper object
scraper = whiskey_web_scraping()

#Generate a soup object from the first page of the website
soup = scraper.scrape_html('https://www.thewhiskyexchange.com/c/316/campbeltown-single-malt-scotch-whisky', 1)

# Collecting the div objects from the first page
proudcts_info_content = scraper.get_page_content(soup)
proudcts_info_price = scraper.get_page_price(soup)

# Extracting from the div objects the name, alcohol percent, alcohol amount and price of each product
product_name = scraper.get_product_name(proudcts_info_content)
product_al_percent = scraper.get_product_alcohol_percent(proudcts_info_content)
product_al_amount = scraper.get_product_alcohol_amount(proudcts_info_content)
product_price = scraper.get_product_price(proudcts_info_price)

# Creating a DataFrame from the first page
df = scraper.create_df(names=product_name, alcohol_amount=product_al_amount,
                       alcohol_percent=product_al_percent, price= product_price )
print(df.info())