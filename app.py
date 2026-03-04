from flask import Flask

app = Flask(__name__)

def page(content):
    return f"""
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Uber Rider - Professional Ride Booking</title>

<script src="https://maps.googleapis.com/maps/api/js?key=YOUR_GOOGLE_MAPS_API_KEY&libraries=places"></script>

<style>
* {{
    margin:0;
    padding:0;
    box-sizing:border-box;
    font-family:Arial, sans-serif;
}}

body {{
    background:#111;
    color:white;
}}

header {{
    background:black;
    padding:20px 40px;
    display:flex;
    justify-content:space-between;
}}

header h1 {{
    color:#00ffcc;
}}

nav a {{
    color:white;
    text-decoration:none;
    margin-left:20px;
}}

nav a:hover {{
    color:#00ffcc;
}}

.hero {{
    padding:60px;
    text-align:center;
}}

input, select {{
    padding:12px;
    width:260px;
    margin:10px;
    border-radius:5px;
    border:none;
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

#map {{
    height:400px;
    width:100%;
    margin-top:30px;
}}

footer {{
    background:black;
    padding:30px;
    text-align:center;
    margin-top:40px;
    color:#aaa;
}}
</style>

<script>
let map;
let directionsService;
let directionsRenderer;

function initMap() {{
    map = new google.maps.Map(document.getElementById("map"), {{
        center: {{ lat: 28.6139, lng: 77.2090 }},
        zoom: 10,
    }});

    directionsService = new google.maps.DirectionsService();
    directionsRenderer = new google.maps.DirectionsRenderer();
    directionsRenderer.setMap(map);
}}

function calculateRoute() {{
    const pickup = document.getElementById("pickup").value;
    const drop = document.getElementById("drop").value;
    const rideType = document.getElementById("rideType").value;

    let pricePerKm = 12;

    if (rideType === "Bike") {{
        pricePerKm = 8;
    }} else if (rideType === "Mini") {{
        pricePerKm = 12;
    }} else if (rideType === "Sedan") {{
        pricePerKm = 18;
    }}

    directionsService.route(
        {{
            origin: pickup,
            destination: drop,
            travelMode: "DRIVING",
        }},
        function (result, status) {{
            if (status === "OK") {{
                directionsRenderer.setDirections(result);

                const distance = result.routes[0].legs[0].distance.value / 1000;
                const price = distance * pricePerKm;

                document.getElementById("price").innerHTML =
                    "Ride Type: " + rideType + "<br>" +
                    "Distance: " + distance.toFixed(2) + " km<br>" +
                    "Rate: ₹" + pricePerKm + "/km<br>" +
                    "<b>Estimated Fare: ₹" + price.toFixed(2) + "</b>";
            }} else {{
                alert("Could not calculate route.");
            }}
        }}
    );
}}
</script>
</head>

<body onload="initMap()">

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
    <p>© 2026 Uber Rider Clone</p>
</footer>

</body>
</html>
"""

@app.route("/")
def home():
    return page("""
    <div class="hero">
        <h2>Book Your Ride</h2>

        <input type="text" id="pickup" placeholder="Enter Pickup Location">
        <input type="text" id="drop" placeholder="Enter Drop Location"><br>

        <select id="rideType">
            <option value="Bike">Bike - ₹8/km</option>
            <option value="Mini">Mini - ₹12/km</option>
            <option value="Sedan">Sedan - ₹18/km</option>
        </select>
        <br>

        <button class="btn" onclick="calculateRoute()">Calculate Ride</button>

        <div id="price" style="margin-top:20px; font-size:18px;"></div>

        <div id="map"></div>
    </div>
    """)

@app.route("/about")
def about():
    return page("""
    <div class="hero">
        <h2>About Uber Rider</h2>
        <p>Professional ride booking system built with Python Flask 
        and Google Maps integration with dynamic pricing.</p>
    </div>
    """)

@app.route("/contact")
def contact():
    return page("""
    <div class="hero">
        <h2>Contact</h2>
        <p>Email: as3126061@gmail.com</p>
    </div>
    """)

if __name__ == "__main__":
    app.run(debug=True)
