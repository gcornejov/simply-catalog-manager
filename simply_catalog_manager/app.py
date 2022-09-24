import os

from flask import Flask, render_template

from .src import category_builder

app = Flask(__name__)


@app.route("/")
def hello_world():
    # return "<p>Hello, World!</p>"

    # test_dict = {
    #     "hello": "world"
    # }

    # return test_dict

    return render_template("index.html")


@app.route("/products")
def load_categories():
    print(os.getcwd())
    print(os.listdir())
    categories = category_builder.read_categories(
        "simply_catalog_manager/data/categories.json"
    )

    return render_template("categories.html", categories=categories)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
