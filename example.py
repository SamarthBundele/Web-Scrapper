import requests
from bs4 import BeautifulSoup 
import pandas as pd 

url = "https://www.eazydiner.com/mumbai/restaurants"

response = requests.get(url) 

if response.status_code == 200: 
    print("Success!")
else:
    print("Error")

data = []
soup = BeautifulSoup(response.text, 'html.parser')


restaurants = soup.find_all('div', class_="padding-10 radius-4 bg-white restaurant margin-b-10")
for restaurant in restaurants: 
    name = restaurant.find('h3', class_='grey res_name font-20 bold inline-block').text 
    rating = restaurant.find('span', class_='critic').text 
    print(name, rating)  
    data.append({"Name": name, "Rating": rating})

df = pd.DataFrame(data)
df.to_csv("restaurants.csv", index=False)






        
