# 🌤️ WeatherApp

A Python-based weather application that fetches current weather information for any city and announces it using text-to-speech. Get weather updates with voice announcements!

## 🚀 Features

- ✅ Real-time weather data fetching
- ✅ Voice announcement of weather information
- ✅ Support for cities worldwide
- ✅ Temperature in Celsius
- ✅ User-friendly command-line interface
- ✅ API integration with WeatherAPI

## 📋 Requirements

- Python 3.x
- requests library
- pyttsx3 library
- WeatherAPI key

## 🛠️ Installation

1. Clone the repository:
```bash
git clone https://github.com/Sudo-Aditya/WeatherApp.git
cd WeatherApp
```

2. Install required dependencies:
```bash
pip install requests pyttsx3
```

3. Get a free API key from [WeatherAPI](https://www.weatherapi.com/)

4. Update the API key in `main.py`:
```python
url = f"http://api.weatherapi.com/v1/current.json?key=YOUR_API_KEY&q={city}"
```

## 🎯 Usage

1. Run the script:
```bash
python main.py
```

2. Enter the name of the city when prompted
3. The app will fetch and display the current temperature
4. Listen to the voice announcement

## 📖 Example

```
Enter the name of the city
London
15.5
# Voice: "The current weather in London is 15.5 degrees"
```

## 🔧 Features You Can Add

- **Weather Details**: Add humidity, wind speed, and conditions
- **Forecast**: Show weather forecast for upcoming days
- **Units**: Toggle between Celsius and Fahrenheit
- **GUI**: Create a graphical user interface
- **Multiple Cities**: Compare weather across different cities

## 🌐 API Information

This app uses the WeatherAPI service to fetch real-time weather data. The API provides:
- Current weather conditions
- Temperature data
- Location-based weather information
- High accuracy and reliability

## 🤝 Contributing

Feel free to fork this project and submit pull requests for improvements such as:
- Enhanced weather details
- Better error handling
- GUI implementation
- Unit conversion options
- Weather forecast functionality

## 📄 License

This project is open source and available under the MIT License.

## 👨‍💻 Author

Created by **Aditya Naik** - [GitHub](https://github.com/Sudo-Aditya)

---

⭐ Don't forget to star this repository if you found it helpful!