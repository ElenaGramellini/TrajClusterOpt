import os
import math
import copy
from ROOT import *
import math
from os import listdir
from os.path import isfile, join
from array import array


fileName = "FoM.root"
rootFile    = TFile(fileName )
gStyle.SetOptStat(0)

t = rootFile.Get("t1") 


hIntegralRatio   = TH1D("hIntegralRatio","hIntegralRatio; Configuration index 1; hIntegralRatio",162,-0.5,161.5)
hMean   = TH1D("hMean","hMean; Configuration index 1; Delta L Mean",162,-0.5,161.5)
hStdDev = TH1D("hStdDev","hStdDev; Configuration index; Delta L StdDev",162,-0.5,161.5)
hVtxDist      = TH1D("hVtxDist","hVtxDist; Configuration index; VtxDist Ratio",162,-0.5,161.5)
hEndDist      = TH1D("hEndDist","hEndDist; Configuration index; EndDist Ratio",162,-0.5,161.5)


binCounter = 1
getCombo = 4
for event in t:
      strCombo = str(event.comboCode)
      if '0' in strCombo[getCombo] :
            print strCombo[0],  strCombo[1],  strCombo[2],  strCombo[3],  strCombo[4],  strCombo
            hMean   .SetBinContent(binCounter, event.mean)
            hStdDev .SetBinContent(binCounter, event.stdDev)
            hEndDist.SetBinContent(binCounter, event.endDistRatio)
            hVtxDist.SetBinContent(binCounter, event.vtxDistRatio)
            hIntegralRatio.SetBinContent(binCounter, event.integralRatio)
            binCounter += 1
for event in t:
      strCombo = str(event.comboCode)
      if '1' in strCombo[getCombo] :
            print strCombo[0],  strCombo[1],  strCombo[2],  strCombo[3],  strCombo[4],  strCombo
            hMean   .SetBinContent(binCounter, event.mean)
            hStdDev .SetBinContent(binCounter, event.stdDev)
            hEndDist.SetBinContent(binCounter, event.endDistRatio)
            hVtxDist.SetBinContent(binCounter, event.vtxDistRatio)
            hIntegralRatio.SetBinContent(binCounter, event.integralRatio)
            binCounter += 1

print "NEW LOOP"
for event in t:
      strCombo = str(event.comboCode)
      if '2' in strCombo[getCombo] :
            print strCombo[0],  strCombo[1],  strCombo[2],  strCombo[3],  strCombo[4],  strCombo
            hMean   .SetBinContent(binCounter, event.mean)
            hStdDev .SetBinContent(binCounter, event.stdDev)
            hEndDist.SetBinContent(binCounter, event.endDistRatio)
            hVtxDist.SetBinContent(binCounter, event.vtxDistRatio)
            hIntegralRatio.SetBinContent(binCounter, event.integralRatio)
            binCounter += 1

print "NEW LOOP"
for event in t:
      strCombo = str(event.comboCode)
      if '3' in strCombo[getCombo] :
            print strCombo[0],  strCombo[1],  strCombo[2],  strCombo[3],  strCombo[4],  strCombo
            hMean   .SetBinContent(binCounter, event.mean)
            hStdDev .SetBinContent(binCounter, event.stdDev)
            hEndDist.SetBinContent(binCounter, event.endDistRatio)
            hVtxDist.SetBinContent(binCounter, event.vtxDistRatio)
            hIntegralRatio.SetBinContent(binCounter, event.integralRatio)
            binCounter += 1



cNTOF3 = TCanvas("cft3","ctf3",600,600)
cNTOF3.cd()
hMean.SetLineColor(kRed)
hMean.SetLineWidth(2)
hMean.Draw("")


cNTOF4 = TCanvas("cft4","ctf4",600,600)
cNTOF4.cd()
hStdDev.SetLineColor(kBlue)
hStdDev.SetLineWidth(2)
hStdDev.Draw("")


cNTOF5 = TCanvas("cft5","ctf5",600,600)
cNTOF5.cd()
hEndDist.SetLineColor(kGreen-2)
hEndDist.SetLineWidth(2)
hEndDist.Draw("")


cNTOF6 = TCanvas("cft6","ctf6",600,600)
cNTOF6.cd()
hIntegralRatio.SetLineColor(kYellow-2)
hIntegralRatio.SetLineWidth(2)
hIntegralRatio.Draw("")

cNTOF7 = TCanvas("cft7","ctf7",600,600)
cNTOF7.cd()
hVtxDist.SetLineColor(kPink)
hVtxDist.SetLineWidth(2)
hVtxDist.Draw("")



raw_input()  



 


#  LocalWords:  hIntegralRatio
