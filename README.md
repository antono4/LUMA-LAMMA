# 🤖 LUMA-LAMMA

AI Chat Agent dengan Ollama - **100% Local, Private, & Free!**

Chat dengan berbagai model LLM open-source langsung dari komputer Anda tanpa perlu internet atau API key.

## ✨ Fitur

- 🏠 **100% Local** - Tidak perlu koneksi internet
- 🔒 **100% Private** - Data tidak pernah meninggalkan komputer Anda
- 💰 **100% Free** - Tidak perlu API key atau credits
- ⚡ **Cepat** - Jalankan langsung di mesin lokal
- 🎨 **UI Modern** - Interface web yang clean dan responsif
- 💬 **Conversation History** - Menyimpan histori percakapan
- 🧠 **Multi Model** - Pilihan berbagai model LLM populer

## 🚀 Quick Start

### 1. Install Ollama

```bash
# macOS/Linux
curl -fsSL https://ollama.com/install.sh | sh

# Windows - Download dari https://ollama.com
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Jalankan

```bash
python app.py
```

### 4. Buka Browser

```
http://localhost:5000
```

## 📡 Model yang Tersedia

| Model | Parameter | Tipe |
|-------|-----------|------|
| **Mistral** ⭐ | 7B | General |
| **Llama 3** | - | General |
| **Llama 3.2** | - | General |
| **Phi-3** | 3.8B | General |
| **Qwen 2.5** | 7B | General |
| **Gemma 2** | 2B | General |
| **Code Llama** | 7B | Code |
| **DeepSeek Coder** | 6.7B | Code |

## 🔧 Install Model Tambahan

```bash
# Umum
ollama pull llama3
ollama pull phi3
ollama pull qwen2.5
ollama pull gemma2

# Coding
ollama pull codellama
ollama pull deepseek-coder
```

## 📁 Struktur Project

```
LUMA-LAMMA/
├── app.py              # Flask Backend API
├── index.html          # Web Interface
├── requirements.txt    # Python Dependencies
├── .env                # Environment Config
└── README.md           # Dokumentasi
```

## 🎯 Penggunaan

1. **Pilih Model** - Klik dropdown di bagian atas
2. **Ketik Pesan** - Tulis pertanyaan Anda
3. **Kirim** - Tekan Enter atau klik Send
4. **Clear Chat** - Klik tombol untuk reset percakapan

## 💡 Keunggulan

| | Ollama |
|--|--------|
| 🌐 Internet | ❌ Tidak perlu |
| 🔐 Privacy | ✅ 100% private |
| 💳 Credit/Key | ❌ Tidak perlu |
| 💸 Biaya | ✅ Gratis |
| ⚡ Speed | ✅ Sangat cepat |
| 📱 Offline | ✅ Bisa offline |

## 📚 Sumber

Model dari [Ollama Library](https://ollama.com/library)

## 📜 License

MIT License
