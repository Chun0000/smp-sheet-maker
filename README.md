# smp-sheet-maker

This script create sample sheet for sarek pipeline.

### How to run this?

1. Download this entire repo.

2. Modify setting in `smp-sheet-maker.sh`

> All `fastq` file formats need to match this pattern `O36X1_22HMLNLT3_L1_R2.fastq.gz`.

- `data_path`: path to folder that contain all fastq files
- `patient`: patient identifier
- `normal`: name of normal sample
- `output`: output sample sheet
- `sex`: sex of the patient

3. Run in termnal

```
sh smp_sheet_maker.sh
```
