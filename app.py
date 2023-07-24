# """Flask app for Cupcakes"""
# from flask import Flask, request, jsonify, render_template

# from models import db, connect_db, Cupcake

# app = Flask(__name__)
# app.app_context().push()

# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SECRET_KEY'] = "cupcakesaregood"

# connect_db(app)

# @app.route("/")
# def root():
#     """Render homepage."""

#     return render_template("index.html")

# # Route for getting data about all cupcakes
# @app.route('/api/cupcakes', methods=['GET'])
# def get_all_cupcakes():
#     cupcakes = Cupcake.query.all()
#     serialized_cupcakes = [cupcake.to_dict() for cupcake in cupcakes]
#     return jsonify(cupcakes=serialized_cupcakes)

# # Route for getting data about a single cupcake
# @app.route('/api/cupcakes/<int:cupcake_id>', methods=['GET'])
# def get_cupcake(cupcake_id):
#     cupcake = Cupcake.query.get_or_404(cupcake_id)
#     serialized_cupcake = cupcake.to_dict()
#     return jsonify(cupcake=serialized_cupcake)

# # Route for creating a new cupcake
# @app.route('/api/cupcakes', methods=['POST'])
# def create_cupcake():

#     data = request.json

#     flavor = data['flavor']
#     size = data['size']
#     rating = data['rating']
#     image = data.get('image', 'https://tinyurl.com/demo-cupcake')

#     cupcake = Cupcake(flavor=flavor, size=size, rating=rating, image=image)
#     db.session.add(cupcake)
#     db.session.commit()

#     serialized_cupcake = cupcake.to_dict()
#     return jsonify(cupcake=serialized_cupcake), 201  # 201 status code for resource created


# # Route for updating a cupcake
# @app.route('/api/cupcakes/<int:cupcake_id>', methods=['PATCH'])
# def update_cupcake(cupcake_id):
#     cupcake = Cupcake.query.get_or_404(cupcake_id)
    
#     data = request.json
#     cupcake.flavor = data['flavor']
#     cupcake.size = data['size']
#     cupcake.rating = data['rating']
#     cupcake.image = data.get('image', 'https://tinyurl.com/demo-cupcake')

#     db.session.commit()

#     return jsonify(cupcake=cupcake.to_dict())

# # Route for deleting a cupcake
# @app.route('/api/cupcakes/<int:cupcake_id>', methods=['DELETE'])
# def delete_cupcake(cupcake_id):
#     cupcake = Cupcake.query.get_or_404(cupcake_id)

#     db.session.delete(cupcake)
#     db.session.commit()

#     return jsonify(message='Deleted')

# # Run the Flask app
# if __name__ == '__main__':
#     app.run(debug=True, static_url_path='/static')


"""Flask app for Cupcakes"""

from flask import Flask, request, jsonify, render_template

from models import db, connect_db, Cupcake

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "oh-so-secret"

connect_db(app)


@app.route("/")
def root():
    """Render homepage."""

    return render_template("index.html")


@app.route("/api/cupcakes")
def list_cupcakes():
    """Return all cupcakes in system.

    Returns JSON like:
        {cupcakes: [{id, flavor, rating, size, image}, ...]}
    """

    cupcakes = [cupcake.to_dict() for cupcake in Cupcake.query.all()]
    return jsonify(cupcakes=cupcakes)


@app.route("/api/cupcakes", methods=["POST"])
def create_cupcake():
    """Add cupcake, and return data about new cupcake.

    Returns JSON like:
        {cupcake: [{id, flavor, rating, size, image}]}
    """

    data = request.json

    cupcake = Cupcake(
        flavor=data['flavor'],
        rating=data['rating'],
        size=data['size'],
        image=data['image'] or None)

    db.session.add(cupcake)
    db.session.commit()

    # POST requests should return HTTP status of 201 CREATED
    return (jsonify(cupcake=cupcake.to_dict()), 201)


@app.route("/api/cupcakes/<int:cupcake_id>")
def get_cupcake(cupcake_id):
    """Return data on specific cupcake.

    Returns JSON like:
        {cupcake: [{id, flavor, rating, size, image}]}
    """

    cupcake = Cupcake.query.get_or_404(cupcake_id)
    return jsonify(cupcake=cupcake.to_dict())


@app.route("/api/cupcakes/<int:cupcake_id>", methods=["PATCH"])
def update_cupcake(cupcake_id):
    """Update cupcake from data in request. Return updated data.

    Returns JSON like:
        {cupcake: [{id, flavor, rating, size, image}]}
    """

    data = request.json

    cupcake = Cupcake.query.get_or_404(cupcake_id)

    cupcake.flavor = data['flavor']
    cupcake.rating = data['rating']
    cupcake.size = data['size']
    cupcake.image = data['image']

    db.session.add(cupcake)
    db.session.commit()

    return jsonify(cupcake=cupcake.to_dict())


@app.route("/api/cupcakes/<int:cupcake_id>", methods=["DELETE"])
def remove_cupcake(cupcake_id):
    """Delete cupcake and return confirmation message.

    Returns JSON of {message: "Deleted"}
    """

    cupcake = Cupcake.query.get_or_404(cupcake_id)

    db.session.delete(cupcake)
    db.session.commit()

    return jsonify(message="Deleted")


