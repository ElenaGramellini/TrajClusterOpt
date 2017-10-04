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
                    fclName      = "fcl/TrjClusterBaseLArIAT_"+str(Config_Number)+".fcl"
                    cp_fcl       = "cp TrjClusterBaseLArIAT_LOLOLO.fcl " + fclName 
                    print cp_fcl
                    os.system(cp_fcl)
                    sub_name     = "sed -i \'s/LOLOLO/"+ str(Config_Number) +"/g\' " + fclName 
                    print sub_name
                    os.system(sub_name)
                    sub_KINK1   = "sed -i \'s/KINK1/"+ str(K1) +"/g\' " + fclName 
                    sub_KINK2   = "sed -i \'s/KINK2/"+ str(K2) +"/g\' " + fclName 
                    sub_KINK3   = "sed -i \'s/KINK3/"+ str(K3) +"/g\' " + fclName 
                    sub_MODE   = "sed -i \'s/MODE/"+ str(Q1) +"/g\' " + fclName 
                    sub_HITERR   = "sed -i \'s/HITERR/"+ str(Q2) +"/g\' " + fclName 
                    print sub_KINK1
                    os.system(sub_KINK1)
                    print sub_KINK2   
                    os.system(sub_KINK2)
                    print sub_KINK3   
                    os.system(sub_KINK3)
                    print sub_MODE
                    os.system(sub_MODE)
                    print sub_HITERR
                    os.system(sub_HITERR)


