from flask import Flask, render_template, request, jsonify
from ai_module import generate_response

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    try:
        data = request.get_json()

        if not data:
            return jsonify({"response": "No input received"}), 400

        topic = data.get("topic")
        semesters = data.get("semesters")

        if not topic or not semesters:
            return jsonify({"response": "Please provide both topic and semesters."}), 400

        prompt = f"""
        Generate a detailed {semesters}-semester curriculum for {topic}.
        For each semester include:
        - Course names
        - Short description
        - Key topics
        """

        result = generate_response(prompt)

        return jsonify({"response": result})

    except Exception as e:
        return jsonify({"response": f"Server error: {str(e)}"}), 500


if __name__ == "__main__":
    app.run(debug=True)
