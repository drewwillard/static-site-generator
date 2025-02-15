def markdown_to_blocks(markdown):
    split_lines = markdown.splitlines()
    list_of_blocks = []
    new_block = ""
    for i in range(len(split_lines)):
        if split_lines[i] == "":
            if len(new_block) != 0:
                list_of_blocks.append(new_block)
                new_block = ""
            else:
                continue
        else:
            if len(new_block) == 0:
                new_block = split_lines[i].strip()
            else:
                new_block = new_block + "\n" + split_lines[i].strip()
    if len(new_block) != 0:
        list_of_blocks.append(new_block)

    return list_of_blocks

def block_to_block_type(block):
    if block == "":
        return "paragraph"
    if block.startswith("#"):
        return "heading"
    if block.startswith("```"):
        return "code"
    block_list = block.split("\n")
    if all(line[0] == ">" for line in block_list):
        return "quote"
    if all(line.strip().startswith(("* ", "- ")) for line in block_list):
        return "unordered_list"
    if all(line[0].isdigit() for line in block_list) and all(line[1] == "." for line in block_list):
        return "ordered_list"
    else:
        return "paragraph"
