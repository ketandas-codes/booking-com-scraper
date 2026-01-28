
import pandas as pd
import numpy as np


row_Data = pd.read_csv("Booking.com_data.csv")
df = row_Data.copy()

# Drop  duplicates 
df = df.drop_duplicates().reset_index(drop=True)
str_cols = df.select_dtypes(include="object").columns
df[str_cols] = df[str_cols].apply(lambda s: s.str.strip().str.lower())

# Clean hotel name
if "hotel_name" in df.columns:
    df["hotel_name"] = df["hotel_name"].str.replace(r"\s+", " ", regex=True).str.strip()

# Clean price
if "price" in df.columns:
    df["price"] = (
        df["price"].astype(str)
        .str.replace(r"[^\d\.]", "", regex=True)  
        .replace("", np.nan)
    )
    df["price"] = pd.to_numeric(df["price"], errors="coerce")

# Clean rating
if "rating" in df.columns:
    df["rating"] = pd.to_numeric(df["rating"], errors="coerce")

# Clean reviews
if "reviews" in df.columns:
    df["reviews"] = (
        df["reviews"].astype(str)
        .str.replace(r"[^\d]", "", regex=True)
        .replace("", np.nan)
    )
    df["reviews"] = pd.to_numeric(df["reviews"], errors="coerce").fillna(0).astype(int)

# Prepayment
if "prepayment" in df.columns:
    df["prepayment"] = df["prepayment"].astype(str).str.replace("prepayment", "", regex=False).str.strip()
    df["prepayment"] = df["prepayment"].replace({"": np.nan, "nan": np.nan}).fillna("unknown")

# Room description
if "property_type" in df.columns:
    df["room_description"] = df["property_type"].astype(str)
    df["room_description"] = df["room_description"].str.replace(r"\([^)]*\d+[^)]*\)", "", regex=True)
    df["room_description"] = df["room_description"].str.split(r"\swith\s| - |,", regex=True).str[0].str.strip()
    df["room_description"] = df["room_description"].replace({"": np.nan})

# Stay nights and adults handle 
stay_candidates = ["stay_dayes", "stay_days", "stay_nights", "stay"]
stay_col = next((c for c in stay_candidates if c in df.columns), None)

if stay_col:
    extracted = df[stay_col].astype(str).str.extract(r"(?P<nights>\d+)\s*nights?,?\s*(?P<adults>\d+)\s*adults?", expand=True)
    df["nights"] = pd.to_numeric(extracted["nights"], errors="coerce").fillna(0).astype(int)
    df["adults"] = pd.to_numeric(extracted["adults"], errors="coerce").fillna(0).astype(int)
else:
    
    df["nights"] = 0
    df["adults"] = 0

# Final columns to export 
final_data = [
    "hotel_name",
    "price",
    "hotel_url",      
    "rating",
    "reviews",
    "address",
    "cancellations",
    "prepayment",
    "room_description",
    "nights",
    "adults",
]
final_existing = [c for c in final_data if c in df.columns]

df[final_existing].to_csv("booking.com_delhi_hotel_data.csv", index=False)