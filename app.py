from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def home():
    with open('major.json', 'r') as major_file, \
         open('pentacles.json', 'r') as pentacles_file, \
         open('swords.json', 'r') as swords_file, \
         open('cups.json', 'r') as cups_file, \
         open('wands.json', 'r') as wands_file:
        major_data = json.load(major_file)
        pentacles_data = json.load(pentacles_file)
        swords_data = json.load(swords_file)
        cups_data = json.load(cups_file)
        wands_data = json.load(wands_file)
    return render_template('index.html', major=major_data, pentacles=pentacles_data, swords=swords_data, cups=cups_data, wands=wands_data)

if __name__ == '__main__':
    app.run(debug=True)