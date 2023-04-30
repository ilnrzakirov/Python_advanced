
from flask import Flask
from flask import request, Response
from flask import jsonify

from module_15_networking_basics.homework.models import init_db, Room, add_room_to_db, get_rooms

app: Flask = Flask(__name__)



@app.route('/add-room', methods=['POST'])
def add_room() -> Response:
    if request.method == "POST":
        data = request.get_json()
        room = Room(
            id=None,
            floor=data["floor"],
            beds=data["beds"],
            guestNum=data["guestNum"],
            price=data["price"]
        )
        add_room_to_db(room)
        return Response(status=200)


@app.route('/room', methods=['GET'])
def get_room() -> Response:
    if request.args.get('checkIn') and request.args.get('checkOut'):
        rooms = get_rooms(request.args.get('checkIn'), request.args.get('checkOut'))
    else:
        rooms = get_rooms()
    properties: dict = {}
    properties["rooms"] = []
    for room in rooms:
        properties["rooms"].append({
            "roomId": room.id,
            "floor": room.floor,
            "beds": room.beds,
            "questNum": room.guestNum,
            "price": room.price
        })
    print(properties)
    return jsonify(properties)


@app.route('/room/<checkIn>/<checkOut>/<int:guestsNum>', methods=['GET'])
def get_room_for_date(checkIn: str, checkOut: str, guestNum: int):
    print(checkIn)
    print(checkOut)
    print(guestNum)


if __name__ == '__main__':
    init_db()
    app.config["WTF_CSRF_ENABLED"] = False
    app.run(debug=True, port=5000, host="127.0.0.1")
