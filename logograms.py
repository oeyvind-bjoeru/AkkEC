import re

with open('data/akk-x-oldbab.glo', 'r') as f:
    data = f.read().split('\n\n')

logograms = set()

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

            # Take off lower case signs at the end.
            while form[-1:].islower() or form[-1:] == '-' or (form[-1:] in ['₀', '₁', '₂', '₃', '₄', '₅', '₆', '₇', '₈', '₉'] and form[-2:-1].islower()):
                form = form[0:-1]

            # Take off MEŠ or HI.A
            if form[-5:] in ['-HI.A', '.HI.A']: form = form[0:-5]
            if form[-4:] in ['-MEŠ', '.MEŠ']: form = form[0:-4]

            # Only . not -
            form = form.replace('-', '.')

            if form[0:1].isupper():
                logogram = form + '#' + cf + '#' + gw
                logograms.add(logogram)

with open('data/logograms.txt', 'w') as f:
    logograms = sorted(list(logograms))
    for logogram in logograms:
        f.write(logogram + '\n')


