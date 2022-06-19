from flask import Flask
import sys
from housing.logger import logging
from housing.exception import HousingException

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    try:
        raise Exception("We are testing customs exception")
    except Exception as e:
        # pass
        housing = HousingException(e, sys)
        logging.info(housing.error_message)
        logging.info("We are testing logging module")
    return "Starting ML Project 123334" 


if __name__ == "__main__":
    app.run(debug=True)
    #app.run(host='0.0.0.0', port=8080)