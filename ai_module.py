import requests

def generate_response(prompt):
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "gemma:2b",
                "prompt": prompt,
                "stream": False
            },
            timeout=120
        )

        if response.status_code == 200:
            return response.json()["response"]
        else:
            return f"Model error: {response.text}"

    except Exception as e:
        return f"Error: {str(e)}"
