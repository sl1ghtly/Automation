import requests
from bs4 import BeautifulSoup
import pandas as pd
# method to extract the soup page data
def extract(jobtitle, location, page):
	# user agent for our browser
	userAgent = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36' }
	# formatted string with job title, location and page that moves up in 10s
	website = f'https://ie.indeed.com/jobs?q={jobtitle}&l={location}&start={page}'
	r = requests.get(website, userAgent)
	# save parsed html content into soup variable and return it
	soup = BeautifulSoup(r.content, 'html.parser')
	return soup
# method to transform the soup page data
def transform(soup):
	# find all containers with jobs, can be changed by indeed pretty often
	divs = soup.find_all('div', class_ = 'slider_container css-11g4k3a eu4oa1w0')
	for item in divs:
		# get data into variables
		title = item.find('a').text
		company = item.find('span', class_ = 'companyName').text
		date = item.find('span', class_ = 'date').text
		link = item.find('a').get("href")
		description = item.find('div', class_ = 'job-snippet').text.replace('\n', '')
		# job object that holds variables
		job = { 
			'Job Title': title,
			'Company': company,
			'Date Posted': date,
			'Post Link': 'https://ie.indeed.com' + link,
			'Description': description }
		# add job object to jobList
		jobList.append(job)
	return	
# declare a list to store the job objects
jobList = []
# take in variables, pages move up in 10s
jobTitleIn = input('>Enter desired job title: ')
jobLocationIn = input('>Enter desired location: ')
pagesAmount = int(input('>Enter amount of pages to scrape: ')) * 10
# loop to iterate over amount of pages
for i in range(0, pagesAmount, 10):
	print(f'Scraping Page: {int((i + 10) / 10)}')
	pageData = extract(jobTitleIn, jobLocationIn, i)
	transform(pageData)
# save jobList as a data frame and save data frame to csv format
df = pd.DataFrame(jobList)
filename = 'jobs.csv'
df.to_csv(filename)
print(f'Total Amount of Scapped Jobs: {len(jobList)} in {filename}')