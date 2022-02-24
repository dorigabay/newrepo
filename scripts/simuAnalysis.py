# Accommodation of simuAnalysis to the command prompt.
import sys
import argparse
import os
from simuAnalysis_calculation import save_xtcAnalysis,iterPDBAnalysis,zip2pdb
from calc_LSE import run_preCalcLSE,plot_LSE
<<<<<<< HEAD
import subprocess
import re
=======

>>>>>>> 6a030d4bb88b17b83d05ca246c9aacc97cbceb48

if len(sys.argv) < 2:
    exit ("Not enough arguments")

parser = argparse.ArgumentParser()
<<<<<<< HEAD
parser.add_argument('--manual','--man', action='store_true')
args = vars(parser.parse_args())
if args["manual"]:
    os.chdir(os.path.dirname(__file__))
    os.chdir("../")
    subprocess.Popen("cat manual.txt", shell=True)
    exit()

parser = argparse.ArgumentParser()
parser.add_argument('--simulationType','--t',help="The name of model used to create the results. Either 'coarse' or 'atomistic'. (obligatory)",choices=['atomistic','coarse'],required=True)
parser.add_argument('--directory','--d', help="Directory path withholds the simulation’s results.  For ‘coarse’ any parent directory will be enough. (obligatory, ‘atomistic’, ’coarse’)",type=str, required=True)
parser.add_argument('--seqName','--s', help="Sequence name of which its atomistic simulations are quested to be analyzed. (obligatory, ‘atomistic’)",type=str)
parser.add_argument('--startStep','--start', help="Simulation time point in which to begin the analysis should be given as an integer. (‘atomistic’, ’coarse’)",type=int)
parser.add_argument('--endStep','--end', help="Simulation time point in which to end the analysis should be given as an integer. (‘atomistic’, ’coarse’)",type=int)
parser.add_argument('--outputDir','--o', help="Directory path to save the analysis output. (‘atomistic’, ’coarse’)",type=str)
parser.add_argument('--calculateFret','--calcFRET', help="To calculate estimated FRET measurements. (‘atomistic’)",action='store_true')
parser.add_argument('--runMode', help="Either ‘full’ for default analysis of atomistic simulation (RG, residue distance), or ‘calcLSE’ to create a graph with fitted Flory exponent to the observed results. (‘atomistic’)",choices=["calcLSE","full"],type=str)
args = vars(parser.parse_args())



if args["outputDir"]==None:
    args["outputDir"]=os.path.join(args["directory"], "AnalyzedData")
=======
parser.add_argument('--simulationType','--t',help='',choices=['atomistic','coarse'],required=True)
parser.add_argument('--directory','--d', help='',type=str, required=True)
parser.add_argument('--seqName','--s', help='',type=str)
parser.add_argument('--startStep','--start', help='',type=int)
parser.add_argument('--endStep','--end', help='',type=int)
parser.add_argument('--outputDir','--o', help='',type=str)
parser.add_argument('--calculateFret','--fret', help='',action='store_true')
parser.add_argument('--runMode', help='',choices=["calcLSE","full"],type=str)
args = vars(parser.parse_args())
>>>>>>> 6a030d4bb88b17b83d05ca246c9aacc97cbceb48

if args["simulationType"]=="atomistic":
    if args["seqName"]==None:
        exit("---------------Missing segment name ('-seqName')---------------")
    if args["runMode"] == "full":
<<<<<<< HEAD
        save_xtcAnalysis(args["directory"], args["seqName"],args["calculateFret"], args["outputDir"], args["startStep"], args["endStep"])
    elif args["runMode"] ==  "calcLSE":
        run_preCalcLSE(args["directory"], args["outputDir"], args["seqName"], args["startStep"], args["endStep"])
        plot_LSE(args["outputDir"],args["seqName"],args["outputDir"])
    elif args["runMode"] == None:
        save_xtcAnalysis(args["directory"], args["seqName"],args["calculateFret"], args["outputDir"], args["startStep"], args["endStep"])
=======
        save_xtcAnalysis(args["directory"], args["seqName"], args["outputDir"], args["startStep"], args["endStep"])
    elif args["runMode"] ==  "calcLSE":
        run_preCalcLSE(args["directory"], args["outputDir"], args["seqName"], args["startStep"], args["endStep"])
        plot_LSE(os.path.join(args["directory"], "AnalyzedData"),args["seqName"],args["outputDir"])
    elif args["runMode"] == None:
        save_xtcAnalysis(args["directory"], args["seqName"], args["outputDir"], args["startStep"], args["endStep"])
>>>>>>> 6a030d4bb88b17b83d05ca246c9aacc97cbceb48

if args["simulationType"]=="coarse":
    zip2pdb(args["directory"])
    iterPDBAnalysis(args["directory"],args["outputDir"], args["startStep"], args["endStep"])
