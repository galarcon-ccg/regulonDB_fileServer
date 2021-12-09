from flask import Flask, send_file
from flask_cors import CORS
import pysftp
import os

app = Flask(__name__)
cors = CORS(app)

@app.route('/ht')
def index():
    return('hola mundo')

@app.route('/ht/download/<type>/<id>', methods=['GET'])
def dataset(type,format,id):
    cnopts = pysftp.CnOpts()
    cnopts.hostkeys = None
    localFilePath = "./cache/ht_collections_web/"+id+"_"+type+".gff3"
    if format == 'png':
      return send_file(localFilePath,mimetype='image/png')
    return send_file(localFilePath,mimetype='text/plaint')

@app.route('/ht/download/dataset/chip-seq/<type>/<format>/<id>', methods=['GET'])
def dataset(type,format,id):
    cnopts = pysftp.CnOpts()
    cnopts.hostkeys = None
    localFilePath = "./cache/coleccion_ChIP-Seq/"+id+"/"+id+"_"+type+"."+format
    if format == 'png':
      return send_file(localFilePath,mimetype='image/png')
    return send_file(localFilePath,mimetype='text/plaint')
        
@app.route('/ht/regulondb_files/<type>/<format>/<name>', methods=['GET'])
def regulonDB(type,format,name):
    cnopts = pysftp.CnOpts()
    cnopts.hostkeys = None
    localFilePath = "./cache/RegulonDBFiles/TF_bed/"+name+".bed"
    if format == 'png':
      return send_file(localFilePath,mimetype='image/png')
    return send_file(localFilePath,mimetype='text/plaint')
    
    """[summary]
with pysftp.Connection(host=myHostname, port=myPort, username=myUsername, password=myPassword, cnopts=cnopts) as sftp:
            print("Connection succesfully stablished ... ")
            # Define the file that you want to download from the remote directory
            remoteFilePath = '/var/sftp/uploads/ht-collections_v1.0/chip-seq-collection/'+id+'/'+id+'_peaks.bed'
            # Define the local path where the file will be saved
            localFilePath = './'+id+'_peaks.bed'
            sftp.get(remoteFilePath, localFilePath)
            return send_file(localFilePath,mimetype='text/plaint')
    """
    
