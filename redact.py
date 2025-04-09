import fitz  # PyMuPDF
import yaml
import os


def load_redactions(config_file="./redactions.yaml"):
    with open(config_file, 'r') as file:
        config = yaml.safe_load(file)
    return config


def redact_pdf(path, output_path, config):
    pdf = fitz.open(path)

    for page_num in range(len(pdf)):
        page = pdf.load_page(page_num)

        if page_num+1 in config.keys():
            redactions = config[page_num+1]
        else :
            redactions = config[0]

        for redaction in redactions:
            rect = fitz.Rect(
                redaction[0] * page.rect.width,
                redaction[1] * page.rect.height,
                redaction[2] * page.rect.width,
                redaction[3] * page.rect.height
            )
            page.add_redact_annot(rect, fill=config["fill"])
        page.apply_redactions()


    pdf.save(output_path)
    pdf.close()


if __name__ == "__main__":
    config = load_redactions()
    
    # load files in subdirectory pdfs
    files = os.listdir("pdfs")

    for file in files:
        redact_pdf(os.path.join("pdfs", file), os.path.join("pdfs_redacted", file[:-4] + "_redacted.pdf"), config)
        print(f"Redacted {file}")