from flask import Flask, render_template, redirect, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('/index.html')

@app.route('/product')
def product():
    return render_template('/product.html')

@app.route('/product-detail')
def product_detail():
    return render_template('/product-details.html')

@app.route('/cart')
def cart():
    return render_template('/cart.html')

@app.route('/account')
def account():
    return render_template('/account.html')



if __name__ == '__main__':
    app.run(debug=True)
