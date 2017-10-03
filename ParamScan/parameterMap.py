'''
Scope: reduce the number of optimization paramters by understanding which ones are relevant to the LArIAT XS analysis.
TrajClusterAlg has 20+ parameters -- a blind map optimization is simply not doable from a computation stand point.

Starting from the default parameter set (par), this code produces a series of .fcl files where only 1 parameter at the time is changed.
This new value for the parameter is drawn from the altPar list. 

The following is the mapping from parameter names to default values
physics.producers.trajcluster.TrajClusterAlg.MinPts          : [PAR0, PAR1]          # [5,5]    
physics.producers.trajcluster.TrajClusterAlg.MinPtsFit       : [PAR2, PAR3]          # [4,4]             
physics.producers.trajcluster.TrajClusterAlg.MinMCSMom       : [PAR4, PAR5]          # [0,0]    
physics.producers.trajcluster.TrajClusterAlg.MaxVertexTrajSep: [PAR6, PAR7]          # [4,4]
physics.producers.trajcluster.TrajClusterAlg.ChargeCuts      : [PAR8, PAR9, PAR10]   # [4, 0.15, 0.25]
physics.producers.trajcluster.TrajClusterAlg.KinkCuts        : [PAR11, PAR12, PAR13] # [ 0.2, 1.5, 3 ]  
physics.producers.trajcluster.TrajClusterAlg.QualityCuts     : [PAR14, PAR15]        # [0.8, 3.]
physics.producers.trajcluster.TrajClusterAlg.HitErrFac       : PAR16                 # 1.4   
physics.producers.trajcluster.TrajClusterAlg.Mode            : PAR17                 # 1  
physics.producers.trajcluster.TrajClusterAlg.SkipAlgs        : [ "ChkStop", "ChkAllStop", "EndMerge" ]
'''


import re, copy
import os
import math



par     = [ 5, 5, 4, 4, 0,  0, 4, 4, 4, 0.15, 0.25,  0.2, 1.5, 3 , 0.8, 3., 1.4 , 1  ]
altPar  = [ 4, 6, 3, 5, 1,  1, 3, 5, 6, 0.25, 0.15, 0.05, 3.0, 1 , 0.5, 1., 0.1 , -1 ]

keys = []
for x in xrange(len(par)):
    keys.append("PAR"+str(x))




for i in xrange(len(par)):
    fclName      = "TrjClusterBaseLArIAT_PAR"+str(i)+".fcl"
    cp_fcl       = "cp templates/TrjClusterBaseLArIAT_TEMPLATE.fcl " + fclName
    print cp_fcl
    os.system(cp_fcl)

    currentPar = copy.copy(par)
    currentPar[i] = altPar[i]

    dictionary = dict(zip(keys, currentPar))
    print currentPar

    fn = fclName
    if fn in os.listdir('.'):
        if os.path.isfile(fn):
            s = open(fn).read()
            s = re.sub('anaTree_histo_baseline.root', 'anatree_par'+str(i)+'.root', s, 1)

            for i in dictionary:
                link = dictionary[i]        
                s = re.sub(r'\b'+i+r'\b', '%s' %link, s, 1)


            print "%s updated" %fn
            
            f = open(fn, 'w')
            f.write(s)
            f.close()

