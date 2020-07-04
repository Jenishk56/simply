import re
import collections
st = "my ip is 10.12.122.50 and 10.12.122.51 and 10.12.122.52 10.12.122.50 10.12.122.52"
ips = re.findall( r'[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+', st )
counters = collections.Counter(ips).most_common(2)

counter = {}
for ip in ips:
    if ip in counter:
        counter[ip] += 1
    else:
        counter[ip] = 1

ips = sorted(counter.items(), key = lambda kv:(kv[1], kv[0]), reverse=True)
max = 2
print(ips[:max])


print(counters)