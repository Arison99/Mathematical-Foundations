# Mathematical Foundations

An open-source learning project connecting mathematical theory, language-independent pseudocode, algorithmic reasoning, and implementations in multiple programming languages. The first concept, the greatest common divisor, now includes mathematical documentation and Python and C++ implementations with tests.

## Contents

- [Purpose and principles](#purpose-and-principles)
- [Topics](#topics)
- [Language status](#language-status)
- [Repository structure](#repository-structure)
- [Learning workflow](#learning-workflow)
- [Example: Euclidean algorithm](#example-euclidean-algorithm)
- [Testing and verification](#testing-and-verification)
- [Getting started](#getting-started)
- [Contributing](#contributing)
- [Roadmap](#roadmap)
- [License and acknowledgements](#license-and-acknowledgements)

## Purpose and principles

Mathematics gives algorithm designers tools to describe problems precisely, prove that solutions work, and reason about their resource costs. These skills support competitive programming and reliable software engineering, where correctness and efficiency matter as much as code that runs.

The project aims to make those connections understandable and reusable. Contributions should prioritize:

- **Mathematical correctness:** state definitions, assumptions, and reasoning accurately.
- **Clarity:** explain notation and give readers enough context to follow an idea.
- **Reproducibility:** make examples and verification instructions concrete and repeatable.
- **Language independence:** keep mathematical explanations and pseudocode separate from language-specific details.
- **Maintainability:** use canonical concept documentation, consistent structure, and honest status descriptions.

## Topics

Topics with documentation are linked; the others remain planned.

- Discrete mathematics and logic — planned
- [Number theory](mathematics/number-theory/README.md) — includes the [GCD concept](mathematics/number-theory/gcd/README.md)
- Linear algebra and matrices — planned
- Algebra and polynomials — planned
- Combinatorics, including Stirling numbers — planned
- Probability and statistics — planned
- Recurrence relations and generating functions — planned
- Numerical methods and computational mathematics — planned

## Language status

Python and C++ currently have a GCD implementation and tests; see the [concept page](mathematics/number-theory/gcd/README.md) for commands and limitations. No other language implementations are present. A language should be listed as implemented only when its code, usage instructions, and verification expectations are available.

## Repository structure

The repository contains project and governance documents, shared standards, a number-theory concept, and Python and C++ implementations. The following layout shows the main current files and intended content areas:

```text
.
├── README.md                 # Project overview and navigation
├── CONTRIBUTING.md           # Contribution process
├── CODE_OF_CONDUCT.md        # Community expectations
├── SECURITY.md               # Vulnerability reporting
├── CHANGELOG.md              # Meaningful project changes
├── LICENSE                   # Existing GNU GPL version 3 license
├── docs/                     # Shared architecture and writing standards
│   ├── architecture.md
│   ├── documentation-standard.md
│   ├── pseudocode-standard.md
│   ├── roadmap.md
│   └── style-guide.md
├── mathematics/number-theory/ # Canonical GCD theory, examples, and proof worksheet
├── implementations/python/   # GCD implementation and unit tests
├── implementations/cpp/      # GCD implementation and standalone test
└── tests/                    # Reserved for future shared conformance materials
```

Each concept belongs in one canonical document under `mathematics/`. Implementations live under `implementations/<language>/` and refer back to that concept, avoiding repeated mathematical explanations. Tests and shared fixtures belong under `tests/`; language-specific tests may live beside their implementation when appropriate. No empty placeholder directories are required.

## Learning workflow

Work through a concept from its mathematical definition and assumptions to intuition and worked examples, then language-independent pseudocode, implementation, tests, correctness notes, and complexity analysis. The concept document remains the source of truth for the mathematics; implementation pages explain language-specific usage and limitations.

## Example: Euclidean algorithm

For integers `a` and `b`, with `a ≥ 0` and `b ≥ 0`, the Euclidean algorithm uses the fact that `gcd(a, b) = gcd(b, a mod b)` while `b > 0`. It repeatedly replaces `(a, b)` with `(b, a mod b)`; when `b = 0`, `a` is the greatest common divisor. For `(48, 18)`, the successive pairs are `(48, 18)`, `(18, 12)`, `(12, 6)`, and `(6, 0)`, so the result is `6`.

This calculation illustrates the mathematical reduction; it is not a substitute for the open proof worksheet. The [GCD concept page](mathematics/number-theory/gcd/README.md) links to the theory, implementations, and tests. Its documented convention covers negative integers by magnitude and defines `gcd(0, 0) = 0` for computation.

## Testing and verification

The GCD has Python unit tests and a standalone C++ assertion-based test. From the repository root, run the Python tests with `python -m unittest discover -s implementations/python/number-theory/gcd -p "test_*.py"`. Compile and run the C++ test with `g++ -std=c++17 -Wall -Wextra -pedantic implementations/cpp/number-theory/gcd/test_gcd.cpp -o gcd-test.exe; .\\gcd-test.exe` in PowerShell (remove the generated executable afterward). These commands were run successfully in this environment. There is not yet a shared cross-language conformance harness.

## Getting started

Clone or download the repository and read this overview. No package installation is needed for the standard-library Python code or standalone C++ test. The GCD page documents how to run each test. Browse the files with your editor or use Git to inspect changes:

```sh
git status --short
git log --oneline
```

These commands inspect repository history and working-tree status; they do not build or test code.

## Contributing

Before proposing a topic or implementation, check the existing concept documentation to avoid duplication. New concepts should include definitions, assumptions, notation, examples, pseudocode, correctness reasoning, complexity, and links to available implementations. New implementations should point to their canonical concept page and document execution requirements and tests. See [CONTRIBUTING.md](CONTRIBUTING.md) for the contribution process and [docs/documentation-standard.md](docs/documentation-standard.md) for the documentation checklist.

## Roadmap

The first mathematical concept and Python and C++ implementations are in place. Future work includes independent completion of the GCD proof worksheet, additional researched number-theory concepts, and language implementations selected by contributors. See the [roadmap](docs/roadmap.md) for planned work.

## License and acknowledgements

This repository includes the [GNU General Public License, version 3](LICENSE). Contributions are welcome; consult the license text for its terms. Acknowledgements and source references should be credited in the relevant concept documentation and collected here as the project develops. The GCD introduction is a standard mathematical topic; no external source or contributor is specifically credited for its documentation.
