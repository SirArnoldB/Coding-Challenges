### Background 
""" 
- Markdown (https://en.wikipedia.org/wiki/Markdown) is a formatting syntax used by many documents (these
- instructions, for example!) because of it's plain-text simplicity and it's ability to be translated directly into HTML.
"""
### Task 
"""
- Let's write a simple markdown parser function that will take in a single line of markdown and be translated into the
appropriate HTML. 
- To keep it simple, we'll support only one feature of markdown in atx syntax: headers.
Headers are designated by (1-6) hashes followed by a space, followed by text. 
- The number of hashes determines the header level of the HTML output.
"""
### Examples 
"""
# Header will become <h1>Header</h1>
## Header will become <h2>Header</h2>
###### Header will become <h6>Header</h6>
"""

### Additional Rules 
"""
# Header content should only come after the initial hashtag(s) plus a space character.
# Invalid headers should just be returned as the markdown that was recieved, no translation necessary.
# Spaces before and after both the header content and the hashtag(s) should be ignored in the resulting output.
"""
def markdown_parser(markdown):
    # remove any trailing whitespaces 
    markdown.strip()
    # test
    print(markdown)

    # function to get the number of hashes
    def getHashes(markdown):
        # keeps track of the hashes
        count = 0
        i = 0
        # loop through the markdown
        while i < len(markdown):
            if count == 6:
                if markdown[i] == " ":
                    # content starts from i + 1
                    return (count, i )
                else:
                    return ("Invalid Input!", 0)
            elif count < 6:
                if markdown[i] == "#":
                    count += 1
                elif markdown[i] == " ":
                    # content starts from i
                    return (count, i )
                else:
                    return ("Invalid Input!", 0)
    
    # get the hashes and content start
    hashesCount, contentStart = getHashes(markdown)
    # check for invalid input
    if str(hashesCount) == "Invalid Input!":
        return markdown
    else:
        # mapping of the headers
        headers = {1: ["<h1>", "</h1>"], 2: ["<h2>", "</h2>"], 3: ["<h3>", "</h3>"], 4: ["<h4>", "</h4>"], 5: ["<h5>", "</h5>"], 6: ["<h6>", "</h6>"]}
        # get the content of the markdown
        content = markdown[contentStart:].strip()
    return headers[hashesCount][0] + content + headers[hashesCount][1]

import unittest
class Test(unittest.TestCase):
    def test_markdown_parser_basic_valid_cases(self):
        self.assertEqual(markdown_parser("# header"), "<h1>header</h1>")
        self.assertEqual(markdown_parser("## smaller header"), "<h2>smallerheader</h2>")
        # self.assertEqual(markdown_parser("*Emphasis*"), "<em>Emphasis</em>")
        # self.assertEqual(markdown_parser("*Emphasized Text*"), "<em>EmphasizedText</em>")
    def test_markdown_parser_basic_invalid_cases(self):
        self.assertEqual(markdown_parser("#Invalid"), "#Invalid")
        # self.assertEqual(markdown_parser("* Invalid *"), "* Invalid *")





