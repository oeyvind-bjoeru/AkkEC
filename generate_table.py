
html = """
<html>
<body>
<table style="width:100%">
<tr>
<th style="text-align:left">Logogram</th>
<th style="text-align:left">Akkadian</th>
<th style="text-align:left">English</th>
</tr>
"""

with open('data/logograms.txt', 'r') as f:
    data = f.read().split('\n')

for entry in data:
    if entry != '':
        form, cf, gw = entry.split('#')
        html += "<tr><td>" + form + "</td><td>" + cf + "</td><td>" + gw + "</td></tr>" + '\n'

html += '</table></body></html>'

with open('data/logograms.html', 'w') as f:
    f.write(html)