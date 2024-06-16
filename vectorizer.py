#!/usr/bin/env python
# -*- coding: utf-8 -*-

import typer
from PIL import Image, ImageChops

def remove_background(input_image_path: str, output_image_path: str, background_color_hex: str):
    # Convert hex color to RGB
    background_color = tuple(int(background_color_hex[i:i+2], 16) for i in (0, 2, 4))
    
    # Load the image
    img = Image.open(input_image_path).convert("RGB")
    
    # Create a background image of the same size and color
    background = Image.new("RGB", img.size, background_color)
    
    # Compute the difference
    diff = ImageChops.difference(img, background).convert("L")
    
    # Threshold the difference
    mask = diff.point(lambda p: p > 50 and 255)
    
    # Apply the mask
    result = Image.composite(img, background, mask)
    
    # Save the result
    result.save(output_image_path)
    print(f"Processed image saved to {output_image_path}")

def main(input_image_path: str = typer.Argument(..., help="Path to the input image file"),
         output_image_path: str = typer.Argument(..., help="Path to save the cleaned image file"),
         background_color_hex: str = typer.Option("efece0", "--color", "-c", help="Background color in hex to remove")):
    """
    This script removes a specified background color from an image.
    """
    remove_background(input_image_path, output_image_path, background_color_hex)

if __name__ == "__main__":
    typer.run(main)


