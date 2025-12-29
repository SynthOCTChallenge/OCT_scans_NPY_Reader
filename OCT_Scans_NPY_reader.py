# =============================================================================
# Skin OCT scans reader for dataset DOI: {will be provided soon}
#
# Created by: Dr. Lev Matveev, OpticElastograph LLC
# =============================================================================

import numpy as np
import matplotlib.pyplot as plt
import os

def read_oct_file(filepath):
    """
    Reads a .npy file from the specified path.
    
    Args:
        filepath (str): Full path to the .npy file.
        
    Returns:
        numpy.ndarray: The 2D array containing the OCT scan data, or None if failed.
    """
    if not os.path.exists(filepath):
        print(f"Error: File not found at: {filepath}")
        return None

    try:
        # Load the data
        scan_data = np.load(filepath)
        
        # Print basic info to console
        print(f"Successfully loaded: {os.path.basename(filepath)}")
        print(f"Data shape: {scan_data.shape}")
        print(f"Data type: {scan_data.dtype}")
        
        return scan_data
        
    except Exception as e:
        print(f"Error reading the file: {e}")
        return None

def visualize_oct_scan(scan_data, filename):
    """
    Visualizes the 2D OCT scan data in a figure window.
    
    Args:
        scan_data (numpy.ndarray): The 2D array to visualize.
        filename (str): Name of the file for the plot title.
    """
    if scan_data is None:
        return

    # Create a figure
    plt.figure(figsize=(10, 6))
    
    # Display the image
    # cmap='gray': Standard grayscale for OCT
    # aspect='auto': Stretches the image to fill the window
    # vmin=0, vmax=255: Ensures consistent brightness scaling for 8-bit data
    plt.imshow(scan_data, cmap='gray', aspect='auto', vmin=0, vmax=255)
    
    # Add labels and colorbar
    plt.colorbar(label='Signal (a.u.)')
    plt.title(f"OCT B-Scan: {filename}")
    plt.xlabel('Lateral Position (pixels)')
    plt.ylabel('Depth (pixels)')
    
    # Adjust layout and show
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # -------------------------------------------------------------------------
    # SETTINGS: Define the file path here
    # -------------------------------------------------------------------------
    # Example path. Replace this string with the actual path to your .npy file.
    # Use 'r' before the string to handle backslashes in Windows paths correctly.
    FILE_PATH = r"S:\DATASET_NPY\Male\1990-2000\Cheek\shcheka_lev_frame450.npy"
    
    # -------------------------------------------------------------------------
    # EXECUTION
    # -------------------------------------------------------------------------
    print("--- Starting OCT Reader ---")
    
    # 1. Read the file
    oct_data = read_oct_file(FILE_PATH)
    
    # 2. Visualize the data
    if oct_data is not None:
        visualize_oct_scan(oct_data, os.path.basename(FILE_PATH))
        
    print("--- Done ---")
