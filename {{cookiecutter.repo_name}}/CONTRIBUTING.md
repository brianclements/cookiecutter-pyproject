# Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

## Types of Contributions

### Report Bugs
Report bugs at https://github.com/{{cookiecutter.github_username}}/{{
cookiecutter.repo_name}}/issues.

If you are reporting a bug, please include:

* Your operating system name and version.
* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.

### Fix Bugs
Look through the GitHub issues for bugs. Anything tagged with "bug"
is open to whoever wants to implement it.

### Implement Features
Look through the GitHub issues for features. Anything tagged with "feature"
is open to whoever wants to implement it.

### Write Documentation
{{cookiecutter.project_name}} could always use more documentation, whether as
part of the official {{cookiecutter.project_name}} docs, in docstrings, or even
on the web in blog posts, articles, and such.

### Submit Feedback
The best way to send feedback is to file an issue at https://github.com/{{
cookiecutter.github_username}}/{{cookiecutter.repo_name}}/issues.

If you are proposing a feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.
* Remember that this is a volunteer-driven project, and that contributions
  are welcome

## Code Guidelines
Please:

* Obey [PEP 8][pep8] and [PEP 257][pep257].
* Write [good commit messages][goodcommits].
* For small items and fixes, [squash][sqashcommits] your commits, i.e. make your pull
  requests just one commit.
* *Always* add tests and docs for your code.
* Use [Semantic versioning][semvar].
* Use appropriate branching strategy:
    * [GitHub Flow][gitflow] for small projects.
    * [Vincent Driessen's][gitbranching] branching model for large projects.
* Add yourself to the [AUTHORS](AUTHORS.md) file in an alphabetical order.

## Getting Started
* Make sure you have a [GitHub account][github].
* Submit a ticket for your issue, assuming one does not already exist.
    * Clearly describe the issue including steps to reproduce when it is a bug.
    * Make sure you fill in the earliest version that you know has the issue.
* Fork the repository on GitHub.
* Clone the repository onto your local machine:

    `git clone https://github.com/username/project.git`

## Making Changes

### Small Projects
The branching strategy for small projects is inspired by GitHub's own
[GitHub Flow][gitflow]:

* Make a descriptively named topic branch off of the `master` branch.

    `git branch my_contribution master`

    Then checkout with:

    `git checkout my_contribution`
    
    Or all at once:

    `git checkout -b my_contribution master`

### Large Projects
For larger projects, inspiration is from Vincent Driessen's [branching
model][gitbranching].

* Make a sub-topic branch based on the `develop` topic-branch. So you would
  prefix your topic branch with "develop":

    `git checkout -b develop/my_contribution master`

* If other supporting branches are present, use the appropriate sub-topic
  branch as your prefix:

    `git checkout -b feature/my_contribution develop`

    or:

    `git checkout -b hotfix/my_contribution master`

    etc.

* If you are working on a particular issue, include that number in your topic
  branch:

    `git checkout -b develop/123-fixing-an-issue develop`

### For All Projects
* Please avoid working directly on the "master" branch.
* Make commits of logical units.
* Check for unnecessary whitespace with `git diff --check` before committing.
* Please use spaces for all indentation and alignment, _no tabs_.
* Make sure your commit messages are in the [proper format][goodcommits]:

```
    (#99999) Make the example in CONTRIBUTING imperative and concrete

    Without this patch applied the example commit message in the CONTRIBUTING
    document is not a concrete example. This is a problem because the
    contributor is left to imagine what the commit message should look like
    based on a description rather than an example. This patch fixes the
    problem by making the example concrete and imperative.

    The first line is a real life imperative statement with a ticket number
    from our issue tracker. The body describes the behavior without the patch,
    why this is a problem, and how the patch fixes the problem when applied.
```

* Make sure you have added the necessary tests for your changes.
* Run _all_ the tests to assure nothing else was accidentally broken:

    `$ python setup.py test`

### Trivial Documentation Changes
For changes of a trivial nature to comments and documentation, it is not
always necessary to create a new ticket. In this case, it is
appropriate to start the first line of a commit with '(doc)' instead of
a ticket number:

```
    (doc) Add documentation commit example to CONTRIBUTING

    There is no example for contributing a documentation commit
    to the repository. This is a problem because the contributor
    is left to assume how a commit of this nature may appear.

    The first line is a real life imperative statement with '(doc)' in
    place of what would have been the ticket number in a 
    non-documentation related commit. The body describes the nature of
    the new documentation or comments added.
```

## Submitting Changes
Before submitting, make sure you have reviewed the [standard GitHub
workflow][git-workflow] and understand the difference between your fork (origin) and
repository from which you forked from (upstream).

* [Squash][sqashcommits] your commits if needed first.

* [Push][github-push] your changes to a topic branch in your fork of the repository:

    `git push origin develop/my_contribution`

* Submit a [pull request][github-pr] to the upstream repository.

## Versioning Policy
This project supports exactly one stable release at any given time and follows
the [Semantic Versioning][semvar] for its releases:
`(Major).(Minor).(Patch)`.

* **Major version**: Whenever there is something significant or any
    backwards-incompatible changes are introduced.
* **Minor version**: When new backwards-compatible functionality is introduced,
    a minor feature is introduced, or when a set of smaller features are
    rolled out.
* **Patch number**: When backwards compatible bug fixes are introduced that fix
    incorrect behavior.

The current stable release will receive security patches and bug fixes
(eg. `5.0` -> `5.0.1`).  Feature releases will mark the next supported stable
release where the minor version is increased numerically by increments of one
(eg. `5.0 -> 5.1`).

## Additional Resources
* [GitHub documentation][github-help]
* [Git documentation][git-doc]

Thank you for your involvement!
[pep8]: http://www.python.org/dev/peps/pep-0008
[pep257]: http://www.python.org/dev/peps/pep-0257
[goodcommits]: http://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html
[sqashcommits]: http://gitready.com/advanced/2009/02/10/squashing-commits-with-rebase.html 
[semvar]: http://semver.org
[gitbranching]: http://nvie.com/posts/a-successful-git-branching-model
[gitflow]: http://scottchacon.com/2011/08/31/github-flow.html
[github]: https://github.com/signup/free
[github-push]: https://help.github.com/articles/pushing-to-a-remote 
[github-pr]: https://help.github.com/articles/using-pull-requests 
[github-help]: http://help.github.com
[git-doc]: http://git-scm.com/documentation 
[git-workflow]: http://stackoverflow.com/q/9257533/2607578
