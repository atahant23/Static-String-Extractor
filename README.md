<div align="center">
  <a href="https://istinye.edu.tr">
    <img src="docs/assets/istinye-university-logo.webp" alt="Istinye University" width="180"/>
  </a>

  # Static String Extractor and Classifier / Statik String Çıkartıcı ve Sınıflandırıcı

  ![GitHub](https://img.shields.io/badge/GitHub-Private-red?style=flat-square&logo=github)
  ![Language](https://img.shields.io/badge/Language-[Rust|Python|Go]-blue?style=flat-square)
  ![Status](https://img.shields.io/badge/Status-In%20Progress-yellow?style=flat-square)
  ![Course](https://img.shields.io/badge/Course-BGT210-purple?style=flat-square)
  ![License](https://img.shields.io/badge/License-Educational-green?style=flat-square)
</div>

---

## 🎓 Instructor / Danışman

| | |
|---|---|
| **Name / Ad** | Keyvan Arasteh |
| **GitHub** | [@keyvanarasteh](https://github.com/keyvanarasteh) |
| **Email** | [keyvan.arasteh@istinye.edu.tr](mailto:keyvan.arasteh@istinye.edu.tr) |
| **LinkedIn** | [keyvanarasteh](https://www.linkedin.com/in/keyvanarasteh/) |
| **Website** | [qline.tech](https://qline.tech) |

---

## 👤 Student / Öğrenci

| | |
|---|---|
| **Name / Ad Soyad** | Atahan Turna |
| **Student ID / Öğrenci No** | `***0191***` |
| **GitHub** | [@atahant23](https://github.com/atahant23) |
| **Email** | [atahanturna@hotmail.com](mailto:atahanturna@hotmail.com) |
| **LinkedIn** | [Atahan Turna](https://www.linkedin.com/in/atahan-turna-077051283//) |

---

## 📚 Course Information / Ders Bilgileri

| | |
|---|---|
| **Course Name / Ders Adı** | Reverse Engineering / Tersine Mühendislik |
| **Course Code / Ders Kodu** | BGT210 |
| **Credits / Kredi** | 3 ECTS |
| **Semester / Dönem** | 2025-2026 Spring / 2025-2026 Bahar |
| **Institution / Üniversite** | [Istinye University](https://istinye.edu.tr) |

---

## 📋 Project Overview / Proje Özeti
---
Static String Extractor & Classifier is an advanced static analysis and threat intelligence engine developed as a final project for the BGT210 Reverse Engineering course at Istinye University.
Containerized entirely within Docker, the tool automatically detects target binary architectures (ELF, PE, APK) via magic bytes, extracts printable ASCII strings, flags high-risk cryptographic structures using Shannon Entropy, and maps heuristic behavioral capabilities (suspicious system calls and APIs). The pipeline cross-compiles these multi-vector forensic metrics into a structured JSON payload and a high-contrast, interactive dark-mode web dashboard (report.html) for seamless security audits.


Proje Özeti
Static String Extractor & Classifier, İstinye Üniversitesi BGT210 Tersine Mühendislik dersi final projesi kapsamında geliştirilmiş gelişmiş bir statik analiz ve tehdit istihbaratı motorudur.
Docker üzerinde tamamen izole şekilde çalışan bu araç; sihirli byte'lar (magic bytes) aracılığıyla hedef dosya mimarilerini (ELF, PE, APK) otomatik olarak tanımlar, basılabilir ASCII karakter dizilimlerini ayıklar, Shannon Entropisi hesaplayarak yüksek riskli kriptografik yapıları işaretler ve sezgisel (heuristic) davranışsal yetenekleri (şüpheli sistem çağrıları ve API'ler) haritalandırır. Geliştirilen boru hattı, elde edilen tüm çok vektörlü adli bilişim metriklerini yapılandırılmış bir JSON verisine ve kusursuz güvenlik denetimleri için yüksek kontrastlı, interaktif bir karanlık mod web paneline (report.html) dönüştürür.

---

## 🗂 Repository Structure / Repo Yapısı

```
Static-String-Extractor/
├── docs/                   
│   ├── modules/
│       └── string_extractor_classifier.md
│   └── research/ 
│       └── entropy_analysis_notes.md
├── reports/
│   ├── report.html
│   └── report.json
├── src/
│   ├── __init__.py
│   ├── classifier.py
│   ├── extractor.py
│   ├── main.py             
│   └── reporter.py
├── targets/       
│   ├── curl_binary     
│   ├── real_binary   
│   └── sample.bin 
├── .env
├── .env.example 
├── .gitignore
├── docker-compose.yml 
├── Dockerfile
├── requirements.txt
└── ROADMAP.md
```

---

## 🚀 Getting Started / Kurulum

```
git clone https://github.com/atahant23/Static-String-Extractor.git
cd static-string-extractor
cp .env.example .env
gcc targets/test.c -o targets/real_binary
strip targets/real_binary
docker-compose up --build
opera reports/report.html

```

---

## 📊 Deliverables / Teslimler

| Deliverable Item | Status |
|:---|:---:|
| **Core Analytics & String Extraction Engine** (`src/`) | ✅ Completed |
| **Structured Threat Intelligence Reports** (`reports/report.json` & `report.html`) | ✅ Completed |
| **Academic Roadmap & Forensic Research Notes** (`docs/` & `ROADMAP.md`) | ✅ Completed |
| **Isolated Deployment Environment** (`Dockerfile` & `docker-compose.yml`) | ✅ Completed |

---

| Teslim Edilen Madde | Durum |
|:---|:---:|
| **Çekirdek Analitik ve String Çıkarım Motoru** (`src/`) | ✅ Tamamlandı |
| **Yapılandırılmış Tehdit İstihbaratı Raporları** (`reports/report.json` & `report.html`) | ✅ Tamamlandı |
| **Akademik Yol Haritası ve Adli Araştırma Notları** (`docs/` & `ROADMAP.md`) | ✅ Tamamlandı |
| **İzole Çalışma ve Dağıtım Ortamı** (`Dockerfile` & `docker-compose.yml`) | ✅ Tamamlandı |

---

## 📚 Documentation / Belgeleme

Comprehensive technical documentation, architectural blueprints, and forensic research papers are systematically organized within the repository:

- **[Module Specification](docs/modules/string_extractor_classifier.md):** Detailed code architecture, regex patterns, and processing pipeline definitions.
- **[Forensic Research Notes](docs/research/entropy_analysis_notes.md):** Theoretical and mathematical modeling of Shannon Entropy in binary obfuscation detection.
- **[Project Roadmap](ROADMAP.md):** Milestone tracking, version history, and future structural evolution plans.
- **[Modül Özellikleri](docs/modules/string_extractor_classifier.md):** Detaylı kod mimarisi, regex kalıpları ve işleme boru hattı tanımları.
- **[Adli Araştırma Notları](docs/research/entropy_analysis_notes.md):** Binary gizleme/paketleme tespitinde Shannon Entropisinin teorik ve matematiksel modellemesi.
- **[Proje Yol Haritası](ROADMAP.md):** Kilometre taşı takibi, versiyon geçmişi ve gelecekteki mimari gelişim planları.

## 🔗 References / Kaynaklar

- [GNU Binutils - strings(1) Manual Page](https://sourceware.org/binutils/docs/binutils/strings.html)
- [An Introduction to Shannon Entropy in Malware Analysis](https://www.sciencedirect.com/)
- [Executable and Linkable Format (ELF) Specification](https://refspecs.linuxfoundation.org/elf/elf.pdf)
- [Docker Architecture & Volume Mapping Guide](https://docs.docker.com/)
- [GNU Binutils - strings(1) El Kitabı](https://sourceware.org/binutils/docs/binutils/strings.html)
- [Malware Analizinde Shannon Entropisine Giriş](https://www.sciencedirect.com/)
- [Executable and Linkable Format (ELF) Spesifikasyonu](https://refspecs.linuxfoundation.org/elf/elf.pdf)
- [Docker Mimarisi ve Hacim (Volume) Eşleme Kılavuzu](https://docs.docker.com/)
