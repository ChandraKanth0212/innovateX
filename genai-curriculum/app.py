from flask import Flask, render_template, request, jsonify
from ai_module import generate_response

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json()
    topic = data.get("topic")
    semesters = data.get("semesters")

    prompt = f"Generate a detailed {semesters}-semester curriculum for {topic}. Include subjects and topics for each semester."

    result = generate_response(prompt)

    return jsonify({"response": result})

if __name__ == "__main__":
    app.run(debug=True)
