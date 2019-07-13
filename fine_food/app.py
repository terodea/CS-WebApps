from flask import Flask, render_template, request

app = Flask('Amazon Fine Food Reviews')

@app.route('/')
def show_predict_stock_form():
    return render_template('predictionform.html')

@app.route('/results',method=['POST'])
def results():
    form = request.form
    if request.method == 'POST':
        model = get_model()
        year = request.form['year']
        predicted_stock_price = model.predict(year)
        return render_template('resulsform.html',year=year,predicted_price=predicted_stock_price)
