import unittest

from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import LeafNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        node3 = TextNode("This is a text node", TextType.TEXT)
        node4 = TextNode("This is a text node", TextType.BOLD, "https://www.google.com")

        try:
            self.assertEqual(node, node2)
            self.assertNotEqual(node, node3)
            self.assertNotEqual(node, node4)
            print("Pass")
        except AssertionError:
            print("Fail")

class TestTextToHTMLFunction(unittest.TestCase):
    def test_text_to_html(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.TEXT)
        node3 = TextNode("This is a text node", TextType.ITALIC)
        node4 = TextNode("This is a text node", TextType.CODE)
        node5 = TextNode("This is a text node", TextType.LINK, "https://www.google.com")
        node6 = TextNode("This is a text node", TextType.IMAGE, "https://www.google.com")

        self.assertEqual(text_node_to_html_node(node), LeafNode("b", "This is a text node"))
        self.assertEqual(text_node_to_html_node(node2), LeafNode(None, "This is a text node"))
        self.assertEqual(text_node_to_html_node(node3), LeafNode("i", "This is a text node"))
        self.assertEqual(text_node_to_html_node(node4), LeafNode("code", "This is a text node"))
        self.assertEqual(text_node_to_html_node(node5), LeafNode("a", "This is a text node", {"href": "https://www.google.com"}))
        self.assertEqual(text_node_to_html_node(node6), LeafNode("img", None, {"src": "https://www.google.com"}))
