import unittest
from extractors import extract_markdown_images, extract_markdown_links

class TestExtractors(unittest.TestCase):
    def test_extract_links_from_text(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        expected_links = [
            ("to boot dev", "https://www.boot.dev"),
            ("to youtube", "https://www.youtube.com/@bootdotdev")
        ]
        self.assertEqual(extract_markdown_links(text), expected_links)

    def test_extract_images_from_text(self):
        text = "This is an image ![alt text](https://example.com/image.png)"
        expected_images = [
            ("alt text", "https://example.com/image.png")
        ]
        self.assertEqual(extract_markdown_images(text), expected_images)
