from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

def explore_data(file_path):
    data = pd.read_csv(file_path)
    if data.isnull().any().any():
        info = data.info()
    else:
        info = "No missing values in the dataset."
    stats = data.describe()
    preview = data.head()
    return info, stats, preview

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file_path = request.form['file_path']
        info, stats, preview = explore_data(file_path)
        return render_template('result.html', info=info, stats=stats, preview=preview)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

