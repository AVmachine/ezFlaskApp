from flask import Flask, render_template
import df

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello_world():
    dataframe = df.test_df()
    return render_template('index.html', dataframe=dataframe)


if __name__ == '__main__':
    app.run()
