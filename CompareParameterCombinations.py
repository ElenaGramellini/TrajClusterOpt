'''
Given a list of .root files, this code saves a bunch of histograms, most notably:
- recoL - trueL histogram
- vtxDist
- endDist
- trueInteractionAngle

and compares the efficiencies for the input files 
vtxDist efficiency:  vtxDist < 1 cm / all vtx
endDist efficiency:  endDist < 1 cm / all end
deltaL  efficiency:  |DeltaL| < 5 cm / all DeltaL
 
Error bars for efficiency plots should be ok even with small stat
'''


import os
import math
import copy
from ROOT import *
import math
from os import listdir
from os.path import isfile, join
from array import array


def errorPropEff (A, B, eff):

    k = TEfficiency()
    k.SetStatisticOption(TEfficiency.kFFC)

    eff_upper = k.FeldmanCousins(B,A,0.6827,True)
    eff_lower = k.FeldmanCousins(B,A,0.6827,False)
    del k

    return eff_lower, eff_upper




dirName = "/lariat/data/users/elenag/trackingOpt/optimizationData/"
onlyfiles = [f for f in listdir(dirName) if isfile(join(dirName, f)) and f.find(".root") != -1]
combo     = [x.replace('.root', '').replace('anatree_', '') for x in onlyfiles]


if len(onlyfiles) != len(combo) :
    exit("Different list length, please look back at whatttadoing!")
nComboAvailable = len(onlyfiles)

print onlyfiles
print combo
print "Number of combinations available ", nComboAvailable


outfile = TFile( 'ParamScan.root', 'recreate' )

vtxEffNum = []
vtxEffDen = []
vtxEff    = []

endEffNum = []
endEffDen = []
endEff    = []

deltaLEffNum = []
deltaLEffDen = []
deltaLEff    = []

for i in xrange(nComboAvailable) :
    # get ROOT files and right TTrww
    f = onlyfiles[i]
    rootFileName = dirName+f
    print rootFileName
    rootFile  = TFile( rootFileName )
    _Tree = rootFile.Get("TruthTeller/effTree")

    
    # declare output histos
    thisSetName = combo[i]
    _hTrueL            = TH1D("hTrueL"            , "hTrueL           ;  True L [cm]" ,200,0,200)
    _hRecoL            = TH1D("hRecoL"            , "hRecoL           ;  Reco L [cm]" ,200,0,200)
    _hIntAngle         = TH1D("hIntAngle"         , "hIntAngle        ;  Interaction Angle [Deg]" ,180,0,180)
    _hDeltaL           = TH1D("hDeltaL"           , "hDeltaL          ;  Reco L - True L [cm]" ,200,-100,100)
    _hDeltaLGood       = TH1D("hDeltaLGood"       , "hDeltaLGood      ;  Reco L - True L [cm]" ,200,-100,100)
    _hVtxDist          = TH1D("hVtxDist"          , "hVtxDist         ;  Vtx Dist [cm]" ,200,0,100)
    _hEndDist          = TH1D("hEndDist"          , "hEndDist         ;  End Dist [cm]" ,200,0,100)                                              
    _hDelatLVsIntAngle = TH2D("hDelatLVsIntAngle" , "hDelatLVsIntAngle;  Delta L [cm] ; Interaction Angle [Deg]" ,200,-100,100,180,0,180)
    _hRecoLVsTrueLGood = TH2D("hRecoLVsTrueLGood" , "hRecoLVsTrueLGood;  True L [cm]" ,200,0,200,200,0,200)
    _hRecoLVsTrueL     = TH2D("hRecoLVsTrueL"     , "hRecoLVsTrueL    ;  True L [cm]" ,200,0,200,200,0,200)


    _Tree.Draw("trueL>>hTrueL"            , "")
    _Tree.Draw("recoL>>hRecoL"            , "")
    _Tree.Draw("intAngle>>hIntAngle"      , "")
    _Tree.Draw("recoL-trueL>>hDeltaL"     , "recoL>0")
    _Tree.Draw("recoL-trueL>>hDeltaLGood" , "recoL>0&&vtxDist<1&&endDist<1")
    _Tree.Draw("vtxDist>>hVtxDist"        , "recoL>0")
    _Tree.Draw("endDist>>hEndDist"        , "recoL>0")
    _Tree.Draw("intAngle:recoL-trueL>>hDelatLVsIntAngle" , "recoL>0")
    _Tree.Draw("recoL:trueL>>hRecoLVsTrueLGood"          , "recoL>0&&vtxDist<1&&endDist<1")
    _Tree.Draw("recoL:trueL>>hRecoLVsTrueL"              , "recoL>0")

    vtxEffN    = (100*float(_hVtxDist.Integral( 0 ,   2)) /float(_hVtxDist.Integral()))
    endEffN    = (100*float(_hEndDist.Integral( 0 ,   2)) /float(_hEndDist.Integral()))
    deltaLEffN = (100*float(_hDeltaL .Integral( 96, 104)) /float(_hDeltaL .Integral()))

    vtxEffNum .append(_hVtxDist.Integral( 0 ,   2))
    vtxEffDen .append(_hVtxDist.Integral( ))
    vtxEff    .append(vtxEffN)
    
    endEffNum .append(_hEndDist.Integral( 0 ,   2))
    endEffDen .append(_hEndDist.Integral( ))
    endEff    .append(endEffN)
    
    deltaLEffNum .append(_hDeltaL.Integral( 96, 104))
    deltaLEffDen .append(_hDeltaL.Integral( ))
    deltaLEff    .append(deltaLEffN)

    # Print some stats for each combo
    print "vtx dist < 1 cm      : ",'%.2f' % vtxEffN   , "% times"
    print "end dist < 1 cm      : ",'%.2f' % endEffN   , "% times"
    print "reco - true L < 5 cm : ",'%.2f' % deltaLEffN, "% times"
    # Write this histos to file
    outfile.cd()
    _hTrueL            .Write("htrueL"+thisSetName)
    _hRecoL            .Write("hRecoL"+thisSetName)      
    _hIntAngle         .Write("hIntAngle"+thisSetName)   
    _hDeltaL           .Write("hDeltaL"+thisSetName)     
    _hDeltaLGood       .Write("hDeltaLGood"+thisSetName) 
    _hVtxDist          .Write("hVtxDist"+thisSetName)    
    _hEndDist          .Write("hEndDist"+thisSetName)    
    _hDelatLVsIntAngle .Write("hDelatLVsIntAngle"+thisSetName) 
    _hRecoLVsTrueLGood .Write("hRecoLVsTrueLGood"+thisSetName) 
    _hRecoLVsTrueL     .Write("hRecoLVsTrueL"+thisSetName)     


