# Apparel & Textiles — Data Landscape Strategy

Week 1 internship project for **Data Landscape Strategy and Planning**.

## Objective
Build a practical, reproducible data foundation for apparel and textiles analytics using authoritative public sources. The project focuses on trade, production, labour, raw materials and textile circularity.

## Core public sources
1. UN Comtrade — bilateral merchandise trade by reporter, partner and product.
2. World Bank WITS — trade, tariff and market-access analytics.
3. WTO Statistics — global merchandise trade indicators.
4. Eurostat PRODCOM — EU industrial production by product.
5. ILOSTAT / ILO sector resources — employment and labour indicators.
6. FAOSTAT / OECD-FAO — cotton and upstream agricultural indicators.
7. European Environment Agency — textile consumption, waste and circularity indicators.

## Project design
The project follows a simple **Textile Data Spine**:

`Raw → Standardized → Validated → Analytical → Presentation`

Raw files are never overwritten. Source metadata, quality flags and transformation rules are retained.

## Repository structure
```text
apparel-textile-data-landscape/
├── README.md
├── LICENSE
├── requirements.txt
├── .gitignore
├── report/
│   └── Week_1_Data_Landscape_Strategy.docx
├── config/
│   └── source_register.csv
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
│   └── 01_data_landscape_eda.ipynb
├── src/
│   ├── ingestion.py
│   ├── cleaning.py
│   ├── validation.py
│   └── metrics.py
└── outputs/
    ├── figures/
    └── tables/
```

## Reproducibility
This repository intentionally does **not** contain fabricated or redistributed datasets. Download data from the official portals listed in `config/source_register.csv`, place source files in `data/raw/`, then run the scripts.

Example:
```bash
python src/cleaning.py
python src/validation.py
python src/metrics.py
```

The scripts are designed to work with a simple CSV containing:
- `reporter`
- `partner`
- `product_code`
- `year`
- `trade_value_usd`
- `quantity_kg`

If a source uses different field names, map them in the cleaning step and preserve the original columns.

## Suggested next analysis
- YoY trade growth
- Partner share and HHI concentration
- Export market share
- Revealed Comparative Advantage (RCA)
- Production vs export growth
- Labour/productivity context
- Textile waste and circularity indicators

## Data quality principles
- Never treat missing as zero.
- Preserve source codes and original units.
- Keep raw and processed data separate.
- Flag outliers instead of deleting them automatically.
- Record download dates and source revisions.
- Document classification mappings.

## Report
The submission-ready report is in `report/Week_1_Data_Landscape_Strategy.docx`.


## Included real dataset

This repository includes a small **real official-data extract** from the European Environment Agency (EEA) Circularity Metrics Lab. It contains published EU textile indicators such as textile consumption, textile waste generation, capture rate, treatment share, raw-material use, GHG emissions, synthetic-fibre share, reuse and used-textile exports.

The raw extract is:
`data/raw/eea_textile_indicators.csv`

It is intentionally small and transparent: each row includes the indicator, year, value, unit, geography, source and official source URL. The values were transcribed from the corresponding EEA indicator pages and are not synthetic data.

## Run the included analysis

```bash
pip install -r requirements.txt
python src/ingestion.py
python src/cleaning.py
python src/validation.py
python src/metrics.py
```

The repository already contains generated outputs:
- `outputs/tables/validation_summary.csv`
- `outputs/tables/indicator_summary.csv`
- `outputs/tables/percentage_indicators.csv`
- `outputs/tables/analysis_insights.md`
- `outputs/figures/eea_circularity_indicators.png`

## What the first analysis demonstrates

The included analysis is a **minimum viable data-science pipeline**: official-source ingestion → cleaning → validation → descriptive metrics → visualization → business interpretation. It is designed to be extended later with UN Comtrade/WITS trade data, Eurostat production data and ILO labour indicators.
