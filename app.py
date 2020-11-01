from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello_world():
    list = [0, 1, 2, 3]
    return render_template('index.html', list=list)




if __name__ == '__main__':
    app.run()
