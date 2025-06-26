import requests
import json

#vars for get valors
url = "http://192.168.159.62:8000/api/dcim/devices/"
headers = {"Authorization": "Token 8993072c5a67d0df6690582d9e30f48cd36c48c6"}
resultados = []


while url:
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        datos = response.json()
        dispositivos = datos.get("results", [])

        for d in dispositivos:
            tenant_obj = d.get("tenant", {}) or {}
            tenant_name = tenant_obj.get("name", "Sin tenant")

            if tenant_name == "COGNET":  # Solo exactamente "MW"
                device_name = d.get("name", "Sin nombre")
                ip_obj = d.get("primary_ip", {}) or {}
                ip = ip_obj.get("address", "Sin ip")
                resultados.append({
                    "tenant": tenant_name,
                    "device": device_name,
                    "ip": ip
                })
        url = datos.get("next")  # Siguiente página si existe
    else:
        print("Error:", response.status_code, response.text)
        break

print(json.dumps(resultados, indent=2))
