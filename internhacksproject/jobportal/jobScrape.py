from bs4 import BeautifulSoup
import requests
import re

# This is just a variable I set to test it, however the website should have a drop down menu or an input field to get this
location = "Montreal Quebec Canada"

# This just breaks up the location to have it fit the URL format
for char in location:
    if char in " ":
        location = location.replace(char, '%2C')

# This is just a variable I set to test it out. In this case this is the search field
fieldToSearch = 'software development'

# This just adds the %20 inbetween spaces to make it a proper url
for char in fieldToSearch:
    if char in " ":
        fieldToSearch = fieldToSearch.replace(char, '%20')

# This adds the fields to generate the proper URL
url = "https://www.linkedin.com/jobs/search/?keywords=" + fieldToSearch + "&location=" + location

# Any printing was just to test it and see it
print(url)

# Getting the webpage
response = requests.get(url)
# Getting source code
data = response.text
# Pass source code to BeautifulSoup
soup = BeautifulSoup(data, features="lxml")

# Finds all the urls of the job postings and puts it in a list
links=[]
for link in soup.findAll(attrs={ 'class': "result-card__full-card-link"}):
    links.append(link['href'])

# Finds all the information for each job posting
jobPosting = []
for link in links:
    # Creates the webpages data for each individual job posting
    indivResponse = requests.get(link)
    indivData = indivResponse.text
    indivSoup = BeautifulSoup(indivData, features="lxml")


    jobInfo = {
            # The postings URL
            'URL':link,
            # The postings title
            'Title':(indivSoup.find(attrs={ 'class': "topcard__title"})).getText(),
            # The postings Company
            'Company':(indivSoup.find(attrs={ 'class': "topcard__flavor"})).getText()
            }

    # The postings Date posted (for some reason just using find wont work for the specific class, however findAll in a loop only looping once works)
    count = 0
    for date in indivSoup.findAll(attrs={ 'class': "topcard__flavor--metadata posted-time-ago__text"}):
        if count == 0:
            jobInfo['Date Posted'] = date.getText()
            break

    # This gets the whole Description of the post including the requirments that may be listed
    descrip = ''
    for li in indivSoup.findAll(attrs={ 'class': "show-more-less-html__markup"}):
        descrip = descrip + li.getText()
    jobInfo['Description'] = descrip

    # Criteria section have the same class, so by getting the first 2 we can get the Seniority level (ex Entry) and the Employment type (ex fulltime)
    for critList in indivSoup.findAll(attrs={ 'class': "job-criteria__text job-criteria__text--criteria"}):
        if count == 0:
            jobInfo['Seniority Level'] = critList.getText()
        elif count == 1:
            jobInfo['Employment Type'] = critList.getText()
            break
        count+=1

    jobPosting.append(jobInfo)

print(jobPosting[1])
