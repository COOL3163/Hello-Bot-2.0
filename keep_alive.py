from flask import Flask
from threading import Thread
from waitress import serve

app = Flask('')

@app.route('/')
def main():
  return "Hello Bot is now ready and on port 8080"

def run():
  app.run(host="0.0.0.0", port=8080)
  #serve(app, host="0.0.0.0", port=8080)

def keep_alive():
  server = Thread(target=run)
  server.start()