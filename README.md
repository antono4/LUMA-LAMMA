# 🦙 LUMA-LAMMA

**Free AI Chat** - Chat dengan berbagai model LLM gratis langsung dari browser! Tanp API key!

![LUMA-LAMMA](https://img.shields.io/badge/Status-Active-success?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-blue?style=flat-square)
![Platform](https://img.shields.io/badge/Platform-Web-orange?style=flat-square)
![API Key](https://img.shields.io/badge/API_Key-Not_Required-green?style=flat-square)

## ✨ Fitur

| Fitur | Keterangan |
|-------|------------|
| 🌐 **Online** | Tidak perlu install software, buka langsung di browser |
| 🔑 **No API Key** | Langsung pakai tanpa register API key! |
| 💰 **100% Free** | Multiple provider gratis (OpenRouter, Cerebras, xAI) |
| 🎨 **UI Modern** | Interface web yang clean, responsif & mudah digunakan |
| ⚡ **Cepat** | Response time yang cepat |
| 🧠 **Multi Model** | Pilihan berbagai model LLM populer |

## 🚀 Quick Start

### Jalankan Langsung

```bash
# Download file
curl -O https://raw.githubusercontent.com/antono4/LUMA-LAMMA/main/index.html

# Buka langsung di browser
open index.html
```

**Atau buka langsung dari GitHub Pages:**
```
https://antono4.github.io/LUMA-LAMMA/
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

### OpenRouter (Free Tier - 20 req/min)

| Model | Provider | Keterangan |
|-------|----------|------------|
| 💎 Gemma 3 27B | Google | Google's latest |
| 💎 Gemma 4 26B | Google | Latest Gemma |
| 🧠 Liquid Thinking | Liquid | Reasoning model |
| ⚡ Nemotron Nano 9B | NVIDIA | Fast & small |
| 🤖 GPT-OSS 20B | OpenAI | Open source |
| 💻 Qwen Coder | Alibaba | Code specialist |
| 🏊 Laguna XS | Poolside | Small & fast |

### Cerebras (Ultra Fast - 30 req/min)

| Model | Provider | Keterangan |
|-------|----------|------------|
| 🦙 Llama 3.3 70B | Meta | High performance |
| 🦙 Llama 3.1 8B | Meta | Fast & small |
| 🔮 Qwen 2.5 32B | Alibaba | Large context |

### xAI Grok (Free Access)

| Model | Keterangan |
|-------|------------|
| 🤖 Grok 2 Mini | Small & fast |
| 🚀 Grok 2 | Full version |
| ⚡ Grok Beta | Beta release |

### Ollama (Local/Offline)

```bash
# Install Ollama
curl -fsSL https://ollama.com/install.sh | sh

# Download models
ollama pull llama3.2
ollama pull codellama

# Jalankan
ollama serve
```

## 📁 Struktur Project

```
LUMA-LAMMA/
├── index.html          # Web Interface (single file - bisa jalan sendiri)
├── app.py              # Flask Backend (optional - untuk Ollama)
├── requirements.txt     # Python dependencies
├── favicon.svg         # App icon
└── README.md           # Dokumentasi
```

## 🎯 Cara Penggunaan

1. **Buka** `index.html` di browser (atau buka https://antono4.github.io/LUMA-LAMMA/)
2. **Pilih Provider** - Klik tab provider di sidebar
3. **Pilih Model** - Pilih model dari daftar di sidebar
4. **Mulai Chat** - Ketik pesan dan tekan Enter

**Tidak perlu API key!** Langsung pakai.

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

## 📚 Referensi

- [OpenRouter](https://openrouter.ai) - LLM API Aggregator
- [Cerebras](https://cloud.cerebras.ai/) - Ultra Fast Inference
- [xAI Grok](https://x.ai/) - Grok Models
- [Ollama](https://ollama.com) - Local LLM Runtime
- [Free LLM API Resources](https://github.com/cheahjs/free-llm-api-resources)

## 📜 License

MIT License - Free untuk digunakan!

---

⭐ Star repo ini jika bermanfaat!
