# Web-Scraping-using-Python
The SingleArticleScraper script will show how to scrape data from a news website. The news website that I used in this script is Inquirer.net which is the leading newspaper in the Philippines. The code will perform the following in sequence:

1. It first will take the url and then convert it to BeautifulSoup object
2. It will then scrape for the author,date and title of the article and save it to a list
3. It will then get all the body of text under the 'p' tag. It also removes unwanted text advertisements which are children of the 'p' tag, thus I used the decompose python method
4. Lastly, it will save the scraped data into a text file
