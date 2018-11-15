# View As

## Questions

9.1. Access tokens are strings that are given to users that
exchange authentication credentials. Then, users send the token
to the server which looks up the credentials of the user and sees if
they are authorized.

9.2. The View As privacy feature incorrectly provided the opportunity to post a video, the video uploader
incorrectly generated an access token giving permission of the facebook mobile app and the video uploader showed up
as part of View As, and so it gave the access token for the user you tried to look up. Therefore, these bugs allowed attackers
to get ahold of access tokens they shouldn't have

9.3. They logged accounts out to reset the access tokens of the users they knew were affected.
This was to take away the attackers ability to utilize the tokens.

9.4. Session cookies are temporary unlike access tokens because session cookies are not retained after the browser is closed.
Also, the information stored is not a personal identifier but rather a session identification.

## Debrief

a. https://newsroom.fb.com/news/2018/09/security-update/
https://www.webopedia.com/TERM/S/session_cookie.html

b. 15 minutes
