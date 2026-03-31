# Morse Code Decoder

## Problem

Write a program that translates a Morse-code message into plain text.

Use a tree representation of Morse code:

- `.` means go to the left branch
- `-` means go to the right branch

The input format is:

- a single space separates Morse tokens for adjacent characters
- a double space separates words

Assume the Morse mapping follows the standard Morse code table for letters and digits.

Return the decoded message.

## Example

Input:
-.-. --- -.. .

Output:
CODE