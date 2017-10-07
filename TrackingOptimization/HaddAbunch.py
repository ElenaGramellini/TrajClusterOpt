

import os
import math



#Define the parameter space
KINK1  = [0.1,0.2,0.3]
KINK2  = [1.2,1.5,1.7]
KINK3  = [1,3,5]
MODE   = [1,-1]
HITERR = [0.1,1.,2.]

 
for K1 in KINK1:
    for K2 in KINK2:
        for K3 in KINK3:
            for Q1 in MODE:
                for Q2 in HITERR:
                    Config_Number = (1+KINK1.index(K1))*10000 +  (1+KINK2.index(K2))*1000 +  (1+KINK3.index(K3))*100  +  (1+MODE.index(Q1))*10   + HITERR.index(Q2) 
                    fileNameEnd = "/pnfs/lariat/scratch/users/elenag/TrackingOPT/"+str(Config_Number)+"/ana_"+str(Config_Number)+".root"
                    print os.path.isfile(fileNameEnd)
                    if os.path.isfile(fileNameEnd):
                        continue
                    
                    hadd_cmd      = "hadd ana_"+str(Config_Number)+".root /pnfs/lariat/scratch/users/elenag/TrackingOPT/"+str(Config_Number)+"/v06_34_01/*_*/anaTree_*_histo.root"
                    print hadd_cmd
                    os.system(hadd_cmd)
#                    cp_cmd      = "cp ana_"+str(Config_Number)+".root /pnfs/lariat/scratch/users/elenag/TrackingOPT/"+str(Config_Number)+"/."
#                    print cp_cmd
#                    os.system(cp_cmd)
#                    rm_cmd = "rm ana_"+str(Config_Number)+".root"
#                    print rm_cmd
#                    os.system(rm_cmd)

