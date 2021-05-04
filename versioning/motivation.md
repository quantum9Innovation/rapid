# The motivation behind the Rapid Versioning System
In other words, why you need to stop using semantic versioning and embrace its saner equivalent

---
Semantic versioning works great for many projects. It provides a clear, concise framework for marking different versions of software or other works so that users can understand just by looking at a version number what they've missed.

The problem, however, is that semantic versioning with the form `a.b.c` relies too heavily on the `b` marker to indicate new versions. According to the semantic versioning document, `b` 

> MUST be incremented if new, backwards compatible functionality is introduced to the public API. It MUST be incremented if any public API functionality is marked as deprecated. It MAY be incremented if substantial new functionality or improvements are introduced within the private code. It MAY include patch level changes. Patch version MUST be reset to 0 when minor version is incremented.

The issue here is that `b` is used for too many things. It's used to mark backwards-compatible functionality, deprecation, new functionality, improvements on the code, and sometimes patch-level changes.

On the other hand, according to semantic versioning, the marker `a` (for major releases)

> MUST be incremented if any backwards incompatible changes are introduced to the public API. It MAY also include minor and patch level changes. Patch and minor version MUST be reset to 0 when major version is incremented.

As you can see, there is too much overlap with `b` since both are used to mark patch and minor updates. Most packages just use the first definition to increment `a` which means `a` is *only* updated to mark deprecating changes.

So how do we fix these problems? We need a versioning system that addresses the following issues:
- Addresses the dependency management problem
- Provides clear indicators of deprecation
- Clearly distinguishes between *major* and *minor* enhancements
- Correctly determines whether a bugfix is critical or not and which marker should be used to address it
- Does not overuse one marker over other markers

And from this, rapid versioning was born. To understand how rapid versioning works and how it solves this problem, continue reading [here](definition.md).
