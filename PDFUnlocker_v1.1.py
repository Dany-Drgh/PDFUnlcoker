# Version: 1.0
# Dany A. Darghouth
import pikepdf
import os
from tqdm import tqdm
from art import tprint
from time import sleep

directory = None
input_file = None
output_file = None

tprint("PDF Unlocker", font="xcourb")
print("Version: 1.1")

print("Welcome to the PDF Unlocker!, a neat little tool to unlock your PDF files.\n")
print("\33[1mDisclaimer : only unlock PDF files that you own or have permission to unlock.\n\33[0m")
help = input("\nPress Enter to start or type 'help' for usage instructions.\n").strip().lower()
if help == 'help':

    print("\n\33[1mUsage:\33[0m")
    print("1. To unlock all PDF files in a directory, enter the directory path when prompted.")
    print("2. To unlock a single PDF file, enter the file path when prompted.")
    print("3. If not output filename is provided,  the unlocked files will be saved with '_unlocked' suffix in the same location.")
    print("4. If the output file already exists, you will be prompted to overwrite it.\n")
    input("Press Enter to continue...")


user_input = input("\nDo you want to unlock a directory of PDFs? y/N\n").strip().lower()

if user_input == 'y':
    directory = input("Enter the directory path:\n").strip().replace('\\', '/')
    
else:
    input_file = input("Enter the PDF file path:\n").strip()
    output_file = input("Enter the output PDF file path (optional, press Enter to skip):\n").strip()

    if not output_file:
        output_file = os.path.splitext(input_file)[0] + '_unlocked.pdf'


if directory: # Directory mode

    print("\33[1m\33[93m WARNING:\33[0m Directory mode is enabled. All PDF files in the directory will be unlocked.\33[0m")
    # Check if the input file is a directory
    if not os.path.isdir(directory):
        print(f"\33[1m\33[91mERROR:\33[0mThe path '{directory}' is not a directory.")
        input("Press Enter to exit.")
        exit(1)

    # List all PDF files in the directory
    pdf_files = [f for f in os.listdir(directory) if f.endswith('.pdf')]

    if not pdf_files:
        print("\33[1m\33[91mNo PDF files found in the directory.\33[0m")
        input("Press Enter to exit.")
        exit(1)

    converted_files = 0

    for pdf_file in tqdm(pdf_files, desc="Unlocking PDFs", unit="file", bar_format='{desc}: {bar:30} {percentage:3.0f}%'):
        input_path = os.path.join(directory, pdf_file)
        output_path = os.path.join(directory, f"{os.path.splitext(pdf_file)[0]}_unlocked.pdf")
        
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

    print('_____\n\x1B[3m Dany A. Darghouth \x1B[0m')
    sleep(5)
    exit(0)

else:
    # Check if the input file exists
    if not os.path.exists(input_file):
        print(f"\33[1m\33[91mERROR:\33[0m The file '{input_file}' does not exist.\33[0m")
        input("Press Enter to exit.")
        exit(1)

    # Check if the input file is a PDF
    if not input_file.lower().endswith('.pdf'):
        print(f"\33[1m\33[91mERROR:\33[0m The file '{input_file}' is not a PDF file.\33[0m")
        input("Press Enter to exit.")
        exit(1)

    # Check if the output file is provided
    if output_file is None:
        output_file = os.path.splitext(input_file)[0] + '_unlocked.pdf'

    # Check if the output file is a PDF
    if not output_file.lower().endswith('.pdf'):
        print(f"\33[1m\33[91mERROR:\33[0m The file '{output_file}' is not a PDF file.\33[0m")
        input("Press Enter to exit.")
        exit(1)

    # Check if the output file already exists
    if os.path.exists(output_file):
        print(f"\33[93m\33[1mWARNING:\33[0m\33[1mThe file '{output_file}' already exists.\33[0m")
        user_input = input("Continue ? y/N\n").strip().lower()
        if user_input != 'y':
            print("Operation cancelled, closing..")
            print('_____\n\x1B[3m Dany A. Darghouth \x1B[0m')
            sleep(5)
            exit(0)

    # Unlock the PDF file
    try:
        with pikepdf.open(input_file) as pdf:
            pdf.save(output_file)
        print(f"\33[1m\33[92mDone!\33[0m Unlocked '{input_file}' and saved to '{output_file}'.")
        print('_____\n\x1B[3m Dany A. Darghouth \x1B[0m')
        sleep(5)
    except pikepdf.PdfError as e:
        print(f"\33[1m\33[91mERROR unlocking PDF: {e}\33[0m")
        input("Press Enter to exit.")
        exit(1)

