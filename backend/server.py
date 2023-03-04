import scrape_profile as sp
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/scrape-profiles/<username>')
def scrape_profiles(username):
    data = sp.scrape_profile(username)
    print('res to response : ', data)
    return data

if __name__ == '__main__':
    app.run(port=8080)
