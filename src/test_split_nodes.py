import unittest
from textnode import TextNode, TextType
from split_nodes import split_nodes_delimiter, split_nodes_link

class TestSplitNodes(unittest.TestCase):
    def test_split_nodes_delimiter(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes_1 = split_nodes_delimiter([node], "`", TextType.CODE)
        expected_nodes_1 = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT)
        ]
        self.assertEqual(new_nodes_1, expected_nodes_1)

        node2 = TextNode("**Bold** is text with a **bold** word", TextType.TEXT)
        node3 = TextNode("This is text with another also **bold** word", TextType.TEXT)
        new_nodes_2 = split_nodes_delimiter([node2, node3], "**", TextType.BOLD)
        expected_nodes_2 = [
            TextNode("Bold", TextType.BOLD),
            TextNode(" is text with a ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" word", TextType.TEXT),
            TextNode("This is text with another also ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" word", TextType.TEXT)
        ]
        self.assertEquals(expected_nodes_2, new_nodes_2)

        node4 = TextNode("This is text with a *italic* word", TextType.TEXT)
        new_nodes_3 = split_nodes_delimiter([node4], "*", TextType.ITALIC)
        expected_nodes_3 = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word", TextType.TEXT)
        ]
        self.assertEqual(new_nodes_3, expected_nodes_3)

    def test_split_nodes_link(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        expected_nodes = [
            TextNode("This is text with a link ", TextType.TEXT),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" and ", TextType.TEXT),
            TextNode(
                "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
            ),
        ]
        self.assertEqual(new_nodes, expected_nodes)

        node2 = TextNode(
            "[oh a link](www.waitwhat.com) and also some other stuff [oh a link](www.waitwhat.com)", TextType.TEXT
        )
        new_nodes_2 = split_nodes_link([node2])
        expected_nodes_2 = [
            TextNode("oh a link", TextType.LINK, "www.waitwhat.com"),
            TextNode(" and also some other stuff ", TextType.TEXT),
            TextNode("oh a link", TextType.LINK, "www.waitwhat.com")
        ]
        self.assertEqual(new_nodes_2, expected_nodes_2)

        node3 = TextNode(
            "This is text with no link it's just regular text",
            TextType.TEXT,
        )
        node4 = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )
        new_nodes_3 = split_nodes_link([node3, node4])
        expected_nodes_3 = [
            TextNode("This is text with no link it's just regular text", TextType.TEXT),
            TextNode("This is text with a link ", TextType.TEXT),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" and ", TextType.TEXT),
            TextNode(
                "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
            ),
        ]
        self.assertEqual(new_nodes_3, expected_nodes_3)
