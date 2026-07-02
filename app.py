"""
LUMA-LAMMA - Free AI Chat Application
Flask Backend Server

Supports:
- Groq API (Free tier)
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
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

# Models
GROQ_MODELS = [
    {"id": "llama-3.3-70b-versatile", "name": "Llama 3.3 70B", "icon": "🦙", "provider": "Meta"},
    {"id": "llama-3.1-8b-instant", "name": "Llama 3.1 8B", "icon": "🦙", "provider": "Meta"},
    {"id": "mixtral-8x7b-32768", "name": "Mixtral 8x7B", "icon": "🌀", "provider": "Mistral"},
    {"id": "gemma2-9b-it", "name": "Gemma 2 9B", "icon": "💎", "provider": "Google"},
]

OLLAMA_MODELS = [
    {"id": "llama3.2", "name": "Llama 3.2", "icon": "🦙", "provider": "Meta"},
    {"id": "llama3", "name": "Llama 3", "icon": "🦙", "provider": "Meta"},
    {"id": "mistral", "name": "Mistral 7B", "icon": "🌬️", "provider": "Mistral"},
    {"id": "phi3", "name": "Phi-3", "icon": "📘", "provider": "Microsoft"},
    {"id": "qwen2.5", "name": "Qwen 2.5", "icon": "🔮", "provider": "Alibaba"},
    {"id": "gemma2", "name": "Gemma 2", "icon": "💎", "provider": "Google"},
    {"id": "codellama", "name": "Code Llama", "icon": "💻", "provider": "Meta"},
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
                info = next((x for x in OLLAMA_MODELS if x["id"] == name), None)
                installed.append({
                    "id": name,
                    "name": info["name"] if info else name,
                    "icon": info["icon"] if info else "🤖",
                    "provider": info["provider"] if info else "Local"
                })
            return installed
    except Exception:
        pass
    return OLLAMA_MODELS


@app.route("/")
def index():
    """Serve the frontend"""
    return send_from_directory(".", "index.html")


@app.route("/api/providers", methods=["GET"])
def list_providers():
    """List all available providers"""
    return jsonify({
        "groq": {
            "name": "Groq (Free)",
            "models": GROQ_MODELS
        },
        "ollama": {
            "name": "Ollama (Local)",
            "models": get_ollama_models()
        }
    })


@app.route("/api/chat", methods=["POST"])
def chat():
    """Handle chat requests"""
    data = request.json
    provider = data.get("provider", "groq")
    model = data.get("model")
    message = data.get("message", "")
    history = data.get("history", [])
    api_key = data.get("apiKey") or data.get("api_key")  # Accept both formats
    
    if not message:
        return jsonify({"error": "Message required"}), 400
    
    if provider == "groq":
        return chat_groq(model, message, history, api_key)
    elif provider == "ollama":
        return chat_ollama(model, message, history)
    
    return jsonify({"error": "Unknown provider"}), 400


def chat_groq(model, message, history, api_key=None):
    """Chat with Groq API"""
    if not api_key:
        return jsonify({"error": "API key required for Groq"}), 400
    
    try:
        messages = [{"role": msg.get("role", "user"), "content": msg.get("content", "")} 
                     for msg in history]
        messages.append({"role": "user", "content": message})
        
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "model": model or "llama-3.3-70b-versatile",
            "messages": messages
        }
        
        response = requests.post(
            GROQ_API_URL,
            headers=headers,
            json=payload,
            timeout=60
        )
        
        if response.status_code != 200:
            return jsonify({"error": f"Groq API error: {response.text}"}), response.status_code
        
        result = response.json()
        response_text = result.get("choices", [{}])[0].get("message", {}).get("content", "No response")
        
        return jsonify({
            "response": response_text.strip(),
            "provider": "groq",
            "model": model
        })
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500


def chat_ollama(model, message, history):
    """Chat with Ollama"""
    try:
        messages = [{"role": msg.get("role", "user"), "content": msg.get("content", "")} 
                     for msg in history]
        messages.append({"role": "user", "content": message})
        
        payload = {
            "model": model or "llama3.2",
            "messages": messages,
            "stream": False
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
        return jsonify({"error": "Request timeout"}), 504
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/health", methods=["GET"])
def health():
    """Health check"""
    return jsonify({
        "status": "ok",
        "app": "LUMA-LAMMA",
        "version": "3.0",
        "info": "Free AI Chat - Using Groq API!"
    })


if __name__ == "__main__":
    print("🦙 LUMA-LAMMA - Free AI Chat Server")
    print("=" * 40)
    print("\n📡 Providers:")
    print("   • Groq (Free API)")
    print(f"   • Ollama: {OLLAMA_URL}")
    print("\n⚡ Groq Models:")
    for m in GROQ_MODELS:
        print(f"   • {m['icon']} {m['name']}")
    print(f"\n🌐 Starting on http://localhost:{PORT}")
    print("\n💡 Ollama: ollama serve (for local models)")
    app.run(host="0.0.0.0", port=PORT, debug=False)
