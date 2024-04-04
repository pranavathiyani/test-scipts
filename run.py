import subprocess

def read_srr_ids_from_file(file_path):
    """
    Reads SRR IDs from a text file (one SRR ID per line).

    Args:
        file_path (str): Path to the file containing SRR IDs.

    Returns:
        list: List of SRR IDs.
    """
    try:
        with open(file_path, "r") as file:
            srr_ids = [line.strip() for line in file]
            return srr_ids
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return []

def download_fastq_files(srr_ids, output_directory="."):
    """
    Downloads FASTQ files for a list of SRR IDs using fasterq-dump.

    Args:
        srr_ids (list): List of SRR IDs.
        output_directory (str): Directory where the downloaded files will be saved.
    """
    for srr_id in srr_ids:
        try:
            # Run fasterq-dump command
            subprocess.run(["fasterq-dump", srr_id], check=True, cwd=output_directory)
            print(f"Downloaded FASTQ files for {srr_id}")
        except subprocess.CalledProcessError:
            print(f"Error downloading FASTQ files for {srr_id}")

# Example usage
if __name__ == "__main__":
    input_file_path = "SRR_Acc_List.txt"  # Update with your file path
    srr_ids_to_download = read_srr_ids_from_file(input_file_path)
    if srr_ids_to_download:
        download_fastq_files(srr_ids_to_download, output_directory="./fastq_data")
    else:
        print("No valid SRR IDs found in the input file.")
