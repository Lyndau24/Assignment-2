import requests
from flask import Flask, render_template

#import weather

app = Flask('app')

@app.route('/')

def Home():
  return render_template("index.html")

@app.route('/edu')
def Education():
  return render_template("edu.html")

@app.route('/exp')
def Experience():
  return render_template("exp.html")

@app.route('/skills')
def Skills():
  return render_template("skills.html")

@app.route('/art')
def Articles():
  return render_template("art.html")

@app.route('/links')
def Links():
  return render_template("links.html")


@app.route('/weather')
def Weather():
     
    city = 'Ottawa'
    url = f"https://api.openweathermap.org/data/2.5/weather?q=Ottawa&appid=0a8ea4b77962efa777bb237b4e923d1a&units=metric"

    response = requests.get(url)
    data = response.json()

    weather_details = {
        'temperature': data['main']['temp'],
        'wind': data['wind']['speed'],
        'pressure': data['main']['pressure'],
        'humidity': data['main']['humidity'],
        'description': data['weather'][0]['description']
    }

    return render_template("weather.html", weather=weather_details)

@app.route('/bmi')
def BMI():
    #values for weight and height
    weight = 93  # in kg
    height = 172  # in meters

    # BMI Calculation
    bmi_value = round(weight / (height ** 2),2)

    # Determine BMI status
    if bmi_value < 18.5:
        status = "Underweight"
    elif bmi_value < 25:
        status = "Normal weight"
    elif bmi_value < 30:
        status = "Overweight"
    else:
        status = "Obese"
      
    print(f"Your BMI is: {bmi_value}")
    print(f"Status: {status}")

    return render_template("bmi.html", weight=weight, height=height, bmi=bmi_value, status=status)


if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8080)
  