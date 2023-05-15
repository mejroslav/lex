#!/bin/python3
import os
import re
import argparse
import random

REGEX_CHEATSHEET = """
REGEX CHEATSHEET
----------------

Anchors:
^       Start of string or line
$       End of string or line
\\b     Word Boundary
\\B     Not Word Boundary

Character Classes:
[abc]   Character Set
[^abc]  Negated Character Set
[a-z]   Range
.       Dot
\w      Word
\W      Not Word
\d      Digit
\D      Not Digit
\s      Whitespace
\S      Not Whitespace

Quantifiers And Alternation:
+       Plus (One or More)
*       Asterisk (Zero or More)
?       Optional (Zero or One)
{1,3}   Quantifier
|       Alternation

Flags:
i       Ignore case
g       Global
m       Multiline

Group & References:
()      Group
\\1     Reference
(?:)    Non Capturing Group
"""

parser = argparse.ArgumentParser(
    prog="lex", description="Finds words that match the regex in a database of English words.")
parser.add_argument("-p", "--pattern", dest="pattern",
                    help="pattern to be matched")
parser.add_argument("-l", "--limit", dest="limit",
                    default="", help="limit of the matched words")
parser.add_argument("-r", "--random", dest="random",
                    action="store_true", help="randomize the matched words")
parser.add_argument("-d", "--delimeter", default=" ",
                    dest="delimeter", help="delimeter")
parser.add_argument("--cheatsheet", dest="cheatsheet",
                    action="store_true", help="show regex cheatsheet")


args = parser.parse_args()


def main():

    if args.cheatsheet:
        print(REGEX_CHEATSHEET)
        return

    if args.limit != "":
        limit_num = int(args.limit)
    else:
        limit_num = None

    randomize = args.random
    base = os.path.dirname(__file__)
    path = os.path.join(base, "words.txt")
    with open(path, "r") as f:
        english_words: list[str] = f.read().splitlines()

    pattern = r"{}".format(args.pattern)
    matching_words = [
        word for word in english_words if re.match(pattern, word)]

    if randomize:
        random.shuffle(matching_words)

    if limit_num:
        limit = min(limit_num, len(matching_words))
        matching_words = matching_words[:limit]

    output = (args.delimeter).join(matching_words)

    print(output)


if __name__ == '__main__':
    main()
