class HTMLNode():
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.children = children
        self.props = props
        self.value = value

    def to_html(self):
        raise NotImplementedError("to_html not implemented")

    def props_to_html(self):
        if self.props:
            return f" href={self.props['href']} target={self.props['target']}"
        else:
            print("No props found")

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.children}, {self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag = None, value = None, props = None):
        super().__init__(tag, value, None, props)


    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode must have a value")
        elif self.tag is None:
            return str(self.value)
        elif self.props is None:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag = None, children = None, props = None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode must have a tag")
        elif self.children is None:
            raise ValueError("ParentNode must have children")
        child_list = []
        for child in self.children:
            if child.children is not None:
                child_list.append(child.to_html())
        if self.props is None:
            return f"<{self.tag}>{''.join(child_list)}</{self.tag}>"
        else:
            return f"<{self.tag}{self.props_to_html()}>{''.join(child_list)}</{self.tag}>"
