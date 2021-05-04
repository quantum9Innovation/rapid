# Rapid Versioning System
The sane alternative to semantic versioning

---
The rapid versioning system is currently being developed by [**@quantum9innovation**](https://github.com/quantum9innovation) to be a better alternative to semantic versioning.

## Why not semantic versioning?
The rapid versioning system is best described as "the sane alternative to semantic versioning." The problem with semantic versioning is that in any given version `a.b.c`, `b` is frequently overused because it encompasses almost any update that's not a bugfix or deprecation. In fact, if you follow good programming practice and *never* deprecate a feature, semantic versioning will mean `a` never exceeds 1! To understand why this is important, see [motivation.md](motivation.md).

## What is rapid versioning then?
Rapid versioning follows the same syntax as semantic versioning (`a.b.c`), but instead uses `a` to denote large updates (not just deprecations), `b` to denote minor updates (e.g. small features, large bugfixes), and `c` to denote patches (not just bugfixes though—this can encompass anything from fixing typos to reformatting code). Read more about it [here](definition.md).

## I've read the definition. How do I put it into practice for my project?
Check out [practice.md](practice.md).

## How can I show that my project uses rapid versioning?
Use this badge in Markdown:
```markdown
[![versioning: rapid](https://shields.mitmproxy.org/badge/versioning-rapid-blue)]
(https://quantum9innovation.github.io/rapid/versioning/definition)
```
[![versioning: rapid](https://shields.mitmproxy.org/badge/versioning-rapid-blue)](https://quantum9innovation.github.io/rapid/versioning/definition)

You can insert it as one line just after your README title (preferable) or link to it at the bottom of your README or CONTRIBUTING documents

## Have suggestions?
Add them to this README or one of its respective links and submit a PR. Contributions are always welcome.