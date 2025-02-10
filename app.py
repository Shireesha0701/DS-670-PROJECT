from flask import Flask, render_template, request
import pandas as pd
import os

app = Flask(__name__)

# Load CSV file (Ensure the correct path)
csv_path = "MERGED_FOOD_DATA_WITH_GRAMS.csv"
if not os.path.exists(csv_path):
    raise FileNotFoundError(f"ERROR: CSV file '{csv_path}' not found. Ensure the file exists in the project directory.")

df = pd.read_csv(csv_path, encoding="utf-8")

@app.route("/", methods=["GET", "POST"])
def index():
    results = None
    if request.method == "POST":
        query = request.form.get("query", "").lower()
        if query:
            results = df[df['food_name'].str.lower().str.contains(query, na=False)]
    return render_template("index.html", results=results)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
