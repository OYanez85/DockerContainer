from flask import Flask, send_file
from plotdata import regression_plot

app = Flask(__name__)

@app.route('/', methods=['GET'])
def regi_plot():
    image = regression_plot()  # Ensure this function returns a valid path or file object
    return send_file(image, mimetype='image/png')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)  # Consider setting debug=True for development

