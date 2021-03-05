from flask import Flask
from flask import render_template , request
from color_check.controllers.get_color_code import get_color_code
from color_check.controllers.record_log import record_log
from datetime import datetime


app = Flask(__name__)



@app.route('/')
def index():
    
    return render_template('index.html', page_title="Color Check")


@app.route('/color', methods=['POST'])
def show_color():
    # When the user submits the form at /, the contents of the form
    # will be send to this route, and whatever code you write here will
    # be run by your server. In order to render a new page for your user,
    # you will need to do a few things:
    # - extract the data submitted by the user
    # - check if the color exists in our list, return the hex code if it does
    # - render a new page which shows a square of that color and its name
    # - if the color doesn't exist, give the user a useful error message.
    # - create a log.txt file which records (logs) the user requests. 
    log_timestamp = datetime.now()
    user_submitted_string = request.form.get("color")
    color_hex_code = get_color_code(user_submitted_string)
    

    if not color_hex_code:
        inquiery = "Invalid Input"
        record_log(user_submitted_string, log_timestamp, inquiery)
        return render_template('invalid_color.html', message="There's no color as such", log_timestamp = log_timestamp)
    
    else:
        inquiery = "Valid Input"
        record_log(user_submitted_string, log_timestamp, inquiery)
        return render_template('color.html', page_title="Show Color",
                            color_hex_code=color_hex_code,log_timestamp = log_timestamp, color = user_submitted_string)


if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)
