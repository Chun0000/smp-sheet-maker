module load python/3.12.2

data_path=/staging/biology/u3414958/OM3_WGS/RAWDATA
patient=OM3
normal=N1
sex=XX
output=/staging/biology/u3414958/OM3_WGS/sample_sheet.csv

python ./smp_sheet_maker.py $data_path $patient $normal $output $sex