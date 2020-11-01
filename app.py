from flask import Flask, render_template
import df

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello_world():
    dataframe = df.return_dataframe()
    return render_template('index.html', dataframe=dataframe)




if __name__ == '__main__':
    app.run()
