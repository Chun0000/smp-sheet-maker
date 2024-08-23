module load python/3.12.2

data_path=/staging/biology/u3414958/Pan3_WES/RAWDATA
patient=Pan3
normal=N1
sex=XX
lane=L1
output=/staging/biology/u3414958/Pan3_WES/sample_sheet.csv

python ./smp_sheet_maker.py $data_path $patient $normal $output $sex $lane