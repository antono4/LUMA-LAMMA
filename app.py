"""
Free LLM AI Agent - Flask Backend
Supports: Ollama (Local), Groq, OpenRouter (Cloud APIs - Free Tiers)
"""

import os
import requests
from flask import Flask, request, jsonify, send_file
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

OLLAMA_URL = "http://localhost:11434"
GROQ_API_KEY = os.environ.get("GROQ_API_KEY", "")
OPENROUTER_API_KEY = os.environ.get("OPENROUTER_API_KEY", "")


# Default providers (used when API keys are not set)
DEFAULT_PROVIDERS = {
    "ollama": {
        "name": "Ollama (Local)",
        "models": [
            {"id": "mistral", "name": "Mistral 7B", "free": True, "icon": "🌬️"},
            {"id": "llama3", "name": "Llama 3", "free": True, "icon": "🦙"},
            {"id": "llama3.2", "name": "Llama 3.2", "free": True, "icon": "🦙"},
            {"id": "phi3", "name": "Phi-3", "free": True, "icon": "📘"},
            {"id": "qwen2.5", "name": "Qwen 2.5", "free": True, "icon": "🔮"},
            {"id": "gemma2", "name": "Gemma 2", "free": True, "icon": "💎"},
            {"id": "codellama", "name": "Code Llama", "free": True, "icon": "💻"},
            {"id": "deepseek-coder", "name": "DeepSeek Coder", "free": True, "icon": "🔧"},
        ]
    },
    "groq": {
        "name": "Groq (Cloud)",
        "description": "Free tier - 30 RPM, Ultra-fast",
        "models": [
            {"id": "llama-3.3-70b-versatile", "name": "Llama 3.3 70B", "free": True, "icon": "🦙"},
            {"id": "llama-3.1-8b-instant", "name": "Llama 3.1 8B", "free": True, "icon": "🦙"},
            {"id": "qwen-3-32b", "name": "Qwen 3 32B", "free": True, "icon": "🔮"},
        ]
    },
    "openrouter": {
        "name": "OpenRouter (Cloud)",
        "description": "Free models available",
        "models": [
            {"id": "meta-llama/llama-3.3-70b-instruct:free", "name": "Llama 3.3 70B (Free)", "free": True, "icon": "🦙"},
            {"id": "qwen/qwen3-coder:free", "name": "Qwen Coder (Free)", "free": True, "icon": "💻"},
            {"id": "google/gemma-4-31b-it:free", "name": "Gemma 4 31B (Free)", "free": True, "icon": "💎"},
        ]
    }
}

PROVIDERS = DEFAULT_PROVIDERS.copy()

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
    except requests.exceptions.ConnectionError:
        return jsonify({"error": "Ollama is not running"}), 503
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/providers", methods=["GET"])
def get_providers():
    """Get all available providers and their installed models"""
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
    
    # Return all default providers if Ollama is not available
    return jsonify(DEFAULT_PROVIDERS)


@app.route("/api/chat", methods=["POST"])
def chat():
    """Send a chat message to LLM provider (Ollama, Groq, or OpenRouter)"""
    data = request.json
    
    model = data.get("model", "mistral")
    message = data.get("message")
    history = data.get("history", [])
    provider = data.get("provider", "ollama")
    
    if not message:
        return jsonify({"error": "Message required"}), 400
    
    try:
        # Build messages array
        messages = []
        for msg in history:
            role = msg.get("role", "user")
            content = msg.get("content", "")
            messages.append({"role": role, "content": content})
        messages.append({"role": "user", "content": message})
        
        # Route to appropriate provider
        if provider == "groq" or model.startswith("llama-") or model.startswith("qwen-"):
            return chat_groq(model, messages)
        elif provider == "openrouter" or ":" in model:
            return chat_openrouter(model, messages)
        else:
            return chat_ollama(model, messages)
            
    except requests.exceptions.Timeout:
        return jsonify({"error": "Request timeout, try a smaller model"}), 504
    except requests.exceptions.ConnectionError:
        return jsonify({"error": "Connection failed. Please check your internet or Ollama."}), 503
    except Exception as e:
        return jsonify({"error": str(e)}), 500


def chat_ollama(model, messages):
    """Send chat to Ollama (local)"""
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


def chat_groq(model, messages):
    """Send chat to Groq API (free tier)"""
    if not GROQ_API_KEY:
        return jsonify({"error": "GROQ_API_KEY not set. Please set environment variable."}), 401
    
    payload = {
        "model": model,
        "messages": messages,
        "temperature": 0.7,
        "max_tokens": 512
    }
    
    response = requests.post(
        "https://api.groq.com/openai/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json"
        },
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


def chat_openrouter(model, messages):
    """Send chat to OpenRouter API (free models)"""
    if not OPENROUTER_API_KEY:
        return jsonify({"error": "OPENROUTER_API_KEY not set. Please set environment variable."}), 401
    
    payload = {
        "model": model,
        "messages": messages,
        "temperature": 0.7,
        "max_tokens": 512
    }
    
    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json"
        },
        json=payload,
        timeout=60
    )
    
    if response.status_code != 200:
        return jsonify({"error": f"OpenRouter API error: {response.text}"}), response.status_code
    
    result = response.json()
    response_text = result.get("choices", [{}])[0].get("message", {}).get("content", "No response")
    
    return jsonify({
        "response": response_text.strip(),
        "provider": "openrouter",
        "model": model
    })


@app.route("/api/status", methods=["GET"])
def status():
    """Check all LLM provider statuses"""
    ollama_online = False
    try:
        response = requests.get(f"{OLLAMA_URL}/", timeout=5)
        ollama_online = response.status_code == 200
    except:
        pass
    
    return jsonify({
        "ollama": ollama_online,
        "groq": bool(GROQ_API_KEY),
        "openrouter": bool(OPENROUTER_API_KEY),
        "ollama_url": OLLAMA_URL
    })


@app.route("/api/health", methods=["GET"])
def health():
    """Health check"""
    total_models = sum(len(p.get("models", [])) for p in PROVIDERS.values())
    return jsonify({
        "status": "ok",
        "providers": list(PROVIDERS.keys()),
        "total_models": total_models,
        "info": "100% Free AI Chat - Local & Cloud Options"
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
