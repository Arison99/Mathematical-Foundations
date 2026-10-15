# Documentation standard

## Documentation hierarchy

- **Root README:** project identity, current status, navigation, and contribution entry points.
- **Domain README:** scope, prerequisites, and links to its concepts.
- **Concept README:** definition, intuition, notation, assumptions, worked examples, algorithm or pseudocode, complexity, correctness notes, references, and available implementations.
- **Implementation README, when useful:** link to the canonical concept and explain language-specific usage, runtime requirements, execution commands, numeric limitations, and tests.
- **Shared standards:** architecture, pseudocode, style, and contribution conventions in `docs/` and the root contribution guide.

## Keeping documentation accurate

- Links must resolve to existing files; update references when files move.
- Describe implementation and language status from repository contents, not directory names.
- Verify commands before presenting them as executable. Mark unverified snippets as examples and future commands as planned.
- Label planned work separately from completed work.
- Every implementation must link to its canonical mathematical documentation.
- Link to repeated explanations rather than copying them.
- Update relevant READMEs when structure, behavior, or implementation status changes.
- Treat broken links and inaccurate status statements as documentation defects.

## Review checklist

- [ ] Are definitions, assumptions, notation, and references clear and accurate?
- [ ] Does each concept have one canonical mathematical page?
- [ ] Do implementation and status claims match files that exist?
- [ ] Do relative links and image references resolve?
- [ ] Are commands verified, or clearly labeled as examples or planned?
- [ ] Are complexity and correctness statements supported and scoped to stated assumptions?
- [ ] Were related navigation pages updated without duplicating the explanation?
