import unittest
from htmlnode import HTMLNode

class HTMLNode_Test(unittest.TestCase):
    def test_htmlnode(self):
        node = HTMLNode(tag="a", value="Click me", props={"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.tag, "a")
        self.assertEqual(node.value, "Click me")
        self.assertEqual(node.props, {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), " href=https://www.google.com target=_blank")

class LeafNode_Test(unittest.TestCase):
    def test_leafnode(self):
        node = HTMLNode(tag="a", value="Click me", props={"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.tag, "a")
        self.assertEqual(node.value, "Click me")
        self.assertEqual(node.props, {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), " href=https://www.google.com target=_blank")

class ParentNode_Test(unittest.TestCase):
    def test_parentnode(self):
        root = HTMLNode(tag="div", value = None, props={"class": "container"})

        header = HTMLNode(tag="header", value=None, props={"class": "header"})
        main = HTMLNode(tag="main", value=None, props={"class": "main-content"})
        root.children = [header, main]

        nav = HTMLNode(tag="nav", value=None)
        title = HTMLNode(tag="h1", value="Page Title")
        header.children = [nav, title]

        link1 = HTMLNode(tag="a", value="Home", props={"href": "/"})
        link2 = HTMLNode(tag="a", value="About", props={"href": "/about"})
        nav.children = [link1, link2]

        article = HTMLNode(tag="article", value=None)
        sidebar = HTMLNode(tag="aside", value=None, props={"class": "sidebar"})
        main.children = [article, sidebar]

        self.assertEqual(len(root.children), 2)
        self.assertEqual(len(header.children), 2)
        self.assertEqual(len(nav.children), 2)
        self.assertEqual(len(main.children), 2)

        self.assertEqual(link1.value, "Home")
        self.assertEqual(title.value, "Page Title")
