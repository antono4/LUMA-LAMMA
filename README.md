# 🦙 LUMA-LAMMA

**Free AI Chat** - Chat dengan berbagai model LLM gratis langsung dari browser!

![LUMA-LAMMA](https://img.shields.io/badge/Status-Active-success?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-blue?style=flat-square)
![Platform](https://img.shields.io/badge/Platform-Web-orange?style=flat-square)

## ✨ Fitur

| Fitur | Keterangan |
|-------|------------|
| 🌐 **Online** | Tidak perlu install software, buka langsung di browser |
| 💰 **100% Free** | Multiple provider gratis (OpenRouter, Groq, Google AI) |
| 🎨 **UI Modern** | Interface web yang clean, responsif & mudah digunakan |
| ⚡ **Cepat** | Response time yang cepat dengan streaming support |
| 🧠 **Multi Model** | Pilihan berbagai model LLM populer |

## 🚀 Quick Start

### Jalankan Lokal (Single File)

```bash
# Download file
curl -O https://raw.githubusercontent.com/antono4/LUMA-LAMMA/main/index.html

# Buka langsung di browser
open index.html
```

### Jalankan dengan Backend (Ollama Support)

```bash
# Install dependencies
pip install -r requirements.txt

# Jalankan server
python app.py

# Buka browser
open http://localhost:5000
```

## 🤖 Model yang Tersedia

### OpenRouter (20 req/min, Free Tier)

| Model | Provider | Keterangan |
|-------|----------|------------|
| 🎲 Auto | Auto-select | Pilih model terbaik otomatis |
| 🧠 Claude 3.5 Haiku | Anthropic | Fast reasoning |
| ⚡ Nemotron 70B | NVIDIA | High performance |
| 💎 Gemma 4 27B | Google | Google's latest |
| 🔵 DeepSeek V4 | DeepSeek | Chinese LLM |
| 🏊 Poolside 70B | Poolside | Open source |
| 🦙 Llama 3 8B | Meta | Facebook's LLM |

### Groq (Fast Inference)

| Model | Provider | Keterangan |
|-------|----------|------------|
| 🦙 Llama 3.3 70B | Meta | Versatile |
| 🦙 Llama 3.1 8B | Meta | Fast & small |
| 🌀 Mixtral 8x7B | Mistral | Mixture of experts |
| 💎 Gemma 2 9B | Google | Lightweight |

### Google AI (Gemini)

| Model | Keterangan |
|-------|------------|
| ⚡ Gemini 2.0 Flash | Latest, fastest |
| 💨 Gemini 1.5 Flash | Balanced |
| 🔮 Gemini 1.5 Pro | Most capable |

### Ollama (Local/Offline)

```bash
# Install Ollama
curl -fsSL https://ollama.com/install.sh | sh

# Download models
ollama pull llama3.2
ollama pull codellama

# Jalankan server
ollama serve
```

## 📁 Struktur Project

```
LUMA-LAMMA/
├── index.html          # Web Interface (single file - bisa jalan sendiri)
├── app.py              # Flask Backend (optional - untuk Ollama)
├── requirements.txt    # Python dependencies
├── favicon.svg         # App icon
└── README.md           # Dokumentasi
```

## 🎯 Cara Penggunaan

1. **Buka** `index.html` di browser (atau jalankan `python app.py`)
2. **Pilih Provider** - Klik tab provider di sidebar
3. **Set API Key** - Klik tombol "Set API Key" di header
4. **Pilih Model** - Pilih model dari daftar di sidebar
5. **Mulai Chat** - Ketik pesan dan tekan Enter

## 🔑 API Key Setup

### OpenRouter
1. Kunjungi [openrouter.ai/keys](https://openrouter.ai/keys)
2. Generate API key baru
3. Copy dan paste di aplikasi

### Groq
1. Kunjungi [console.groq.com](https://console.groq.com)
2. Buat API key
3. Masukkan di aplikasi

### Google AI
1. Kunjungi [aistudio.google.com](https://aistudio.google.com)
2. Get API key dari settings
3. Gunakan di aplikasi

## 🔧 Setup Ollama (Optional)

Untuk AI offline tanpa internet:

```bash
# Install Ollama
# macOS/Linux
curl -fsSL https://ollama.com/install.sh | sh

# Windows: Download dari https://ollama.com

# Download model
ollama pull llama3.2

# Jalankan (akan berjalan di background)
ollama serve

# Model lainnya
ollama pull mistral
ollama pull codellama
ollama pull phi3
```

## 🌐 Deployment

### Static Hosting (index.html only)
Upload `index.html` ke:
- GitHub Pages
- Netlify
- Vercel
- Cloudflare Pages

### Docker

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]
```

### Railway / Render

1. Connect repository
2. Set build command: `pip install -r requirements.txt`
3. Set start command: `python app.py`

## 📚 Referensi

- [OpenRouter](https://openrouter.ai) - LLM API Aggregator
- [Groq](https://console.groq.com) - Fast LLM Inference
- [Google AI Studio](https://aistudio.google.com) - Gemini API
- [Ollama](https://ollama.com) - Local LLM Runtime
- [Free LLM API Resources](https://github.com/cheahjs/free-llm-api-resources)

## 📜 License

MIT License - Free untuk digunakan!

---

⭐ Star repo ini jika bermanfaat!
