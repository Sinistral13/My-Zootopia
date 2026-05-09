Animal Data Generator



A simple Python project that fetches animal information from the API Ninjas Animals API and generates an HTML page displaying the results.





Features



Fetches real-time animal data from an external API

Generates a dynamic HTML file

Displays:

Animal name

Diet

Location

Type

Handles invalid animal names gracefully

Uses environment variables to securely store the API key.





Requirements



Python 3.x

requests

python-dotenv





API Setup



This project uses the Animals API from API Ninjas.



Create an account at:

https://api-ninjas.com/

Generate your API key.





How It Works



The user enters an animal name.

The program sends a request to the API.

Animal data is retrieved and processed.

The placeholder inside the HTML template is replaced with generated animal cards.

A new animals.html file is created.





Usage



Run the program: animal\_web\_generator.py



Example:

Please enter an animal name: lion



After running the script, an animals.html file will be generated in the project directory.



Open it in your browser to view the results.

