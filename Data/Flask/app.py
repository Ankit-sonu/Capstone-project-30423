from flask import Flask, render_template, request


app = Flask(__name__)
books = []
book = any;

@app.route("/")
def home():
    return render_template("login.html")

@app.route("/add")
def add():
    return render_template("addbookpage.html")

@app.route("/addbook")
def addbook():
    isbn = request.args.get('isbn')
    name = request.args.get('name')
    publisher = request.args.get('publisher')
    price = request.args.get('price')
    book = {
        "isbn":isbn,
        "name":name,
        "publisher":publisher,
        "price":price
    }
    books.append(book)
    return render_template('success.html')

@app.route("/display")
def display():
    return render_template("display.html", books=books)

@app.route("/validate")
def validate():
    username = request.args.get('lid')
    password = request.args.get('pwd')
    if username == "admin" and password == "12345":
        return render_template('success.html', username=username)
    else:
        return render_template("fail.html", username=username)

@app.route("/search", methods=["GET", "POST"])
def search():
    result = None
    if request.method == "POST":
        isbn = request.form.get("isbn")
        for book in books:
            if book["isbn"] == isbn:
                result = book
                break
    return render_template("search.html", result=result)

@app.route("/delete", methods=["GET", "POST"])
def delete():
    message = ""
    if request.method == "POST":
        isbn = request.form.get("isbn")
        for book in books:
            if book["isbn"] == isbn:
                books.remove(book)
                message = f"Book with ISBN {isbn} deleted successfully."
                break
        else:
            message = f"No book found with ISBN {isbn}."
    return render_template("delete.html", message=message)

if __name__ == '__main__':
    app.run(debug=True)