# Holiday-Planner
Here’s a `README.md` file for your Python project that scrapes hotel data from Booking.com using BeautifulSoup and saves it into a CSV file:

---

# 🏨 Hotel Data Scraper for Booking.com

This Python script scrapes hotel listings for Paris from [Booking.com](https://www.booking.com/) and extracts details like hotel name, location, price, and rating. The data is saved in a CSV file for further analysis or usage.

## 📌 Features

* Scrapes hotel data from Booking.com search results
* Extracts:

  * Hotel name
  * Location
  * Price
  * Rating
* Saves data to a `hotels.csv` file

## ⚠️ Disclaimer

This script is for educational purposes only. Web scraping Booking.com may violate their [Terms of Service](https://www.booking.com/general.en-gb.html). Always check and comply with a website’s terms before scraping.

---

## 🛠 Requirements

* Python 3.7+
* `requests`
* `beautifulsoup4`
* `pandas`

### Install dependencies

```bash
pip install requests beautifulsoup4 pandas
```

---

## 🚀 Usage

1. Clone or download this repository.
2. Run the script:

```bash
python scrape_hotels.py
```

3. The scraped data will be saved to `hotels.csv` in the same directory.

---

## 📁 Output Format

The output CSV file contains:

| name             | location       | price | rating |
| ---------------- | -------------- | ----- | ------ |
| Hotel ABC        | Central Paris  | €120  | 8.5    |
| Paris Luxury Inn | Champs-Elysées | €220  | 9.1    |

---

## 🔧 Customization

You can change the `url` variable in the script to scrape a different city or set of search parameters. Make sure the structure of the Booking.com page hasn’t changed, as this may break the scraper.

---

## 📬 Contact

If you have any questions or improvements, feel free to open an issue or submit a pull request.

---

Would you like me to save this as a file (`README.md`) or help you format it for GitHub or another platform?
