[JENKINS-29482](https://issues.jenkins-ci.org/browse/JENKINS-29482) - prune blocks history

The git plugin change in 2.4.1 to suppress some portion of BuildData
also broke the history display if stale branch pruning is enabled.
BuildData is a very challenging part of the plugin to modify without
causing some unexpected break.

This test uses the JENKINS-29482 branch for verification.
