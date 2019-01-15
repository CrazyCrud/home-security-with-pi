import datetime
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    date_now = datetime.datetime.now()
    date_now_formatted = date_now.strftime("%Y-%m-%d %H:%M")

    template_data = {
        'title': 'HELLO!',
        'time': date_now_formatted
    }

    return render_template('index.html', **template_data)


if __name__ == "__main__":
    app.run(debug=True, port=80, host='0.0.0.0')
