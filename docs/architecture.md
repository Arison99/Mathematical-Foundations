# Repository architecture

## Organization

Mathematical concepts are the primary units of organization. `mathematics/<domain>/<concept>/README.md` is the canonical source for definitions, assumptions, derivations, examples, pseudocode, correctness notes, and complexity. Domain READMEs introduce scope and link to concept pages.

Language-specific code belongs in `implementations/<language>/<domain>/<concept>/` (or another consistently documented language-native layout). It links to the canonical concept page and contains only language-specific usage, runtime requirements, and limitations. Do not duplicate theory across implementations. Add language directories when there is real code to put there.

Shared fixtures and cross-language conformance material belong under `tests/`; tests tightly coupled to a language implementation may live alongside it. `docs/` contains conventions that apply across concepts and languages. This separation lets domains and languages grow independently while concepts remain the stable link between them.

## Status and maintenance

An implementation is available only when its files and instructions exist. A language directory alone does not establish support. Update affected navigation and status claims with structural changes. Keep planned work visibly distinct from completed documentation or code. Do not create nested Git repositories.

This describes the intended organization; the current repository has not yet created these content directories.
