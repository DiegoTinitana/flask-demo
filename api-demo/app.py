from flask import Flask, jsonify
from flask import request

app = Flask(__name__)

movies_list = [
    {
        "name": "The Shawshank Redemption",
        "casts": ["Tim Robbins", "Morgan Freeman", "Bob Gunton", "William Sadler"],
        "genres": ["Drama"]
    },
    {
       "name": "The Godfather ",
       "casts": ["Marlon Brando", "Al Pacino", "James Caan", "Diane Keaton"],
       "genres": ["Crime", "Drama"]
    }
]


@app.route('/')
@app.route('/movies')
def movies():
    return jsonify(movies_list), 200


@app.route('/movies', methods=['POST'])
def add_movie():
    movie = request.get_json()
    movies_list.append(movie)
    return {'id': len(movies_list)}, 201


@app.route('/movies/<int:index>', methods=['PUT'])
def update_movie(index):
    movie = request.get_json()
    movies_list[index] = movie
    return jsonify(movies_list[index]), 200


@app.route('/movies/<int:index>', methods=['DELETE'])
def delete_movie(index):
    movies_list.pop(index)
    return jsonify(movies_list), 204


if __name__ == '__main__':
    app.run()
