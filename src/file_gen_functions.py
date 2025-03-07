import os
import shutil
from markdown_to_html import markdown_to_html

def copy_static_to_public():
    # Delete public/ directory if it exists, then create it and copy static/ into it
    if os.path.exists("public/") == True:
        try:
            shutil.rmtree("public/")
        except:
            Exception("Error: public/ directory could not be deleted")
    os.mkdir("public/")
    dir = "static/"
    def copy_tree(current_directory):
        for item in os.listdir(current_directory):
            item_path = os.path.join(current_directory, item)
            if os.path.isdir(item_path):
                shutil.copytree(item_path, item_path.replace("static/", "public/"), dirs_exist_ok=True)
                copy_tree(item_path)
            else:
                shutil.copy(item_path, item_path.replace("static/", "public/"))
    return copy_tree(dir)

def extract_title(markdown):
    # Extract the title from the markdown file
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return str(line[2:])
    raise Exception("Error: No title found in markdown file")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating {dest_path} from {from_path} using {template_path}")
    markdown_file = open(from_path).read()
    template_file = open(template_path).read()
    html_nodes = markdown_to_html(markdown_file)
    html_string = html_nodes.to_html()
    title = extract_title(markdown_file)
    template_file = template_file.replace("{{ Content }}", html_string)
    template_file = template_file.replace("{{ Title }}", title)
    try:
        open(dest_path, "w").write(template_file)
    except:
        Exception(f"Error: {dest_path} could not be created")

def generate_pages_recursive(from_path, template_path, dest_path):
    for item in os.listdir(from_path):
        item_path = os.path.join(from_path, item)
        relative_dest_path = os.path.join(dest_path, item)
        if os.path.isdir(item_path):
            os.makedirs(relative_dest_path.replace("content/", "public/"), exist_ok=True)
            generate_pages_recursive(item_path, template_path, relative_dest_path)
        else:
            if item.endswith(".md"):
                generate_page(item_path, template_path, os.path.join(dest_path, item.replace(".md", ".html")))
            else:
                raise Exception(f"Error: {item} is not a markdown file")
