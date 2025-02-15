from textnode import TextNode
from textnode import TextType
from extractors import extract_markdown_images, extract_markdown_links
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        parts = node.text.split(delimiter)
        if len(parts) <= 1:
            new_nodes.append(node)
            continue

        current_text = ""
        is_inside_delimiter = False

        for i, text in enumerate(parts):
            if text == "":
                is_inside_delimiter = not is_inside_delimiter
                continue
            if is_inside_delimiter:
                new_nodes.append(TextNode(text.strip(), text_type))
            else:
                new_nodes.append(TextNode(text, TextType.TEXT))

            is_inside_delimiter = not is_inside_delimiter


    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        node_text = node.text
        pattern = r"\[(.*?)\)"
        split_node = re.split(pattern, node_text)
        link_parts = extract_markdown_links(node.text)
        if link_parts == []:
            new_nodes.append(node)
        else:
            for part in split_node:
                if part == "":
                    continue
                if link_parts == []:
                    new_nodes.append(TextNode(part, TextType.TEXT))
                    break
                elif link_parts[0][0] in part:
                    new_nodes.append(TextNode(link_parts[0][0], TextType.LINK, link_parts[0][1]))
                    link_parts.pop(0)
                else:
                    new_nodes.append(TextNode(part, TextType.TEXT))

    return new_nodes

def split_nodes_images(old_nodes):
    new_nodes = []
    for node in old_nodes:
        node_text = node.text
        pattern = r"\!\[(.*?)\)"
        split_node = re.split(pattern, node_text)
        image_parts = extract_markdown_images(node.text)
        if image_parts == []:
            new_nodes.append(node)
        else:
            for part in split_node:
                    if part == "":
                            continue
                    if image_parts == []:
                        new_nodes.append(TextNode(part, TextType.TEXT))
                        break
                    elif image_parts[0][0] in part:
                        new_nodes.append(TextNode(image_parts[0][0], TextType.IMAGE, image_parts[0][1]))
                        image_parts.pop(0)
                    else:
                        new_nodes.append(TextNode(part, TextType.TEXT))

    return new_nodes

def text_to_textnodes(text):
    list_text = [TextNode(text, TextType.TEXT)]
    image_nodes = split_nodes_images(list_text)
    link_nodes = split_nodes_link(image_nodes)
    bold_nodes = split_nodes_delimiter(link_nodes, "**", TextType.BOLD)
    italic_nodes = split_nodes_delimiter(bold_nodes, "*", TextType.ITALIC)
    code_nodes = split_nodes_delimiter(italic_nodes, "`", TextType.CODE)

    return code_nodes
