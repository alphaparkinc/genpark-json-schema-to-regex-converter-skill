# genpark-json-schema-to-regex-converter-skill

Compiles structured JSON Schemas into equivalent regular expressions for logit-constrained decoding.

## Architecture

```mermaid
flowchart LR
    Schema[OpenAPI / JSON Schema] --> Compiler[Schema-to-Regex Compiler]
    Compiler --> Regex[Deterministic Regex Pattern]
    Regex --> Tokenizer[Regex Constrained Sampler]
```

## Features
- **Enum Support**: Exact branch constraints for enum fields.
- **Pure Python**: 100% standard library.
