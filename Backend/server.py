from flask import Flask, send_file, render_template
import io
import pandas as pd
import plotly.express as px

app = Flask(__name__, template_folder='../Frontend/templates', static_folder='../Frontend/static')

data = pd.DataFrame({
    'x': [1, 2, 3, 4, 5],
    'y': [10, 15, 12, 18, 22]
})

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/plot')
def plot():
    fig = px.line(data, x='x', y='y', title='Линейный график')
    
    img = io.BytesIO()
    fig.write_image(img, format='png')
    img.seek(0)
    
    return send_file(img, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
