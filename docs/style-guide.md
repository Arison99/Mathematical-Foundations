# Style guide

- Use lowercase kebab-case for domain and concept directory names; use descriptive names that match the mathematics.
- Keep one canonical concept README under `mathematics/`. Link to it from implementations and navigation pages.
- Use headings in a logical hierarchy, define notation before relying on it, and label assumptions and planned work explicitly.
- Prefer concise explanations, meaningful examples, and comments that explain intent or non-obvious constraints.
- Follow the conventions and formatters of each implementation language when they are adopted. Document commands and runtime requirements beside the relevant code.
- Put shared fixtures and conformance requirements under `tests/`; keep language-specific tests with their implementation when appropriate.
- Update links, status statements, and relevant READMEs in the same change as structural or implementation changes.

See the [pseudocode standard](pseudocode-standard.md) and [documentation standard](documentation-standard.md) for more specific requirements.
