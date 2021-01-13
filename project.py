from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World"

contacts = [
    {
        'id' : 1,
        'name' : 'Aakash',
        'contact' : '1234567890',
        'done' : False
    },
    {
        'id' : 2,
        'name' : 'Rahul',
        'contact' : '0987654321',
        'done' : False
    }
]

@app.route('/add_data', methods = ['POST'])
def add_task():
    if not request.json:
        return jsonify({
            'status' : 'error',
            'message' : 'please provide data'
        }, 400)

    task = {
        'id' : contacts[-1]['id'] + 1,
        'name' : request.json['name'],
        'contact' : request.json.get('contact', ''),
        'done' : False
    }

    contacts.append(task)
    return jsonify({
        'status' : 'success',
        'message' : 'task added successfully'
    })

@app.route('/get_data')
def get_task():
    return jsonify({
        'data' : contacts
    })

if (__name__ == '__main__'):
    app.run(debug = True)