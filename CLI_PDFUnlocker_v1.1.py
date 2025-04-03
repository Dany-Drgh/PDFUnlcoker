# Version: 1.0
# Dany A. Darghouth
import pikepdf
import os
import argparse
from tqdm import tqdm

# Parse arguments
parser = argparse.ArgumentParser(description='Unlock a PDF file using pikepdf.')
parser.add_argument('-d', '--directory', type=str, help='Directory mode: unlock all PDFs in the directory and save them with "_unlocked" suffix')
parser.add_argument('-i','--input_file', type=str, help='Path to the input PDF file, required if not in directory mode')
parser.add_argument('-o', '--output_file', type=str, help='Path to the output PDF file (when not in directory mode) (optional), defaults to input_file_unlocked.pdf')
args = parser.parse_args()

if args.directory: # Directory mode

    print("\33[1m\33[93m WARNING:\33[0m Directory mode is enabled. All PDF files in the directory will be unlocked.\33[0m")
    # Check if the input file is a directory
    if not os.path.isdir(args.directory):
        print(f"\33[1m\33[91mERROR:\33[0mThe path '{args.directory}' is not a directory.")
        exit(1)

    # List all PDF files in the directory
    pdf_files = [f for f in os.listdir(args.directory) if f.endswith('.pdf')]

    if not pdf_files:
        print("\33[1m\33[91mNo PDF files found in the directory.\33[0m")
        exit(1)

    converted_files = 0

    for pdf_file in tqdm(pdf_files, desc="Unlocking PDFs", unit="file", bar_format='{desc}: {bar:30} {percentage:3.0f}%'):
        input_path = os.path.join(args.directory, pdf_file)
        output_path = os.path.join(args.directory, f"{os.path.splitext(pdf_file)[0]}_unlocked.pdf")
        
        # Unlock the PDF file
        try:
            with pikepdf.open(input_path) as pdf:
                pdf.save(output_path)
                converted_files += 1
        except pikepdf.PdfError as e:
            print(f"\33[1m\33[91mERROR\33[0m unlocking PDF '{input_path}': {e}\33[0m")
   
    if converted_files == len(pdf_files):
        print(f"\33[1m\33[92mUnlocked {converted_files} out of {len(pdf_files)} files\33[0m")
    else:
        print(f"\33[1mUnlocked {converted_files} out of {len(pdf_files)}\33[0m")
        print("\33[1m\33[93mSome files could not be unlocked.\33[0m")
    exit(0)

else:
    # Check if the input file exists
    if not os.path.exists(args.input_file):
        print(f"\33[1m\33[91mERROR:\33[0m The file '{args.input_file}' does not exist.\33[0m")
        exit(1)

    # Check if the input file is a PDF
    if not args.input_file.lower().endswith('.pdf'):
        print(f"\33[1m\33[91mERROR:\33[0m The file '{args.input_file}' is not a PDF file.\33[0m")
        exit(1)

    # Check if the output file is provided
    if args.output_file is None:
        args.output_file = os.path.splitext(args.input_file)[0] + '_unlocked.pdf'

    # Check if the output file is a PDF
    if not args.output_file.lower().endswith('.pdf'):
        print(f"\33[1m\33[91mERROR:\33[0m The file '{args.output_file}' is not a PDF file.\33[0m")
        exit(1)

    # Check if the output file already exists
    if os.path.exists(args.output_file):
        print(f"\33[93m\33[1mWARNING:\33[0m\33[1mThe file '{args.output_file}' already exists.\33[0m")
        user_input = input("Continue ? y/N\n").strip().lower()
        if user_input != 'y':
            print("Operation cancelled, closing..")
            exit(0)

    # Unlock the PDF file
    try:
        with pikepdf.open(args.input_file) as pdf:
            pdf.save(args.output_file)
        print(f"\33[1m\33[92mDone!\33[0m Unlocked '{args.input_file}' and saved to '{args.output_file}'.")
    except pikepdf.PdfError as e:
        print(f"\33[1m\33[91mERROR unlocking PDF: {e}\33[0m")
        exit(1)