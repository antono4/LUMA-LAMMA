# 🦙 LUMA-LAMMA

**Free AI Chat** - AI chat yang berjalan 100% offline di browser Anda! Tidak perlu internet, tidak perlu API key.

![LUMA-LAMMA](https://img.shields.io/badge/Status-Active-success?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-blue?style=flat-square)
![Platform](https://img.shields.io/badge/Platform-Web-orange?style=flat-square)
![Offline](https://img.shields.io/badge/Offline-100%25-green?style=flat-square)

## ✨ Fitur

| Fitur | Keterangan |
|-------|------------|
| 🔒 **Private** | Semua data diproses lokal di browser |
| 💰 **100% Free** | Tidak perlu API key atau subscription |
| 🌐 **Offline** | Berfungsi tanpa koneksi internet (setelah model di-download) |
| ⚡ **Cepat** | Menggunakan WebGPU untuk akselerasi |
| 🧠 **Multi Model** | Pilih dari berbagai model AI |

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

## 🤖 Model yang Tersedia

| Model | Ukuran | Keterangan |
|-------|--------|------------|
| 🦙 Llama 3.2 3B | ~2GB | Meta's latest - great balance |
| 📘 Phi-3.5 Mini | ~2.5GB | Microsoft - very fast |
| 🔮 Qwen 2.5 7B | ~4.5GB | Alibaba - large & capable |
| 🔮 Qwen 2.5 3B | ~2GB | Alibaba - fast & capable |
| 💎 Gemma 2 2B | ~1.5GB | Google - smallest & fastest |

## 🎯 Cara Penggunaan

1. **Buka** `index.html` di browser
2. **Pilih Model** - Pilih model AI dari dropdown di sidebar
3. **Tunggu Download** - Model akan di-download pertama kali (~1-5GB)
4. **Mulai Chat** - Ketik pesan dan tekan Enter!

**Tidak perlu internet setelah model ter-download!**

## 🔧 Requirements

- **Browser:** Chrome 113+, Edge 113+, Firefox 121+, Safari (WebGPU support)
- **RAM:** Minimal 4GB (disarankan 8GB+)
- **Storage:** ~2-5GB untuk model

### Cek WebGPU Support

Buka `chrome://gpu/` di Chrome/Edge dan pastikan "WebGPU" aktif.

## 📁 Struktur Project

```
LUMA-LAMMA/
├── index.html          # Web Interface (single file)
├── app.py              # Flask Backend (optional - untuk Ollama)
├── requirements.txt    # Python dependencies
├── favicon.svg         # App icon
└── README.md           # Dokumentasi
```

## 🌐 Teknologi

LUMA-LAMMA menggunakan teknologi berikut:

- **[WebLLM](https://webllm.mlc.ai/)** - Run LLM directly in browser
- **[WebGPU](https://webgpu.io/)** - Hardware-accelerated graphics
- **[Apache TVM** + **MLC-LLM](https://mlc.ai/)** - Efficient model runtime

## 📚 Referensi

- [WebLLM](https://webllm.mlc.ai/) - Browser-based LLM inference
- [MLC LLM](https://mlc.ai/) - Machine Learning Compilation
- [WebGPU](https://webgpu.io/) - Next-gen graphics API

## 📜 License

MIT License - Free untuk digunakan!

---

⭐ Star repo ini jika bermanfaat!
