import os
import re
import shutil

def relocate_images_for_markdown(root_dir):
    asset_root = os.path.join(root_dir, 'README_Assets')
    os.makedirs(asset_root, exist_ok=True)

    image_exts = ['.png', '.jpg', '.jpeg', '.gif', '.bmp', '.webp', '.svg']
    md_image_pattern = re.compile(r'(!\[.*?\]\()([^\s)]+)(\))')  # matches ![alt](path)

    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith('.md'):
                md_path = os.path.join(dirpath, filename)

                with open(md_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                # Skip markdown files that already reference README_Assets/
                if 'README_Assets/' in content:
                    continue

                updated = False

                def replace_match(match):
                    nonlocal updated
                    original_path = match.group(2)

                    # Ignore remote links or already updated ones
                    if original_path.startswith(('http://', 'https://', 'README_Assets/')):
                        return match.group(0)

                    # Resolve full path of image
                    original_image_path = os.path.normpath(os.path.join(dirpath, original_path))
                    if not os.path.isfile(original_image_path):
                        return match.group(0)

                    # Build new asset path
                    rel_path_from_root = os.path.relpath(original_image_path, root_dir)
                    new_image_path = os.path.join(asset_root, rel_path_from_root)

                    # Make parent directory if needed
                    os.makedirs(os.path.dirname(new_image_path), exist_ok=True)

                    # Copy image if needed
                    if not os.path.exists(new_image_path):
                        shutil.copy2(original_image_path, new_image_path)

                    # Delete original image
                    try:
                        os.remove(original_image_path)
                    except Exception as e:
                        print(f"Failed to delete {original_image_path}: {e}")

                    # Build new relative path from markdown file to image
                    new_rel_path = os.path.relpath(new_image_path, os.path.dirname(md_path))
                    updated = True
                    return f"{match.group(1)}{new_rel_path.replace(os.sep, '/')}{match.group(3)}"

                new_content = md_image_pattern.sub(replace_match, content)

                if updated:
                    with open(md_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"Updated: {md_path}")

# Run it
if __name__ == "__main__":
    root_directory = os.getcwd()
    relocate_images_for_markdown(root_directory)
