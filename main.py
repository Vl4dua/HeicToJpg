import os
from PIL import Image
import pillow_heif

def convert_heic_to_jpeg(input_path, output_path):
    try:
        # Leggi il file HEIC
        heif_file = pillow_heif.read_heif(input_path)
        
        # Converti l'immagine HEIC a un oggetto Image di PIL
        image = Image.frombytes(
            heif_file.mode, 
            heif_file.size, 
            heif_file.data,
            "raw",
            heif_file.mode,
            heif_file.stride,
        )
        
        # Salva l'immagine come JPEG
        image.save(output_path, "JPEG")
        print(f"Converted {input_path} to {output_path}")
    except Exception as e:
        print(f"Failed to convert {input_path}: {e}")

def batch_convert_heic_to_jpeg(input_dir):
    output_dir = os.path.join(input_dir, 'converted_jpegs')
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for filename in os.listdir(input_dir):
        input_path = os.path.join(input_dir, filename)
        if filename.lower().endswith(".heic"):
            output_path = os.path.join(output_dir, os.path.splitext(filename)[0] + ".jpg")
            convert_heic_to_jpeg(input_path, output_path)
        else:
            print(f"Skipping non-HEIC file: {input_path}")

if __name__ == "__main__":
    input_directory = input("Please enter the path to the folder containing HEIC files: ")
    if os.path.isdir(input_directory):
        batch_convert_heic_to_jpeg(input_directory)
        print("Conversion complete!")
    else:
        print("The specified directory does not exist.")
