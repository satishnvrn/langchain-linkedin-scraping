from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify
from ice_breaker import ice_breaker_with

load_dotenv()

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/process", methods=["POST"])
def process():
    name = request.form["name"]
    summary, profile_pic_url = ice_breaker_with(name)
    return jsonify(
        {
            "summary": summary.to_dict(),
            "profile_pic_url": profile_pic_url,
        }
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=3000)
