import numpy as np
import h5py



def write_to_hdf5(array_of_interest,file):





if __name__ == '__main__':

    # Example
    joint_positions ={
	"timestamp": 0.0,
	"joint_1" : 0.0, 
	"joint_2" : 0.0, 
	"joint_3" : 0.0, 
	"joint_4" : 0.0, 
	"joint_5" : 0.0, 
	"joint_6" : 0.0, 
	"joint_7" : 0.0, 
	"joint_8" : 0.0, 
	} 
    
    # Convert and write JSON object to file
    with open("/run/user/1000/gvfs/sftp:host=billys-macbook-pro-5.local/Users/billymazotti/Documents/UofM/StirlingGroup/OSAM_HRI/OSAM-Project/test_connection.json", "w") as outfile: 
        json.dump(joint_positions, outfile,indent = 4)