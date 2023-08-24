import requests
from bs4 import BeautifulSoup
import pandas as pd
# take in variables
jobTitleIn = input('>Enter desired job title: ')
pagesAmount = int(input('>Enter amount of pages to scrape: '))
# declare a list to store the job objects
jobList = []
# method to extract the soup page data
def extract(jobtitle, page):
	# referer url and user agent for our browser
	headers  = {'Referer' : 'https://www.irishjobs.ie/', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36' }
	# formatted string with job title and page number
	website = f'https://www.irishjobs.ie/ShowResults.aspx?Keywords={jobtitle}&Page={page}'
	r = requests.get(website, headers = headers)
	# save parsed html content into soup variable and return it
	soup = BeautifulSoup(r.content, 'html.parser')
	return soup
# method to transform the soup page data
def transform(soup):
	divs = soup.find_all('div', class_ = 'module job-result')
	for item in divs:
		# get data into variables
		title = item.find('h2').find('a').text
		company = item.find('h3').find('a').text
		date = item.find('li', class_ = 'updated-time').text
		link = item.find('h2').find('a').get("href")
		description = item.find('p').find('span').text.replace('\n', '')
		# job object that holds variables
		job = { 
			'Job Title': title,
			'Company': company,
			'Date Posted': date,
			'Post Link': 'https://www.irishjobs.ie' + link,
			'Description': description }
		# add job object to jobList
		jobList.append(job)
	return
# loop to iterate over amount of pages
for i in range(1, (pagesAmount + 1)):
	print(f'Scraping Page: {int(i)}')
	pageData = extract(jobTitleIn, i)
	transform(pageData)
# save jobList as a data frame and save data frame to csv format
df = pd.DataFrame(jobList)
filename = 'Task2.csv'
df.to_csv(filename)
print(f'Successfully Scrapped {len(jobList)} jobs! ')