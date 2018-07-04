from flask import Flask, render_template, redirect, request

app = Flask(__name__)

counts = [{'GET':0},{'POST':0},{'PUT':0},{'DELETE':0}]


@app.route('/')
def open_front_page():
    global counts
    return render_template('list.html', counts = counts)

@app.route('/request-counter', methods=['POST', 'GET', 'PUT', 'DELETE'])
def count_request():
    global counts
    if request.method == 'GET':
        counts[0]['GET'] += 1
    if request.method == 'POST':
        counts[1]['POST'] += 1
    if request.method == 'PUT':
        counts[2]['PUT'] += 1
    if request.method == 'DELETE':
        counts[3]['DELETE'] += 1
    return redirect('/')


if __name__ == '__main__':
    app.run(
        debug=True,
        port=5000
    )