# getting candidate SNPs and CPGs


	cut -f3,6 top_results_5.tsv  |grep -v snp_id > gwas_pvalues.txt
	cut -f4,6 top_results_5.tsv  |grep -v gene > ewas_pvalues.txt

# generating ANNOVAR input

	./make_annovar_input.py snp_info.txt gwas_pvalues.txt  > gwas_annovar.input
	./make_annovar_input.py cpg_info.txt ewas_pvalues.txt  > ewas_annovar.input

# running ANNOVAR

	annovar/table_annovar.pl gwas_annovar.input annovar/humandb/ -buildver hg19 -out gwas_anno -protocol refGeneWithVer,avsnp151 -operation g,f -remove -nastring . -polish
	annovar/table_annovar.pl ewas_annovar.input annovar/humandb/ -buildver hg19 -out ewas_anno -protocol refGeneWithVer,avsnp151 -operation g,f -remove -nastring . -polish

# make gene mask

	./make_genemask.py gwas_anno.hg19_multianno.txt snp_info.txt gwas_pvalues.txt 0.01 snp_mask snp_rows snp_cols peg1casecontrol.header
	./make_genemask.py ewas_anno.hg19_multianno.txt cpg_info.txt ewas_pvalues.txt 0.01 cpg_mask cpg_rows cpg_cols peg1casecontrol.header

# pathway mask
	
	./make_pathwaymask.py CPDB_pathways_genes.tab snp_cols.txt snpgene_mask snpgene_rows snpgene_cols
	./make_pathwaymask.py CPDB_pathways_genes.tab cpg_cols.txt cpggene_mask cpggene_rows cpggene_cols
