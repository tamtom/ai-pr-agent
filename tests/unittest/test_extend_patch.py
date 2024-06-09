
# Generated by CodiumAI


from ai_pr_agent.algo.git_patch_processing import extend_patch

"""
Code Analysis

Objective:
The objective of the 'extend_patch' function is to extend a given patch to include a specified number of surrounding 
lines. This function takes in an original file string, a patch string, and the number of lines to extend the patch by, 
and returns the extended patch string.

Inputs:
- original_file_str: a string representing the original file
- patch_str: a string representing the patch to be extended
- num_lines: an integer representing the number of lines to extend the patch by

Flow:
1. Split the original file string and patch string into separate lines
2. Initialize variables to keep track of the current hunk's start and size for both the original file and the patch
3. Iterate through each line in the patch string
4. If the line starts with '@@', extract the start and size values for both the original file and the patch, and 
calculate the extended start and size values
5. Append the extended hunk header to the extended patch lines list
6. Append the specified number of lines before the hunk to the extended patch lines list
7. Append the current line to the extended patch lines list
8. If the line is not a hunk header, append it to the extended patch lines list
9. Return the extended patch string

Outputs:
- extended_patch_str: a string representing the extended patch

Additional aspects:
- The function uses regular expressions to extract the start and size values from the hunk header
- The function handles cases where the start value of a hunk is less than the number of lines to extend by by setting 
the extended start value to 1
- The function handles cases where the hunk extends beyond the end of the original file by only including lines up to 
the end of the original file in the extended patch
"""


class TestExtendPatch:
    # Tests that the function works correctly with valid input
    def test_happy_path(self):
        original_file_str = 'line1\nline2\nline3\nline4\nline5'
        patch_str = '@@ -2,2 +2,2 @@ init()\n-line2\n+new_line2\nline3'
        num_lines = 1
        expected_output = '@@ -1,4 +1,4 @@ init()\nline1\n-line2\n+new_line2\nline3\nline4'
        actual_output = extend_patch(original_file_str, patch_str, num_lines)
        assert actual_output == expected_output

    # Tests that the function returns an empty string when patch_str is empty
    def test_empty_patch(self):
        original_file_str = 'line1\nline2\nline3\nline4\nline5'
        patch_str = ''
        num_lines = 1
        expected_output = ''
        assert extend_patch(original_file_str, patch_str, num_lines) == expected_output

    # Tests that the function returns the original patch when num_lines is 0
    def test_zero_num_lines(self):
        original_file_str = 'line1\nline2\nline3\nline4\nline5'
        patch_str = '@@ -2,2 +2,2 @@ init()\n-line2\n+new_line2\nline3'
        num_lines = 0
        assert extend_patch(original_file_str, patch_str, num_lines) == patch_str

    # Tests that the function returns the original patch when patch_str contains no hunks
    def test_no_hunks(self):
        original_file_str = 'line1\nline2\nline3\nline4\nline5'
        patch_str = 'no hunks here'
        num_lines = 1
        expected_output = 'no hunks here'
        assert extend_patch(original_file_str, patch_str, num_lines) == expected_output

    # Tests that the function extends a patch with a single hunk correctly
    def test_single_hunk(self):
        original_file_str = 'line1\nline2\nline3\nline4\nline5'
        patch_str = '@@ -2,3 +2,3 @@ init()\n-line2\n+new_line2\nline3\nline4'
        num_lines = 1
        expected_output = '@@ -1,5 +1,5 @@ init()\nline1\n-line2\n+new_line2\nline3\nline4\nline5'
        actual_output = extend_patch(original_file_str, patch_str, num_lines)
        assert actual_output == expected_output

    # Tests the functionality of extending a patch with multiple hunks.
    def test_multiple_hunks(self):
        original_file_str = 'line1\nline2\nline3\nline4\nline5\nline6'
        patch_str = '@@ -2,3 +2,3 @@ init()\n-line2\n+new_line2\nline3\nline4\n@@ -4,1 +4,1 @@ init2()\n-line4\n+new_line4'  # noqa: E501
        num_lines = 1
        expected_output = '@@ -1,5 +1,5 @@ init()\nline1\n-line2\n+new_line2\nline3\nline4\nline5\n@@ -3,3 +3,3 @@ init2()\nline3\n-line4\n+new_line4\nline5'  # noqa: E501
        actual_output = extend_patch(original_file_str, patch_str, num_lines)
        assert actual_output == expected_output
