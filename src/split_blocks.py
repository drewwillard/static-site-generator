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
