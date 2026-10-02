mkdir -p data/gonl
for chr in {1..22}; do
  wget -P data/gonl/ "https://download.molgeniscloud.org/downloads/gonl_public/variants/release5/gonl.chr${chr}.snps_indels.r5.vcf.gz"
done
wget -P data/gonl/ "https://download.molgeniscloud.org/downloads/gonl_public/variants/release5/gonl.SV.r5.vcf.gz"
