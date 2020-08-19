# Django Two Factor Authentication

Setting up ENV

    pip install -r requirments.txt
  
Running server

    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver
  
Setting up email for reset password

    Goto the setting file and update
    
    EMAIL_HOST=smtp.gmail.com
    EMAIL_HOST_USER=<email_address>
    EMAIL_HOST_PASSWORD=<email_password>
    
