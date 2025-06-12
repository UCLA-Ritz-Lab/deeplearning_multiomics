# generating ANNOVAR input

	./make_annovar_input.py snpinfo.txt gwas_pvalues.txt  > gwas_annovar.input
	./make_annovar_input.py cpg_info.txt ewas_pvalues.txt  > ewas_annovar.input

# running ANNOVAR

	annovar/table_annovar.pl gwas_annovar.input annovar/humandb/ -buildver hg19 -out gwas_anno -protocol refGeneWithVer,avsnp151 -operation g,f -remove -nastring . -polish
	annovar/table_annovar.pl ewas_annovar.input annovar/humandb/ -buildver hg19 -out ewas_anno -protocol refGeneWithVer,avsnp151 -operation g,f -remove -nastring . -polish

# make mask

	/make_genemask.py gwas_anno.hg19_multianno.txt snpinfo.txt gwas_pvalues.txt 0.01 snp_mask.pkl snp_rows.pkl snp_cols.pkl peg1casecontrol.header
	./make_genemask.py ewas_anno.hg19_multianno.txt cpg_info.txt ewas_pvalues.txt 0.01 cpg_mask.pkl cpg_rows.pkl cpg_cols.pkl peg1casecontrol.header
