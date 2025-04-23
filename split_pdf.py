import os
import PyPDF2

def split_pdf(input_pdf_path, output_parent_dir, page_ranges):
    # Extract the input PDF file name without the extension
    input_pdf_name = os.path.splitext(os.path.basename(input_pdf_path))[0]
    
    # Create a directory with the PDF name
    output_dir = os.path.join(output_parent_dir, input_pdf_name)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Open the input PDF file
    with open(input_pdf_path, "rb") as input_file:
        reader = PyPDF2.PdfReader(input_file)

        # Loop through the page ranges
        for idx, page_range in enumerate(page_ranges):
            start, end = page_range
            writer = PyPDF2.PdfWriter()

            # Add pages in the specified range
            for page_num in range(start - 1, end):  # Page numbers are 0-indexed in PyPDF2
                writer.add_page(reader.pages[page_num])

            # Create a custom output filename based on the page range
            range_str = f"{start}-{end}" if start != end else f"{start}"
            output_pdf_name = f"{input_pdf_name}_{range_str}.pdf"
            output_pdf_path = os.path.join(output_dir, output_pdf_name)

            # Write the current range to a separate PDF
            with open(output_pdf_path, "wb") as output_file:
                writer.write(output_file)

            print(f"PDF for pages {range_str} has been saved as {output_pdf_path}")


if __name__ == "__main__":
    input_pdf_path = r"your-path"
    output_parent_dir = r"your-path"
    
    page_ranges = [
        (1, 5), (6, 6), (7, 16), (17, 26), (66, 92), (93, 116),
        (132, 135), (137, 137), (142, 142), (143, 168), (169, 169),
        (170, 171), (172, 176), (178, 181), (187, 188), (189, 191),
        (198, 211), (244, 402), (419, 431)
    ]
    
    split_pdf(input_pdf_path, output_parent_dir, page_ranges)





