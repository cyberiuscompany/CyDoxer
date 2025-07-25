![GitHub release downloads](https://img.shields.io/github/downloads/CyberiusCompany/Cyberius-Unzip-Cracker/latest/total)
![Versión](https://img.shields.io/badge/versión-1.0.0-blue)
![Sistema](https://img.shields.io/badge/windows-x64-green)
![Sistema](https://img.shields.io/badge/linux-x64-green)
![Licencia](https://img.shields.io/badge/licencia-Privada-red)
![Uso](https://img.shields.io/badge/uso-solo%20legal-important)
![Python](https://img.shields.io/badge/python-3.7%2B-yellow)
![Tested on](https://img.shields.io/badge/tested%20on-Windows%2010%2F11%20%7C%20Ubuntu%2022.04-blue)

<p align="center">
  <img src="https://flagcdn.com/w40/es.png" alt="Español" title="Español">
  <strong>Español</strong>
  &nbsp;|&nbsp;
  <a href="README.en.md">
    <img src="https://flagcdn.com/w40/us.png" alt="English" title="English">
    <strong>English</strong>
  </a>
  &nbsp;|&nbsp;
  <a href="https://www.youtube.com/watch?v=xvFZjo5PgG0&list=RDxvFZjo5PgG0&start_radio=1&pp=ygUTcmljayByb2xsaW5nIG5vIGFkc6AHAQ%3D%3D">
    <img src="https://flagcdn.com/w40/jp.png" alt="日本語" title="Japanese">
    <strong>日本語</strong>
  </a>
</p>

# CyDoxer
Esta es una herramienta de recopilación de información personal (Doxing) desarrollada en Flask. Permite investigar personas a partir de su nombre, alias, correo electrónico o dirección IP, utilizando múltiples fuentes públicas y APIs especializadas. 

---

<p align="center">
  <img src="/fotos_herramienta/Foto Icono.png" width="500" alt="Demostración de CyberiusUnzipCracker">
</p>

---

## 🚀 Funcionalidades principales

- 🔍 **Búsqueda por nombre real**: Permite iniciar la investigación a partir de nombres completos o parciales asociados a una persona.
- 🕵️ **Detección de alias o nicks**: Analiza posibles pseudónimos utilizados en redes sociales, foros, leaks o plataformas públicas.
- 📧 **Análisis de correos electrónicos**: Consulta filtraciones conocidas, registros en servicios online y perfiles vinculados.
- 🌐 **Investigación por dirección IP**: Muestra detalles geográficos, proveedores, historial conocido y posibles actividades relacionadas con una IP.
    
## 🧰 Tecnologías utilizadas

- **Python 3.11** – Lenguaje principal de la herramienta.
- **Flask** – Framework web ligero para construir la interfaz y rutas de la aplicación.
- **HTML5 + CSS3** – Para la estructura visual y el diseño estilizado de la interfaz.
- **APIs externas** – Se integran mediante peticiones `requests` (Recuerda añadir las tuyas propias):
  - [VirusTotal](https://www.virustotal.com/)
  - [Numverify](https://numverify.com/)
- **JSON** – Gestión de configuración y claves API.

## 📡 Integración con APIs externas

- Leaks de correos electrónicos
- Detección de perfiles en redes sociales
- Búsqueda de teléfonos y dominios asociados
- Análisis de IPs y correos con VirusTotal

## 📁 Estructura del proyecto

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

## 🎥 Demostraciónes en vivo sobre como usar la herramienta

<p align="center">
  <table border="0" cellspacing="10" cellpadding="0">
    <tr>
      <td><img src="/fotos_herramienta/Analizando Nombres.gif" alt="Panel principal" width="400"/></td>
       <td><img src="/fotos_herramienta/Analizando Correo.gif" alt="Búsqueda por nombre" width="400"/></td>
    </tr>
    <tr>
      <td><img src="/fotos_herramienta/Analizando Número de telefono.gif" alt="Búsqueda por IP" width="400"/></td>
      <td><img src="/fotos_herramienta/Analizando IP.gif" alt="Leak de correo" width="400"/></td>
    </tr>
  </table>
</p>

---

## 📄 Documentación adicional

- [🤝 Código de Conducta](.github/CODE_OF_CONDUCT.md)
- [📬 Cómo contribuir](.github/CONTRIBUTING.md)
- [🔐 Seguridad](.github/SECURITY.md)
- [⚠️Aviso legal](DISCLAIMER.md)
- [📜 Licencia](LICENSE)
- [📢 Soporte](.github/SUPPORT.md)


---

## ⚙️ 1.1 Instalación básica con clonado 🪟 Windows

```bash
git clone https://github.com/cyberiuscompany/CyDoxer.git
cd CyDoxer
python -m venv venv (No es obligatorio este comando)
.\venv\Scripts\activate (No es obligatorio este comando)
pip install -r requirements.txt
python app.py
```

## ⚙️ 1.2 Instalación básica con clonado 🐧 Linux / macOS

```bash
git clone https://github.com/cyberiuscompany/CyDoxer.git
cd CyDoxer
python3 -m venv venv (No es obligatorio este comando)
source venv/bin/activate (No es obligatorio este comando)
pip install -r requirements.txt
python3 app.py
```

## ⚙️ 2.1 Instalación en un túnel sobre Windows 🪟 (Para que este público en internet)
```bash
# En una primera consola lo siguiente:
git clone https://github.com/cyberiuscompany/CyDoxer.git
cd CyDoxer
python3 -m venv venv (No es obligatorio este comando)
.\venv\Scripts\activate (No es obligatorio este comando)
pip install -r requirements.txt
python3 app.py

# En una segunda consola lo siguiente:
Descarga: https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-windows-amd64.exe 
Renombralo como:  cloudflared.exe
cloudflared.exe --version
cloudflared.exe tunnel --url http://localhost:80

Entar a: https://DOMINIO-CLOUDFLARED
```
