import os
import math



#Define the parameter space
KINK1 = [0.1,0.2,0.3]
KINK2 = [1.2,1.5,1.7]
KINK3 = [1,3,5]
QUAL1 = [0.7,0.8,0.9]
QUAL2 = [1,3,5]
 
for K1 in KINK1:
    for K2 in KINK2:
        for K3 in KINK3:
            for Q1 in QUAL1:
                for Q2 in QUAL2:
                    Config_Number = (1+KINK1.index(K1))*10000 +  (1+KINK2.index(K2))*1000 +  (1+KINK3.index(K3))*100  +  (1+QUAL1.index(Q1))*10   + QUAL2.index(Q2) 
                    xmlName      = "list/genFileList"+str(Config_Number)+".list"
                    cp_fcl       = "cp /lariat/data/users/elenag/trackingOptimization/genFileList.list /lariat/data/users/elenag/trackingOptimization/" + xmlName 
                    os.system(cp_fcl)


#                lar_cmd = "lar -c TOFReco_"+str(Config_Number)+".fcl /lariat/data/users/elenag/v06_13_00/LowTOFEff/allInterestingFiles/WCTrackFilter.root &> fatlog"+str(Config_Number)+".log &"
#                print lar_cmd
#                os.system(lar_cmd)
