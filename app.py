from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

DIGITS = "0123456789ABCDEF"
CHAR_TO_VALUE = {str(i): i for i in range(10)}
CHAR_TO_VALUE.update({chr(ord("A") + i): 10 + i for i in range(6)})

WORD_BITS = {"8": 8, "16": 16, "32": 32, "64": 64}
BASES = {"2": 2, "8": 8, "10": 10, "16": 16}

def digit_value(ch):
    ch = ch.upper()
    if ch not in CHAR_TO_VALUE:
        raise ValueError(f"Dígito inválido: {ch}")
    return CHAR_TO_VALUE[ch]

def validate_digits(number, base):
    if not number:
        raise ValueError("Ingrese un número.")
    for ch in number.upper():
        value = digit_value(ch)
        if value >= base:
            raise ValueError(f"El dígito '{ch}' no pertenece a la base {base}.")

def base_to_decimal(number, base):
    number = number.strip().upper()
    validate_digits(number, base)
    result = 0
    power = 1
    for ch in reversed(number):
        result += digit_value(ch) * power
        power *= base
    return result

def decimal_to_base(value, base):
    if value == 0:
        return "0"
    remainders = []
    current = value
    while current > 0:
        quotient = current // base
        remainder = current - quotient * base
        remainders.append(DIGITS[remainder])
        current = quotient
    result = ""
    for i in range(len(remainders) - 1, -1, -1):
        result += remainders[i]
    return result

def pad_left(value, width):
    while len(value) < width:
        value = "0" + value
    return value

def convert_all(number, source_base, bits):
    decimal_value = base_to_decimal(number, source_base)
    max_value = (2 ** bits) - 1
    if decimal_value > max_value:
        raise OverflowError(
            f"Overflow / Desbordamiento de Registro. "
            f"El máximo para {bits} bits es {max_value}."
        )
    binary = pad_left(decimal_to_base(decimal_value, 2), bits)
    octal = pad_left(decimal_to_base(decimal_value, 8), (bits + 2) // 3)
    decimal = decimal_to_base(decimal_value, 10)
    hexadecimal = pad_left(decimal_to_base(decimal_value, 16), (bits + 3) // 4)
    return {
        "binary": binary,
        "octal": octal,
        "decimal": decimal,
        "hexadecimal": hexadecimal,
        "decimal_value": decimal_value,
        "max_value": max_value,
    }

def normalize_binary(value):
    value = value.strip()
    if not value:
        raise ValueError("Ingrese un valor binario.")
    for ch in value:
        if ch not in "01":
            raise ValueError("La ALU solo acepta cadenas binarias.")
    return value

def alu_operation(a, b, operation):
    a, b = normalize_binary(a), normalize_binary(b)
    if len(a) != len(b):
        raise ValueError("Las dos cadenas binarias deben tener la misma longitud.")
    result = ""
    for i in range(len(a)):
        x, y = a[i], b[i]
        if operation == "AND":
            bit = "1" if x == "1" and y == "1" else "0"
        elif operation == "OR":
            bit = "1" if x == "1" or y == "1" else "0"
        elif operation == "XOR":
            bit = "1" if x != y else "0"
        else:
            raise ValueError("Operación ALU no válida.")
        result += bit
    return result

@app.get("/")
def index():
    return render_template("index.html")

@app.post("/api/convert")
def api_convert():
    try:
        data = request.get_json(force=True)
        source_base = BASES.get(str(data.get("base", "")))
        bits = WORD_BITS.get(str(data.get("bits", "")))
        if source_base is None:
            raise ValueError("Base de entrada no válida.")
        if bits is None:
            raise ValueError("Tamaño de palabra no válido.")
        return jsonify(convert_all(str(data.get("number", "")), source_base, bits))
    except OverflowError as exc:
        return jsonify({"error": str(exc)}), 422
    except ValueError as exc:
        return jsonify({"error": str(exc)}), 400

@app.post("/api/alu")
def api_alu():
    try:
        data = request.get_json(force=True)
        return jsonify({"result": alu_operation(
            str(data.get("a", "")),
            str(data.get("b", "")),
            str(data.get("operation", "")).upper()
        )})
    except ValueError as exc:
        return jsonify({"error": str(exc)}), 400

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
