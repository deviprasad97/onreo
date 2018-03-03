from flask import Flask, request, session, redirect, url_for, escape, jsonify

app = Flask(__name__)
api = Api(app)
app.secret_key = 'DBFHWIV9238Rhvhfdwi2939r8109201dbiqhiu'

class User_login(Resource):
    def post(self):
        return "Hello"
    def get(self):
	return "hello"

api.add_resource(User_login, '/')
app.run(host='0.0.0.0')

