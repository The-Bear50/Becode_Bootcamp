# A look at phishing

## Overview of the project
While only knowing that Bob has a dog and is fond of it, I should try to forge an email to lure him into giving me his credentials. Whatever they are.

## Walkthrough
For this, I'll try to force him to log in to Facebook by luring him into sending him an email stating that there are multiple interesting groups that Facebook found around "Dogs".

### Fake Facebook login page
To do this, I just took the HTML and CSS code of the original Facebook login page, saved it locally and I changed it a bit. What I did is deleting all unnecessary scripts and ensure that the page was still running afterwards.
When done, I adapted the HTML code to run a script containing my Webhook.site link page so that each times someone would enter data into the login page, I'd get the answers back on my website.
Here's an example of it :

On the user's side, the first login redirects to the same page which is actually the real URL, as you can see on top :

![1](https://github.com/The-Bear50/Becode_Bootcamp/assets/85135970/b8b08644-6188-4b82-9526-44b579825d88)

![image](https://github.com/The-Bear50/Phishing/assets/85135970/a5ec6f3b-a9fb-4e3f-8f0e-def212aad1b3)

On my side, I got the credentials :

![image](https://github.com/The-Bear50/Phishing/assets/85135970/1908b1b2-406d-4d31-9dd4-2222b1b6b966)

### Fake mail

Couldn't find the time yet in this exercise, but my aim would be to impersonate a Facebook mail that looks like this, but mentioning doglovers groups :

![Untitled](https://github.com/The-Bear50/Becode_Bootcamp/assets/85135970/334ce9f1-7d54-4cb9-9ba9-22b6f971a194)

The Facebook mail I'd want to fake is "suggestions@facebookmail.com" as this domain is owned by Meta, although the mail address probably doesn't exist.
