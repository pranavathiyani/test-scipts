def filter_fasta(fasta_file, headers_file, output_file):
    with open(headers_file, 'r') as f:
        headers = {line.strip() for line in f}

    with open(fasta_file, 'r') as f, open(output_file, 'w') as out:
        write = False
        for line in f:
            if line.startswith('>'):
                header = line.strip()[1:]
                write = header not in headers
            if write:
                out.write(line)


filter_fasta('Mab.fasta', 'res_headers.txt', 'Mab_nomatch.fasta')
