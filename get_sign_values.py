import re

with open('/Users/oeyvind/Google Drive/Projects/AkkEC/temp/akk.glo', 'r') as f:
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

print(list(values))

with open('data/values.txt', 'w') as f:
    values = sorted(list(values))
    for value in values:
        f.write(value + '\n')