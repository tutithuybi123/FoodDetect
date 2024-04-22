from flask import Flask, render_template
from detect import get_ingredients
from api import get_nutrion_by_id, get_recipes_by_ingredients
import os

# Get file path
def get_file_path(filename):
    return os.path.join(os.path.dirname(__file__), filename)

app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')

if __name__ == '__main__':  
   app.run(host="127.0.0.1", port=2010, debug=True)