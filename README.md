[JENKINS-26197](https://issues.jenkins-ci.org/browse/JENKINS-26197) - confirm JGit prunes stale remote tracking branches correctly

Shows a problem in the development version of git plugin 2.3.6.  If
the development version polls this repository, the polling job will
never stop building new copies of itself.

The 2.3.5 plugin does not have that problem (at least in my testing).