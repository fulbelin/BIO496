#This script uses the "ensembl_hg19.txt" file (in the longest_gene_homework folder) and writes a script that finds the following:
1- Average number of exons in the transcriptome
4- The longest gene on the plus strand
5- The longest gene in the minus strand
# and writes the calculations into a file that is called "outfile.txt".

with open('output_file.txt', 'w') as f:
    my_dict = {}
    my_dict_2 = {"+": {}, "-": {}}
    exon_count = []
    cds_dif_plus = []
    cds_dif_neg = []
    gene_names_plus = []
    gene_names_neg = []
    with open("ensembl_kisa.txt", "r") as myfile:
        header = myfile.readline()
        my_keys = header.strip().split("\t")
        lines = myfile.readlines()
        for line in lines:
            my_values = line.strip().split("\t")
            exon_count.append(int(my_values[8]))
            if my_values[3] == "+":
                cds_dif_plus.append(int(my_values[7]) - int(my_values[6]))
                gene_names_plus.append(my_values[12])
            else:
                cds_dif_neg.append(int(my_values[7]) - int(my_values[6]))
                gene_names_neg.append(my_values[12])

    avg = sum(exon_count) / len(exon_count)
    print("1- Average number of exons in the transcriptome :", str(avg))

    max = cds_dif_plus[0]
    index = 0
    for i in range(0, len(cds_dif_plus)):
        if cds_dif_plus[i] > max:
            max = cds_dif_plus[i]
            index = i

    print("4-The longest gene in the plus strand:", str(gene_names_plus[index]))

    max = cds_dif_neg[0]
    index = 0
    for i in range(0, len(cds_dif_neg)):
        if cds_dif_neg[i] > max:
            max = cds_dif_neg[i]
            index = i

    print("5-The longest gene in the negative strand:", str(gene_names_neg[index]))

    f.write("1- Average number of exons in the transcriptome :" + f"{avg}\n")

    f.write("4-The longest gene in the plus strand:" + f"{gene_names_plus[index]}\n")

    f.write("5-The longest gene in the negative strand:" + f"{gene_names_neg[index]}\n")
