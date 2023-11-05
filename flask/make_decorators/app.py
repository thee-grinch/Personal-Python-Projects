from flask import Flask

def make_bold(func):
    """this function makes the rendered template to be bold"""
    def wrapper():
        return f"<b>{func()}</b>"
    return wrapper
def make_italic(func):
    """this function makes the rendered template to be italics"""
    def wrapper():
        return f"<em>{func()}</em>"
    return wrapper
def make_underline(func):
    """this function makes the rendered template to be underline"""
    def wrapper():
        return f"<u>{func()}</u>"
    return wrapper

app = Flask(__name__)

@app.route("/")
@make_bold
@make_italic
@make_underline
def say_bye():
    return "<p>Bye</p>"

if __name__ == "__main__":
    app.run(debug=True)
