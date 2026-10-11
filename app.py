import random

from flask import Flask, render_template, request

app = Flask(__name__)

# Same character set as the original main.py
PASSWORD_CHARS = "+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"


def generate_password(length):
    return "".join(random.choice(PASSWORD_CHARS) for _ in range(length))


@app.route("/", methods=["GET", "POST"])
def index():
    password = None
    error = None
    if request.method == "POST":
        try:
            length = int(request.form.get("length", "16"))
            if length < 1:
                error = "Length must be at least 1."
            elif length > 1000:
                error = "Length must be 1000 or less."
            else:
                password = generate_password(length)
        except ValueError:
            error = "Please enter a valid number."
    return render_template("index.html", password=password, error=error)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)
