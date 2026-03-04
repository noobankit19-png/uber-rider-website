from flask import Flask, request

app = Flask(__name__)

def page(content):
    return f"""
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Uber Rider - Professional Ride Booking</title>

<style>
* {{
    margin:0;
    padding:0;
    box-sizing:border-box;
    font-family:Arial, sans-serif;
}}

body {{
    background:#0f0f0f;
    color:white;
}}

header {{
    background:black;
    padding:20px 40px;
    display:flex;
    justify-content:space-between;
    align-items:center;
}}

header h1 {{
    color:#00ffcc;
}}

nav a {{
    color:white;
    text-decoration:none;
    margin-left:20px;
    font-weight:bold;
}}

nav a:hover {{
    color:#00ffcc;
}}

.hero {{
    height:100vh;
    display:flex;
    justify-content:center;
    align-items:center;
    text-align:center;
    background:linear-gradient(to right, #000000, #1c1c1c);
}}

.hero h2 {{
    font-size:48px;
    margin-bottom:20px;
}}

.hero p {{
    font-size:18px;
    margin-bottom:30px;
}}

.btn {{
    padding:12px 25px;
    background:#00ffcc;
    border:none;
    color:black;
    font-weight:bold;
    cursor:pointer;
    border-radius:5px;
}}

.section {{
    padding:80px 40px;
    text-align:center;
}}

.card {{
    background:#1e1e1e;
    padding:30px;
    margin:20px;
    border-radius:10px;
    display:inline-block;
    width:250px;
}}

input {{
    padding:12px;
    width:250px;
    margin:10px;
    border-radius:5px;
    border:none;
}}

footer {{
    background:black;
    padding:30px;
    text-align:center;
}}

footer p {{
    margin:5px 0;
    color:#aaa;
}}
</style>
</head>

<body>

<header>
    <h1>Uber Rider</h1>
    <nav>
        <a href="/">Home</a>
        <a href="/about">About</a>
        <a href="/contact">Contact</a>
    </nav>
</header>

{content}

<footer>
    <p><b>Designed & Developed by ANKIT SAINI</b></p>
    <p>Email: as3126061@gmail.com</p>
    <p>Phone: 8930853165</p>
    <p>© 2026 Uber Rider. All Rights Reserved.</p>
</footer>

</body>
</html>
"""

# ---------------- HOME ----------------
@app.route("/")
def home():
    return page("""
    <div class="hero">
        <div>
            <h2>Book a Ride in Seconds</h2>
            <p>Safe • Fast • Affordable</p>

            <form action="/book" method="POST">
                <input type="text" name="pickup" placeholder="Enter Pickup Location" required><br>
                <input type="text" name="drop" placeholder="Enter Drop Location" required><br>
                <button class="btn" type="submit">Book Now</button>
            </form>
        </div>
    </div>

    <div class="section">
        <h2>Choose Your Ride</h2>
        <div class="card">
            <h3>Bike</h3>
            <p>Low cost, fast ride</p>
        </div>
        <div class="card">
            <h3>Mini</h3>
            <p>Comfortable city rides</p>
        </div>
        <div class="card">
            <h3>Sedan</h3>
            <p>Premium experience</p>
        </div>
    </div>
    """)

# ---------------- BOOK ----------------
@app.route("/book", methods=["POST"])
def book():
    pickup = request.form.get("pickup")
    drop = request.form.get("drop")

    return page(f"""
    <div class="section">
        <h2>Ride Confirmed 🚖</h2>
        <p><b>Pickup:</b> {pickup}</p>
        <p><b>Drop:</b> {drop}</p>
        <p>Your driver will arrive shortly.</p>
        <br>
        <a href="/"><button class="btn">Book Another Ride</button></a>
    </div>
    """)

# ---------------- ABOUT ----------------
@app.route("/about")
def about():
    return page("""
    <div class="section">
        <h2>About Uber Rider</h2>
        <p>This is a professional ride booking web application built using Python Flask.</p>
        <br>
        <h3>Developer</h3>
        <p><b>ANKIT SAINI</b></p>
        <p>Email: as3126061@gmail.com</p>
        <p>Phone: 8930853165</p>
    </div>
    """)

# ---------------- CONTACT ----------------
@app.route("/contact")
def contact():
    return page("""
    <div class="section">
        <h2>Contact Us</h2>
        <p>Email: as3126061@gmail.com</p>
        <p>Phone: 8930853165</p>
    </div>
    """)

# ---------------- RUN ----------------
if __name__ == "__main__":
    app.run(debug=True)
