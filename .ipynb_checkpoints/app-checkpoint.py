{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "4c105b09-18a1-4053-a345-7f8811138537",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "🚀 Starting Food Genie...\n",
      "✅ Loading CSV file...\n",
      "📊 Column Names in CSV: Index(['Unnamed: 0.1', 'food', 'serving_size', 'Caloric Value', 'Fat',\n",
      "       'Saturated Fats', 'Monounsaturated Fats', 'Polyunsaturated Fats',\n",
      "       'Carbohydrates', 'Sugars', 'Protein', 'Dietary Fiber', 'Cholesterol',\n",
      "       'Sodium', 'Water', 'Vitamin A', 'Vitamin B1', 'Vitamin B11',\n",
      "       'Vitamin B12', 'Vitamin B2', 'Vitamin B3', 'Vitamin B5', 'Vitamin B6',\n",
      "       'Vitamin C', 'Vitamin D', 'Vitamin E', 'Vitamin K', 'Calcium', 'Copper',\n",
      "       'Iron', 'Magnesium', 'Manganese', 'Phosphorus', 'Potassium', 'Selenium',\n",
      "       'Zinc', 'Nutrition Density', 'Category'],\n",
      "      dtype='object')\n",
      "🚀 Flask server is starting on http://127.0.0.1:5000/\n",
      " * Serving Flask app '__main__'\n",
      " * Debug mode: on\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.\n",
      " * Running on all addresses (0.0.0.0)\n",
      " * Running on http://127.0.0.1:5000\n",
      " * Running on http://192.168.30.251:5000\n",
      "Press CTRL+C to quit\n",
      " * Restarting with stat\n"
     ]
    },
    {
     "ename": "SystemExit",
     "evalue": "1",
     "output_type": "error",
     "traceback": [
      "An exception has occurred, use %tb to see the full traceback.\n",
      "\u001b[1;31mSystemExit\u001b[0m\u001b[1;31m:\u001b[0m 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\bhaskar\\AppData\\Local\\Packages\\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\\LocalCache\\local-packages\\Python310\\site-packages\\IPython\\core\\interactiveshell.py:3587: UserWarning: To exit: use 'exit', 'quit', or Ctrl-D.\n",
      "  warn(\"To exit: use 'exit', 'quit', or Ctrl-D.\", stacklevel=1)\n"
     ]
    }
   ],
   "source": [
    "from flask import Flask, render_template, request\n",
    "import pandas as pd\n",
    "import os\n",
    "\n",
    "app = Flask(__name__)\n",
    "\n",
    "# Define CSV path\n",
    "csv_path = r\"C:\\Users\\bhaskar\\Downloads\\MERGED_FOOD_DATA_WITH_GRAMS.csv\"\n",
    "\n",
    "# Debugging: Print confirmation that the script is running\n",
    "print(\"🚀 Starting Food Genie...\")\n",
    "\n",
    "# Check if CSV file exists\n",
    "if not os.path.exists(csv_path):\n",
    "    print(f\"❌ ERROR: CSV file '{csv_path}' not found!\")\n",
    "    raise FileNotFoundError(f\"CSV file '{csv_path}' not found.\")\n",
    "\n",
    "# Load CSV data\n",
    "print(\"✅ Loading CSV file...\")\n",
    "df = pd.read_csv(csv_path, encoding=\"utf-8\")\n",
    "\n",
    "# Debug: Print column names\n",
    "print(\"📊 Column Names in CSV:\", df.columns)\n",
    "\n",
    "# Ensure 'food' column exists\n",
    "food_column = \"food\"  # Change based on actual column name\n",
    "if food_column not in df.columns:\n",
    "    raise KeyError(f\"❌ ERROR: '{food_column}' column not found in CSV.\")\n",
    "\n",
    "@app.route(\"/\", methods=[\"GET\", \"POST\"])\n",
    "def index():\n",
    "    results = None\n",
    "    if request.method == \"POST\":\n",
    "        query = request.form.get(\"query\", \"\").strip().lower()\n",
    "        print(f\"🔍 Searching for: {query}\")  # Debugging search\n",
    "        if query:\n",
    "            results = df[df[food_column].str.lower().str.contains(query, na=False)]\n",
    "    return render_template(\"index.html\", results=results)\n",
    "\n",
    "# Debugging: Print a message when the server starts\n",
    "if __name__ == \"__main__\":\n",
    "    print(\"🚀 Flask server is starting on http://127.0.0.1:5000/\")\n",
    "    app.run(debug=True, host=\"0.0.0.0\", port=5000)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f1af9add-0355-4a75-ae97-9e2577530e7c",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.11"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
