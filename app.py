from flask import Flask, request, redirect, render_template_string

app = Flask(__name__)

marketplace = []

HTML = """
<!DOCTYPE html>
<html>
<head>
<title>StudyHub Marketplace</title>

<style>
body {
    margin: 0;
    font-family: Arial, sans-serif;
    color: white;
    text-align: center;
    overflow-x: hidden;
    background: black;
}

/* holographic animated background */
body::before {
    content: "";
    position: fixed;
    width: 200%;
    height: 200%;
    background: linear-gradient(45deg, #ff00cc, #3333ff, #00ffff, #ff00cc);
    background-size: 400% 400%;
    animation: holoMove 8s linear infinite;
    z-index: -1;
}

@keyframes holoMove {
    0% { transform: translate(-25%, -25%) rotate(0deg); }
    50% { transform: translate(-10%, -10%) rotate(180deg); }
    100% { transform: translate(-25%, -25%) rotate(360deg); }
}

.container {
    background: rgba(255,255,255,0.95);
    color: black;
    max-width: 600px;
    margin: 60px auto;
    padding: 25px;
    border-radius: 15px;
    box-shadow: 0 15px 40px rgba(0,0,0,0.4);
}

h1 {
    margin-top: 30px;
    font-size: 42px;
}

input {
    padding: 10px;
    width: 80%;
    margin: 5px;
    border-radius: 8px;
    border: 1px solid #ccc;
}

button {
    padding: 10px 20px;
    background: #4f46e5;
    color: #50C878;
    border: none;
    border-radius: 8px;
    cursor: pointer;
}

button:hover {
    background: #3730a3;
}

ul {
    list-style: upper-roman;
    padding: 0;
}

li {
    background: #f3f4f6;
    margin: 8px;
    padding: 10px;
    border-radius: 8px;
}
</style>

</head>

<body>

<h1>📑 StudyHub Marketplace🌷</h1>

<div class="container">

<form method="POST">
<input name="name" placeholder="Your Name"><br>
<input name="item" placeholder="Item Name"><br>
<input name="price" placeholder="Price"><br>
<button type="submit">Add Listing</button>
</form>

<h2>Available Listings</h2>

<ul>
{% for listing in listings %}
<li>
<b>{{listing['item']}}</b> — ₹{{listing['price']}}
<br>
Seller: {{listing['name']}}
</li>
{% endfor %}
</ul>

</div>

</body>
</html>
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
    app.run(debug=True)
