import requests
from bs4 import BeautifulSoup

URL = 'https://www.monster.com/jobs/search/?q=Software-Developer&where=Australia'
page = requests.get(URL)

# we create a Beautiful Soup object to parse through the html that is in there
soup = BeautifulSoup(page.content, 'html.parser')

# we find the elments by id
results = soup.find(id='ResultsContainer')
print(results)

print('\n')
"""
# finding elements by HTML class name, but we grab EVERYTHING
job_elems = results.find_all('section', class_='card-content')

## iterates through all of the HTML, and returns the job listings displayed on the page (but there's a lot of them)
for job_elem in job_elems:
    print(job_elem, end='\n'*2)

for job_elem in job_elems:
    # Each job_elem is a new BeautifulSoup object.
    # You can use the same methods on it as you did before.

    # We find the title, company and locations in the h2, div tags that are found within the HTML
    title_elem = job_elem.find('h2', class_='title')
    company_elem = job_elem.find('div', class_='company')
    location_elem = job_elem.find('div', class_='location')
    if None in (title_elem, company_elem, location_elem):
        continue
    print(title_elem.text.strip())
    print(company_elem.text.strip())
    print(location_elem.text.strip())
    print()
"""

# finds all <h2> elements contained string matches 'Python Developer'
# we find out there's nothing
python_jobs = results.find_all('h2', string=lambda text: 'python' in text.lower())

for p_job in python_jobs:
    link = p_job.find('a')['href']
    print(p_job.text.strip())
    print(f"Apply here: {link}\n")