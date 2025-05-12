import sys
import os
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import cairosvg
from pyswf import SWF, Bitmap, Frame

def select_svg_file():
    """Open a file dialog to select an SVG file."""
    Tk().withdraw()  # Hide the root window
    file_path = askopenfilename(
        title="Select an SVG file",
        filetypes=[("SVG files", "*.svg")],
    )
    if file_path and file_path.lower().endswith('.svg'):
        print(f"Selected file: {file_path}")
        return file_path
    else:
        print("No valid SVG file selected.")
        return None

def convert_svg_to_swf(svg_file_path, swf_file_path):
    """
    Convert an SVG file to an SWF file.

    Args:
        svg_file_path (str): Path to the input SVG file.
        swf_file_path (str): Path to the output SWF file.
    """
    try:
        # Convert SVG to PNG using cairosvg
        png_file_path = svg_file_path.replace(".svg", ".png")
        cairosvg.svg2png(url=svg_file_path, write_to=png_file_path)
        print(f"Converted SVG to PNG: {png_file_path}")

        # Create an SWF file and embed the PNG
        swf = SWF()
        bitmap = Bitmap(png_file_path)
        frame = Frame()
        frame.add(bitmap)
        swf.add(frame)

        # Save the SWF file
        with open(swf_file_path, "wb") as swf_file:
            swf_file.write(swf.to_bytes())
        print(f"SWF file created: {swf_file_path}")

    except Exception as e:
        print(f"Error during conversion: {e}")

def main():
    """Main function to handle SVG file selection."""
    print("Welcome to the SVG file loader!")
    svg_file = select_svg_file()
    if svg_file:
        swf_file = svg_file.replace(".svg", ".swf")
        convert_svg_to_swf(svg_file, swf_file)
    else:
        print("Exiting application.")

if __name__ == "__main__":
    main()