# Accommodation of simuAnalysis to the command prompt.
import sys


if len(sys.argv) < 2:
    exit ("Not enough arguments")


arguments_given = dict(zip(sys.argv[2::2], sys.argv[3::2]))

if sys.argv[1] == "atomistic":
    # prepare arguments
    directory, sequence_name, start_step, end_step,outdir,calc_fret,run_mode= ["" for x in range(7)]
    if "-f" not in arguments_given.keys():
        exit("""---------------Missing input directory ('-f')---------------""")
    else:
        directory = str(arguments_given["-f"])+"/"
    if "-seqName" not in arguments_given.keys():
        exit("---------------Missing segment name ('-seqName')---------------")
    else:
        sequence_name = str(arguments_given["-seqName"])
    if "-start" in arguments_given.keys():
        start_step = int(arguments_given["-start"])
    else: start_step = None
    if "-end" in arguments_given.keys():
        end_step = int(arguments_given["-end"])
    else: end_step = None
    if "-out" in arguments_given.keys():
        outdir = str(arguments_given["-out"])
    else: outdir = directory+"/AnalyzedData/"
    if "-calcFRET" in arguments_given.keys():
        if arguments_given["-calcFRET"] not in ["True","False","T","F","TRUE","FALSE"]:
            exit('---------------Argument "-calcFRET" should be boolean (True/False/T/F/TRUE/FALSE)---------------')
        elif arguments_given["-calcFRET"] in ["True","TRUE","T"]:
            calc_fret = True
        else: calc_fret = False
    else: calc_fret = False

    # run xtcAnalysis or calcLSE
    if "-runMode" in arguments_given.keys() and arguments_given["-runMode"] == "full":
        from simuAnalysis_calculation import save_xtcAnalysis
        save_xtcAnalysis(directory, sequence_name, outdir, start_step, end_step)
    elif "-runMode" in arguments_given.keys() and arguments_given["-runMode"] == "calcLSE":
            from calc_LSE import run_preCalcLSE,plot_LSE
            run_preCalcLSE(directory,outdir, sequence_name, start_step, end_step)
            plot_LSE(directory+"/AnalyzedData/",sequence_name,outdir)
    elif "-runMode" not in arguments_given.keys():
        from simuAnalysis_calculation import save_xtcAnalysis
        save_xtcAnalysis(directory, sequence_name, outdir, start_step, end_step)


elif sys.argv[1] == "coarse":
    # prepare arguments
    directory, start_step,end_step,outdir = ["" for x in range(4)]
    if "-f" not in arguments_given.keys():
        exit("""---------------Missing input directory ('-f')---------------""")
    else:
        directory = str(arguments_given["-f"])+"/"
    if "-start" in arguments_given.keys():
        start_step = int(arguments_given["-start"])
    else: start_step = None
    if "-end" in arguments_given.keys():
        end_step = int(arguments_given["-end"])
    else: end_step = None
    if "-out" in arguments_given.keys():
        outdir = str(arguments_given["-out"])
    else: outdir = directory+"/AnalyzedData/"
    # run function
    from simuAnalysis_calculation import zip2pdb, iterPDBAnalysis
    zip2pdb(directory)
    iterPDBAnalysis(directory,outdir, start_step,end_step)



elif sys.argv[1] != "coarse" or sys.argv[1] != "atomistic":
    exit("---------------Missing simulation type ('atomistic' or 'coarse')---------------")