import unittest
from split_blocks import markdown_to_blocks

class TestSplitBlocks(unittest.TestCase):
    def test_split_blocks(self):
        text = "This is a paragraph.\n\nThis is another paragraph."
        expected_blocks = ["This is a paragraph.", "This is another paragraph."]
        self.assertEqual(markdown_to_blocks(text), expected_blocks)

        text_with_newlines = "This is a paragraph.\n\nThis is another paragraph.\n\nAnd yet another one."
        expected_blocks_with_newlines = ["This is a paragraph.", "This is another paragraph.", "And yet another one."]
        self.assertEqual(markdown_to_blocks(text_with_newlines), expected_blocks_with_newlines)

        text_without_newlines = "This is a single paragraph with no newlines."
        expected_single_block = ["This is a single paragraph with no newlines."]
        self.assertEqual(markdown_to_blocks(text_without_newlines), expected_single_block)

        text_with_leading_trailing_newlines = "\nThis is a paragraph.\n\nThis is another paragraph.\n"
        expected_blocks_with_leading_trailing_newlines = ["This is a paragraph.", "This is another paragraph."]
        self.assertEqual(markdown_to_blocks(text_with_leading_trailing_newlines), expected_blocks_with_leading_trailing_newlines)

        text_with_multiple_newlines = "This is a paragraph.\n\n\nThis is another paragraph."
        expected_blocks_with_multiple_newlines = ["This is a paragraph.", "This is another paragraph."]
        self.assertEqual(markdown_to_blocks(text_with_multiple_newlines), expected_blocks_with_multiple_newlines)
