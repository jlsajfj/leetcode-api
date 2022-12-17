import flask, os
from flask_cors import CORS
from helper import get_all_user, get_all_problems


app = flask.Flask(__name__)
CORS(app)

@app.route('/health-check', methods=['GET'])
def health_check():
  return 'alive', 200

@app.route('/usage', methods=['POST'])
def post_usage():
  return flask.send_file('api.yaml')

@app.route('/user', methods=['POST'])
def post_user():
  f_body = flask.request.json
  
  if 'username' not in f_body:
    return 'username missing in request', 400
  
  user = f_body['username']
  
  return get_all_user(user), 200

@app.route('/user', methods=['GET'])
def get_user():
  f_args = flask.request.args
  
  if 'username' not in f_args:
    return 'username missing in request', 400
  
  user = f_args['username']
  
  return get_all_user(user), 200

if __name__ == '__main__':
  port = int(os.environ.get('PORT', 5050))
  app.run(debug=False, host='0.0.0.0', port=port)
