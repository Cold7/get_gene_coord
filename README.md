# get_gene_coord
I start using ENCFF159KBI.gtf from downloaded form ENCODE project, then I created a file called gene_coords.bed with the command 
``awk '{ if ($0 ~ "transcript_id") print $0; else print $0" transcript_id \"\";"; }' ENCFF159KBI.gtf | gtf2bed - | cut -f1-6> gene_coords.bed`` 

so finally with this file I use the python script in this repo
