f = open("gene_coords.bed","r") #gene_coord.bed lo saque con bedops de esta forma (el awk es para evitar el error de missing transcript)
#awk '{ if ($0 ~ "transcript_id") print $0; else print $0" transcript_id \"\";"; }' ENCFF159KBI.gtf | gtf2bed - | cut -f1-6> gene_coords.bed 
data = {}
for line in f:
	aux = line[:-1].split("\t")
	chr = aux[0]
	init = aux[1]
	end = aux[2]
	gene = aux[3].split(".")[0]
	geneID = chr+"_"+gene
	strand = aux[5]
	if id not in data:
		data[geneID] = {"chr":chr, "gene":gene,"init": init,"end":end}

	else:
		data[geneID]["end"] = end
	

for gene in data:
	print(data[gene]["chr"]+"\t"+data[gene]["gene"]+"\t"+data[gene]["init"]+"\t"+data[gene]["end"])
