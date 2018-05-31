import re
p = r'^\[.{31}\] \[(.*?)\]'
cp = re.compile(p)

d = {}


with open('error.log') as fh:
    for line in fh:
        #m = re.search(p, line)
        m = cp.search(line)
        if m:
            #d[':error'] = d[':error'] + 1
            d[m.group(1)] = d.get(m.group(1), 0) + 1

print d
