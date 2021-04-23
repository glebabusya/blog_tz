# Blog post on Heroku:
## https://drftzblog.herokuapp.com/posts <br>
urls: <br>
- posts/ list of all posts + create post<br>
- posts/(id) post read, update, delete operations <br>
- posts/upvote/(id) endpoit to upvote posts <br>
- comments/ list of all comments <br>
- comments/create create comment <br>
- comments/(id) read, update, delete operations <br>

Instruction: <br>
-git clone https://github.com/glebabusya/blog_tz blog_tz<br>
-cd blog_tz <br>
-docker-compose build<br>
-docker-compose up <br>
<br>
local urls = [127.0.0.1, localhost]<br>
<br>

To create user: <br>
open other terminal and past:
#### docker-compose exec -it blog_tz_web_1 python manage.py createsuperuser



<br>
Postman invite:
<a>https://identity.getpostman.com/accounts?cta=join-team&invite_code=e1397d63be86c207db7bda06fe850ec2&ws=058852f6-d086-408c-b570-360c335e6022&continue=https%3A%2F%2Fapp.getpostman.com%2Fweb-invite-accept%3Finvite_code%3De1397d63be86c207db7bda06fe850ec2%26ws%3D058852f6-d086-408c-b570-360c335e6022</a>
<br>
