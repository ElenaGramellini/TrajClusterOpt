import os
import math



#Define the parameter space
KINK1 = [0.1,0.2,0.3]
KINK2 = [1.2,1.5,1.7]
KINK3 = [1,3,5]
QUAL1 = [0.7,0.8,0.9]
QUAL2 = [1,3,5]


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
                    xmlName      = "xml/OptTracking_"+str(Config_Number)+".xml"
                    cp_fcl       = "cp OptTracking_LOLOL.xml " + xmlName 
                    print cp_fcl
                    os.system(cp_fcl)
                    sub_name     = "sed -i \'s/LOLOLO/"+ str(Config_Number) +"/g\' " + xmlName 
                    print sub_name
                    os.system(sub_name)
