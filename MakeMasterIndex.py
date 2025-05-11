import os
import pandas as pd

# Root directory where all phase folders are located
root_dir = "./SSOT/"
output_dir = "./SSOT/"
master_df = pd.DataFrame()

# Iterate through all entries in the root directory
for folder_name in os.listdir(root_dir):
    if folder_name.startswith("phase") and os.path.isdir(os.path.join(root_dir, folder_name)):
        metadata_file = os.path.join(root_dir, folder_name, f"{folder_name.capitalize()}_Metadata.csv")
        if os.path.isfile(metadata_file):
            print(f"Processing: {metadata_file}")
            df = pd.read_csv(metadata_file)
            df["Source_Phase"] = folder_name  # Add traceability
            master_df = pd.concat([master_df, df], ignore_index=True)

# Save the combined DataFrame to a master CSV
output_file = os.path.join(output_dir, "Master_Index_Register.csv")
master_df.to_csv(output_file, index=False)
print("Master_Index_Register.csv has been created.")