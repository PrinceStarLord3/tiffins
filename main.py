
from flask import Flask, render_template
from pymongo import MongoClient
import config

app = Flask(__name__)
client = MongoClient(config.MONGO_URI)
db = client.get_default_database()

@app.route('/')
def index():
    tiffins = db.tiffins.find()
    return render_template('index.html', tiffins=tiffins)

if __name__ == '__main__':
    app.run(host=config.FQDN, port=config.PORT, debug=True)
