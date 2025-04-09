# Multi PDF Redactor

A quick way of redacting multiple PDFs that have similar layouts. This repository works best for PDFs where specific content appears in the same positions across multiple pages, and redacting these.


### Repository Structure  

- 📂 `pdfs/`: Folder for PDFs to redact
- 📂 `pdfs_redacted/`: Output folder for redacted PDFs  
- 📄 `redact.py`: Python script to redact all files in `pdfs/` folder
- 📄 `redactions.yaml`: Configuration file that defines the locations for redacting content in the PDFs

## Getting Started

### Requirements
- Python (≥ 3.0)

### Setup
Clone repository and install [PyMuPDF](https://pymupdf.readthedocs.io/en/latest/index.html) dependency:  
```bash
git clone https://github.com/Elizabeth-Flx/pdf-redacter.git
cd pdf-redacter
pip install PyMuPDF  
```

### How to Use

1. Put PDFs that require redacting into `/pdfs` folder
2. Edit `redactions.yaml` to specify the redaction areas for your PDFs. (For more details, check the explanations in the YAML file itself)
    - Tip: Use a bright color for the redaction fill when testing to easily visualize the areas being redacted.
3. Run the script using:
```bash
python redact.py
```
