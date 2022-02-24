#!/bin/csh -f
#
#$ -cwd
#$ -j y
#$ -S /bin/csh
#
#$ -M myemail
#$ -e error_file
#$ -o MDWrapper.log
#$ -q all.q
set hostname = `hostname`
set out_dir = /cluster_data/dor/pyCourseProject/coarse/seq3//output
set scratch = /scratch/dor/seq3_0.3_872208
echo '#########################'
echo Running on host `hostname`
echo Time is `date`
echo Directory is /cluster_data/dor/pyCourseProject/coarse/seq3/
echo temp Directory is $scratch
mkdir -p $scratch
cp /cluster_data/dor/pyCourseProject/coarse/seq3//input/settings_872208.dat $scratch/settings.dat
cp /cluster_data/dor/pyCourseProject/coarse/seq3//input/random_872208.dat $scratch/random.dat
cp ./seq3.dat /cluster_data/dor/pyCourseProject/coarse/seq3//input/
cp /home/dor/scripts/MD_base_hydrophobic_exceed_limit_p53/MD.exe $scratch
cp ./seq3.dat $scratch
cd $scratch
time  ./MD.exe >& time_seq3_0.3_872208.out
bzip2 TemperatureFile_seq3_0.3_872208.dat
bzip2 2body_seq3_0.3_872208.dat
bzip2 3body_seq3_0.3_872208.dat
bzip2 Etotal_seq3_0.3_872208.dat
bzip2 EbyType_seq3_0.3_872208.dat
bzip2 seq3_0.3_872208.log
time  bzip2 Traj_seq3_0.3_872208.dat >>& time_seq3_0.3_872208.out
cp Final_seq3_0.3_872208.dat $out_dir/LastCord
cp seq3_0.3_872208.log.bz2 $out_dir/Log
cp TemperatureFile_seq3_0.3_872208.dat.bz2 $out_dir/Temperature
cp 2body_seq3_0.3_872208.dat.bz2 $out_dir/2Body
cp 3body_seq3_0.3_872208.dat.bz2 $out_dir/3Body
cp Etotal_seq3_0.3_872208.dat.bz2 $out_dir/Etotal
cp EbyType_seq3_0.3_872208.dat.bz2 $out_dir/EbyType
time cp Traj_seq3_0.3_872208.dat.bz2 $out_dir/Traj >>& time_seq3_0.3_872208.out
cp time_seq3_0.3_872208.out $out_dir
rm -r $scratch
echo End of job. Time is `date`
