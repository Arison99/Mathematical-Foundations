# Contributing

Contributions that improve mathematical clarity and reproducibility are welcome. Before starting substantial work, open an issue or discussion describing the concept or change so its scope and canonical location can be agreed. Do not add an implementation without its mathematical concept documentation.

## Proposing a concept

1. Check `mathematics/` and the roadmap for existing or planned coverage.
2. Propose the scope, prerequisites, definitions, and references.
3. Place accepted documentation under the relevant domain, with one canonical README per concept.
4. Include notation, assumptions, worked examples, language-independent pseudocode, correctness reasoning, complexity, and links to available implementations. Do not present an unverified claim as a proof.

## Adding pseudocode or an implementation

Pseudocode belongs with the canonical concept explanation and follows [the pseudocode standard](docs/pseudocode-standard.md). Put language-specific code under `implementations/<language>/`, organized by concept, and link to the canonical mathematics rather than copying it. Document runtime requirements, commands, numeric limitations, and tests in a nearby README when needed. Do not claim language support until code and its instructions are present.

## Tests and review

Add tests appropriate to the implementation and edge cases stated by the concept. Shared fixtures and cross-language conformance material belong in `tests/`. Report commands actually run and their results; distinguish examples from verified commands. Review the [documentation checklist](docs/documentation-standard.md) and [style guide](docs/style-guide.md), check relative links, and update affected READMEs when structure or status changes.
