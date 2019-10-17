# ElementTree automatically parses all attributes and sorts them 
# alphabetically when writing the file back out, therefore this
# needs to be done to both files to make a proper comparison!

import xml.etree.ElementTree as ET
from pathlib import Path

# build a list of all files that will be sorted
rootdir = Path('C:/Development/grader/Grader.RegressionTest/TestFiles')
file_list = [f for f in rootdir.glob('*/*') if f.is_file()]

# sort and rewrite files
for file in file_list:
    tree = ET.parse(file)
    root = tree.getroot()

    # sort files by boardId
    root[:] = sorted(root, key=lambda child: (child.tag, child.get('Id')))

    tree.write(file)