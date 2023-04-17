from paramiko import SSHClient
from scp import SCPClient
import pandas as pd

def downloadOpusFiles(path):
    batch_df = pd.read_csv(path)
    batch_ids = batch_df['batch_id'].values
    for batch in batch_ids:
        ssh = SSHClient()
        ssh.load_system_host_keys()
        ssh.connect('alphaspectral.cropnuts.com',username="opus", password ='8Qy08#uazSKv' )
        print("Downloading")
        scp = SCPClient(ssh.get_transport())

        scp.get(f"../../mnt/volume_lon1_01/spc_backup/batch_{batch}", recursive=True)

        scp.close()

downloadOpusFiles("./batch.csv")