import os
import json
import yaml
import shutil
import zipfile
import sys

# Configuration
DIST_DIR = "dist"
THEMES_DIR = "themes"
THEMES_JSON_FILE = "themes.json"
REPO_NAME = os.environ.get("GITHUB_REPOSITORY", "relaycraft/relaycraft-themes")
# Use run_number to generate a unique tag for this run
RUN_NUMBER = os.environ.get("GITHUB_RUN_NUMBER", "1")
TAG_NAME = f"v1.0.{RUN_NUMBER}" # Simple incremental versioning for the release tag
DOWNLOAD_BASE_URL = f"https://github.com/{REPO_NAME}/releases/download/{TAG_NAME}"

def load_themes_json():
    if not os.path.exists(THEMES_JSON_FILE):
        return {"version": "1.0", "plugins": []}
    with open(THEMES_JSON_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_themes_json(data):
    with open(THEMES_JSON_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def find_theme_dirs():
    theme_dirs = []
    if not os.path.exists(THEMES_DIR):
        return []
    
    for item in os.listdir(THEMES_DIR):
        full_path = os.path.join(THEMES_DIR, item)
        if os.path.isdir(full_path) and not item.startswith("."):
            if os.path.exists(os.path.join(full_path, "theme.yaml")):
                theme_dirs.append(full_path)
    return theme_dirs

def build_theme(theme_dir, output_dir):
    with open(os.path.join(theme_dir, "theme.yaml"), "r", encoding="utf-8") as f:
        manifest = yaml.safe_load(f)
    
    theme_id = manifest.get("id")
    version = manifest.get("version")
    
    if not theme_id or not version:
        print(f"Skipping {theme_dir}: Missing id or version in theme.yaml")
        return None

    filename = f"{theme_id}-v{version}.rctheme"
    output_path = os.path.join(output_dir, filename)
    
    # Create zip file (renamed to .rctheme)
    with zipfile.ZipFile(output_path, "w", zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(theme_dir):
            for file in files:
                file_path = os.path.join(root, file)
                # Calculate archive name (relative path inside the zip)
                # We want the root of the zip to be the contents of the theme dir
                arcname = os.path.relpath(file_path, theme_dir)
                zipf.write(file_path, arcname)
    
    print(f"Built {filename}")
    return {
        "id": theme_id,
        "version": version,
        "filename": filename,
        "manifest": manifest
    }

def main():
    if not os.path.exists(DIST_DIR):
        os.makedirs(DIST_DIR)
        
    themes_data = load_themes_json()
    # Note: themes.json currently uses "plugins" key
    existing_themes_map = {p["id"]: p for p in themes_data.get("plugins", [])}
    
    theme_dirs = find_theme_dirs()
    
    print(f"Found theme directories: {theme_dirs}")
    
    for t_dir in theme_dirs:
        build_result = build_theme(t_dir, DIST_DIR)
        if not build_result:
            continue
            
        t_id = build_result["id"]
        t_version = build_result["version"]
        filename = build_result["filename"]
        manifest = build_result["manifest"]
        
        # Update or add entry in themes.json
        download_url = f"{DOWNLOAD_BASE_URL}/{filename}"
        
        entry = existing_themes_map.get(t_id, {})
        
        # Update fields from manifest
        entry["id"] = t_id
        entry["name"] = manifest.get("name", entry.get("name"))
        entry["version"] = t_version
        entry["description"] = manifest.get("description", entry.get("description"))
        entry["author"] = manifest.get("author", entry.get("author"))
        # Use existing url if not present (pointing to raw yaml)
        entry["url"] = entry.get("url", "") 
        entry["downloadUrl"] = download_url
        entry["category"] = "theme"
        
        # Optional fields
        if "locales" in manifest:
            entry["locales"] = manifest["locales"]
        if "tags" in manifest:
            entry["tags"] = manifest["tags"]
            
        existing_themes_map[t_id] = entry

    # Reconstruct list
    themes_data["plugins"] = list(existing_themes_map.values())
    
    save_themes_json(themes_data)
    print("Updated themes.json")

if __name__ == "__main__":
    main()
