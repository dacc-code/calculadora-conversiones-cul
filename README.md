# Motor de Conversión de Bases y Aritmética de Bajo Nivel

![Python](https://img.shields.io/badge/python-3.11-blue.svg?style=flat&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/flask-3.x-black.svg?style=flat&logo=flask&logoColor=white)
![GitHub Pages](https://img.shields.io/badge/demo-GitHub_Pages-green.svg?style=flat)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

Proyecto académico para Electrónica Digital (CUL) — Calculadora multibase (2, 8, 10, 16) + ALU (AND/OR/XOR) con overflow por tamaño de palabra (8/16/32/64 bits).

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/dacc-code/calculadora-conversiones-cul)

**✅ DEMO EN VIVO (GRATIS, sin pago): https://dacc-code.github.io/calculadora-conversiones-cul/**

**Repo:** https://github.com/dacc-code/calculadora-conversiones-cul

## ✅ GitHub Pages (ACTIVO - Gratis sin tarjeta)

Ya está desplegado: **https://dacc-code.github.io/calculadora-conversiones-cul/**
- No pide pago, no se duerme, funciona offline. Es la versión estática (misma lógica pero 100% en el navegador).
- Cada `git push` a `main` actualiza la página automáticamente.

## 🚀 Deploy en Render (Requiere tarjeta, alternativo)

1. Click en **Deploy to Render** arriba o ve a https://dashboard.render.com/select-repo?type=web
2. Conecta tu GitHub y selecciona `dacc-code/calculadora-conversiones-cul`
3. Configuración (ya viene en `render.yaml`):
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`
   - **Plan:** Free
4. Click **Deploy** → URL tipo `https://calculadora-conversiones-cul.onrender.com`

> Alternativas: Railway.app (`railway up`), PythonAnywhere, Fly.io — mismo `Procfile`.

## 💻 Ejecutar local

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python app.py
# Abrir http://127.0.0.1:5000
```

## 🧮 Algoritmos

- Cualquier base -> decimal: multiplicación posicional.
- Decimal -> cualquier base: divisiones sucesivas.
- Hexadecimal: mapeo manual 0-15 <-> 0-9/A-F.
- Overflow: validación contra 2^bits - 1.
- Padding: registros completos.
- ALU: AND, OR y XOR bit a bit.
- No se usan `parseInt(numero, base)` ni `toString(base)`.

## 📦 Entregable CUL

- TODO: verificar ZIPs de entrega (`calculadora_conversiones_cul-v2.zip`, `calculadora_conversiones_cul.zip` mencionados históricamente pero no presentes en el repo).

## 🧱 Stack y arquitectura

| Capa | Tecnología |
|------|------------|
| Backend | Python + Flask 3.x (`app.py`), gunicorn |
| Frontend Flask | `templates/index.html` + `static/` |
| Demo web | HTML estático (`index.html` = `docs/`) |
| Deploy | GitHub Pages (principal) + Render (alternativo) |
| Deps | `requirements.txt` (Flask 3.x, gunicorn) |

```text
Flask: input → validate_digits(base) → base_to_decimal ↔ decimal_to_base → ALU/overflow(2^bits-1)
Estática: misma lógica 100% en el navegador, sin servidor
```

## 📁 Estructura

```text
├── app.py             # Flask + conversión multibase y ALU
├── templates/ | static/
├── index.html | docs/ # demo estática (idénticas)
├── requirements.txt | Procfile | render.yaml
├── README.md
├── LICENSE            # MIT
└── AGENTS.md           # instrucciones para agentes de IA
```

## 🧪 Testing

Sin suite automatizada. Verificación manual:

1. `python app.py` → http://127.0.0.1:5000 responde 200.
2. `FF` hex → `255` dec; `AND(1010,1100)=1000`.
3. Dígito inválido para la base → error en español.

- TODO: unit tests de conversión/ALU/overflow + CI (`py_compile` + smoke test).

## 🔒 Seguridad

Sin autenticación ni credenciales (calculadora pública). Validación estricta dígito-base con `ValueError`. No commitear `.env` (ignorado).

## 📄 Licencia

MIT — ver [LICENSE](LICENSE).
