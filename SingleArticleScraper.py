from urllib.request import Request
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup

def converToSoup(url):
	''' 
        This function will parse the url to BeautifulSoup(BS)
        '''
	try:
		urlRequest = Request(url,headers={'User-Agent':'Mozilla/6.0'})
		urlOpen = urlopen(urlRequest)
		urlRead = urlOpen.read()
		urlClose = urlOpen.close()
		urlBSoup = BeautifulSoup(urlRead,"html.parser")
		return urlBSoup
	except HTTPError:
		print ("The server returned an HTTP error")
	except URLError:
		print ("The server could not be found")
		
def getNewsInfo(urlBSoup):
	''' 
        This function will get title,author,date information
        '''
	Title = urlBSoup.find("h1",{"class":"entry-title"}).text
	checkAuthorisNull = urlBSoup.find("div",{"id":"art_author"})
	
	if checkAuthorisNull == None:
		Author = ""
	else:
		Author = checkAuthorisNull.text.replace("\n","")
		
	Date = urlBSoup.find("div",{"id":"art_plat"}).text
	
	NewsInfo = [Title,Author,Date]
	
	return NewsInfo
	
def getWholeArticle(urlBSoup):
	''' 
        This function will get article's body. It also removes unwanted text after the <p> tag making use of the decompose method		
        '''
	soupBody = urlBSoup.findAll("div",{"id":"article_content"})
	articleBody = soupBody[0].div
	
	for unwantedText in articleBody.findAll("div"):
		unwantedText.decompose()
	
	wholeArticle = articleBody.get_text()
	
	return wholeArticle
	
def saveData(newsInfo,url,wholeArticle):
	''' 
        This function will save the scraped data to a text file	
        '''
	filename = newsInfo[0].replace(" ","_") + ".txt"
	f = open(filename,"w")
	f.write(newsInfo[0] + "\n")
	f.write(newsInfo[1] + "\n")
	f.write(newsInfo[2] + "\n")
	f.write(url + "\n")
	f.write(wholeArticle)
	f.close()
	return True
	
def main():
	# The url of the website we will scrape
	url="https://opinion.inquirer.net/117659/a-hard-hitting-biography-of-duterte"
	
	# This function (converToSoup) will convert the url to BeautifulSoup
	urlBSoup = converToSoup(url)
	
	# This function will get the title,author,date of the article
	newsInfo = getNewsInfo(urlBSoup)
	print (newsInfo)
	
	# This function will retrieve the content of the entire article
	wholeArticle = getWholeArticle(urlBSoup)
	print (wholeArticle)
	
	# This function will save the scraped data to a text file
	saveData(newsInfo,url,wholeArticle)
	
main()
