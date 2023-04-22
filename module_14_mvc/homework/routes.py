from flask import Flask, render_template
from typing import List
from flask import request, Response
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired

from models import init_db, get_all_books, DATA, Book, add_book

app: Flask = Flask(__name__)


def _get_html_table_for_books(books: List[dict]) -> str:
    table = """
<table>
    <thead>
    <tr>
        <th>ID</td>
        <th>Title</td>
        <th>Author</td>
    </tr>
    </thead>
    <tbody>
        {books_rows}
    </tbody>
</table>
"""
    rows: str = ''
    for book in books:
        rows += '<tr><td>{id}</tb><td>{title}</tb><td>{author}</tb></tr>'.format(
            id=book['id'], title=book['title'], author=book['author'],
        )
    return table.format(books_rows=rows)


@app.route('/books')
def all_books() -> str:
    return render_template(
        'index.html',
        books=get_all_books(),
    )


class AddBookForm(FlaskForm):
    book_title = StringField(validators=[InputRequired()])
    author_name = StringField(validators=[InputRequired()])


@app.route('/books/form', methods=['GET', 'POST'])
def get_books_form() -> str | Response:
    if request.method == 'GET':
        return render_template('add_book.html')
    elif request.method == "POST":
        form = AddBookForm(request.form)
        if form.validate_on_submit():
            book = Book(
                title=request.form["book_title"],
                author=request.form["author_name"],
                id=None
            )
            add_book(book)
            return Response({"msg": "Ok"}, status=200, mimetype='application/json')
        else:
            return Response(status=418)


if __name__ == '__main__':
    init_db(DATA)
    app.config["WTF_CSRF_ENABLED"] = False
    app.run(debug=True)
