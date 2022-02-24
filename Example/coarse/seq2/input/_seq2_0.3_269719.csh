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
set out_dir = /cluster_data/dor/pyCourseProject/coarse/seq2//output
set scratch = /scratch/dor/seq2_0.3_269719
echo '#########################'
echo Running on host `hostname`
echo Time is `date`
echo Directory is /cluster_data/dor/pyCourseProject/coarse/seq2/
echo temp Directory is $scratch
mkdir -p $scratch
cp /cluster_data/dor/pyCourseProject/coarse/seq2//input/settings_269719.dat $scratch/settings.dat
cp /cluster_data/dor/pyCourseProject/coarse/seq2//input/random_269719.dat $scratch/random.dat
cp ./seq2.dat /cluster_data/dor/pyCourseProject/coarse/seq2//input/
cp /home/dor/scripts/MD_base_hydrophobic_exceed_limit_p53/MD.exe $scratch
cp ./seq2.dat $scratch
cd $scratch
time  ./MD.exe >& time_seq2_0.3_269719.out
bzip2 TemperatureFile_seq2_0.3_269719.dat
bzip2 2body_seq2_0.3_269719.dat
bzip2 3body_seq2_0.3_269719.dat
bzip2 Etotal_seq2_0.3_269719.dat
bzip2 EbyType_seq2_0.3_269719.dat
bzip2 seq2_0.3_269719.log
time  bzip2 Traj_seq2_0.3_269719.dat >>& time_seq2_0.3_269719.out
cp Final_seq2_0.3_269719.dat $out_dir/LastCord
cp seq2_0.3_269719.log.bz2 $out_dir/Log
cp TemperatureFile_seq2_0.3_269719.dat.bz2 $out_dir/Temperature
cp 2body_seq2_0.3_269719.dat.bz2 $out_dir/2Body
cp 3body_seq2_0.3_269719.dat.bz2 $out_dir/3Body
cp Etotal_seq2_0.3_269719.dat.bz2 $out_dir/Etotal
cp EbyType_seq2_0.3_269719.dat.bz2 $out_dir/EbyType
time cp Traj_seq2_0.3_269719.dat.bz2 $out_dir/Traj >>& time_seq2_0.3_269719.out
cp time_seq2_0.3_269719.out $out_dir
rm -r $scratch
echo End of job. Time is `date`
