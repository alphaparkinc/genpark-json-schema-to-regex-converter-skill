"""JSON Schema to Regex Converter.
100% Python Standard Library.
"""

import re

class JSONSchemaToRegex:
    """Translates simple JSON schemas into regex patterns for constrained decoding."""
    @staticmethod
    def schema_to_regex(schema: dict) -> str:
        stype = schema.get("type")
        if stype == "string":
            if "enum" in schema:
                options = "|".join(re.escape(opt) for opt in schema["enum"])
                return f'"({options})"'
            return r'"[^"]*"'
        elif stype == "integer":
            return r'-?\d+'
        elif stype == "number":
            return r'-?\d+(\.\d+)?'
        elif stype == "boolean":
            return r'(true|false)'
        elif stype == "object":
            props = schema.get("properties", {})
            parts = []
            for k, prop_schema in props.items():
                val_regex = JSONSchemaToRegex.schema_to_regex(prop_schema)
                parts.append(f'"{re.escape(k)}":\s*{val_regex}')
            body = r',\s*'.join(parts)
            return r'\{\s*' + body + r'\s*\}'
        return r'.*'
