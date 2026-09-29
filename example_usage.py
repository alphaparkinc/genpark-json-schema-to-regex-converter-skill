from client import JSONSchemaToRegex

schema = {"type": "object", "properties": {"status": {"type": "string", "enum": ["ok", "err"]}}}
regex_pat = JSONSchemaToRegex.schema_to_regex(schema)
print("Compiled Regex:", regex_pat)
