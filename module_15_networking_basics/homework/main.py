import wtforms_json
from flask import Flask
from flask import request, Response
from flask import jsonify
from wtforms import Form, IntegerField
from wtforms.validators import InputRequired


from module_15_networking_basics.homework.models import init_db, Room, add_room_to_db, get_rooms

app: Flask = Flask(__name__)
wtforms_json.init()


class RoomForm(Form):
    floor = IntegerField(validators=[InputRequired()])
    beds = IntegerField(validators=[InputRequired()])
    guestNum = IntegerField(validators=[InputRequired()])
    price = IntegerField(validators=[InputRequired()])


@app.route('/add-room', methods=['POST'])
def add_room() -> Response:
    if request.method == "POST":
        data = request.get_json()
        room = Room(
            floor=data["floor"],
            beds=data["beds"],
            guestNum=data["guestNum"],
            price=data["price"]
        )
        add_room_to_db(room)
        return Response(status=200)

@app.route('/room', methods=['GET'])
def get_room() -> Response:
    rooms = get_rooms()
    properties: dict = {}
    properties["rooms"] = []
    for room in rooms:
        properties["rooms"].append({
            "id": room.id,
            "floor": room.floor,
            "beds": room.beds,
            "questNum": room.guestNum,
            "price": room.price
        })
    return jsonify(properties)


if __name__ == '__main__':
    init_db()
    app.config["WTF_CSRF_ENABLED"] = False
    app.run(debug=True, port=5000, host="127.0.0.1")
