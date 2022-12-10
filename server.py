from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET"])
def root():
    return render_template("index.html")


@app.route("/predict", methods=["GET"])
def predict():
    # user's input
    experience = float(request.args.get("experience"))

    import pickle

    model_file = open("salary_prediction.pk", "rb")
    model = pickle.load(model_file)
    model_file.close()
    salaries = model.predict([[experience]])
    return f"Your salary = {salaries[0]}"


app.run(port=8080, debug=True, host="0.0.0.0")
