from flask import Flask, render_template, request
import pandas as pd
import os

app = Flask(__name__)

# Define CSV path (Corrected for Windows)
csv_path = r"D:\Project food Genie\MERGED_FOOD_DATA_WITH_GRAMS.csv"

# Debugging: Print confirmation that the script is running
print("🚀 Starting Food Genie...")

# Check if CSV file exists
if not os.path.exists(csv_path):
    print(f"❌ ERROR: CSV file '{csv_path}' not found!")
    raise FileNotFoundError(f"CSV file '{csv_path}' not found.")

# Load CSV data
print("✅ Loading CSV file...")
df = pd.read_csv(csv_path, encoding="utf-8")

# Debug: Print column names
print("📊 Column Names in CSV:", df.columns)

# Ensure 'food' column exists
food_column = "food"  # Change based on actual column name
if food_column not in df.columns:
    raise KeyError(f"❌ ERROR: '{food_column}' column not found in CSV.")

@app.route("/", methods=["GET", "POST"])
def index():
    results = None
    if request.method == "POST":
        query = request.form.get("query", "").strip().lower()
        print(f"🔍 Searching for: {query}")  # Debugging search
        if query:
            results = df[df[food_column].str.lower().str.contains(query, na=False)]
    return render_template("index.html", results=results)

# Debugging: Print a message when the server starts
if __name__ == "__main__":
    print("🚀 Flask server is starting on http://127.0.0.1:5000/")
    app.run(debug=True, host="0.0.0.0", port=5000)
