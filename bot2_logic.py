import random
import requests
def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>"
    password = ""
    for i in range(pass_length):
        password += random.choice(elements)
    return password
def tirar_moneda():
    x = random.randint(0, 2)
    if x == 1:
        return "Heads."
    elif x == 2:
        return "Tails."
def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']
def get_dog_image_url():
    url = "https://random.dog/woof.json"
    res = requests.get(url)
    data = res.json()
    return data["url"]
