# qrcode-generator
A simple Python script to generate a QR code from a user-provided link and save it as a PNG image.

# 🔗 QR Code Generator

A simple command-line Python script that generates a QR code from any link provided by the user and saves it as a PNG image file.

## Requirements

Before running the script, you need to install the `qrcode` library, which also requires `Pillow` for image processing. You can install it using pip:

```sh
pip install qrcode[pil]
```

## How to Use

1.  Ensure you have Python and pip installed.
2.  Install the required library by running the command above.
3.  Save the code as a `.py` file (e.g., `qr_code_generator.py`).
4.  Run the script from your terminal:
    ```sh
    python qr_code_generator.py
    ```
5.  When prompted, enter the full link you want to convert into a QR code.
6.  The script will generate the QR code and save it as `myqrcode.png` in the same directory. A confirmation message will be displayed in the terminal.

## Example

```sh
> python qr_code_generator.py
-=--=--=--=--=--=--=--=--=--=--=--=--=--=--=-
QR Code generator

Enter a link to generate a QR Code:
https://www.google.com
QR Code Generated, saved as myqrcode.png

-=--=--=--=--=--=--=--=--=--=--=--=--=--=--=-
```
