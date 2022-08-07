# This script writes a transcript class that uses a line of the 'ensembl_short.txt' file (in the motif_finder_homework folder)  and creates attributes.
# Then it parses the 'ensembl_short.txt' file, create class instances for each transcript and store them in a dictionary, with key as 
#the transcriptID and the value as the object itself. 
# Later, it uses  the api of togows.org to fetch the data that is needed and finds the transcripts containing any of the motifs below and generates a file 
#for the output.
  
mtfs = {"BCL6": "[TA].CTTTC.AGG[AG]AT", "SP1": "[GT]GGGCGG[GA][GA][CT]", "AP1": "TGA[GC]TCA", "NF-I": "TTGGC.{5}GCCAA"}

import re
import requests

def reverse_complement(dna):
    complement = dna.replace("A", "t").replace("T", "a").replace("G", "c").replace("C", "g")
    complement.upper()
    reverse_complement = complement[::-1]
    return reverse_complement

class Transcript():
    def __init__(self,transcriptID,chrNumber,strand, gene,txStart, txEnd ):
        self.transcriptID = transcriptID
        self.chrNumber = chrNumber
        self.strand = strand
        self.gene = gene
        self.txStart = int(txStart)
        self.txEnd = int(txEnd)
    def promoterSequenceFetcher(self):
        if self.strand == "+":
            promoter_start = self.txStart - 5000
            togows = f"http://togows.org/api/ucsc/hg19/{chrNumber}:{promoter_start}-{self.txStart}"
            self.promotersequence = requests.get(togows).text
            return self.promotersequence
        else:
            promoter_start = self.txEnd + 5000
            togows = f"http://togows.org/api/ucsc/hg19/{chrNumber}:{self.txEnd}-{promoter_start}"
            self.promotersequence = reverse_complement(requests.get(togows).text)
            return self.promotersequence

mtfs = {"BCL6": "[TA].CTTTC.AGG[AG]AT", "SP1": "[GT]GGGCGG[GA][GA][CT]", "AP1": "TGA[GC]TCA", "NF-I": "TTGGC.{5}GCCAA"}

ens = 'C:\\Users\\HP\\PycharmProjects\\Hw6\\ensembl_kisa.txt'
data = {} # chr1: [[genomiclength, name]), .....]
with open(ens) as infh:
    for line in infh:
        if line.startswith('#'):continue
        boluk = line.split('\t')
        transcriptID = boluk[1]
        chrNumber = boluk[2]
        strand = boluk[3]
        gene = boluk[12]
        txStart = boluk[4]
        txEnd = boluk[5]
        if transcriptID not in data:
            data[transcriptID] = Transcript(transcriptID,chrNumber,strand, gene,txStart,txEnd)

with open("output", "w") as infhh:
    infhh.write(f"TF_name	TranscriptID	#recog_sites	seq_recog_site	start	end\n")
    for j,l in data.items():
       promoter_sequence = l.promoterSequenceFetcher()
       for tf_name,pattern in mtfs.items():
           x = re.search(pattern,promoter_sequence)
           y = re.findall(pattern,promoter_sequence)
           if x != None:
               a = x.span()
               b = x.group()
               infhh.write(f"{tf_name}\t{j}\t{len(y)}\t{b}\t{a[0]}\t{a[1]}\n")
