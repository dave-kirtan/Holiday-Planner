

from bs4 import BeautifulSoup
import requests
import pandas as pd
import csv

url="https://www.booking.com/searchresults.en-gb.html?ss=Paris%2C+Ile+de+France%2C+France&ssne=Ahmedabad&ssne_untouched=Ahmedabad&efdco=1&label=en-in-booking-desktop-SoQWfYhAMBURf0HSQntj1AS652796016141%3Apl%3Ata%3Ap1%3Ap2%3Aac%3Aap%3Aneg%3Afi%3Atikwd-334108349%3Alp1007759%3Ali%3Adec%3Adm&aid=2311236&lang=en-gb&sb=1&src_elem=sb&src=searchresults&dest_id=-1456928&dest_type=city&ac_position=0&ac_click_type=b&ac_langcode=en&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=5cb7934769a10c88&ac_meta=GhA1Y2I3OTM0NzY5YTEwYzg4IAAoATICZW46BXBhcmlzQABKAFAA&checkin=2025-06-03&checkout=2025-06-10&group_adults=2&no_rooms=1&group_children=0"
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
    'Accept-Language': 'en-US, en;q=0.5'
}

response  = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')
# Find all the hotel elements in the HTML document
hotels = soup.findAll('div', {'data-testid': 'property-card'})

hotels_data = []
# Loop over the hotel elements and extract the desired data
for hotel in hotels:
    # Extract the hotel name
    name_element = hotel.find('div', {'data-testid': 'title'})
    name = name_element.text.strip()

    # Extract the hotel location
    location_element = hotel.find('span', {'data-testid': 'address'})
    location = location_element.text.strip()

    # Extract the hotel price
    price_element = hotel.find('span', {'data-testid': 'price-and-discounted-price'})
    price = price_element.text.strip()
    
    # Extract the hotel rating
    rating_element = hotel.find('div', {'class': 'f63b14ab7a dff2e52086'})
    rating = rating_element.text.strip()
    
    # Append hotes_data with info about hotel
    hotels_data.append({
        'name': name,
        'location': location,
        'price': price,
        'rating': rating
    })
hotels = pd.DataFrame(hotels_data)
hotels.head()
hotels.to_csv('hotels.csv', header=True, index=False)    


   
   
    



