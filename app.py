from flask import Flask, request, redirect, url_for, render_template
from flask import session as login_session
from databases import query_all, createSession

app = Flask(__name__)
app.secret_key = "MY_SUPER_SECRET_KEY"


##### Code here ######
@app.route('/')
def homePage():
	return render_template("home.html")

@app.route('/store')
def store():
	allproducts = query_all()
	return render_template("store.html",allproducts=allproducts)

@app.route('/cart')
def cart():
	n = query_all()
	return render_template("cart.html")

@app.route('/about')
def about():
	return render_template("about.html")
		
#####################

if __name__ == '__main__':
    app.run(debug=True)

# addProduct("denim skirt", 15.78, "product2")
# print(query_all())