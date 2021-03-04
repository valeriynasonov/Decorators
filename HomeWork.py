import requests
import hashlib
class Countrie():

    def __init__(self, url, file):
        self.url = url
        self.file = file

    def create_link(self):
        response = requests.get(self.url).json()
        with open(self.file, "w", encoding = "UTF-8") as f:
            for countrie in response:
                link = "https://en.wikipedia.org/wiki/" + countrie["name"]["official"]
                f.write(countrie["name"]["official"] + ":" + link + "\n")
Countrie("https://raw.githubusercontent.com/mledoze/countries/master/countries.json",
         "Countrie - Wikilink").create_link()

def exctraction_md5(url):
    response = requests.get(url, stream=True).json()
    for element in response:
        for k, v in element.items():
            hash_object_1 = hashlib.sha1(k.encode())
            hex_dig = hash_object_1.hexdigest()
            for name, value in v.items():
                hash_object_2 = hashlib.sha1(name.encode())
                for position, value_position in v
                hash_object_3 = hashlib.sha1(value.encode())

            #print(hash_object.hexdigest())
                yield hex_dig, hash_object_2, hash_object_3

for string in exctraction_md5("https://raw.githubusercontent.com/mledoze/countries/master/countries.json"):
    print(string)








