#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route("/", methods = ['GET'])

def home():
  return("Hello flask!!!")

if __name__ == "__main__":
  app.run(port = 7000, debug=True)
