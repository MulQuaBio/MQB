# Soil microbiome data: metadata

**Data file:** `V.profile_bootstrap_cleaned_Oct18_ver4.csv`

The file contains 58 soil samples (rows). Its first six columns describe the samples; the remaining 9,682 columns are operational taxonomic units (OTUs). Each OTU value is the number of 16S rRNA gene sequences assigned to that OTU in that sample. OTUs are numbered rather than identified by taxon name. A zero means no sequences were recorded for that OTU in that sample; it does not prove that the organism was absent.

| Column in CSV | Meaning | Values or units |
| --- | --- | --- |
| First column (blank header; read by R as `X` by default) | Row number. | 1–58; not a confirmed plot identifier. |
| `Cide` | Pesticide treatment. | `Control` (neither pesticide), `Insect` (insecticide), `Mollusc` (molluscicide). |
| `Liming` | Whether lime was added. | `limed`, `unlimed`. |
| `Depth` | Soil sampling depth category, from shallow to deep. | 1–5; physical depths and units are not available. |
| `Moisture` | Soil moisture. | Percent; measurement method is not available. |
| `ATP.biomass` | ATP measured in soil samples, used here as an indicator related to microbial activity. | Units and measurement details are not available; `NA` means a missing value (3 samples). |

## Collection and processing

Soil was collected from a long-running grassland field experiment with liming and pesticide treatments. DNA was extracted, the 16S rRNA locus amplified and sequenced, and reads processed using QIIME; sequences were clustered into OTUs at 97% similarity. Samples with more than approximately 5,000 sequences were reportedly randomly subsampled to approximately 5,000 sequences. Exact processing and subsampling details need confirmation.

## Information still needed

Plot identifiers, the relationship between samples at different depths, physical depth ranges, treatment replication and allocation, sequencing details, and the exact rarefaction procedure are not currently available. The row number must not be used as a substitute for a plot identifier. These gaps limit conclusions about independence, experimental replication and treatment effects; use the data to explore patterns and generate hypotheses while the design is being clarified.
