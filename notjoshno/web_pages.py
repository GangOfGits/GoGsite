from flask import render_template, session


##The alert object will be used to handler alert:
#states
#types
#starts
#messages

class alert(object):

    def __init__(self, state = True, type = "danger", start = "Danger:",
                 message="You should not be seeing this"):
        self.state = state
        self.type = type
        self.start = start
        self.message = message


##The web page class will be used to handle web page:
#titles
#alerts
#templates

class web_page(object):

    def __init__(self, template, title):
        self.template = template
        self.title = title

    def render(self, alert=alert(state = False)):
        try:
            username = session["username"]
        except:
            username = None
        rendered_logged_in_message = ("Logged in as: " + username) if username is not None\
        else "Not currently logged in"

        return render_template(self.template,
                               title = self.title,
                               logged_in_message=rendered_logged_in_message,
                               alert=alert.state,
                               alert_type=alert.type,
                               alert_start=alert.start,
                               alert_message=alert.message)
