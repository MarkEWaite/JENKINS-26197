#!groovy

@Library('globalPipelineLibraryMarkEWaiteModern@0c30065c158df07e55eeda283a7db3ff19bbfe01') // Checkout JENKINS-48061 SHA1 reference

import com.markwaite.Assert
import com.markwaite.Build

/* Only keep the 10 most recent builds. */
properties([[$class: 'BuildDiscarderProperty',
                strategy: [$class: 'LogRotator', numToKeepStr: '10']]])

def branch='master'

node {
  stage('Checkout') {
    // Need explicit clone of tags for assertion
    checkout([$class: 'GitSCM',
        branches: [[name: branch]],
        browser: [$class: 'GithubWeb', repoUrl: 'git@github.com:MarkEWaite/JENKINS-26197.git'],
        doGenerateSubmoduleConfigurations: false,
        extensions: [
            [$class: 'CloneOption', honorRefspec: true, noTags: false],
            [$class: 'LocalBranch', localBranch: branch]],
        gitTool: scm.gitTool,
        userRemoteConfigs: [[refspec: "+refs/heads/${branch}:refs/remotes/origin/${branch}", url: 'https://github.com/MarkEWaite/JENKINS-26197']]]
    )
  }

  stage('Build') {
    /* Call the ant build. */
    def my_step = new com.markwaite.Build()
    my_step.ant 'info'
  }

  stage('Verify') {
    def my_check = new com.markwaite.Assert()
    /* JENKINS-47496 reports that new tags are not built.  */
    my_check.logDoesNotContain('.*rev-parse.*JENKINS-32570-ran-1-for-.*', 'Missing tag reference')
  }
}
