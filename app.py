from flask import Flask, request, redirect, render_template_string

app = Flask(__name__)

marketplace = []

HTML = """
<h1>Student Marketplace Prototype</h1>

<form method="POST">
    Name: <input name="name"><br>
    Item: <input name="item"><br>
    Price: <input name="price"><br>
    <button type="submit">Add Listing</button>
</form>

<h2>Listings</h2>
<ul>
{% for listing in listings %}
<li><b>{{listing['item']}}</b> - ₹{{listing['price']}} ({{listing['name']}})</li>
{% endfor %}
</ul>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        listing = {
            "name": request.form["name"],
            "item": request.form["item"],
            "price": request.form["price"]
        }
        marketplace.append(listing)
        return redirect("/")

    return render_template_string(HTML, listings=marketplace)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
    