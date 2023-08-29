from flask import render_template
from myproject import app


@app.route('/')
def index():  # put application's code here
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)

