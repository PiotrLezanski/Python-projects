from flask import Flask, render_template, request, send_file
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename

app = Flask(__name__)
# when deploying web app through pythonanywhere, this should be: = 'mysql+mysqlconnector://lezio:flaskapp12321@lezio.mysql.pythonanywhere-services.com/lezio$height_collector'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres12321@localhost/height_collector'
db = SQLAlchemy(app)


class Data(db.Model):
    __tablename__ = "data"
    id = db.Column(db.Integer, primary_key=True)
    # 120 is the limit
    email = db.Column(db.String(120), unique=True)
    height = db.Column(db.Integer)

    def __init__(self, email, height):
        self.email = email
        self.height = height


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/success', methods=["POST"])
def success():
    global file
    # checking if user reached success.html through submitting data
    if request.method == "POST":
        file = request.files["file"]
        file.save(secure_filename("uploaded"+file.filename))
        with open("uploaded"+file.filename, "a") as f:
            f.write("This was added later.")

        return render_template("index.html", btn="download.html")


@app.route('/download')
def download():
    return send_file("uploaded"+file.filename, attachment_filename="yourfile.csv", as_attachment=True)

# db.init_app(app)
# db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
