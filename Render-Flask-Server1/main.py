from flask import Flask
import os

app = Flask(__name__)

@app.route("/ping")
def ping():
    return "✅ I'm alive!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Use Render's PORT env var, else 10000 locally
    app.run(host="0.0.0.0", port=port)
