[JENKINS-26197](https://issues.jenkins-ci.org/browse/JENKINS-26197) - confirm JGit prunes stale remote tracking branches correctly

Shows a problem in the development version of git plugin 2.3.6.  If
the development version polls this repository, the polling job will
never stop building new copies of itself.

The 2.3.5 plugin does not have that problem (at least in my testing).

[JENKINS-30371](https://issues.jenkins-ci.org/browse/JENKINS-30371)
reports that JGit was unable to create a symbolic link even on systems
(like Linux and FreeBSD) where the file system natively supports
symbolic links.

This repository includes two directories, one named "real" and the
other named "symbolic".  Entries in the "symbolic" directory either
point to a file or directory in the "real" directory, or they point to
a non-existent file.

The test job modifies the symbolic/file content, then uses the text-finder
plugin to confirm the real/file content was also changed.

[JENKINS-45447](https://issues.jenkins-ci.org/browse/JENKINS-45447)
and [JENKINS-47169](https://issues.jenkins-ci.org/browse/JENKINS-47169)
report that rev-parse is called for every tag on every build and every
poll, even when the tags do not match the branch name specification.
