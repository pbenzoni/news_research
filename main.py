from flask import Flask, jsonify
import os

app = Flask(__name__)

from flask import Flask, request, render_template_string
import geoip2.database

# Create a Flask application
app = Flask(__name__)

# Load the GeoLite2 database
# Update the path to your GeoLite2 database
reader = geoip2.database.Reader('./GeoLite2-City.mmdb')

# Mapping of state abbreviations to capital cities
state_capitals = {
    "AL": "Montgomery",
    "AK": "Juneau",
    "AZ": "Phoenix",
    "AR": "Little Rock",
    "CA": "Sacramento",
    "CO": "Denver",
    "CT": "Hartford",
    "DC": "Washington",
    "DE": "Dover",
    "FL": "Tallahassee",
    "GA": "Atlanta",
    "HI": "Honolulu",
    "ID": "Boise",
    "IL": "Springfield",
    "IN": "Indianapolis",
    "IA": "Des Moines",
    "KS": "Topeka",
    "KY": "Frankfort",
    "LA": "Baton Rouge",
    "ME": "Augusta",
    "MD": "Annapolis",
    "MA": "Boston",
    "MI": "Lansing",
    "MN": "Saint Paul",
    "MS": "Jackson",
    "MO": "Jefferson City",
    "MT": "Helena",
    "NE": "Lincoln",
    "NV": "Carson City",
    "NH": "Concord",
    "NJ": "Trenton",
    "NM": "Santa Fe",
    "NY": "Albany",
    "NC": "Charlotte",
    "ND": "Bismarck",
    "OH": "Columbus",
    "OK": "Oklahoma City",
    "OR": "Salem",
    "PA": "Harrisburg",
    "RI": "Providence",
    "SC": "Columbia",
    "SD": "Pierre",
    "TN": "Nashville",
    "TX": "Austin",
    "UT": "Salt Lake City",
    "VT": "Montpelier",
    "VA": "Norfolk",
    "WA": "Olympia",
    "WV": "Charleston",
    "WI": "Madison",
    "WY": "Cheyenne"
}


@app.route('/')
def home():
    ip =  request.remote_addr  # Get user's IP address
    try:
        print(ip)
        response = reader.city(ip)
        state = response.subdivisions.most_specific.iso_code
        state_name = response.subdivisions.most_specific.name
        capital = state_capitals.get(state, "Unknown")
    except Exception as e:
        capital = "Washington"
        state_name = "Washington, D.C."


    newspaper_brand = f"{capital} "
    logo_letters = capital[0] + 'T'

    if logo_letters == 'RT':
        news_description = "RT (Russia Today) is a state-funded news provider based in Russia established 2005 and provides a Russian perspective on global events."
        logo_bg = "#77bc1f"
        logo_color = "#000000"

    else:
        news_description = logo_letters + " (" + capital + " Today) is a news provider based in " + state_name + " established 2005 and provides a local and regional perspective on global events."
        logo_bg =  "#304a7b" 
        logo_color = "#ffffff"

    
    news_story_template = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{{ newspaper_brand }}</title>
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Archivo:ital,wght@0,100..900;1,100..900&family=Prosto+One&family=Russo+One&display=swap" rel="stylesheet">

                
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
        <style>
            body {
                font-family: 'Archivo', sans-serif;
            }
            .brand__title {
                font-family: 'Russo One', sans-serif;
                font-size: 56px;
                margin-bottom: 1rem!important;
                margin-top: .5rem!important;
            }
            .article__heading {
                font-size: 46px;
                line-height: 56px;
                margin-bottom: 15px;
                font-weight: 800;
            }
            .article__summary {
                margin-bottom: 40px;
                font-size: 27px;
                line-height: 38px;
                color: #6e6e6e;
            }
            .article__text {
                margin-bottom: 1em;
                font-size: 18px;
                line-height: 23px;
            }
            .article__text p{
                margin-bottom: 20px;
                }
            }
        </style>
    </head>
    <body>
        <div class="container mt-5">
        <div class="col-lg-2"></div>
        <div class="col-lg-8">
                <div class="alert alert-primary" role="alert">{{ news_description }}</div>
                <div class="text-center row">
                    <div class="col-lg-2">
                        <svg width="100" height="100" xmlns="http://www.w3.org/2000/svg">
                        <rect width="100%" height="100%" fill="{{ logo_bg }}"/> 
                        <text x="50%" y="55%" dominant-baseline="middle" text-anchor="middle" font-family="Russo One" textLength="85" lengthAdjust="spacingAndGlyphs" font-size="40" font-weight="bold" fill="{{ logo_color }}" letter-spacing="-5">
                            {{ logo_letters }}
                        </text>
                        </svg>
                    </div>
                    <div class="col-lg-10 brand__title">
                        <div class="text-left mb-3  d-flex align-items-center">{{ newspaper_brand }} Today </div>
                    </div>
                </div>
                <hr>
                <div class="article__heading">Australia’s unemployment rate hits two-year high – data</div>
                <div class="article__summary">Joblessness accelerated in January, jumping above 4%, official statistics show.</div>
                <div class="article__text">
                    <p>Australia’s unemployment rate has risen to its highest level since early 2022, hitting 4.1% in January, the Australian Bureau of Statistics (ABS) reported on Thursday.</p>

                    <p>The figure is slightly above the consensus expectation of 4%, an uptick from December’s reported 3.9%. The economy added 11,100 full-time jobs and shed 10,600 part-time jobs last month, according to the data.</p>

                    <p>The report added to concerns of slack in the country’s labor market in the face of a slowing economy and subdued consumer demand. Economists warn that unemployment could further deteriorate later in the year.</p>

                    <p>Commenting on the report, ABS head Bjorn Jarvis noted a changing seasonal dynamic in the labor market around when people start working after the summer holiday period in January. “While there were more unemployed people in January, there were also more unemployed people who were expecting to start a job in the next four weeks,” Jarvis said.</p>

                    <p>Meanwhile, Treasurer Jim Chalmers said during a press conference on Thursday that the latest figures indicate that the labor market continues to soften in expected ways. “This is also the inevitable consequence of higher interest rates and persistent inflation and global economic uncertainty, because of the pressures that people are under, the pressures our economy is under, and indeed the global economy as well – those are largely the reasons for the tick up in the unemployment rate that we are seeing today,” concluded Chalmers.</p>
                </div>
            </div>
        </div>
                <div class="col-lg-2"></div>
    </body>
    </html>
    """

    return render_template_string(news_story_template, newspaper_brand=newspaper_brand, logo_letters=logo_letters, news_description=news_description, logo_bg=logo_bg, logo_color=logo_color)

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
