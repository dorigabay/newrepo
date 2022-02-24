# Accommodation of simuAnalysis to the command prompt.
import sys
import argparse
import os
from simuAnalysis_calculation import save_xtcAnalysis,iterPDBAnalysis,zip2pdb
from calc_LSE import run_preCalcLSE,plot_LSE


if len(sys.argv) < 2:
    exit ("Not enough arguments")

parser = argparse.ArgumentParser()
parser.add_argument('--simulationType','--t',help='',choices=['atomistic','coarse'],required=True)
parser.add_argument('--directory','--d', help='',type=str, required=True)
parser.add_argument('--seqName','--s', help='',type=str)
parser.add_argument('--startStep','--start', help='',type=int)
parser.add_argument('--endStep','--end', help='',type=int)
parser.add_argument('--outputDir','--o', help='',type=str)
parser.add_argument('--calculateFret','--fret', help='',action='store_true')
parser.add_argument('--runMode', help='',choices=["calcLSE","full"],type=str)
args = vars(parser.parse_args())

if args["simulationType"]=="atomistic":
    if args["seqName"]==None:
        exit("---------------Missing segment name ('-seqName')---------------")
    if args["runMode"] == "full":
        save_xtcAnalysis(args["directory"], args["seqName"], args["outputDir"], args["startStep"], args["endStep"])
    elif args["runMode"] ==  "calcLSE":
        run_preCalcLSE(args["directory"], args["outputDir"], args["seqName"], args["startStep"], args["endStep"])
        plot_LSE(os.path.join(args["directory"], "AnalyzedData"),args["seqName"],args["outputDir"])
    elif args["runMode"] == None:
        save_xtcAnalysis(args["directory"], args["seqName"], args["outputDir"], args["startStep"], args["endStep"])

if args["simulationType"]=="coarse":
    zip2pdb(args["directory"])
    iterPDBAnalysis(args["directory"],args["outputDir"], args["startStep"], args["endStep"])
