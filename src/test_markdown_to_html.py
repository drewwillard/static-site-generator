import unittest

class TestMarkdownToHTML(unittest.TestCase):
    def test_markdown_to_html(self):
        from markdown_to_html import markdown_to_html
        from htmlnode import LeafNode, ParentNode

        # Test case 1: Simple heading
        markdown1 = "# Heading"
        expected_html1 = ParentNode("div", None, [ParentNode("h1", None, [LeafNode(None, "Heading")])])
        self.assertEqual(markdown_to_html(markdown1), expected_html1)

        # Test case 2: Paragraph with text
        markdown2 = "This is a paragraph."
        expected_html2 = ParentNode("div", None, [ParentNode("p", None, [LeafNode(None, "This is a paragraph.")])])
        self.assertEqual(markdown_to_html(markdown2), expected_html2)

        # Test case 3: Code block
        markdown3 = "```\nprint('Hello, World!')\n```"
        expected_html3 = ParentNode("div", None, [
            ParentNode("pre", None, [ParentNode("code", None, [LeafNode(None, "print('Hello, World!')")])])
        ])
        self.assertEqual(markdown_to_html(markdown3), expected_html3)

        # Test case 4: full markdown doc
        markdown4 = """# This is a heading with *italics*

        ```python\nprint('This is code')\n```

        >This is a quote\n>This is **a bold** quote\n>This is a third quote

        * This is a list item\n* This is another list item\n- This is a third list item

        1. This is an ordered list item\n2. This is another ordered list item\n3. This is a third ordered list item

        This is a paragraph with some **bold** text

        This is a paragraph with a [link](https://www.example.com) and an ![image](https://www.example.com/image.png)

        """
        expected_html4 = ParentNode("div", None, [
            ParentNode("h1", None, [
                LeafNode(None, "This is a heading with "),
                LeafNode("i", "italics")
            ]),
            ParentNode("pre", None, [
                ParentNode("code", None, [
                    LeafNode(None, "python\nprint('This is code')")
                ])
            ]),
            ParentNode("blockquote", None, [
                LeafNode(None, "This is a quote\nThis is "),
                LeafNode("b", "a bold"),
                LeafNode(None, " quote\nThis is a third quote")
            ]),
            ParentNode("ul", None, [
                ParentNode("li", None, [LeafNode(None, "This is a list item")]),
                ParentNode("li", None, [LeafNode(None, "This is another list item")]),
                ParentNode("li", None, [LeafNode(None, "This is a third list item")])
            ]),
            ParentNode("ol", None, [
                ParentNode("li", None, [LeafNode(None, "This is an ordered list item")]),
                ParentNode("li", None, [LeafNode(None, "This is another ordered list item")]),
                ParentNode("li", None, [LeafNode(None, "This is a third ordered list item")])
            ]),
            ParentNode("p", None, [
                LeafNode(None, "This is a paragraph with some "),
                LeafNode("b", "bold"),
                LeafNode(None, " text")
            ]),
            ParentNode(
                "p",
                None,
                [
                    LeafNode(
                        None,
                        "This is a paragraph with a "
                    ),
                    LeafNode(
                        "a",
                        "link",
                        {"href": "https://www.example.com"}
                    ),
                    LeafNode(
                        None,
                        " and an "
                    ),
                    LeafNode(
                        "img",
                        None,
                        {"src": "https://www.example.com/image.png"}
                    )
                ]
            )
        ])
        self.assertEqual(markdown_to_html(markdown4), expected_html4)
