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

    def test_block_to_block_type(self):
        from split_blocks import block_to_block_type

        self.assertEqual(block_to_block_type('# This is a heading'), 'heading')
        self.assertEqual(block_to_block_type('```python\nprint("Hello, World!")\n```'), 'code')
        self.assertEqual(block_to_block_type('> This is a quote\n> Another line of the quote'), 'quote')
        self.assertEqual(block_to_block_type('* Item 1\n* Item 2\n- Item 3'), 'unordered_list')
        self.assertEqual(block_to_block_type('1. First item\n2. Second item\n3. Third item'), 'ordered_list')
        self.assertEqual(block_to_block_type('This is a paragraph.'), 'paragraph')
        self.assertEqual(block_to_block_type(''), 'paragraph')
        self.assertEqual(block_to_block_type('Normal text\nwith multiple lines'), 'paragraph')
        self.assertEqual(block_to_block_type('> Quote\nAnother line'), 'paragraph')
