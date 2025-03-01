import os

import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    message: str

class BibleVerse(BaseModel):
    verse: str
    bible_verse: str

CSV_FILE = "C:/Users/Joanna/Dropbox/PC/Downloads/chars/chars.csv"
BIBLE_CSV_FILE = "C:/Users/Joanna/Dropbox/PC/Downloads/chars/bible_verse.csv"

# Ensure chars.csv exists (your existing code)
if not os.path.exists(CSV_FILE):
    df = pd.DataFrame(columns=["name", "message"])
    df.to_csv(CSV_FILE, index=False)

# Bible CSV creation
if not os.path.exists(BIBLE_CSV_FILE):
    df = pd.DataFrame(columns=["verse", "bible_verse"])
    df.to_csv(BIBLE_CSV_FILE, index=False)

# Existing endpoints for /characters
@app.get("/characters")
def get_all_data():
    df = pd.read_csv(CSV_FILE)
    return df.to_dict(orient="records")

@app.get("/characters/{name}")
def get_data(name: str):
    df = pd.read_csv(CSV_FILE)
    filtered_df = df[df["name"] == name]
    if not filtered_df.empty:
        return filtered_df.iloc[0].to_dict()
    else:
        return {"message": "Character not found"}

@app.post("/characters/{name}")
def receive_data(item: Item):
    df = pd.read_csv(CSV_FILE)
    new_data = pd.DataFrame([{"name": item.name, "message": item.message}])
    df = pd.concat([df, new_data], ignore_index=True)
    df.to_csv(CSV_FILE, index=False)
    return {"message": "Data saved successfully", "data": item}

# New endpoints for /bible_verses
@app.get("/bible_verses")
def get_all_bible_verses():
    df = pd.read_csv(BIBLE_CSV_FILE)
    return df.to_dict(orient="records")

@app.get("/bible_verses/{verse}")
def get_bible_verse(verse: str):
    df = pd.read_csv(BIBLE_CSV_FILE)
    filtered_df = df[df["verse"] == verse]
    if not filtered_df.empty:
        return filtered_df.iloc[0].to_dict()
    else:
        return {"message": "Bible verse not found"}

@app.post("/bible_verses/{verse}")
def receive_bible_verse(bible_verse: BibleVerse):
    df = pd.read_csv(BIBLE_CSV_FILE)
    new_data = pd.DataFrame([{"verse": bible_verse.verse, "bible_verse": bible_verse.bible_verse}])
    df = pd.concat([df, new_data], ignore_index=True)
    df.to_csv(BIBLE_CSV_FILE, index=False)
    return {"message": "Bible verse saved successfully", "data": bible_verse}