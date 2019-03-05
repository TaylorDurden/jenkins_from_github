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
          git(url: 'git@github.com:TaylorDurden/jenkins_from_github.git', credentialsId: 'e34e997b899a9188a7f5c969ae3c9b62343421c2')
        }

      }
    }
    stage('build') {
      steps {
        sh 'sudo -H pip install -r requirements.txt'
      }
    }
    stage('run') {
      steps {
        sh 'python app.py'
      }
    }
  }
}