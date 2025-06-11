import os
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MCP_SERVER_URL = os.getenv("MCP_SERVER_URL")
MCP_AUTH_HEADER = os.getenv("MCP_AUTH_HEADER")

@app.route("/query", methods=["POST"])
def query():
    user_input = request.json.get("input", "")

    payload = {
        "model": "gpt-4.1-mini",
        "input": user_input,
        "tools": [
            {
                "type": "mcp",
                "server_label": "zapier",
                "server_url": f"{MCP_SERVER_URL}",
                "require_approval": "never",
                "headers": {
                    "Authorization": f"Bearer {MCP_AUTH_HEADER}"
                }
            }
        ],
        "tool_choice": "required"
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {OPENAI_API_KEY}"
    }

    try:
        response = requests.post(
            "https://api.openai.com/v1/responses",
            json=payload,
            headers=headers
        )
        
        response_data = response.json()
        
        if "output" in response_data and len(response_data["output"]) > 0:
            for item in reversed(response_data["output"]):
                if item.get("type") == "message" and "content" in item:
                    for content_item in item["content"]:
                        if content_item.get("type") == "output_text":
                            return jsonify({"message": content_item["text"]})
        return jsonify({"message": "No message found in response"})
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
