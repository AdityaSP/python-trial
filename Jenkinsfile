node {
    
    stage('HelloWorld') {
       echo 'Hello World'
    }
    
    stage('download') {
        git 'https://github.com/AdityaSP/python-trial'
    }
    stage('linting') {
        bat '''D:\\sw\\python27\\Scripts\\pylint loganalysis.py > pylint.log
            exit 0'''
    }
    stage('archiving') {
        archiveArtifacts allowEmptyArchive: true, artifacts: '*'
    }
}
