import os
import pandas as pd
import argparse


def get_sample_info(path, patient, normal, out_file, sex):
    """
    Function to get sample information and save to a CSV file.
    """
    if not os.path.exists(path):
        print(f"Directory does not exist: {path}")
        return

    data = {}
    for root, _, files in os.walk(path):
        unmatched_files = 0
        matched_files = 0
        for file in files:
            try:
                parts = file.split('_')
                if len(parts) < 3:
                    unmatched_files += 1
                    continue  # Skip files that don't match the expected pattern

                sample = parts[0].replace(patient, '')
                lane = parts[2]
                file_path = os.path.join(root, file)

                if sample not in data:
                    data[sample] = {'status': 0 if sample == normal else 1,
                                    'lane': lane, 'fastq_1': '', 'fastq_2': ''}

                if 'R1' in file:
                    data[sample]['fastq_1'] = file_path
                elif 'R2' in file:
                    data[sample]['fastq_2'] = file_path
                matched_files += 1
            except IndexError:
                print(
                    f"Skipping file with unexpected format: {file}")

    df = pd.DataFrame.from_dict(data, orient='index').reset_index().rename(
        columns={'index': 'sample'})
    df['patient'] = patient
    df['sex'] = sex
    df = df[['patient', 'sex', 'status', 'sample', 'lane', 'fastq_1', 'fastq_2']]
    df.to_csv(out_file, index=False)
    print(f"Matched files: {matched_files}")
    print(f"Unmatched files: {unmatched_files}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Get sample information and save to a CSV file.")
    parser.add_argument("path", help="The directory path to search for files.")
    parser.add_argument("patient", help="Patient identifier.")
    parser.add_argument("normal", help="Normal sample identifier.")
    parser.add_argument("out_file", help="Output CSV file path.")
    parser.add_argument("sex", help="Sex of the patient.")

    args = parser.parse_args()

    get_sample_info(args.path, args.patient,
                    args.normal, args.out_file, args.sex)
