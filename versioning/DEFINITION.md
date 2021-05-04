# The Rapid Versioning System
The official document describing the rapid versioning system and how to apply it to OSS

---

## Summary
A version number is composed of up to four markers denoted `a.b.c.d` where all `a`, `b`, `c`, and `d` are integers greater than or equal to 0. The first version of every package (while in development) shall be `0.1.0`. The first stable version of every package shall be `1.0.0`. The rules for stable packages are listed below:

- `a` marks the MAJOR version
    - A value of 0 indicates that the package and all previous versions are not production ready
    - This value is incremented every time a large deprecation or major feature release occurs
- `b` marks the MINOR version
    - This value is incremented to reflect minor enhancements, critical bugfixes, or minor deprecations (contained deprecations—discussed later)
- `c` marks the PATCH version
    - This value is incremented to reflect small bugfixes and other changes that will not deprecate *anything* nor make many noticeable API changes
- `d` marks the UPDATE version
    - `d` is only used on nightly builds of some applications. `d` implies a possibly unstable or developing version of `a.b.c`. 
    - It should be incremented every time a change is made
    - These versions may be yanked as soon as the next PATCH, MINOR, or MAJOR update is released
    - `d` is not required and should not be specified on any stable version `a.b.c`

The rules for packages in development are very much the same:
- `a` marks the fact that the package is still in development
    - `a` should never exceed 1 while the package is still in development
    - As soon as `a` is 1, versions below 0 may be yanked
- `b` marks the MINOR version
    - This value is incremented to reflect any enhancements or deprecations and critical bugfixes
- `c` marks the PATCH version
    - This value is incremented to reflect small bugfixes and other changes that will not deprecate *anything* nor make many noticeable API changes
- `d` marks the UPDATE version
    - `d` is only used on nightly builds of some applications. `d` implies a possibly unstable or developing version of `0.b.c`.
    - On many developing packages, it may be preferable to merge this into `c` and increment the PATCH version instead since it is understood that the package is unstable
    - It should be incremented every time a change is made
    - These versions may be yanked as soon as the next PATCH, MINOR, or MAJOR update is released
    - `d` is not required and should not be specified on any stable version `0.b.c`

## Introduction
See [MOTIVATION.md](MOTIVATION.md).

