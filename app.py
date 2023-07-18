from flask import Flask, render_template
from packages import wallpaper
app = Flask(__name__)

@app.route('/')
def hello_world():
    img_list = wallpaper.return_img()
    return render_template("index.html", img_list=img_list)

if __name__ == "__main__":
    app.run(debug=True)