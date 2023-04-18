from flask import Flask, Response

app = Flask(__name__)

def generate_text():
    texts = ["Hello", " ", "world!", " ", "How", " ", "are", " ", "you", "?"]
    for text in texts:
        yield text

@app.route('/stream')
def stream():
    return Response(stream_with_context(generate_text()))

app.run(debug=True)
