from bs4 import BeautifulSoup
import requests

data = requests.get("https://www.peakpx.com/en/search?q=anime")

soup = BeautifulSoup(data.text, 'html.parser')
def return_img():
    imgs = soup.find_all('img')
    img_link_list = []

    for i in range(1,len(imgs)):
        # img_link_list.append(imgs[i]["data-src"])
        # print(img_link_list)
        img_link_list.append(imgs[i]["data-src"])
    return img_link_list
