# AGENTS.md — Instrucciones para agentes de IA (calculadora-conversiones-cul)

> Leer antes de modificar. Rama obligatoria: nunca commitear directo a `main`. Cada `push` a `main` republica GitHub Pages.

## Descripción

Calculadora multibase (2/8/10/16) + ALU (AND/OR/XOR) con overflow por palabra (8/16/32/64 bits) para Electrónica Digital (CUL). Doble superficie: backend Flask (`app.py`, 139 líneas, `Flask>=3.0,<4.0` + `gunicorn`) con `templates/` + `static/` (despliegue Render vía `Procfile`/`render.yaml`, Python 3.11) y mirror 100% estático (`index.html` = `docs/index.html`, 179 líneas) servido por GitHub Pages.

## Arquitectura

- `app.py`: `DIGITS`/`CHAR_TO_VALUE`, `WORD_BITS`, `BASES`; `base_to_decimal` (multiplicación posicional), `decimal_to_base` (divisiones sucesivas), validación dígito-base con `ValueError`, ALU bit a bit, overflow contra `2^bits - 1`.
- `templates/index.html` + `static/app.js` (18 líneas) + `static/styles.css`: UI Flask.
- `index.html` / `docs/index.html`: demo estática idéntica (misma lógica en navegador, sin servidor).
- `render.yaml`: `pip install -r requirements.txt` → `gunicorn app:app`, Python 3.11.0.

## Comandos

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python app.py                     # http://127.0.0.1:5000
gunicorn app:app                  # modo producción local
```

Sin linter, tests ni CI.

## Estructura

```text
├── app.py             # Flask + lógica de conversión y ALU (139 líneas)
├── templates/index.html
├── static/app.js | styles.css
├── index.html         # demo estática (idéntica a docs/)
├── docs/index.html    # publicado en GitHub Pages
├── requirements.txt   # Flask>=3.0,<4.0, gunicorn>=21.0
├── Procfile | render.yaml
├── README.md
├── LICENSE            # MIT
└── AGENTS.md          # este archivo
```

## Convenciones

- Mensajes de error en español (`ValueError`).
- Commits imperativos (`feat:`, `fix:`, `docs:`).
- No inventar URLs, ZIPs ni features: lo no verificado va como `TODO`. (Nota: el README menciona ZIPs de entrega que no están en el repo.)

## Reglas de modificación

1. Rama `feat/*`, `fix/*`, `docs/*`, `chore/*`. Jamás a `main` (dispara Pages).
2. `git status` + `git branch --show-current` antes de editar.
3. Si cambia la lógica de conversión/ALU, actualizar Flask + demo estática + `docs/` en el mismo PR (mantener paridad).
4. No cambiar rangos de `requirements.txt` ni `render.yaml` (Python 3.11) sin probar `python app.py` y `gunicorn app:app`.
5. Sin secretos: no hay credenciales; no introducir ninguno.

## Testing / Lint / Build

- Sin suite. Verificación mínima: `python -m py_compile app.py`, `python app.py` y convertir `FF` hex→dec (`255`), ALU `AND(1010,1100)=1000`.
- TODO: tests unitarios de `base_to_decimal`/`decimal_to_base`/ALU + overflow + CI (`py_compile` + smoke test Flask).
- Equipo limitado: no instalar toolchains pesados.

## Deployment

- Pages: sirve `docs/` en cada push a `main` (demo principal, gratis).
- Render: alternativo con tarjeta (misma imagen lógica vía gunicorn). No tocar `render.yaml`/`Procfile` sin aprobación.

## Variables de entorno

`$PORT` (inyectado por el host en `Procfile`). Ninguna otra. `.env` ignorado.

## IA (OpenCode implementa, Codex revisa)

- OpenCode: plan antes de implementar, solo en rama actual.
- Codex: clasificar CRITICAL/HIGH/MEDIUM/LOW/SUGGESTION. Bloquean merge: secretos, validación dígito-base rota, overflow mal calculado, paridad Flask↔estática rota, docs falsas (URLs, ZIPs, demos).
