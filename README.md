# Wordpress Markdown 

wordpress_markdown is a simple python script that converts wordpress posts to markdown. You must first export your wordpress data with the export tool provided by Wordpress. 

## Requirements

* Python3
* Python3 modules: 
	* xml.etree.ElementTree
	* sys
	* datetime
	* html2text
	* re

## Usage 

`python3 wordpress_markdown.py input_file.xml output_dir/`

Note: You must include the trailing / in the output directory path 

## Output 

The resulting files will have the name `YYYMMDD_HH:MM:SS_post_title.md`

Here is a sample of what the  file content will be 
`
# This is a test wordpress post 

Time: Sun Feb 02 08:14:53 EST  2020
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
`
