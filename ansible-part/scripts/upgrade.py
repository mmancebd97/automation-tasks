import requests
import json

url = "http://192.168.159.62:8000/api/dcim/devices/"
headers = {"Authorization": "Token 8993072c5a67d0df6690582d9e30f48cd36c48c6"}
response = requests.get(url, headers=headers)

if response.status_code == 200:
    datos = response.json()
    dispositivos = datos.get("results", [])
    resultados = []

    for d in dispositivos:
        # Obtener el nombre del tenant de forma segura
        tenant_obj = d.get("tenant", {}) or {}
        tenant_name = tenant_obj.get("name", "MW")

        # Solo procesar si el tenant es "MW"
        if tenant_name.strip().lower() == "mw":
        #if tenant_name == "MW":
            device_name = d.get("name", "Sin nombre")

            # Obtener la IP de forma segura
            ip_obj = d.get("primary_ip", {}) or {}
            ip = ip_obj.get("address", "Sin ip")

            resultados.append({
                "tenant": tenant_name,
                "device": device_name,
                "ip": ip
            })

    print(json.dumps(resultados, indent=2))
else:
    print("Error:", response.status_code, response.text)
