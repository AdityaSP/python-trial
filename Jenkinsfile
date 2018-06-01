def pnodes = [:]
pnodes['run_on_slave'] = {
    node('python-node') {
        
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
}

pnodes['run_on_master'] = {
    node('master') {
        
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
}

parallel pnodes
