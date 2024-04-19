#web page that has posts below each other
import requests
from flask import Flask, render_template

app = Flask(__name__)
@app.route('/', strict_slashes=False)
def home():
    posts_url = "https://jsonplaceholder.typicode.com/posts"
    posts_fetching = requests.get(posts_url)
    posts_jsonifying = posts_fetching.json()
    userId = []
    userBody = []
    userTitle = []
    for i in posts_jsonifying:
        userId.append(i["userId"])
        userBody.append(i["body"])
        userTitle.append(i["title"])
        
    usrIdLen = len(userId)
    # return str(usrIdLen)
    return render_template('index.html', userId=userId, userBody=userBody, userTitle=userTitle, usrIdLen=usrIdLen)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
