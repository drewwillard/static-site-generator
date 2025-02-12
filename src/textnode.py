from enum import Enum

class TextType(Enum):
    TEXT = 1
    BOLD = 2
    ITALIC = 3
    CODE = 4
    LINK = 5
    IMAGE = 6

class TextNode():
    def __init__(self, text, text_type: TextType, url=""):
        self.text = text
        self.text_type = text_type
        self.url = url
    def __eq__(self, other):
        if not isinstance(other, TextNode):
            return False
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"

def text_node_to_html_node(text_node: TextNode):
    if text_node.text_type == TextType.TEXT:
        return text_node.text
    elif text_node.text_type == TextType.BOLD:
        return f"<b>{text_node.text}</b>"
    elif text_node.text_type == TextType.ITALIC:
        return f"<i>{text_node.text}</i>"
    elif text_node.text_type == TextType.CODE:
        return f"<code>{text_node.text}</code>"
    elif text_node.text_type == TextType.LINK:
        return f"<a href={text_node.url}>{text_node.text}</a>"
    elif text_node.text_type == TextType.IMAGE:
        return f"<img src={text_node.url} alt={text_node.text}>"
    else:
        raise ValueError("Invalid TextType")
