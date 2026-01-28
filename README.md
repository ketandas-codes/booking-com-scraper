Booking.com Scraper

Project description

This project is a Selenium-based web scraping script that extracts publicly available hotel listing data from Booking.com for a given city search. It is designed as a portfolio-grade automation project demonstrating how to handle dynamic, JavaScript-heavy pages, structured data extraction, and post-processing using pandas.

The scraper collects hotel-level information, such as hotel name, price, rating, reviews, address, cancellation options, property type, and stay details, and exports the cleaned data to CSV files for analysis or reporting.

Intended use: Portfolio demonstration and business-to-business data extraction where the client has the legal right to collect the data. This project does not scrape personal user data and should always be used in compliance with the target website’s Terms of Service.

Table of contents





Project description



Features



Tech stack



Project structure



Installation



Configuration



Usage



Output



How it works (high-level)



Limitations & notes



Troubleshooting



License



Contact

Features





Scrapes dynamic hotel listings rendered with JavaScript



Handles infinite scroll / “Load more results” pagination



Uses WebDriverWait instead of heavy time. sleep



Deduplication of hotel URLs to avoid repeated records



Built-in error handling for stale and missing elements



Data cleaning and normalization using pandas



CSV export for raw and cleaned datasets

Tech stack





Python 3.10+



Selenium



pandas



numpy

Project structure

booking-com-scraper/
│
├── booking_scraper.py        # Selenium scraping logic
├── data_cleaning.py          # Pandas-based data cleaning
├── Booking.com_data.csv      # Raw scraped output (example)
├── booking.com_delhi_hotel_data.csv  # Cleaned dataset (example)
├── requirements.txt
└── README.md


Installation

Clone the repository:

git clone https://github.com/ketandas-codes/booking-com-scraper.git
cd booking-com-scraper


Create and activate a virtual environment:

python -m venv .venv
source .venv/bin/activate      # macOS / Linux
.\.venv\Scripts\activate     # Windows PowerShell


Install dependencies:

pip install -r requirements.txt


Make sure Google Chrome is installed on your system.

Configuration

Most configuration is handled directly inside the script. You can adjust:





Target city (default: New Delhi)



Selenium timeout values



Headless / non-headless browser mode

Base URL used:

https://www.booking.com/


Usage

Run the scraper:

python booking_scraper.py


By default, the script:





Opens Booking.com



Searches hotels for New Delhi



Applies basic filters



Scrolls and loads multiple result pages



Saves hotel data to Booking.com_data.csv



Cleans the data and exports booking.com_delhi_hotel_data.csv

To change the city, update this line in the script:

scraper.script_run(text="New Delhi")


Output

Raw data (Booking.com_data.csv)

Contains unprocessed scraped fields:


hotel_name

price
hotel_url
rating
reviews
address
cancellations
prepayment
property_type
stay_days

Cleaned data (booking.com_delhi_hotel_data.csv)

Includes normalized fields:
hotel_name
price
rating
reviews
address
room_description
nights
adults

How it works (high-level)

Launches a Chrome browser using Selenium

Loads search results for the selected city

Waits for hotel listing cards to appear

Scrolls the page and loads more results

Extracts hotel-level structured data

Stores raw data in CSV format



Cleans and normalizes data using pandas



Exports final CSV files

Limitations & notes

Intended for small to medium data volumes
Website structure changes may require selector updates.
Frequent scraping may trigger temporary blocking.
Always respect the target website’s Terms of Service.
Troubleshooting
If elements are not found, update XPath selectors.
Disable headless mode for debugging UI issues
Reduce scraping frequency if blocking occurs
License
MIT License

Contact
Ketan Das
Python Developer | Web Scraping & Automation
GitHub: @ketandas-codes
Email: ketankumar.codes@gmail.com

Last updated: 2026-01-28
