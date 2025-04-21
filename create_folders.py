#Manual insertion of folder and subfolders


# import os

# def create_folder_strecture(main_folder, subfolders):
#     try:
#         os.makedirs(main_folder, exist_ok=True)
#         print(f"mian folder created: {main_folder}")

#         for subfolder in subfolders:
#             path = os.path.join(main_folder, subfolder)
#             os.makedirs(path, exist_ok=True)
#             print(f"Subfolder created: {path}  ")

#     except Exception as e:
#         print(f"an error occoured: {e}")


# main_folder = "MyProject"
# subfolders = ["data", "Script", "model", "output"]

# create_folder_strecture(main_folder, subfolders)



#Inserting Foldernames with excel
# 
# import os
# import pandas as pd  # type: ignore

# def sanitize_folder_name(folder_name):
#     """
#     Replaces invalid characters and dashes in folder names with safe characters.
#     """
#     name = folder_name.replace('–', '-')  # Replace long dash with normal dash
#     invalid_chars = ['\\', '/', ':', '*', '?', '"', '<', '>', '|']
#     for char in invalid_chars:
#         name = name.replace(char, "_")
#     return name.strip()

# def create_structure_from_excel(excel_file, top_folder_name):
#     try:
#         # Sanitize and create the top-level folder
#         top_folder = sanitize_folder_name(top_folder_name)
#         os.makedirs(top_folder, exist_ok=True)
#         print(f"📁 Top Folder Created: {top_folder}")

#         # Load the Excel file
#         df = pd.read_excel(excel_file)

#         # Iterate through each row in the DataFrame
#         for index, row in df.iterrows():
#             master_class_raw = row['MasterClass']
#             if pd.isna(master_class_raw):
#                 continue  # Skip row if no master class

#             master_class = sanitize_folder_name(str(master_class_raw))
#             master_class_path = os.path.join(top_folder, master_class)
#             os.makedirs(master_class_path, exist_ok=True)
#             print(f"├── 📂 MasterClass folder created: {master_class_path}")

#             # Extract and sanitize valid subclass folder names
#             subclasses = [
#                 sanitize_folder_name(str(val))
#                 for val in row.iloc[1:].tolist()
#                 if pd.notna(val)
#             ]

#             # Create each subclass folder under the master_class
#             for subclass in subclasses:
#                 subclass_path = os.path.join(master_class_path, subclass)
#                 os.makedirs(subclass_path, exist_ok=True)
#                 print(f"│   └─ 📂 Subfolder created: {subclass_path}")

#     except Exception as e:
#         print(f"❌ An error occurred: {e}")

# # === Example usage ===
# excel_file = "folder_structure.xlsx"  # Your Excel file path
# top_folder_name = "Loan Mortgage Classes"  # Top-level directory

# create_structure_from_excel(excel_file, top_folder_name)


import os
import pandas as pd  # type: ignore

def sanitize_folder_name(folder_name: str) -> str:
    """Sanitize folder name by replacing invalid characters."""
    name = folder_name.replace('–', '-').strip()
    invalid_chars = ['\\', '/', ':', '*', '?', '"', '<', '>', '|']
    for char in invalid_chars:
        name = name.replace(char, "_")
    return name

def create_structure_from_excel(excel_file: str, top_folder_name: str) -> None:
    try:
        # Sanitize and create top-level folder
        top_folder = sanitize_folder_name(top_folder_name)
        os.makedirs(top_folder, exist_ok=True)
        print(f"✅ Top folder created: {top_folder}")

        # Load Excel file
        df = pd.read_excel(excel_file)

        for index, row in df.iterrows():
            master_class_raw = row.get('MasterClass')
            if pd.isna(master_class_raw):
                continue  # Skip rows without master class

            # Sanitize master class folder
            master_class = sanitize_folder_name(str(master_class_raw))
            master_class_path = os.path.join(top_folder, master_class)
            os.makedirs(master_class_path, exist_ok=True)
            print(f"📁 Master class created: {master_class_path}")

            # Loop through subclass columns (excluding 'MasterClass' column)
            subclasses = row.drop(labels=['MasterClass'], errors='ignore')
            for subclass in subclasses:
                if pd.isna(subclass):
                    continue
                sanitized_subclass = sanitize_folder_name(str(subclass))
                subclass_path = os.path.join(master_class_path, sanitized_subclass)
                os.makedirs(subclass_path, exist_ok=True)
                print(f"  └── Subfolder created: {subclass_path}")

    except Exception as e:
        print(f"❌ An error occurred: {e}")

# Example usage
excel_file = "folder_structure.xlsx"
top_folder_name = "Loan Mortgage Classes"
create_structure_from_excel(excel_file, top_folder_name)
