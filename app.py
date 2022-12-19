import findPerson
from flask import Flask, request, render_template, send_file
import os

imgDirectory = os.path.join("static", "IMG")
app = Flask(__name__)


app.config["IMG_DIRECTORY"] = imgDirectory



@app.route('/')
def index():
    return render_template("index.html")


@app.route("/img", methods=["POST"])
def FindPeople():
    if request.method == 'POST':
        image = request.form.get('img')
        findPerson.CheckImage(image)

        img = os.path.join(app.config["IMG_DIRECTORY"], "img.jpg")
        return render_template("img.html", user_image=img)


if __name__ == '__main__':
    app.run(debug=True)
