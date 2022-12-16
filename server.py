import flask, os
from flask_cors import CORS
from helper import *


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
  result = get_profile(user)
  problems = get_problems(user)['matchedUser']
  profile = result['profile']
  result |= profile
  
  del result['profile']
  
  print(problems)
  
  for beats in problems['problemsSolvedBeatsStats']:
    result[beats['difficulty'].lower() + 'Beats'] = beats['percentage']
    
  for solved in problems['submitStatsGlobal']['acSubmissionNum']:
    result[solved['difficulty'].lower() + 'Solved'] = solved['count']
  
  return result, 200

if __name__ == '__main__':
  port = int(os.environ.get('PORT', 5050))
  app.run(debug=False, host='0.0.0.0', port=port)