# Calculate Efficiency Plots
vtxEffUpper = []
vtxEffLower = []
endEffUpper = []
endEffLower = []
deltaLEffUpper = []
deltaLEffLower = []

num    = []
numErr = []
for x in xrange(len(deltaLEff)):
    num.append(x)
    numErr.append(0.5)
    effLow, effHigh = errorPropEff(vtxEffNum[x], vtxEffDen[x], vtxEff[x])
    vtxEffUpper.append(effHigh)
    vtxEffLower.append(effLow)

    effLow, effHigh = errorPropEff(endEffNum[x], endEffDen[x], endEff[x])
    endEffUpper.append(effHigh)
    endEffLower.append(effLow)

    effLow, effHigh = errorPropEff(deltaLEffNum[x], deltaLEffDen[x], deltaLEff[x])
    deltaLEffUpper.append(effHigh)
    deltaLEffLower.append(effLow)


from array import array
print num
nPoints=len(num)
x   = array('f', num )
#x   = array('c', combo )
exl = array('f', numErr)
exr = array('f', numErr)


c1=TCanvas("c0" ,"Data" ,200 ,10 ,500 ,500) #make nice
c1.SetGrid ()
y   = array('f', deltaLEff)
eyt = array('f', deltaLEffUpper )
eyb = array('f', deltaLEffLower )


# . . . and hand over to TGraphErros object
gr = TGraphAsymmErrors ( nPoints , x , y , exl, exr , eyb, eyt )
gr.SetTitle("DeltaL Efficiency as a function of Parametrization ; Code; Delta L Efficiency")
gr . GetYaxis().SetRangeUser(0,100)
gr . Draw ( "AP" ) ;
c1 . Update ()


gr.Write("deltaLEff")
    

c2=TCanvas("c2" ,"Data" ,200 ,10 ,500 ,500) #make nice
c2.SetGrid ()
y   = array('f', endEff)
eyt = array('f', endEffUpper )
eyb = array('f', endEffLower )
gr1 = TGraphAsymmErrors ( nPoints , x , y , exl, exr , eyb, eyt )
gr1.SetTitle("EndDist Efficiency as a function of Parametrization ; Code; End Dist Efficiency")
gr1 . GetYaxis().SetRangeUser(0,100)
gr1 . Draw ( "AP" ) ;
c2 . Update ()
gr1.Write("endEff")


c3=TCanvas("c3" ,"Data" ,200 ,10 ,500 ,500) #make nice
c3.SetGrid ()
y   = array('f', vtxEff)
eyt = array('f', vtxEffUpper )
eyb = array('f', vtxEffLower )
gr2 = TGraphAsymmErrors ( nPoints , x , y , exl, exr , eyb, eyt )
gr2.SetTitle("VtxDist Efficiency as a function of Parametrization ; ; VtxDist Efficiency")

'''
ax = gr2.GetHistogram().GetXaxis();

print gr2.GetHistogram().GetNbinsX()
x1 = ax.GetBinLowEdge(2);
x2 = ax.GetBinUpEdge(ax.GetNbins());
gr2.GetHistogram().GetXaxis().Set(20,x1,x2);

for k in xrange(len(combo)):
    gr2.GetHistogram().GetXaxis().SetBinLabel(k+2,combo[k])
    print     gr2.GetHistogram().GetBinContent(k+1), gr2.GetHistogram().GetXaxis().GetBinLabel(k+1), combo[k] 
'''
gr2 . GetYaxis().SetRangeUser(0,100)
c2 . Update ()
gr2 . Draw ( "AP" ) ;
c2 . Update ()

gr2.Write("vtxEff")


outfile.Write()
outfile.Close()

raw_input()  






       

