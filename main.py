from bs4 import BeautifulSoup
import requests

url = 'https://www.officialcharts.com/charts/albums-chart'
#https://www.timeout.com/film/best-movies-of-all-time
#https://www.officialcharts.com/charts/albums-chart
#https://www.cbr.com/greatest-tv-shows-all-time
#https://thegreatestbooks.org/lists/44
#https://www.babbel.com/en/magazine/the-10-most-spoken-languages-in-the-world
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0'}
result = requests.get(url, headers=headers)

soup = BeautifulSoup(result.text, 'html.parser')
images_in_bs4 = soup.find_all("img")
image_list = [image for image in images_in_bs4]
print(len(image_list))