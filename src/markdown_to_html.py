from htmlnode import ParentNode
from split_blocks import markdown_to_blocks, block_to_block_type
from split_nodes import text_to_textnodes
from textnode import text_node_to_html_node



def markdown_to_html(markdown):
    blocks_as_children = []
    block_list = markdown_to_blocks(markdown)
    for block in block_list:
        if len(block.strip()) == 0:
            continue
        block_type = block_to_block_type(block)
        if block_type == "heading":
            tag = header_get_tag(block)
            children = text_to_children(block.replace("#", "").strip())
            main_node = ParentNode(tag, children, None)
            blocks_as_children.append(main_node)
        elif block_type == "code":
            children = text_to_children(block.replace("```", "").strip())
            code_node = ParentNode("code", children, None)
            main_node = ParentNode("pre", [code_node], None)
            blocks_as_children.append(main_node)
        elif block_type == "quote":
            children = text_to_children(block.replace(">", "").strip())
            block_node = ParentNode("blockquote", children, None)
            blocks_as_children.append(block_node)
        elif block_type == "unordered_list":
            blocks_as_children.append(block_to_list_nodes(block))
        elif block_type == "ordered_list":
            blocks_as_children.append(block_to_list_nodes(block, "ol"))
        elif block_type == "paragraph":
            blocks_as_children.append(ParentNode("p", text_to_children(block), None))
    return ParentNode("div", blocks_as_children, None)





def text_to_children(block):
    text_nodes = text_to_textnodes(block)
    html_nodes = []
    for node in text_nodes:
        html_nodes.append(text_node_to_html_node(node))
        html_node = text_node_to_html_node(node)
        print(f"HTML node: {html_node}")
    return html_nodes

def header_get_tag(block):
    if block.startswith("#"):
        return "h1"
    elif block.startswith("##"):
        return "h2"
    elif block.startswith("###"):
        return "h3"
    elif block.startswith("####"):
        return "h4"
    elif block.startswith("#####"):
        return "h5"
    elif block.startswith("######"):
        return "h6"
    else:
        raise ValueError("Invalid header block")

def block_to_list_nodes(block, list_type = "ul"):
    lines = block.split("\n")
    li_items = []
    for line in lines:
        line = line.strip()
        if list_type == "ol":
            li_items.append(ParentNode("li", text_to_children(line[2:].strip()), None))
        else:
            li_items.append(ParentNode("li", text_to_children(line[1:].strip()), None))
    if list_type == "ol":
        return ParentNode("ol", li_items, None)
    else:
        return ParentNode("ul", li_items, None)
