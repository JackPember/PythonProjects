from tkinter import *
from _datetime import datetime
import requests

# Create the GUI Window:

root = Tk()
root.geometry("525x525")  # default window size
root.resizable(0, 0)  # make window fixed size
root.title("Simple Python Weather GUI")

# Functions that fetch weather info from API and display the weather info
city = StringVar()


# change the time format, function checks local time compared to UTC time, as API gives UTC time.
def time_format_for_location(utc_with_tz):
    local_time = datetime.utcfromtimestamp(utc_with_tz)
    return local_time.time()


def getWeather():
    # api key from openweathermap.org, you can get your own by making an account
    api_key = "441e2cb8af7b379cf6fe3e759c77fca4"
    # city name obtained from user input in GUI
    city_name = city.get()
    # URL for api to get weather
    weather_URL = "http://api.openweathermap.org/data/2.5/weather?q=" + city_name + '&appid=' + api_key
    # get api response from the URL
    response = requests.get(weather_URL)
    # change response from json response to a python readable response
    weather_info = response.json()
    # clear text field for every output
    tfield.delete("1.0", "end")
    # as known from API documentation, cod = 200 means that weather data was successfully obtained
    if weather_info['cod'] == 200:
        kelvin = 273  # temperature in kelvin

        # sort the fetched weather values of a city based on user input
        temp = int(weather_info['main']['temp'] - kelvin)
        temp_feels_like = int(weather_info['main']['feels_like'] - kelvin)
        air_pressure = weather_info['main']['pressure']
        humidity = weather_info['main']['humidity']
        wind_speed = weather_info['wind']['speed'] * 3.6
        sunrise = weather_info['sys']['sunrise']
        sunset = weather_info['sys']['sunset']
        timezone = weather_info['timezone']
        cloudy = weather_info['clouds']['all']
        description = weather_info['weather'][0]['description']

        sunrise_time = time_format_for_location(sunrise + timezone)
        sunset_time = time_format_for_location(sunset + timezone)

        # assign values to weather variable for output display
        weather = f"\nWeather of: {city_name}\nTemperature (Celsius): {temp}°\nFeels like in (Celsius): {temp_feels_like}°\nAir Pressure: {air_pressure} hPA\nHumidity: {humidity}%\nSunrise at {sunrise_time}, Sunset at {sunset_time}\nClouds: {cloudy}%\nInfo: {description}"
    else:
        weather = f"\n\tWeather for '{city_name}' not found!\n\tPlease enter a valid city."

    tfield.insert(INSERT, weather)


# starting the GUI
city_label_head = Label(root, text='Enter a City Name', font='Tahoma 12 bold').pack(pady=12)  # label heading
input_city = Entry(root, textvariable=city, width=28, font='Tahoma 14 bold').pack()  # entry field for getting the city
# button to get the weather with the command being the function to fetch weather from API upon button click
Button(root, command=getWeather, text="Check the weather", font="Tahoma 10", bg='cyan', fg='black',
       activebackground='white', padx=5, pady=5).pack(pady=20)
current_weather = Label(root, text="The Current Weather is: ", font='Tahoma 12 bold').pack(pady=10)
tfield = Text(root, width=50, height=12)
tfield.pack()

root.mainloop()
