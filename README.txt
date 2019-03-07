In Python below are steps for getting temperature in fahrenheit for current location, in this project there are two main files,
urls.py in temperature_rest_api folder and views.py in restapiapp folder.

Step1- Install Requests (Python HTTP library,to make HTTP requests simpler and more human-friendly)

Step2- Make api address from (http://api.openweathermap.org online service that provides weather data) after login in to the site and generate Key

Step3- Write url in urls.py, temperature/fahrenheit 

Step4- Make class base view in view.py, TemperatureFahrenheit and inherit it with APIView(from rest_framework of Django)

Step4- Make get method in TemperatureFahrenheit class, this will calculate temperature of current location in fahrenheit

Step5- Hit http://localhost:8000/temperature/fahrenheit, this URL in your favriot browser or POSTMan client

Step6- This URL will give temperature of current location in fahrenheit and also complete details of weather in this location


-------------------------------------------------------------------------------------------------------------------------


