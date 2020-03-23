
import GFFutils

G = GFFutils.GFFDB('dm3.db')
exon_len = []
exon1 = []
exon2 = []
exon3 = []
exon_3 = []
exon_2 = []
exon_1 = []
intron1 = []
intron2 = []
intron3 = []
intron_3 = []
intron_2 = []
intron_1 = []

gene_count = 0
for mRNA in G.features_of_type('mRNA'):
#    print(mRNA)
    exons = list(G.children(mRNA, featuretype='exon'))
    introns = list(G.interfeatures(exons))
    if mRNA.strand == "-":
        first_3_exons = exons[-3:]
        last_3_exons = exons[:3]
        first_3_introns = introns[-3:]
        last_3_introns = introns[:3]
    else:
        first_3_exons = exons[:3]
        last_3_exons = exons[-3:]
        first_3_introns = introns[:3]
        last_3_introns = introns[-3:]

    for idx, ele in enumerate(first_3_exons):
        ele = len(ele)
        if int(idx) == 0:
            exon1.append(ele)
        elif int(idx) == 1:
            exon2.append(ele)
        elif int(idx) == 2:
            exon3.append(ele)

    for idx, ele in enumerate(last_3_exons):
        ele = len(ele)
        if int(idx) == 0:
            exon_3.append(ele)
        elif int(idx) == 1:
            exon_2.append(ele)
        elif int(idx) == 2:
            exon_1.append(ele)
 
    for idx, ele in enumerate(first_3_introns):
        ele = len(ele)
        if int(idx) == 0:
            intron1.append(ele)
        elif int(idx) == 1:
            intron2.append(ele)
        elif int(idx) == 2:
            intron3.append(ele)

    for idx, ele in enumerate(last_3_introns):
        ele = len(ele)
        if int(idx) == 0:
            intron_3.append(ele)
        elif int(idx) == 1:
            intron_2.append(ele)
        elif int(idx) == 2:
            intron_1.append(ele)

#    print ("length of first 3 exons: ", len(ele))

#    print("First 3 exons: ", first_3_exons)
#    print("Last 3 exons: ", last_3_exons)



print sum(exon1)/len(exon1)
print("exon1: ", sum(exon1)/len(exon1),len(exon1))
print("exon2: ",sum(exon2)/len(exon2),len(exon2))
print("exon3: ",sum(exon3)/len(exon3),len(exon3))
print("exon_3: ",sum(exon_3)/len(exon_3), len(exon_3))
print("exon_2: ",sum(exon_2)/len(exon_2), len(exon_2))
print("exon_1: ",sum(exon_1)/len(exon_1), len(exon_1))

print("intron1: ",sum(intron1)/len(intron1),len(intron1))
print("intron2: ",sum(intron2)/len(intron2),len(intron2))
print("intron3: ",sum(intron3)/len(intron3),len(intron3))
print("intron_3: ",sum(intron_3)/len(intron_3), len(intron_3))
print("intron_2: ",sum(intron_2)/len(intron_2), len(intron_2))
print("intron_1: ",sum(intron_1)/len(intron_1), len(intron_1))

