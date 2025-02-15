from file_gen_functions import copy_static_to_public, generate_pages_recursive

def main():

    if __name__ == "__main__":
        copy_static_to_public()
        generate_pages_recursive("content/", "template.html", "public/")

main()
