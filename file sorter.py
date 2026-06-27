import os

# Your downloads directory address
DOWNLOADS_PATH = "C:/Users/lenovo.DESKTOP-QP5CHV4/Downloads"

# The specific subfolders we need to empty out
SUBFOLDERS_TO_UNDO = [
    "Downloaded_Archives",
    "Downloaded_Torrents",
    "Downloaded_Programs",
    "Downloaded_Docs",
    "Downloaded_Images"
]

print("🔄 REVERSING THE FILE SORTING... DUMPING FILES BACK TO DOWNLOADS")
print("="*60)

for folder_name in SUBFOLDERS_TO_UNDO:
    folder_path = DOWNLOADS_PATH + "/" + folder_name
    
    # 1. Only look inside if the folder actually exists
    if os.path.exists(folder_path):
        files_inside = os.listdir(folder_path)
        
        # 2. Loop through every file inside this subfolder
        for file in files_inside:
            current_location = folder_path + "/" + file
            back_to_downloads = DOWNLOADS_PATH + "/" + file
            
            # Move the file back out to the main Downloads folder
            os.rename(current_location, back_to_downloads)
            print(f"↩️ Restored: {file}")
        
        # 3. Now that the folder is completely empty, delete it
        os.rmdir(folder_path)
        print(f"🗑️ Removed empty folder: {folder_name}")

print("="*60)
print("✨ Reset complete! Your Downloads folder is beautifully messy again.")
print("The stage is yours—go build your custom file sorter! 🛠️")