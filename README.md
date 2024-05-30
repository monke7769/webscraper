### Billboard Top 100 Web Scraper

Hayden Chen

Individual project

I created a Billboard Top 100 Web Scraping Python program (scrapingweb.py) which uses BeautifulSoup to parse through the HOT100 page's HTML and grab the desired fields. This includes:
- song names
- artists
- position last week
- peak position on chart
- number of weeks on chart

The data is saved/inserted into the data.csv file. Then top100table.py iteratively creates an HTML table structure in top100table.html using the Python sys module.

#### Benefits

- Saves users' time (won't have to access the Billboard Top 100 website every time!)
- Avoid the ads on the website
- May customize the HTML table CSS to match their desired styling

#### For developers and users

Make sure to import BeautifulSoup and urlopen before running. Import the resulting top100table.html table into another directory to display the HTML in browser window.
