import re

# Set these two. files are downloaded to the temp folder.
glossary = 'akk.glo'
project = 'akkec_ur3akk'

with open('/Users/oeyvind/Google Drive/Projects/AkkEC/temp/' + glossary, 'r') as f:
    data = f.read().split('\n\n')

values = set()

for entry in data:
    lines = entry.split('\n')
    if '@entry' in lines[0]:
        cf, gw, pos = map(str.strip, lines[0].replace('[', '#').replace(']', '#').replace('entry ', '#').split('#')[1:])

    for line in lines:
        if line[0:5] == '@form':
            dollar = line.find('$')

            form = line[line.find(' '):dollar].strip()
            norm = line[dollar:].replace('$', '').strip()

            dets = re.findall('\{.*?\}', form)
            for det in dets:
                form = form.replace(det, '')
                det = det[1:-1].replace('+', '')
                for each in det.split('-'):
                    values.add(each)
                form = form.replace(det, '')

            for each in form.replace('-', ' ').replace('.', ' ').split():
                values.add(each)

path = 'sign_values/' + project + '.txt'

with open(path, 'w') as f:
    values = str(sorted(list(values)))
    f.write(values)