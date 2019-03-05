pipeline {
  agent {
    node {
      label 'dev'
    }

  }
  stages {
    stage('git') {
      steps {
        dir(path: '/home/wolverine/jenkins_from_github') {
          git(url: 'git@github.com:TaylorDurden/jenkins_from_github.git', credentialsId: '9ac89121-fe19-49a2-86be-7ae13a6e894e')
        }

      }
    }
    stage('build') {
      steps {
        sh 'cd test_git && sudo -H pip install -r requirements.txt'
      }
    }
    stage('run') {
      steps {
        sh 'cd test_git && python app.py'
      }
    }
  }
}