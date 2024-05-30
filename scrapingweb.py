import sys
import re
from bs4 import BeautifulSoup
from urllib.request import urlopen

# Redirect standard output to a file named 'data.csv'
sys.stdout = open('data.csv', 'w')

# Open a connection to the Billboard Hot 100 chart webpage
ureq = urlopen('https://www.billboard.com/charts/hot-100/')
html_content = ureq.read()
ureq.close()

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find the HTML element containing the chart results
s = soup.find('div', class_='chart-results-list')

# Find all the song names within the chart results
songnames = s.find_all('h3', id='title-of-a-story')

# Initialize lists to store song information
songs = []  # List to store song names
artists = []  # List to store artist names
lastwk = []  # List to store last week's positions
peakpos = []  # List to store peak positions
wksonchart = []  # List to store weeks on chart

# Extract song names from the songnames list
for i in range(2, 400, 4):
    name = songnames[i].get_text()
    songs.append(name.strip())

# Find all the spans with class containing 'c-label'
spans = s.find_all('span', class_=re.compile('c-label'))

# Initialize a list to store span text
spanlist = []

# Extract span text, removing unnecessary bald NEW entries
for i in range(0, len(spans)):
    bald = spans[i].get_text()
    spanlist.append(bald.strip())

spanlist = [i for i in spanlist if i != 'NEW']

# Split spanlist into different lists for each type of information
artists = [spanlist[i] for i in range(1, 794, 8)]  # List of artists
lastwk = [spanlist[i] for i in range(2, 795, 8)]  # List of last week's positions
peakpos = [spanlist[i] for i in range(3, 796, 8)]  # List of peak positions
wksonchart = [spanlist[i] for i in range(4, 798, 8)]  # List of weeks on chart

# Print the song information in CSV format
for i in range(100):
    print(str(i + 1) + '`' + songs[i] + '`' + artists[i] + '`' + lastwk[i] + '`' + peakpos[i] + '`' + wksonchart[i])
# use '`' as the delimiter since some songname/artist fields may contain comma