import json
from jsonschema import validate, Draft202012Validator
from pathlib import Path

SCHEMA_PATH = Path("schemas/case_schema.json")

def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def main(case_path: str):
    schema = load_json(SCHEMA_PATH)
    instance = load_json(case_path)
    validator = Draft202012Validator(schema)
    errors = sorted(validator.iter_errors(instance), key=lambda e: e.path)
    if errors:
        print("Errores de validación:")
        for e in errors:
            print(f"- {'/'.join(map(str, e.path))}: {e.message}")
    else:
        print("✅ Case válido contra el schema.")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Uso: python src/validate_case.py data/processed/sample_case.json")
        sys.exit(1)
    main(sys.argv[1])
