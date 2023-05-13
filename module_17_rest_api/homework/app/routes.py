from flask import Flask, request
from flask_restful import Api, Resource
from marshmallow import ValidationError

from models import (
    DATA,
    get_all_books,
    init_db,
    add_book, update_book, update_book_by_id, get_book_by_id, delete_book_by_id,
)
from schemas import BookSchema

app = Flask(__name__)
api = Api(app)


class BookList(Resource):
    def get(self) -> tuple[list[dict], int]:
        schema = BookSchema()
        return schema.dump(get_all_books(), many=True), 200

    def post(self) -> tuple[dict, int]:
        data = request.json
        schema = BookSchema()
        try:
            book = schema.load(data)
        except ValidationError as exc:
            return exc.messages, 400

        book = add_book(book)
        return schema.dump(book), 201


class BookRout(Resource):
    def put(self, id: int):
        data = request.json
        schema = BookSchema()
        try:
            book = schema.load(data)
            book.id = id
            update_book_by_id(book)
            return schema.dump(book), 200
        except ValidationError as e:
            return e.messages, 400

    def get(self, id: int):
        schema = BookSchema()
        book = get_book_by_id(id)
        return schema.dump(book), 200

    def delete(self, id: int):
        delete_book_by_id(id)
        return {'msg': "ok"}, 200


class AuthorList(Resource):
    def get(self):
        pass


api.add_resource(BookList, '/api/books')
api.add_resource(BookRout, '/api/book/<int:id>')

if __name__ == '__main__':
    init_db(initial_records=DATA)
    app.run(debug=True)
