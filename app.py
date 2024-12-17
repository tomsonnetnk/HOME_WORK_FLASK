from flask import Flask, jsonify, request

app = Flask(__name__)

# Список пользователей и постов

users = {}

posts = {}

post_id_counter = 1

# Создание пользователя

@app.route('/users', methods=['POST'])

def create_user():

    user_id = len(users) + 1

    users[user_id] = request.json

    return jsonify({'id': user_id}), 201

# Создание поста

@app.route('/posts', methods=['POST'])

def create_post():

    global post_id_counter

    post = request.json

    post['id'] = post_id_counter

    posts[post_id_counter] = post

    post_id_counter += 1

    return jsonify(post), 201

# Получение поста

@app.route('/posts/<int:post_id>', methods=['GET'])

def get_post(post_id):

    return jsonify(posts.get(post_id)), 200

# Изменение поста

@app.route('/posts/<int:post_id>', methods=['PUT'])

def update_post(post_id):

    posts[post_id] = request.json

    return jsonify(posts[post_id]), 200

# Удаление поста

@app.route('/posts/<int:post_id>', methods=['DELETE'])

def delete_post(post_id):

    posts.pop(post_id, None)

    return '', 204

if __name__ == '__main__':

    app.run(debug=True)

