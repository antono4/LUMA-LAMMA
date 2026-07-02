"""
LUMA-LAMMA - Free AI Chat Application
Flask Backend Server

Supports:
- OpenRouter API
- Groq API
- Google AI (Gemini)
- Ollama (Local/Offline)
"""

import os
import requests
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Configuration
OLLAMA_URL = os.environ.get("OLLAMA_URL", "http://localhost:11434")
PORT = int(os.environ.get("PORT", 5000))


# Default Ollama Models
DEFAULT_MODELS = [
    {"id": "llama3.2", "name": "Llama 3.2", "icon": "🦙", "provider": "Meta"},
    {"id": "llama3.3", "name": "Llama 3.3", "icon": "🦙", "provider": "Meta"},
    {"id": "mistral", "name": "Mistral 7B", "icon": "🌬️", "provider": "Mistral"},
    {"id": "phi3", "name": "Phi-3", "icon": "📘", "provider": "Microsoft"},
    {"id": "qwen2.5", "name": "Qwen 2.5", "icon": "🔮", "provider": "Alibaba"},
    {"id": "gemma2", "name": "Gemma 2", "icon": "💎", "provider": "Google"},
    {"id": "codellama", "name": "Code Llama", "icon": "💻", "provider": "Meta"},
    {"id": "deepseek-coder", "name": "DeepSeek Coder", "icon": "🔧", "provider": "DeepSeek"},
]


def get_ollama_models():
    """Get installed Ollama models"""
    try:
        response = requests.get(f"{OLLAMA_URL}/api/tags", timeout=5)
        if response.status_code == 200:
            models = response.json().get("models", [])
            installed = []
            for m in models:
                name = m["name"].split(":")[0]
                info = next((x for x in DEFAULT_MODELS if x["id"] == name), None)
                installed.append({
                    "id": name,
                    "name": info["name"] if info else name,
                    "icon": info["icon"] if info else "🤖",
                    "provider": info["provider"] if info else "Local"
                })
            return installed
    except Exception:
        pass
    return DEFAULT_MODELS


# Routes
@app.route("/")
def index():
    """Serve the frontend"""
    return send_from_directory(".", "index.html")


@app.route("/api/models", methods=["GET"])
def list_models():
    """List available models from all providers"""
    provider = request.args.get("provider", "ollama")
    
    if provider == "ollama":
        models = get_ollama_models()
        return jsonify({
            "provider": "ollama",
            "name": "Ollama (Local)",
            "models": models
        })
    
    return jsonify({"error": "Provider not supported by backend"}), 400


@app.route("/api/chat", methods=["POST"])
def chat():
    """Handle chat requests"""
    data = request.json
    provider = data.get("provider", "ollama")
    model = data.get("model", "llama3.2")
    message = data.get("message", "")
    history = data.get("history", [])
    
    if not message:
        return jsonify({"error": "Message required"}), 400
    
    # Ollama (Local)
    if provider == "ollama":
        return chat_ollama(model, message, history)
    
    return jsonify({"error": "Provider not supported by backend"}), 400


def chat_ollama(model, message, history):
    """Chat with Ollama"""
    try:
        messages = [{"role": msg.get("role", "user"), "content": msg.get("content", "")} 
                     for msg in history]
        messages.append({"role": "user", "content": message})
        
        payload = {
            "model": model,
            "messages": messages,
            "stream": False,
            "options": {
                "temperature": 0.7,
                "num_predict": 2048
            }
        }
        
        response = requests.post(
            f"{OLLAMA_URL}/api/chat",
            json=payload,
            timeout=180
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
    """Check service status"""
    try:
        response = requests.get(f"{OLLAMA_URL}/", timeout=3)
        ollama_online = response.status_code == 200
    except:
        ollama_online = False
    
    return jsonify({
        "status": "ok",
        "providers": {
            "ollama": {
                "online": ollama_online,
                "url": OLLAMA_URL
            }
        }
    })


@app.route("/api/health", methods=["GET"])
def health():
    """Health check"""
    return jsonify({
        "status": "ok",
        "app": "LUMA-LAMMA",
        "version": "2.0",
        "info": "Free AI Chat - No API Key Required for Ollama!"
    })


if __name__ == "__main__":
    print("🦙 LUMA-LAMMA - Free AI Chat Server")
    print("=" * 40)
    print(f"\n📡 Ollama: {OLLAMA_URL}")
    print("\n⚡ Local Models (Ollama):")
    for m in DEFAULT_MODELS:
        print(f"   • {m['icon']} {m['name']}")
    print(f"\n🌐 Starting on http://localhost:{PORT}")
    print("\n💡 Install more models: ollama pull <model>")
    print("   Examples: ollama pull llama3.2, ollama pull codellama")
    app.run(host="0.0.0.0", port=PORT, debug=False)
