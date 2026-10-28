# Soil microbiome data: metadata

**Data file:** `V.profile_bootstrap_cleaned_Oct18_ver4.csv`

The file contains 58 soil samples (rows). Its first six columns describe the samples; the remaining 9,682 columns are operational taxonomic units (OTUs). Each OTU value is the number of 16S rRNA gene sequences assigned to that OTU in that sample. OTUs are numbered rather than identified by taxon name. A zero means no sequences were recorded for that OTU in that sample; it does not prove that the organism was absent.

| Column in CSV | Meaning | Values or units |
| --- | --- | --- |
| First column (blank header; read by R as `X` by default) | Row number. | 1–58; not a confirmed plot identifier. |
| `Cide` | Pesticide treatment. | `Control` (neither pesticide), `Insect` (insecticide), `Mollusc` (molluscicide). |
| `Liming` | Whether lime was added. | `limed`, `unlimed`. |
| `Depth` | Soil sampling depth category, from shallow to deep. | 1 = 0–10 cm; 2 = 10–20 cm; 3 = 20–30 cm; 4 = 30–40 cm; 5 = 40–50 cm. |
| `Moisture` | Soil moisture. | Percent; measurement method is not available. |
| `ATP.biomass` | ATP measured in soil samples, used here as an indicator related to microbial activity. | nmol per gram of soil; `NA` means a missing value (3 samples). Further measurement details are not available. |

## Collection and processing

Soil was collected from a long-running grassland field experiment with liming and pesticide treatments. A 1 cm diameter soil corer was used to sample to 50 cm; each consecutive 10 cm section was pooled to form a depth sample. DNA was extracted, and the 16S rRNA locus was amplified and sequenced. Paired reads were joined and quality-filtered, suspected chimeric sequences were removed, and sequences were clustered into OTUs at 97% similarity. Representative sequences were assigned taxonomy, but this CSV contains numbered OTUs rather than their taxonomic names.

The reported processing included random subsampling (rarefaction). Very rare OTUs with one or two reads may have been removed after subsampling because some could represent sequencing errors. This may help explain why sample totals in this file are below or equal to 5,000 sequences, but the exact subsampling target and filtering steps still need confirmation. See [Mombrikotb et al. (2022)](https://pmc.ncbi.nlm.nih.gov/articles/PMC9804416/) and its supporting information for the published methods.

## Information still needed

Plot and core identifiers, the relationship between rows at different depths, treatment replication and allocation, and the exact subsampling and filtering steps for this file are not currently available. The row number must not be used as a substitute for a plot identifier. These gaps limit conclusions about independence, experimental replication and treatment effects; use the data to explore patterns and generate hypotheses while the design is being clarified.
