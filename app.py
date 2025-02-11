import os
from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Use the correct path for the CSV file
csv_path = r"D:\Project food Genie\MERGED_FOOD_DATA_WITH_GRAMS.csv"

# Verify if the file exists
if not os.path.exists(csv_path):
    raise FileNotFoundError(f"ERROR: CSV file '{csv_path}' not found. Ensure it is in the project directory.")

# Load CSV
df = pd.read_csv(csv_path, encoding="utf-8")

# Ensure correct column name
food_column = "food"
if food_column not in df.columns:
    raise KeyError(f"ERROR: '{food_column}' column not found in CSV. Available columns: {df.columns}")

@app.route("/", methods=["GET", "POST"])
def index():
    results = None
    if request.method == "POST":
        query = request.form.get("query", "").strip().lower()
        if query:
            results = df[df[food_column].str.lower().str.contains(query, na=False)]
    return render_template("index.html", results=results)

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=5000)
