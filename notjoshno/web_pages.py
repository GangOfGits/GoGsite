from flask import render_template, session


##The alert object will be used to handler alert:
#states
#types
#starts
#messages

# class alert(object):
#
#     def __init__(self, state = True, type = "danger", start = "Danger:",
#                  message="You should not be seeing this"):
#         self.state = state
#         self.type = type
#         self.start = start
#         self.message = message

def set_alert(state = False, type = "danger", header = "Danger:",
              message = "You should not be seeing this"):
    session["alert"] = {}
    settings = session["alert"]
    settings["state"] = state
    settings["type"] = type
    settings["header"] = header
    settings["message"] = message


##The web page class will be used to handle web page:
#titles
#alerts
#templates

class web_page(object):

    def __init__(self, template, title):
        self.template = template
        self.title = title

    def render(self):
        try:
            username = session["credentials"]["username"]
        except:
            username = None
        rendered_logged_in_message = ("Logged in as: " + username) if username is not None\
        else "Not currently logged in"

        signed_in_state = True if rendered_logged_in_message[:1] == "L" else False

        alert_settings = session["alert"]
        alert_state = alert_settings["state"]
        alert_type = alert_settings["type"]
        alert_header = alert_settings["header"]
        alert_message = alert_settings["message"]

        return render_template(self.template,
                               title = self.title,
                               logged_in_message = rendered_logged_in_message,
                               signed_in = signed_in_state,
                               alert = alert_state,
                               alert_type = alert_type,
                               alert_header = alert_header,
                               alert_message = alert_message)
