# Motor de Conversión de Bases y Aritmética de Bajo Nivel

Proyecto académico para Electrónica Digital (CUL) — Calculadora multibase (2, 8, 10, 16) + ALU (AND/OR/XOR) con overflow por tamaño de palabra (8/16/32/64 bits).

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/dacc-code/calculadora-conversiones-cul)

**Repo:** https://github.com/dacc-code/calculadora-conversiones-cul

## 🚀 Deploy en Render (Gratis, 2 min)

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

- ZIP listo: `calculadora_conversiones_cul-v2.zip` (5.9K, con Procfile/render.yaml)
- Original: `calculadora_conversiones_cul.zip`
