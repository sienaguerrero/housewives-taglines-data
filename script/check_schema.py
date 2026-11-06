#!/usr/bin/env python3
# Usage: pip install jsonschema && python3 script/check_schema.py

import json
import sys
from pathlib import Path

from jsonschema.validators import validator_for

ROOT = Path(__file__).resolve().parent.parent
schema = json.loads((ROOT / "data" / "schema.json").read_text(encoding="utf-8"))
data_path = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "data" / "taglines.json"
data = json.loads(data_path.read_text(encoding="utf-8"))

Validator = validator_for(schema)
Validator.check_schema(schema)
validator = Validator(schema, format_checker=Validator.FORMAT_CHECKER)
errors = sorted(validator.iter_errors(data), key=lambda e: [str(p) for p in e.absolute_path])

for error in errors:
    where = "/".join(str(p) for p in error.absolute_path) or "(root)"
    print(f"  FAIL  {where}: {error.message}")
if errors:
    sys.exit(f"{len(errors)} error(s) against data/schema.json")
print("OK  taglines.json matches data/schema.json")
