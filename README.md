# Beyond Compare Regression Sorter

Python's ElementTree likes to sort an XML file's attributes alphabetically when writing files back out.  This causes problems when comparing files for differences using Beyond Compare as the original files won't have their attributes alphabetically sorted.  Running this script on both files will ensure that they are both ordered the same so the files can be properly compared.
