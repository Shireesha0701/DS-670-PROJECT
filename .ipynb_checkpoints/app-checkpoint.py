{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "354128d6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
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
    "# Load CSV file (Ensure the correct path)\n",
    "csv_path = \"MERGED_FOOD_DATA_WITH_GRAMS.csv\"\n",
    "if not os.path.exists(csv_path):\n",
    "    raise FileNotFoundError(f\"ERROR: CSV file '{csv_path}' not found. Ensure the file exists in the project directory.\")\n",
    "\n",
    "df = pd.read_csv(csv_path, encoding=\"utf-8\")\n",
    "\n",
    "@app.route(\"/\", methods=[\"GET\", \"POST\"])\n",
    "def index():\n",
    "    results = None\n",
    "    if request.method == \"POST\":\n",
    "        query = request.form.get(\"query\", \"\").lower()\n",
    "        if query:\n",
    "            results = df[df['food_name'].str.lower().str.contains(query, na=False)]\n",
    "    return render_template(\"index.html\", results=results)\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    app.run(debug=True, host=\"0.0.0.0\", port=5000)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "39982446",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "498b4981",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f30d1a7b",
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
