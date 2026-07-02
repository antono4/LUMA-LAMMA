# 🦙 LUMA-LAMMA

**Free AI Chat** - Chat dengan AI gratis langsung dari browser!

![LUMA-LAMMA](https://img.shields.io/badge/Status-Active-success?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-blue?style=flat-square)

## ✨ Fitur

| Fitur | Keterangan |
|-------|------------|
| 💰 **100% Free** | Groq API punya free tier |
| ⚡ **Cepat** | Ultra fast inference dengan Groq |
| 🎨 **UI Modern** | Interface yang clean & responsif |
| 🔒 **Private** | Chat tidak disimpan |

## 🚀 Quick Start

### 1. Jalankan Server

```bash
# Install dependencies
pip install -r requirements.txt

# Jalankan server
python app.py

# Buka browser
open http://localhost:5000
```

### 2. Set API Key

1. Buka https://console.groq.com/keys
2. Buat account (GRATIS)
3. Generate API key baru
4. Copy dan paste di aplikasi (klik tombol "Set API Key" di header)

### 3. Mulai Chat!

Pilih model dan mulai chat!

## 🤖 Model

### Groq (Free Tier - Ultra Fast)

| Model | Provider | Keterangan |
|-------|----------|------------|
| 🦙 Llama 3.3 70B | Meta | High performance |
| 🦙 Llama 3.1 8B | Meta | Fast & lightweight |
| 🌀 Mixtral 8x7B | Mistral | Mixture of experts |
| 💎 Gemma 2 9B | Google | Google's best |

### Ollama (Local)

Jalankan `ollama serve` di komputer Anda, lalu pilih provider "Ollama".

## 💡 Tips

- **Groq API free tier:** 14,400 requests/day, 30 requests/minute
- **Model recommendation:** Llama 3.1 8B untuk kecepatan, Llama 3.3 70B untuk kualitas
- **API key aman?** Ya, disimpan di localStorage browser Anda

## 📁 Struktur Project

```
LUMA-LAMMA/
├── index.html          # Web Interface
├── app.py              # Flask Backend
├── requirements.txt    # Python dependencies
├── favicon.svg         # App icon
└── README.md           # Dokumentasi
```

## 📜 License

MIT License - Free untuk digunakan!

---

⭐ Star repo ini jika bermanfaat!
