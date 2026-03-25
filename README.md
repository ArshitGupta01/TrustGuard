# TrustGuard: Hybrid-AI Fake Review Detector 🛡️

TrustGuard is an advanced browser extension and backend ecosystem designed to identify fake and suspicious reviews on major e-commerce platforms (Amazon, Flipkart, Myntra, etc.) using a **Hybrid Trust Score Algorithm** and **Large Language Models**.

---

## 🚀 Key Features

*   **Hybrid Trust Score**: Combines heuristic analysis (reviewer metadata, verified status, rating distribution) with machine learning predictions.
*   **Qwen AI Second Opinion**: Leverages the `Qwen 2.5` model via Ollama to provide a 2-sentence human-like cross-check of the heuristic score.
*   **Optimized Storage Model**: Designed for system efficiency with a pre-configured data relocation to the D drive (`D:\Finaltry`) to preserve C drive space.
*   **Dynamic Extension UI**: Injects a premium Trust Badge and a dedicated AI Summary box directly onto product pages.

---

## 🛠️ Step 1: Docker Setup (Relocated Storage)

To ensure high performance and prevent C drive exhaustion, TrustGuard is configured to store all heavy assets (Models & DBs) in `D:\Finaltry`.

### 1.1 Prerequisites
- **Docker Desktop** installed.
- **NVIDIA GPU** recommended (with NVIDIA Container Toolkit).

### 1.2 Initialize Storage
Ensure the directory `D:\Finaltry` exists on your system.
```powershell
mkdir D:\Finaltry
```

### 1.3 Launch All Services
From the project root:
```bash
docker compose up --build -d
```
*Note: This will perform a fresh pull of base images. All model data will be strictly stored in `D:\Finaltry\ollama`.*

---

## 🔍 Step 2: Service Verification

Verify that the backend and AI engine are communicating correctly:

1.  **Backend Health**: `curl http://localhost:8000/healthz` 
    *   Expected: `{"status": "healthy", "version": "2.0.0"}`
2.  **Ollama Model**: `docker exec trustguard-ollama ollama list`
    *   Confirm `qwen2.5:latest` is present.

---

## 🧩 Step 3: Browser Extension Installation

1.  Open **Chrome** and go to `chrome://extensions/`.
2.  Enable **Developer mode** (top-right).
3.  Click **Load unpacked** and select the **active extension folder** at:
    `C:\Users\MOHIT\Desktop\trustguar_new_version\trustguard_new\extension`
4.  Navigate to an **Amazon** or **Flipkart** product page.
5.  Look for the **TrustGuard Badge** and **Qwen AI Analysis** boxes injected below the product title.

---

## 📋 Technical Architecture

-   **Backend**: FastAPI, Motor (Async MongoDB), Pydantic.
-   **AI Integration**: Ollama (OpenAI-compatible API).
-   **Database**: MongoDB 7.0.
-   **Security**: All API traffic is routed through the Extension Service Worker to bypass CORS and ensure stability.

---

## 🛡️ Storage & Space Management (Submission Note)

To maintain a clean evaluation environment, we have implemented a **Strict D-Drive Policy**:
-   **MongoDB Data**: `D:\Finaltry\mongodb`
-   **Ollama Models**: `D:\Finaltry\ollama`
-   **C Drive Reclaim**: `docker system prune -a --volumes -f` was used to clear all temporary build layers (approx. 13GB reclaimed).

---

## 📜 Key File Mapping
-   `backend/app.py`: Core logic for Hybrid Trust Score and AI prompt engineering.
-   `extension/content.js`: Real-time DOM scraping and UI injection logic.
-   `extension/styles.css`: Premium dark-mode styling for badges and analysis boxes.
-   `docker-compose.yml`: Manifest for the relocated service architecture.

---

*Evaluated for: Performance, AI Accuracy, and UI/UX Excellence.*

