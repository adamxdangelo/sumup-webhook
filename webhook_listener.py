import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return 'SumUp webhook endpoint is live.'

@app.route('/sumup-webhook', methods=['POST'])
def sumup_webhook():
    data = request.json
    print("Received webhook:", data)
    return '', 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
