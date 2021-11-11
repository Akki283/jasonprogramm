from urllib.request import urlopen
import json, re
# Opens the url for the API
url = "https://ip-ranges.amazonaws.com/ip-ranges.json"
r = urlopen(url)
# This should put the response from API in a Dict
result= r.read().decode('utf-8')
data = json.loads(result)

#This shuld get all the names from the the Dict
a=[]
for x in data['ipv6_prefixes']: #TypeError here.
    a.append(x['region'])
counting=a.count("us-east-1")
print(counting)

'''def Convert(list):
    return set(list)
uniqueRegionNames=Convert(a)
print(uniqueRegionNames)'''

b=set(a)
print(b)

# ip prefix ranges
b=[]
for x in data['prefixes']:
    b.append(x['ip_prefix'])
  
startPrefix='15.230'  
startWith15=[x for x in b if x.startswith(startPrefix)]
print(startWith15)
startPrefix2='10.10'
startWith10=[x for x in b if x.startswith(startPrefix2)]
print(startWith10)
