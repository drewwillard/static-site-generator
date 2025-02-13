from textnode import TextNode, TextType
from split_nodes import split_nodes_delimiter, split_nodes_link, split_nodes_images, text_to_textnodes
from extractors import extract_markdown_images, extract_markdown_links
from split_blocks import markdown_to_blocks
import re

def main():
    text = """
       # This is a heading

    This is a paragraph of text. It has some **bold** and *italic* words inside of it.

    * This is the first list item in a list block
    * This is a list item
    * This is another list item    """
    print(markdown_to_blocks(text))
main()
