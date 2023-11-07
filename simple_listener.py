from flask import Flask, request
import os
import logging


dirname = f'{os.path.dirname(os.path.abspath(__file__))}'
app = Flask(__name__)

# Configure the logger
logging.basicConfig(filename=os.path.join(
    dirname, 'Log.txt'), level=logging.INFO)


@app.route('/echo', methods=['POST'])
def simple_echo():  # Will straight up just print want it receives as testing
    try:
        content = request.json
        print(content)
        return 'OK'
    except Exception as e:
        print(e)
        return f'Error: {str(e)}', 500


@app.route('/log', methods=['POST'])
def logging():  # Will log everything it receives and any errors
    try:
        data = request.json
        logging.info(data)
        return 'OK'
    except Exception as e:
        logging.error(f'Error: {str(e)}')
        return f'Error: {str(e)}', 500


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=1111)
