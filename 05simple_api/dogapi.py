import json
import urllib2

# open the url and the screen name 
# (The screen name is the screen name of the user for whom to return results for)
url = "https://dog.ceo/api/breeds/image/random"

# this takes a python object and dumps it to a string which is a JSON
# representation of that object
data = json.load(urllib2.urlopen(url))
print(data)

#extract url image url
pic_url = data['message']
print(pic_url)

#open a new file named dopapi.html
f = open("dogapi.html", "w4")

#create html code with the image url inlcuded
html_code = "<html> <body><img src={}></body></html>".format(pic_url)

#write code to html file
f.write(html_code)
