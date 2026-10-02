import gzip
import json

DATA_DIR = "/sandbox/data/gonl"

files = [
    *[
        (f"GoNL chr{chrom}", f"{DATA_DIR}/gonl.chr{chrom}.snps_indels.r5.vcf.gz")
        for chrom in range(1, 23)
    ],
    ("GoNL SV", f"{DATA_DIR}/gonl.SV.r5.vcf.gz"),
]

results = []

for label, vcf_path in files:
    pass_count = 0
    inaccessible_count = 0

    with gzip.open(vcf_path, "rt") as vcf:
        for line in vcf:
            if line.startswith("#"):
                continue

            fields = line.rstrip("\n").split("\t")
            filter_value = fields[6]

            if filter_value == "PASS":
                pass_count += 1
            elif filter_value == "Inaccessible":
                inaccessible_count += 1

    total = pass_count + inaccessible_count
    inaccessible_percentage = (
        100 * inaccessible_count / total if total else 0.0
    )

    results.append({
        "dataset": label,
        "PASS": pass_count,
        "Inaccessible": inaccessible_count,
        "total": total,
        "Inaccessible_percentage": round(inaccessible_percentage, 2),
    })

print(json.dumps(results, separators=(",", ":")))
