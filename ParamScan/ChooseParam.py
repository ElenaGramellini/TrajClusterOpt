
import os
import math
import copy
from ROOT import *
import math
from os import listdir
from os.path import isfile, join
from array import array




refFile = "/lariat/data/users/elenag/trackingOpt/paramChange/anaTree_histo_baseline.root"

dirName = "/lariat/data/users/elenag/trackingOpt/paramChange/"
onlyfiles = [f for f in listdir(dirName) if isfile(join(dirName, f)) and f.find(".root") != -1 and f.find("par") !=-1]
combo     = [x.replace('.root', '').replace('anatree_', '') for x in onlyfiles]


if len(onlyfiles) != len(combo) :
    exit("Different list length, please look back at whatttadoing!")
nComboAvailable = len(onlyfiles)

print onlyfiles
print combo
print "Number of combinations available ", nComboAvailable


outfile = TFile( 'ChoosePar.root', 'recreate' )

refRootFile  = TFile( refFile )
refTree      = refRootFile.Get("TruthTeller/effTree")
refRecoL     = TH1D("refRecoL"      , "hRecoL           ;  Reco L [cm]" ,200,0,200)
refDeltaL    = TH1D("refDeltaL"     , "hDeltaL          ;  Reco L - True L [cm]" ,200,-100,100)
refTree.Draw("recoL>>refRecoL"            , "")
refTree.Draw("recoL-trueL>>refDeltaL"     , "recoL>0")
refRecoL .SetLineColor(kRed)
refDeltaL.SetLineColor(kRed)


for i in xrange(nComboAvailable) :
    # get ROOT files and right TTrww
    c0 = TCanvas("c0","c0",600,600)
    c0.cd()
    f = onlyfiles[i]
    rootFileName = dirName+f
    print rootFileName
    rootFile  = TFile( rootFileName )
    _Tree = rootFile.Get("TruthTeller/effTree")

    print combo[i]

    _hRecoL            = TH1D("hRecoL"            , "hRecoL           ;  Reco L [cm]" ,200,0,200)
    _hDeltaL           = TH1D("hDeltaL"           , "hDeltaL          ;  Reco L - True L [cm]" ,200,-100,100)


    _Tree.Draw("recoL>>hRecoL"            , "")
    refRecoL.Draw("sames")
    c0.Update()

    c2 = TCanvas("c2","c2",600,600)
    c2.cd()
    _Tree.Draw("recoL-trueL>>hDeltaL"     , "recoL>0")
    refDeltaL.Draw("sames")
    c2.Update()

    raw_input()  






       

