# The simuAnalysisPoject

A python package to analyze computational simulations of protein dynamics results from either the atomistic (XTC file format) or the coarse-grain models (DAT file format). This tool calculates the mean Radius of Gyration (RG), the distance between two specified residues, and the approximate FRET measurement for each simulation time point. It saves all the repeated results in one CSV file. Also, the tool enables you to predict the Length Scaling Exponent (LSE, or Flory calculation of the exponent) by fitting Flory’s formula with the results: 

<img src="/pics/flory_formula.JPG" width="600">

![mainFunctions](/pics/flory_formula.JPG =100x20)

For the coarse grain model, this tool takes any depth of the directory, searches for the output of Koby’s Lab coarse-grained simulation program, and exports the analysis results in a new directory with the same tree structure as the input directory. 
For the atomistic model, this tool takes all the XTC files in the input directory and considers them as repeats of the same experiment.
