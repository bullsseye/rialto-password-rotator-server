# rialto-password-rotator-server

This project is made to send the notification to the client that the time to change the password has come. 
For now its client is only written in ios whose repo link is: https://github.com/bullsseye/password-changer.
Once the IOS app receives the notification, the website will be highlighted whose password should be changed.

Neccessary Requirements:

  1. Virtual Environment. Follow this https://docs.python-guide.org/dev/virtualenvs/
  2. PIP (package manager)
  
How to run the server:
  1. Switch to <your directory>/rialto-pw-rotator and run the following command:
      a. pip install -r requirements.txt
  2. Switch to <your directory>/rialto-pw-rotator and run the following command:
      a. source env/bin/activate
  3. Switch to <your directory>/rialto-pw-rotator/password_rotator and run the following command:
      a. python manage.py runserver
      
How to send the notification:
  1. Fire a POST request without params to http://127.0.0.1:8000/notification/
  
  
 
 
