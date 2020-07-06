from bs4 import BeautifulSoup
import requests
import re

location = "Montreal Quebec Canada"

for char in location:
    if char in " ":
        location = location.replace(char, '%2C')

fieldToSearch = 'software development'

for char in fieldToSearch:
    if char in " ":
        fieldToSearch = fieldToSearch.replace(char, '%20')

url = "https://www.linkedin.com/jobs/search/?keywords=" + fieldToSearch + "&location=" + location
print(url)
response = requests.get(url)
data = response.text
soup = BeautifulSoup(data, features="lxml")

links=[]
for link in soup.findAll(attrs={ 'class': "result-card__full-card-link"}):
    links.append(link['href'])

jobPosting = []
for link in links:
    indivResponse = requests.get(link)
    indivData = indivResponse.text
    indivSoup = BeautifulSoup(indivData, features="lxml")

    jobInfo = {
            'URL':link,
            'Title':(indivSoup.find(attrs={ 'class': "topcard__title"})).getText(),
            'Company':(indivSoup.find(attrs={ 'class': "topcard__flavor"})).getText()
            #'Description':(indivSoup.find(attrs={ 'class': "show-more-less-html__markup"})).getText()
            }

    count = 0
    for date in indivSoup.findAll(attrs={ 'class': "topcard__flavor--metadata posted-time-ago__text"}):
        if count == 0:
            jobInfo['Date Posted'] = date.getText()
            break

    descrip = ''
    for li in indivSoup.findAll(attrs={ 'class': "show-more-less-html__markup"}):
        descrip = descrip + li.getText()

    jobInfo['Description'] = descrip


    for critList in indivSoup.findAll(attrs={ 'class': "job-criteria__text job-criteria__text--criteria"}):
        if count == 0:
            jobInfo['Seniority Level'] = critList.getText()
        elif count == 1:
            jobInfo['Employment Type'] = critList.getText()
            break
        count+=1

    jobPosting.append(jobInfo)

print(jobPosting[1])