## Directives
Many of these directives have been adopted from the original [Semantic Versioning directives](https://semver.org). Changes **have been made** to adopt these directives into the Rapid Versioning System. This content is licensed under the [CC 3.0 License](https://creativecommons.org/licenses/by/3.0/).

Note on language used:
> The key words “MUST”, “MUST NOT”, “REQUIRED”, “SHALL”, “SHALL NOT”, “SHOULD”, “SHOULD NOT”, “RECOMMENDED”, “MAY”, and “OPTIONAL” in this document are to be interpreted as described in RFC 2119.

(1) Software using Rapid Versioning MUST declare a public API. This API could be declared in the code itself or exist strictly in documentation. However it is done, it SHOULD be precise and comprehensive.

(2) A normal version number MUST take the form `a.b.c.d` where `.d` is optional and `a`, `b`, `c`, and `d` are non-negative integers, and MUST NOT contain leading zeros. `a` is the MAJOR version, `b` is the MINOR version, and `c` is the PATCH version. Optionally, `d` can be used to mark a possibly unstable UPDATE version. Each element MUST increase numerically. For instance: `1.9.0` → `1.10.0` → `1.11.0`.

(3) Once a versioned package has been released, the contents of that version MUST NOT be modified. Any modifications MUST be released as a new version.

(4) Major version zero (0.y.z) is for initial development. Anything MAY change at any time. The public API SHOULD NOT be considered stable.

(5) Version `1.0.0` defines the public API. The way in which the version number is incremented after this release is dependent on this public API and how it changes. After a version `1.0.0` has been published, the following rules apply:

(5.1) Patch version `c` (`a.b.C` \| `a` > 0) MUST be incremented to reflect small bugfixes and other changes that must not deprecate any valid dependents of this package. A *small* bugfix is defined as a backwards-compatible non-breaking API change that fixes a *contained* bug. A bug is *contained* if it affects only one part of the codebase and will not cause any valid dependent code to receive an error.

(6.1) Patch version `c` (`a.b.C` \| `a` = 0) MUST be incremented to reflect small bugfixes and other changes that must not deprecate any valid dependents of this package.

(5.2) Minor version `b` (`a.B.c` \| `a` > 0) MUST be incremented to reflect minor enhancements, critical bugfixes, or minor deprecations. A minor enhancement is a backwards-compatible enhancement that only modifies existing code or is simply a symbolic enhancement (i.e. one that makes it simpler to execute code that could have already been executed another way in the previous version of the package). A critical bugfix is one that fixes an *uncontained* bug or a non-backwards-compatible or breaking API change applied to a *contained* bug. An *uncontained* bug is a bug that is not *contained*—in other words, a bug that affects multiple parts of the codebase, can spread to other parts of the codebase, or will cause valid dependent code to receive an error. Similarly, a minor deprecation is one that is *contained*. Here, a *contained* deprecation MUST be confined to a certain part of the codebase meaning that no valid dependent code will need to be restructured—only have some parts removed or modified slightly.

(6.2) For minor version `b` (`a.B.c` \| `a` = 0), `b` MUST be incremented to reflect any enhancements or deprecations and critical bugfixes.

(5.3) Major version `a` (`A.b.c` \| `a` > 0) MUST be incremented every time a large deprecation or major feature release occurs. A large deprecation is one that is not a minor deprecation and is not *contained*. A major feature release is one that is not a minor enhancement—anything that is non-backwards-compatible and is not a symbolic enhancement.

(6.3) A pre-release version MAY be denoted by appending a hyphen and a series of dot separated identifiers immediately following the patch version. Identifiers MUST comprise only ASCII alphanumerics and hyphens [0-9 : A-Z : a-z]. Identifiers MUST NOT be empty if no `d` version is specified. Numeric identifiers MUST NOT include leading zeros. Pre-release versions have a lower precedence than the associated normal version. A pre-release version indicates that the version is unstable and might not satisfy the intended compatibility requirements as denoted by its associated normal version. Examples: 1.0.0-alpha, 1.0.0-alpha.1, 1.0.0-0.3.7, 1.0.0-x.7.z.92, 1.0.0-x-y-z.–.

(5.4) However, the optional update version `d` can also be used and appended to the version `a.b.c` as `a.b.c.D`. `d` MUST NOT be zero at any time. Update version `d` (`a.b.c.D` \| `a` > 0) MUST imply a possibly unstable or developing version of `a.b.c`. It SHOULD be incremented anytime such a change is made. These versions MAY be yanked as soon as the next PATCH, MINOR, or MAJOR update is released. `d` is not required and MUST NOT be specified on any stable version `a.b.c`.

(6.4) When `a` = 0, it MAY be preferable to merge this into `c` and increment the PATCH version instead since it is understood that the package is unstable.

(7) Build metadata MAY be denoted by appending a plus sign and a series of dot separated identifiers immediately following the patch or pre-release version. Identifiers MUST comprise only ASCII alphanumerics and hyphens [0-9 : A-Z : a-z]. Identifiers MUST NOT be empty. Build metadata MUST be ignored when determining version precedence. Thus two versions that differ only in the build metadata, have the same precedence. Examples: `1.0.0-alpha+001`, `1.0.0+20130313144700`, `1.0.0-beta+exp.sha.5114f85`, `1.0.0+21AF26D3—-117B344092BD`.

(8) Precedence refers to how versions are compared to each other when ordered.

(8.1) Precedence MUST be calculated by separating the version into MAJOR, MINOR, PATCH, UPDATE and pre-release identifiers in that order (Build metadata does not figure into precedence).

(8.2) Precedence is determined by the first difference when comparing each of these identifiers from left to right as follows: MAJOR, MINOR, PATCH, and UPDATE versions are always compared numerically.

(8.3) Example: `1.0.0` < `1.0.1` < `1.0.1.2` < `2.0.0`

(8.4) When MAJOR, MINOR, PATCH, and UPDATE are equal, a pre-release version has lower precedence than a normal version:

(8.5) Example: `1.0.0.0-alpha` < `1.0.0.0`

(8.6) Precedence for two pre-release versions with the same MAJOR, MINOR, PATCH, and UPDATE version MUST be determined by comparing each dot separated identifier from left to right until a difference is found as follows:

(8.7) `1.0.2.1.1.8.0` < `1.0.2.1.1.8.1`

(8.8) Identifiers consisting of only digits are compared numerically.

(8.9) Identifiers with letters or hyphens are compared lexically in ASCII sort order.

(8.10) Numeric identifiers always have **higher** precedence than non-numeric identifiers.

(8.11) A larger set of pre-release fields has a higher precedence than a smaller set, if all of the preceding identifiers are equal.

(8.12) Example: `1.0.0-alpha` < `1.0.0-alpha.beta` < `1.0.0-alpha.1` < `1.0.0-beta` < `1.0.0-beta.2` < `1.0.0-beta.11` < `1.0.0-rc.1` < `1.0.0`.

## Basic Grammar
A version in the form*
```
a.b.c[.d][—-X][-X][+X] (a = 0)
```

*`[foo]` is used to specify an optional argument

is a beta or pre-release of a package with MINOR version `b` and PATCH version `c`. `d` represents the UPDATE version if specified and `X` represents build metadata if specified.
```
a.b.c[.d][—-X][-X][+X] (a > 0)
```
is a stable version if `d` is not provided. Always, `a` is the MAJOR version, `b` is the MINOR version, and `c` is the PATCH version. If specified, `d` is the UPDATE version and the package is unstable. If specified, `X` is the build metadata.

## Putting it into Practice
Please see [practice.md](practice.md) for implementation details and different variants.