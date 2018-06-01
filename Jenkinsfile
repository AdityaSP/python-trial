node {
    
    stage('HelloWorld') {
        echo "picking up python from ${pypath}"
    }
    
    stage('download') {
        git 'https://github.com/AdityaSP/python-trial'
    }
    stage('linting') {
        bat '''${pypath}\\Scripts\\pylint loganalysis.py > pylint.log
            exit 0'''
    }
    stage('archiving') {
        archiveArtifacts allowEmptyArchive: true, artifacts: '*'
    }
}
