from pathlib import Path
import tkinter as tk
from tkinter import filedialog, messagebox

from pypdf import PdfWriter


def merge_pdfs(pdf_paths, output_path):  # pdf_paths is a list of Path objects
    writer = PdfWriter()

    for pdf_path in pdf_paths: # Iterate over Path objects directly
        writer.append(str(pdf_path))

    with open(output_path, "wb") as output_file:
        writer.write(output_file)

    writer.close()


def select_and_merge(): 
    pdf_paths = filedialog.askopenfilenames(
        title="Select PDF files to merge",
        filetypes=[("PDF files", "*.pdf")],
    )

    if not pdf_paths:
        return

    output_path = filedialog.asksaveasfilename(
        title="Save merged PDF as",
        defaultextension=".pdf",
        filetypes=[("PDF files", "*.pdf")],
        initialfile="merged.pdf",
    )

    if not output_path: # User cancelled the save dialog
        return

    try:
        merge_pdfs([Path(pdf) for pdf in pdf_paths], output_path) # Convert to Path objects
    except Exception as error:
        messagebox.showerror("Merge failed", str(error))
        return

    messagebox.showinfo("Success", f"Merged PDF saved to:\n{output_path}")


root = tk.Tk()
root.title("PDF Merger")
root.geometry("360x180")
root.resizable(False, False)

label = tk.Label(
    root,
    text="Choose PDF files and merge them into one document.",
    wraplength=300,
    justify="center",
)
label.pack(pady=25)

merge_button = tk.Button(root, text="Select PDFs and Merge", command=select_and_merge, padx=16, pady=8)
merge_button.pack()

root.mainloop()