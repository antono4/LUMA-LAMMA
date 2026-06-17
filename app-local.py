"""
Free LLM AI Agent - Flask Backend
Supports: Ollama (100% Local, Free, Private)
"""

import requests
from flask import Flask, request, jsonify, send_file
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

OLLAMA_URL = "http://localhost:11434"


# Default models (shown when Ollama is offline or running)
DEFAULT_MODELS = [
    {"id": "mistral", "name": "Mistral 7B", "free": True, "icon": "🌬️"},
    {"id": "llama3", "name": "Llama 3", "free": True, "icon": "🦙"},
    {"id": "llama3.2", "name": "Llama 3.2", "free": True, "icon": "🦙"},
    {"id": "phi3", "name": "Phi-3", "free": True, "icon": "📘"},
    {"id": "qwen2.5", "name": "Qwen 2.5", "free": True, "icon": "🔮"},
    {"id": "gemma2", "name": "Gemma 2", "free": True, "icon": "💎"},
    {"id": "codellama", "name": "Code Llama", "free": True, "icon": "💻"},
    {"id": "deepseek-coder", "name": "DeepSeek Coder", "free": True, "icon": "🔧"},
]

# Providers
PROVIDERS = {
    "ollama": {
        "name": "Ollama (Local)",
        "models": DEFAULT_MODELS
    }
}

# Model info for reference
ALL_MODELS = {
    "mistral": {"name": "Mistral 7B", "icon": "🌬️"},
    "llama3": {"name": "Llama 3", "icon": "🦙"},
    "llama3.2": {"name": "Llama 3.2", "icon": "🦙"},
    "phi3": {"name": "Phi-3", "icon": "📘"},
    "qwen2.5": {"name": "Qwen 2.5", "icon": "🔮"},
    "gemma2": {"name": "Gemma 2", "icon": "💎"},
    "codellama": {"name": "Code Llama", "icon": "💻"},
    "deepseek-coder": {"name": "DeepSeek Coder", "icon": "🔧"},
}


@app.route("/")
def index():
    """Serve the frontend HTML"""
    return send_file("index.html")


@app.route("/api/models", methods=["GET"])
def get_available_models():
    """Get list of installed Ollama models"""
    try:
        response = requests.get(f"{OLLAMA_URL}/api/tags", timeout=5)
        if response.status_code == 200:
            models = response.json().get("models", [])
            installed = []
            for m in models:
                name = m["name"].split(":")[0]  # Remove tag if present
                info = ALL_MODELS.get(name, {"name": name, "icon": "🤖"})
                installed.append({
                    "id": name,
                    "name": info.get("name", name),
                    "icon": info.get("icon", "🤖"),
                    "free": True
                })
            return jsonify({"models": installed})
        return jsonify({"error": "Ollama not responding"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/providers", methods=["GET"])
def get_providers():
    """Get all available providers and their models"""
    try:
        response = requests.get(f"{OLLAMA_URL}/api/tags", timeout=5)
        if response.status_code == 200:
            models = response.json().get("models", [])
            installed_models = []
            for m in models:
                name = m["name"].split(":")[0]
                info = ALL_MODELS.get(name, {"name": name, "icon": "🤖"})
                installed_models.append({
                    "id": name,
                    "name": info.get("name", name),
                    "icon": info.get("icon", "🤖"),
                    "free": True
                })
            
            if installed_models:
                return jsonify({
                    "ollama": {
                        "name": "Ollama (Local)",
                        "models": installed_models
                    }
                })
    except requests.exceptions.RequestException:
        pass
    
    # Always return default models (user can still see UI even if Ollama is offline)
    return jsonify({
        "ollama": {
            "name": "Ollama (Local)",
            "models": DEFAULT_MODELS
        }
    })


@app.route("/api/chat", methods=["POST"])
def chat():
    """Send a chat message to Ollama"""
    data = request.json
    
    model = data.get("model", "mistral")
    message = data.get("message")
    history = data.get("history", [])
    
    if not message:
        return jsonify({"error": "Message required"}), 400
    
    try:
        # Build messages array for Ollama chat API
        messages = []
        
        # Add history
        for msg in history:
            role = msg.get("role", "user")
            content = msg.get("content", "")
            messages.append({"role": role, "content": content})
        
        # Add current message
        messages.append({"role": "user", "content": message})
        
        # Call Ollama API
        payload = {
            "model": model,
            "messages": messages,
            "stream": False,
            "options": {
                "temperature": 0.7,
                "num_predict": 512
            }
        }
        
        response = requests.post(
            f"{OLLAMA_URL}/api/chat",
            json=payload,
            timeout=120
        )
        
        if response.status_code != 200:
            return jsonify({"error": f"Ollama error: {response.text}"}), 500
        
        result = response.json()
        response_text = result.get("message", {}).get("content", "No response")
        
        return jsonify({
            "response": response_text.strip(),
            "provider": "ollama",
            "model": model
        })
        
    except requests.exceptions.Timeout:
        return jsonify({"error": "Request timeout, try a smaller model"}), 504
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/status", methods=["GET"])
def status():
    """Check Ollama status"""
    try:
        response = requests.get(f"{OLLAMA_URL}/", timeout=5)
        return jsonify({
            "ollama": response.status_code == 200,
            "url": OLLAMA_URL
        })
    except:
        return jsonify({"ollama": False})


@app.route("/api/health", methods=["GET"])
def health():
    """Health check"""
    return jsonify({
        "status": "ok",
        "provider": "Ollama (Local)",
        "models": len(PROVIDERS["ollama"]["models"]),
        "info": "100% Free, Private, No API Key Needed!"
    })


if __name__ == "__main__":
    print("🚀 Starting Free LLM AI Agent (Ollama - Local)!")
    print("\n📋 Features:")
    print("   • 100% Local - No internet required")
    print("   • 100% Private - Data never leaves your machine")
    print("   • 100% Free - No API keys, no credits")
    print(f"\n📡 Ollama API: {OLLAMA_URL}")
    print("\n⚡ Available Models:")
    for m in PROVIDERS["ollama"]["models"]:
        print(f"   • {m['name']}")
    print("\n🌐 Starting server on http://localhost:5000")
    print("\n💡 To install more models: ollama pull <model-name>")
    print("   Examples: ollama pull llama3, ollama pull codellama")
    app.run(host="0.0.0.0", port=5000, debug=False, use_reloader=False)
