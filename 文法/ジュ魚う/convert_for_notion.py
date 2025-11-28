import glob
import os
import re

def convert_content(content):
    # Replace GFM alerts with Notion-friendly blockquotes
    replacements = [
        (r'> \[!NOTE\]', r'> ℹ️ **NOTE**'),
        (r'> \[!TIP\]', r'> 💡 **TIP**'),
        (r'> \[!IMPORTANT\]', r'> ❗ **IMPORTANT**'),
        (r'> \[!WARNING\]', r'> ⚠️ **WARNING**'),
        (r'> \[!CAUTION\]', r'> 🛑 **CAUTION**'),
    ]
    
    for pattern, replacement in replacements:
        content = re.sub(pattern, replacement, content, flags=re.IGNORECASE)
    return content

def main():
    source_dir = "."
    target_dir = "Notion"
    
    files = glob.glob(os.path.join(source_dir, "*-Z.md"))
    
    print(f"Found {len(files)} files to process.")
    
    for file_path in files:
        filename = os.path.basename(file_path)
        new_filename = filename.replace("-Z.md", "-N.md")
        target_path = os.path.join(target_dir, new_filename)
        
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            
        new_content = convert_content(content)
        
        with open(target_path, "w", encoding="utf-8") as f:
            f.write(new_content)
            
        print(f"Processed: {filename} -> {new_filename}")

if __name__ == "__main__":
    main()
