import requests
url = "https://akabab.github.io/superhero-api/api/all.json"
h = requests.get(url)
list_new = []
for yu in h.json():
   if yu['name'] == "Hulk" or yu['name'] =="Captain America" or yu['name'] == "Thanos":
       list_new.append(yu['powerstats']['intelligence'])

max_namber = max(list_new)
for yu in h.json():
   if yu['name'] == "Hulk" or yu['name'] =="Captain America" or yu['name'] == "Thanos":
       if yu['powerstats']['intelligence'] ==max_namber:
           print(f'Самый умный супергерой - {yu["name"]}')



