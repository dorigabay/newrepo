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
set out_dir = /cluster_data/dor/pyCourseProject/coarse/seq1//output
set scratch = /scratch/dor/seq1_0.3_333508
echo '#########################'
echo Running on host `hostname`
echo Time is `date`
echo Directory is /cluster_data/dor/pyCourseProject/coarse/seq1/
echo temp Directory is $scratch
mkdir -p $scratch
cp /cluster_data/dor/pyCourseProject/coarse/seq1//input/settings_333508.dat $scratch/settings.dat
cp /cluster_data/dor/pyCourseProject/coarse/seq1//input/random_333508.dat $scratch/random.dat
cp ./seq1.dat /cluster_data/dor/pyCourseProject/coarse/seq1//input/
cp /home/dor/scripts/MD_base_hydrophobic_exceed_limit_p53/MD.exe $scratch
cp ./seq1.dat $scratch
cd $scratch
time  ./MD.exe >& time_seq1_0.3_333508.out
bzip2 TemperatureFile_seq1_0.3_333508.dat
bzip2 2body_seq1_0.3_333508.dat
bzip2 3body_seq1_0.3_333508.dat
bzip2 Etotal_seq1_0.3_333508.dat
bzip2 EbyType_seq1_0.3_333508.dat
bzip2 seq1_0.3_333508.log
time  bzip2 Traj_seq1_0.3_333508.dat >>& time_seq1_0.3_333508.out
cp Final_seq1_0.3_333508.dat $out_dir/LastCord
cp seq1_0.3_333508.log.bz2 $out_dir/Log
cp TemperatureFile_seq1_0.3_333508.dat.bz2 $out_dir/Temperature
cp 2body_seq1_0.3_333508.dat.bz2 $out_dir/2Body
cp 3body_seq1_0.3_333508.dat.bz2 $out_dir/3Body
cp Etotal_seq1_0.3_333508.dat.bz2 $out_dir/Etotal
cp EbyType_seq1_0.3_333508.dat.bz2 $out_dir/EbyType
time cp Traj_seq1_0.3_333508.dat.bz2 $out_dir/Traj >>& time_seq1_0.3_333508.out
cp time_seq1_0.3_333508.out $out_dir
rm -r $scratch
echo End of job. Time is `date`
