# 🏨 Booking.com Scraper
## Project Workflow
. scrape_booking.py — Scrapes hotel data from Booking.com  
. clean_booking.py — Cleans and formats the scraped data  

## Hotel Listings Data Extraction using Selenium

📖 Project Overview  
. This project is a Selenium-based web scraping automation that extracts publicly available hotel listing data from Booking.com for a given city search.  
. It is built as a portfolio-grade project to demonstrate real-world handling of:  
. Dynamic, JavaScript-rendered web pages  
. Reliable element loading using explicit waits  
. Structured data extraction  
. Data cleaning and normalization with pandas  
. The scraper collects hotel-level information and exports clean, analysis-ready datasets in CSV format.  

## 🎯 Intended Use  
. Portfolio demonstration  
. Learning real-world web automation  
. Business-to-business data extraction  

⚠️ This project does not collect personal user data and should always be used in accordance with the target website’s Terms of Service.  

## 📑 Table of Contents  
. Project Overview  
. Features  
. Tech Stack  
. Project Structure  
. Installation  
. Configuration  
. Usage  
. Output  
. How It Works  
. Limitations  
. Troubleshooting  
. License  
. Contact  

## ✨ Features  
. Scrapes dynamic hotel listings rendered with JavaScript  
. Supports infinite scroll / “Load more results” pagination  
. Uses WebDriverWait instead of unreliable time.sleep  
. Prevents duplicate hotel records using URL deduplication  
. Handles missing and stale elements gracefully  
. Cleans and normalizes raw data using pandas  
. Exports both raw and cleaned CSV datasets  

## 🧰 Tech Stack  
. Python 3.10+  
. Selenium  
. pandas  
. numpy  

## 📂 Project Structure  
. booking-com-scraper/  
│ ├── booking_scraper.py # Selenium scraping logic  
│ ├── data_cleaning.py # Data cleaning & normalization  
│ ├── Booking.com_data.csv # Raw scraped data (example)  
│ ├── booking.com_delhi_hotel_data.csv # Cleaned dataset (example)  
│ ├── requirements.txt  
│ └── README.md  

## ⚙️ Installation  
. 1️⃣ Clone the repository  
   git clone https://github.com/ketandas-codes/booking-com-scraper.git  
   cd booking-com-scraper  

. 2️⃣ Create & activate virtual environment  
   python -m venv .venv  
   source .venv/bin/activate # macOS / Linux  
   .venv\Scripts\activate # Windows  

. 3️⃣ Install dependencies  
   pip install -r requirements.txt  

. ✔️ Make sure Google Chrome is installed.  

🔧 Configuration  
. Most settings are controlled directly inside the script:  
. Target city (default: New Delhi)  
. Selenium timeout values  
. Headless / non-headless browser mode  
. Base URL: https://www.booking.com/  

## ▶️ Usage  
. Run the scraper:  
   python booking_scraper.py  

. Default workflow:  
   Opens Booking.com  
   Searches hotels for New Delhi  
   Applies basic filters  
   Loads multiple result pages  
   Saves raw data to Booking.com_data.csv  
   Cleans data and exports booking.com_delhi_hotel_data.csv  

. To change the city:  
   scraper.script_run(text="New Delhi")  

## 📤 Output  
. 🟡 Raw Data — Booking.com_data.csv  
   Unprocessed scraped fields:  
   . hotel_name  
   . hotel_url  
   . price  
   . rating  
   . reviews  
   . address  
   . cancellations  
   . prepayment  
   . property_type  
   . stay_days  

## . 🟢 Cleaned Data — booking.com_delhi_hotel_data.csv  
   Final structured dataset:  
   . hotel_name  
   . hotel_url  
   . price  
   . rating  
   . reviews  
   . address  
   . room_description  
   . cancellations  
   . prepayment  
   . nights  
   . adults  

## 🔍 How It Works (High-Level)  
. Launches Chrome browser using Selenium  
. Loads hotel search results for selected city  
. Waits for hotel cards to load  
. Scrolls page to load additional listings  
. Extracts structured hotel data (including URLs)  
. Stores raw output in CSV  
. Cleans and normalizes data using pandas  
. Exports final CSV files  

## ⚠️ Limitations  
. Designed for small to medium data volumes  
. Website layout changes may require selector updates  
. High-frequency scraping may trigger temporary blocking  

## 🛠 Troubleshooting  
. Update XPath/CSS selectors if elements change  
. Disable headless mode for debugging  
. Reduce scraping frequency if blocked  

## 📜 License  
. MIT License  

## 📬 Contact  
. Ketan Das  
. Python Developer | Web Scraping & Automation  
. GitHub: @ketandas-codes  
. 📧 Email: ketankumar.codes@gmail.com  

