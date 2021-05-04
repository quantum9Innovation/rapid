# Using the Rapid Versioning System in your Project
Implementing the Rapid Versioning System

---

## Why rapid works
Rapid works because it allows safe and easy dependency management, *just like semantic versioning*, **except** it makes the versioning more user-friendly. To understand how rapid can be used to facilitate dependency management, consider the following example:

```
C    (v1.0.0)
\-B     (v1.0.0)
  \-A     (v1.0.0)
```

where **Package A** is a dependency of **Package B** and **Package B** is a dependency of **Package C**. For brevity, we will refer to them as **A**, **B**, and **C**.

Now let's say **A** makes a patch update. **B** knows that their code will still work since the update *cannot* contain a deprecating change. Because of this, **B** can safely write:
```
1.0.0 <= A < 1.1.0
```
in their dependency file. And because **B** has no change, **C** also remains unaffected. Additionally, with this same logic, **C** can write
```
1.0.0 <= B <= 1.1.0
```
in their dependency files.

For this next example, let's say **A** makes a deprecating minor update and changes to `1.1.0`. Since minor updates only have *contained* deprecations, **B** does *not* need to restructure their code, but rather just needs to issue a minor bugfix. This means **B** simply needs to issue a patch release `1.0.1`. This, in turn, means that **B** is still a valid dependency of **C**, so **C** remains unaffected—without having to worry about the nasty dependency of a dependency update problem.

In fact, the only type of release that would require **C** to issue a new release would be a major deprecating release from **A**, which would trigger a minor update of **B**, which would in turn trigger a patch update of **C**. And the path ends there! Any further dependencies are completely unaffected.

## Compatibility with other versioning systems

### Semantic Versioning
While Rapid Versioning offers undeniable benefits over Semantic Versioning, there are still *many*, *many* projects that use semantic versioning. And that's not a bad thing—because Rapid Versioning is for the most part compatible with semantic versioning. For one, Rapid Versioning keeps the same MAJOR.MINOR.PATCH versioning scheme as Sematic Versioning, only with a few twists on what is classified as 'MAJOR,' 'MINOR,' and 'PATCH.' In fact, these two versioning schemes are so similar that you might even consider Rapid Versioning a "specification" of Semantic Versioning, which tightens up some of the vague guidelines of Semantic Versioning.

### GNU-based Versioning Schemes
GNU-based versioning schemes of the form `current.revision.age` also integrate effortlessly with Rapid Versioning. The `current` version number roughly corresponds to the MAJOR and MINOR versions while the `revision` corresponds to the PATCH version number. `age` is not recorded in Rapid Versioning because of its uselessness to the end user of a package—it says nothing about what new features, issues, or revisions have been issued.

## Python: PEP 440
See the full directive [here](https://www.python.org/dev/peps/pep-0440/). Rapid versioning is **fully** compatible with this scheme. See [Usage](#usage) for details on how to list compatible releases.

## Usage

### For Using a Project that follows Rapid Versioning

Let's say you're using a dependency `PACKAGE` that has been tested in your code for version `a.b.c`. In your dependency file, be it a `requirements.txt` in Python or a `Gemfile` in Ruby, put the equivalent statement to indicate compatability with a package you're using*:
```
a.b.0 <= PACKAGE < a.<b+1>.0
```

*The notation `<formula>` is used to denote an expression within the version number

Make sure to replace `PACKAGE` with your dependency's version number and follow the appropriate syntax for the file you're using (the snippet above is simply psuedocode).

The semi-open window open at `a.b.0` and closed at `a.<b+1>.0` is the range of *full compatibility*. Any dependency with a version in this range will be fully supported by your package—no deprecations, internal restructuring, etc.

However, Rapid Versioning also offers *partial compatibility* in the semi-open window open at `a.0.0` and closed at `<a+1>.0.0`. Partial compatibility means that there is a *possibility* of deprecation—however, such deprecations **will not** require a restructuring of your code, the dependent. The worst case scenario would entail a simple patch update that would remove or modify existing code. In the case that there is not a deprecation, then all code should work perfectly although you may be missing out on new features.

## For Showing that you Follow Rapid Versioning
To show that you follow Rapid Versioning, include the following badge on one line in a Markdown document (e.g. a README, CONTRIBUTING guidelines, etc.):
```markdown
[![versioning: rapid](https://shields.mitmproxy.org/badge/versioning-rapid-blue)]
(https://quantum9innovation.github.io/rapid/versioning/definition)
```
[![versioning: rapid](https://shields.mitmproxy.org/badge/versioning-rapid-blue)](https://quantum9innovation.github.io/rapid/versioning/definition)

## Further Reading
Please see [our recommendations](recommendations.md) (optional) for using Rapid Versioning in your project.

