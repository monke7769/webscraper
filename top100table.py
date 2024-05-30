import sys
import csv

# Read data from the 'data.csv' file and store it in the 'lines' list
lines = []
with open('data.csv') as file_e:
    reader_obj = csv.reader(file_e, delimiter='`')
    for row in reader_obj:
        lines.append(row)

# Initialize the 'strTable' variable with HTML and external dependencies
strTable = '<head><link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/1.13.4/css/jquery.dataTables.min.css"><script type="text/javascript" language="javascript" src="https://code.jquery.com/jquery-3.6.0.min.js"></script><script>var define = null;</script><script type="text/javascript" language="javascript" src="https://cdn.datatables.net/1.13.4/js/jquery.dataTables.min.js"></script></head><body><h1><center>Billboard Hot 100 Webscrape (Last Updated September 9 2023)</center></h1><table id="demo" class="table"><thead><tr><th>#</th><th>Song</th><th>Artist(s)</th><th>Position Last Week</th><th>Peak Position</th><th>Weeks on Chart</th></tr></thead><tbody>'

# Iterate through the 'lines' list and append HTML table rows
for i in lines:
    nextstr = '<tr><td>'+i[0]+'</td><td>'+i[1]+'</td><td>'+i[2]+'</td><td>'+i[3]+'</td><td>'+i[4]+'</td><td>'+i[5]+'</td></tr>'
    strTable += nextstr

# Finalize the HTML structure with a script to initialize DataTables
strTable = strTable + '</tbody></table></body><script>$("#demo").DataTable();</script>'

# Redirect standard output to a file named 'top100table.html'
sys.stdout = open('top100table.html','w')

# Print the generated HTML table to the output file
print(strTable)
