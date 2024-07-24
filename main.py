import requests
from flask import Flask, render_template


app = Flask(__name__)

blog_data = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

@app.route('/')
def home():
    return render_template("index.html", blog_data_=blog_data)


@app.route('/blog/<int:blog_id>')
def get_blog(blog_id):
    requested_post = None
    for blog_post in blog_data:
        if blog_post['id'] == blog_id:
            requested_post = blog_post
    return render_template("post.html", blog_id_=blog_id, blog_data_=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
