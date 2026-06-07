# ROADMAP — Static String Extractor and Classifier
 ---
 
## Phase 0 / Faz 0: Understand Before You Build / Yazmadan Önce Anla

### Before writing a single line of code, I answered these questions:
### Tek satır kod yazmadan önce şu soruları yanıtladım:

1. **What is the project? / Proje nedir?**
   * It is a static analysis and security automation tool that extracts readable text from compiled binary files or Android APKs, categorizes them using pattern matching, and screens them for sensitive data leaks via entropy calculation.
   * Derlenmiş binary dosyalarından veya Android APK'larından okunabilir metinleri çıkaran, bunları kalıp eşleme yöntemiyle kategorize eden ve entropi hesaplaması yoluyla hassas veri sızıntılarını tarayan bir statik analiz ve güvenlik otomasyon aracıdır.

---

## Phase 1 / Faz 1: Research & Investigation / Araştırma ve Keşif

> Folder / Klasör: `docs/research/`

| Topic / Konu | Status / Durum | Notes / Notlar |
|--------------|----------------|----------------|
| 1. Research binary byte-stream processing in Python / Python'da binary byte-akışı işlemeyi araştırın | [X] Completed / Tamamlandı | Base logic done / Temel mantık bitti |
| 2. Design high-precision Regex patterns / Yüksek hassasiyetli Regex kalıpları tasarlayın | [X] Completed / Tamamlandı | Patterns integrated / Kalıplar entegre edildi |
| 3. Model the Shannon Entropy mathematical algorithm / Shannon Entropisi matematiksel algoritmasını modelleyin | [X] Completed / Tamamlandı | Entropy analysis operational / Entropi analizi aktif |

---

## Phase 2 / Faz 2: Environment Setup / Ortam Kurulumu

- [X] Isolated lab environment (Docker) / İzole lab ortamı (Docker)
- [X] Tools installed and verified / Araçlar kuruldu ve test edildi
- [X] `.env.example` created / `.env.example` oluşturuldu

---

## Phase 3 / Faz 3: Implementation / Uygulama

### Module / Modül: Static String Processing Engine / Statik String İşleme Motoru

1. Step 1 / Adım 1 — Core Extraction Module (`extractor.py`) [X]
2. Step 2 / Adım 2 — Classification Engine (`classifier.py`) [X]
3. Step 3 / Adım 3 — Structured Reporter (`reporter.py`) [X]

---

## Phase 4 / Faz 4: Testing & Reporting / Test ve Raporlama

- [X] Ran tests against target/sample / Hedef/örnek üzerinde testler çalıştırıldı
- [X] Documented all findings with evidence / Tüm bulgular kanıtlarıyla belgelendi
- [X] Wrote final report (Markdown) / Final raporu yazıldı

---

## Phase 5 / Faz 5: Delivery / Teslim

- [X] GitHub repository is clean and organized / Repo temiz ve düzenli
- [X] README.md complete / eksiksiz
- [X] Docker verified (`docker-compose up`) / Docker doğrulandı
