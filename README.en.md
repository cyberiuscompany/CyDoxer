
![GitHub release downloads](https://img.shields.io/github/downloads/CyberiusCompany/Cyberius-Unzip-Cracker/latest/total)
![Version](https://img.shields.io/badge/version-1.0.0-blue)
![System](https://img.shields.io/badge/windows-x64-green)
![System](https://img.shields.io/badge/linux-x64-green)
![License](https://img.shields.io/badge/license-Private-red)
![Usage](https://img.shields.io/badge/usage-legal%20only-important)
![Python](https://img.shields.io/badge/python-3.7%2B-yellow)
![Tested on](https://img.shields.io/badge/tested%20on-Windows%2010%2F11%20%7C%20Ubuntu%2022.04-blue)

<p align="center">
  <a href="README.md">
    <img src="https://flagcdn.com/w40/es.png" alt="Español" title="Español">
    <strong>Español</strong>
  </a>
  &nbsp;|&nbsp;
  <img src="https://flagcdn.com/w40/us.png" alt="English" title="English">
  <strong>English</strong>
  &nbsp;|&nbsp;
  <a href="https://www.youtube.com/watch?v=xvFZjo5PgG0&list=RDxvFZjo5PgG0&start_radio=1&pp=ygUTcmljayByb2xsaW5nIG5vIGFkc6AHAQ%3D%3D">
    <img src="https://flagcdn.com/w40/jp.png" alt="Japanese" title="Japanese">
    <strong>日本語</strong>
  </a>
</p>

# CyDoxer

This is a personal information gathering tool (Doxing) developed in Flask. It allows you to investigate individuals based on their name, alias, email address or IP address, using multiple public sources and specialized APIs.

---

<p align="center">
  <img src="/fotos_herramienta/Foto Icono.png" width="500" alt="CyDoxer Icon">
</p>

---

## 🚀 Main Features

- 🔍 **Search by real name**: Investigate using full or partial names associated with a person.
- 🕵️ **Alias or nickname detection**: Analyzes potential pseudonyms used on social networks, forums, leaks, or public platforms.
- 📧 **Email analysis**: Checks known leaks, registrations on online services, and linked profiles.
- 🌐 **IP address investigation**: Shows geographic details, ISPs, known history, and possible activities tied to an IP.

## 🧰 Technologies Used

- **Python 3.11** – Main programming language.
- **Flask** – Lightweight web framework for interface and routes.
- **HTML5 + CSS3** – Visual structure and stylish interface design.
- **External APIs** – Integrated via `requests`:
  - [VirusTotal](https://www.virustotal.com/)
  - [Numverify](https://numverify.com/)
- **JSON** – For configuration and API key handling.

## 📡 External API Integrations

- Email leak detection
- Social profile discovery
- Phone and domain associations
- IP and email analysis with VirusTotal

## 📁 Project Structure

```bash
├── app.py
├── templates/
│   └── index.html
├── static/
│   ├── styles.css
│   └── fondo.webm
├── templates/
│   └── index.html
├── requirements.txt
└── README.md
```

---

## 🎥 Live Demonstrations

<p align="center">
  <table border="0" cellspacing="10" cellpadding="0">
    <tr>
      <td><img src="/fotos_herramienta/Analizando Nombres.gif" alt="Name Analysis" width="400"/></td>
      <td><img src="/fotos_herramienta/Analizando Correo.gif" alt="Email Search" width="400"/></td>
    </tr>
    <tr>
      <td><img src="/fotos_herramienta/Analizando Número de telefono.gif" alt="Phone Search" width="400"/></td>
      <td><img src="/fotos_herramienta/Analizando IP.gif" alt="IP Leak" width="400"/></td>
    </tr>
  </table>
</p>

---

## 📄 Additional Documentation

- [🤝 Code of Conduct](.github/CODE_OF_CONDUCT.md)
- [📬 How to Contribute](.github/CONTRIBUTING.md)
- [🔐 Security](.github/SECURITY.md)
- [⚠️ Legal Notice](DISCLAIMER.md)
- [📜 License](LICENSE)
- [📢 Support](.github/SUPPORT.md)

---

## ⚙️ 1.1 Basic Installation 🪟 Windows

```bash
git clone https://github.com/cyberiuscompany/CyDoxer.git
cd CyDoxer
python -m venv venv (Optional)
.env\Scriptsctivate (Optional)
pip install -r requirements.txt
python app.py
```

## ⚙️ 1.2 Basic Installation 🐧 Linux / macOS

```bash
git clone https://github.com/cyberiuscompany/CyDoxer.git
cd CyDoxer
python3 -m venv venv (Optional)
source venv/bin/activate (Optional)
pip install -r requirements.txt
python3 app.py
```

## ⚙️ 2.1 Tunnel Setup on Windows 🪟 (To expose it publicly)

```bash
# First terminal:
git clone https://github.com/cyberiuscompany/CyDoxer.git
cd CyDoxer
python3 -m venv venv (Optional)
source venv/bin/activate (Optional)
pip install -r requirements.txt
python3 app.py

# Second terminal:
Download: https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-windows-amd64.exe 
Rename to: cloudflared.exe
cloudflared.exe --version
cloudflared.exe tunnel --url http://localhost:80

Access: https://CLOUDFLARED-DOMAIN
```
