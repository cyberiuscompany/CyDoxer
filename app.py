from flask import Flask, render_template, request
import requests
import json
from datetime import datetime
import webbrowser
import socket
import os

app = Flask(__name__)

# Filtro para convertir timestamps a fecha legible
def format_date(timestamp):
    try:
        return datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
    except:
        return "-"

app.jinja_env.filters['datetimeformat'] = format_date

# Cargar API key desde config.json
with open("config.json") as f:
    config = json.load(f)
    VT_API_KEY = config.get("virustotal_api_key")
    NUMVERIFY_API_KEY = config.get("numverify_api_key")

# Plataformas seleccionadas con favicon
SOCIAL_PLATFORMS = {
    "GitHub": "https://github.com/{}",
    "Twitter": "https://twitter.com/{}",
    "Instagram": "https://www.instagram.com/{}",
    "TikTok": "https://www.tiktok.com/@{}",
    "Facebook": "https://www.facebook.com/{}",
    "Snapchat": "https://story.snapchat.com/@{}",
    "Twitch": "https://www.twitch.tv/{}",
    "YouTube": "https://www.youtube.com/@{}",
    "Spotify": "https://open.spotify.com/user/{}",
    "Blogger": "https://{}.blogspot.com",
    "LinkedIn": "https://www.linkedin.com/in/{}",
    "Roblox": "https://www.roblox.com/users/profile?username={}",
    "Steam": "https://steamcommunity.com/id/{}"
}

def virustotal_lookup(ip):
    headers = {"x-apikey": VT_API_KEY}
    url = f"https://www.virustotal.com/api/v3/ip_addresses/{ip}"
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            return data.get("data", {}).get("attributes", {})
    except:
        pass
    return {}

def check_email_leak(email):
    url = f"https://leakcheck.io/api/public?check={email}"
    try:
        r = requests.get(url, timeout=5)
        if r.status_code == 200:
            data = r.json()
            return data.get("found", False)
    except:
        pass
    return False

def validate_phone_number(phone, country_code=""):
    url = "http://apilayer.net/api/validate"
    params = {
        "access_key": NUMVERIFY_API_KEY,
        "number": phone,
        "country_code": country_code,
        "format": 1
    }
    try:
        r = requests.get(url, params=params, timeout=5)
        if r.status_code == 200:
            return r.json()
    except:
        pass
    return {}

@app.route('/', methods=['GET', 'POST'])
def index():
    results = {}
    vt_info = {}
    email = ip = name = phone = ""
    email_leaked = False
    phone_info = {}
    input_type = ""

    if request.method == 'POST':
        input_type = request.form['input_type']

        if input_type == 'name':
            name = request.form['value']
            for platform, url_template in SOCIAL_PLATFORMS.items():
                if name.strip():
                    url = url_template.format(name)
                    try:
                        r = requests.get(url, timeout=5)
                        if r.status_code == 200:
                            favicon = f"https://www.google.com/s2/favicons?sz=32&domain={url_template.split('/')[2]}"
                            results[f"{platform} ({name})"] = {"url": url, "favicon": favicon}
                    except:
                        continue

        elif input_type == 'email':
            email = request.form['value']
            email_leaked = check_email_leak(email)

        elif input_type == 'ip':
            ip = request.form['value']
            vt_info = virustotal_lookup(ip)

        elif input_type == 'phone':
            phone = request.form['value']
            phone_info = validate_phone_number(phone)

    return render_template("index.html", results=results, vt_info=vt_info, name=name, email=email, ip=ip, phone=phone, email_leaked=email_leaked, phone_info=phone_info, input_type=input_type)

if __name__ == '__main__':
    # Obtener IP local
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    local_ip = s.getsockname()[0]
    s.close()

    # Mostrar ambas IPs sólo una vez (evita duplicado por debug)
    if os.environ.get("WERKZEUG_RUN_MAIN") == "true":
        print("\n[+] Accede a la herramienta desde:")
        print("   -> http://127.0.0.1:80")
        print(f"   -> http://{local_ip}:80\n")

    # Ejecutar Flask en todas las interfaces
    app.run(host='0.0.0.0', port=80, debug=True)
