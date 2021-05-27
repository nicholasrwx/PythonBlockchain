from flask import Flask
from flask_cors import CORS
from wallet import Wallet

#set up our flask server, and give it the name of the file being executed
app = Flask(__name__)
#create a wallet Instance
wallet = Wallet()
#calls the constructor of the CORS class, and pass in the server code we created -> app
#this allows for multiple nodes aside from the host server to send and receive requests also.
CORS(app)

#default end-point get route
@app.route('/', methods=['GET'])
def get_ui():
  return 'This works'


#launch the server only if i'm directly running this file
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)


