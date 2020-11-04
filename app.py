from flask import Flask, render_template, Response
import df, io
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import pylab

app = Flask(__name__)


@app.route('/', methods=['GET'])
def get_data():
    dataframe = df.test_df()
    return render_template('index.html', dataframe=dataframe)


@app.route('/plot.png')
def plot_png():
    fig = create_figure()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')


def create_figure():
    dataframe = df.test_df()
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    axis.hist(dataframe['averageRating'])
    return fig


if __name__ == '__main__':
    app.run()
