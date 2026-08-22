# Motor de Conversión de Bases y Aritmética de Bajo Nivel

Proyecto académico para Electrónica Digital (CUL).

## Ejecutar

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Abrir http://127.0.0.1:5000

## Algoritmos

- Cualquier base -> decimal: multiplicación posicional.
- Decimal -> cualquier base: divisiones sucesivas.
- Hexadecimal: mapeo manual 0-15 <-> 0-9/A-F.
- Overflow: validación contra 2^bits - 1.
- Padding: registros completos.
- ALU: AND, OR y XOR bit a bit.
- No se usan parseInt(numero, base) ni toString(base).
