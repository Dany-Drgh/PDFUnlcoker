# PDFUnlocker - Unlock Password-Free PDF Files

**Version:** 1.1  
**Author:** Dany A. Darghouth  
**License:** MIT  
**Platform:** Windows (.exe) or cross-platform (Python script)

---

## 📝 Description

**PDFUnlocker** is a lightweight utility that unlocks PDF files that are password-protected for editing, copying, or printing (but *do not require a password to open*).

It works in two modes:

- **Single File Mode:** Unlock one PDF file.
- **Directory Mode:** Unlock all PDFs in a folder.

---

## 💡 Key Features

- 🔓 Unlocks restrictions on PDFs using `pikepdf`
- 📁 Supports both individual files and batch processing of folders
- 📦 Available as a standalone executable (no Python needed!)

---

## 📥 Download & Installation

You can download the standalone `.exe` file from the [releases section of this repository](https://github.com/Dany-Drgh/PDFUnlcoker/releases). This executable is built using `PyInstaller` and includes all necessary dependencies, so you can simply download it, extract it, and run it directly — no installation required.

If you're using the Python script instead, continue below.

---

## 🖥️ Usage (Executable)

Once you have the `PDFUnlocker.exe` file, you can run it directly from the command line or by double-clicking it. The program will prompt you for the necessary inputs.

- **Help Mode:** Run the executable and type `help` to see usage instructions.
- **Directory Mode:** Run the executable and specify a directory to unlock all PDF files within it.
- **Single File Mode:** Run the executable and follow the prompts to unlock a single PDF file.

## Contact & Support

For any questions, issues, or feature requests, please open an issue in the GitHub repository or contact me directly, either on GitHub, via email at 
danydarghouth@gmail.com, or on X at [@dany_drgh
](https://x.com/dany_drgh).

## 📜 Usage (Python Script)

### Requirements
- Python 3.x
- `pikepdf` library (install via `pip install pikepdf`)
- `tqdm` library (install via `pip install tqdm`)
- `argparse` library (install via `pip install argparse`)

- `PyInstaller` *(used only to create an executable from the PDFUnlocker.py script not used  CLI_PDFUnlocker_v1.1.py)*

 All dependencies are included in the `requirements.txt` file. To install all dependencies, run the following command in your terminal:

```bash
pip install -r requirements.txt
```

### CLI Usage

> ⚠️ **NOTE:** Although running `PDFUnlocker.py` directly is possible, it is recommended to use the `CLI_PDFUnlocker_v1.1.py` script for command line usage, as it provides a better argument parser and user experience.

```bash
python CLI_PDFUnlocker_v1.1.py [-h] [-d DIRECTORY] [-i INPUT_FILE] [-o OUTPUT_FILE]
```

### Arguments

- `-h`, `--help`            show this help message and exit

- `-d DIRECTORY`, `--directory DIRECTORY`
                    Directory mode: unlock all PDFs in the directory and save them with "_unlocked" suffix

- `-i INPUT_FILE`, `--input_file INPUT_FILE`
                    Path to the input PDF file, required if not in directory mode

- `-o OUTPUT_FILE`, `--output_file OUTPUT_FILE`
                    Path to the output PDF file (when not in directory mode) (optional), defaults to input_file_unlocked.pdf

---
*Dany A. Darghouth - April 2025*