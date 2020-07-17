from flask import Flask
from flask import request
from flask import render_template
from validate import validate
from flask import redirect, url_for
from predict import predict
app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return render_template("hello.html", messages=request.args.get("messages") if request.args.get("messages") else None)


@app.route("/data", methods=["post"])
def data():
    form = validate(request.form)
    if(form.validate()):
        predictData = predict(
            age=form.age.data, sex=form.sex.data, embarked=form.embarked.data)
    return redirect(url_for("index", messages=predictData if predictData else 0))
