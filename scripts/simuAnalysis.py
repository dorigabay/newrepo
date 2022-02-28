# Accommodation of simuAnalysis to the command prompt.
import sys
import argparse
import os
from simuAnalysis_calculation import save_xtcAnalysis,iterPDBAnalysis,zip2pdb
from calc_LSE import run_preCalcLSE,plot_LSE
import subprocess
import re


if len(sys.argv) < 2:
    exit ("Not enough arguments")


#parser = argparse.ArgumentParser()
#parser.add_argument('--manual','--man', action='store_true')
#args = vars(parser.parse_args())
#if args["manual"]:
#    os.chdir(os.path.dirname(__file__))
#    os.chdir("../")
#    subprocess.Popen("cat manual.txt", shell=True)
#    exit()


parser = argparse.ArgumentParser()
parser.add_argument('--simulationType','--t',help="The name of model used to create the results. Either 'coarse' or 'atomistic'. (obligatory)",choices=['atomistic','coarse'],required=True)
parser.add_argument('--directory','--d', help="Directory path withholds the simulation’s results.  For ‘coarse’ any parent directory will be enough. (obligatory, ‘atomistic’, ’coarse’)",type=str, required=True)
parser.add_argument('--seqName','--s', help="Sequence name of which its atomistic simulations are quested to be analyzed. (obligatory, ‘atomistic’)",type=str)
parser.add_argument('--startStep','--start', help="Simulation time point in which to begin the analysis should be given as an integer. (‘atomistic’, ’coarse’)",type=int)
parser.add_argument('--endStep','--end', help="Simulation time point in which to end the analysis should be given as an integer. (‘atomistic’, ’coarse’)",type=int)
parser.add_argument('--outputDir','--o', help="Directory path to save the analysis output. (‘atomistic’, ’coarse’)",type=str)
parser.add_argument('--calculateFret','--calcFRET', help="To calculate estimated FRET measurements. (‘atomistic’)",action='store_true')
parser.add_argument('--calculateLSE','--calcLSE', help="‘calcLSE’ creates a graph with fitted Flory exponent to the observed results. (‘atomistic’)",action='store_true')
args = vars(parser.parse_args())


if args["outputDir"]==None:
    args["outputDir"]=os.path.join(args["directory"], "AnalyzedData/")

if args["simulationType"]=="atomistic":
    if args["seqName"]==None:
        exit("---------------Missing segment name ('-seqName')---------------")
    elif not args["calculateLSE"]:
        save_xtcAnalysis(args["directory"], args["seqName"],args["calculateFret"], args["outputDir"], args["startStep"], args["endStep"])
    elif args["calculateLSE"]:
        run_preCalcLSE(args["directory"], args["outputDir"], args["seqName"], args["startStep"], args["endStep"])
        plot_LSE(os.path.join(args["directory"], "AnalyzedData/"),args["seqName"],args["outputDir"])

if args["simulationType"]=="coarse":
    zip2pdb(args["directory"])
    iterPDBAnalysis(args["directory"],args["outputDir"], args["startStep"], args["endStep"])
