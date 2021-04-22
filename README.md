Blog post on Heroku:
https://drftzblog.herokuapp.com/  <br>
urls: <br>
    - posts/ list of all posts + create post<br>
    - posts/(id) post read, update, delete operations <br>
    - posts/upvote/(id) endpoit to upvote posts <br>
    - comments/ list of all comments <br>
    - comments/create  create comment <br>
    - comments/(id) read, update, delete operations <br>

Instruction: <br>
-docker-compose build<br>
-docker-compose run python manage.py makemigrations<br>
-docker-compose run python manage.py migrate<br>
-docker-compose run python manage.py createsuperuser<br>
-docker-compose up <br>
-go to your browser and insert 'http://127.0.0.1:8000/' <br>


<br>
Postman invite: 
<a>https://identity.getpostman.com/accounts?cta=join-team&invite_code=e1397d63be86c207db7bda06fe850ec2&ws=058852f6-d086-408c-b570-360c335e6022&continue=https%3A%2F%2Fapp.getpostman.com%2Fweb-invite-accept%3Finvite_code%3De1397d63be86c207db7bda06fe850ec2%26ws%3D058852f6-d086-408c-b570-360c335e6022</a>