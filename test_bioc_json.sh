#!/bin/sh

### test bioc_json.py

JSON_SRC=json
XML_SRC=xml_old
XML_SRC=xml
XML_TARGET=xml
DIFF_OPT=-q

./bioc_json.py -b $JSON_SRC/collection.json z.xml
diff $DIFF_OPT xml/collection.xml z.xml

./bioc_json.py -b $JSON_SRC/abbr.json z.xml
diff $DIFF_OPT xml/abbr.xml z.xml

./bioc_json.py -b $JSON_SRC/everything.json z.xml
diff $DIFF_OPT xml/everything.xml z.xml

./bioc_json.py -b $JSON_SRC/everything-sentence.json z.xml
diff $DIFF_OPT xml/everything-sentence.xml z.xml

./bioc_json.py -j $XML_SRC/collection.xml z.json
diff $DIFF_OPT json/collection.json z.json

./bioc_json.py -j $XML_SRC/abbr.xml z.json
diff $DIFF_OPT json/abbr.json z.json

./bioc_json.py -j $XML_SRC/everything.xml z.json
diff $DIFF_OPT json/everything.json z.json

./bioc_json.py -j $XML_SRC/everything-sentence.xml z.json
diff $DIFF_OPT json/everything-sentence.json z.json

exit

## various commands for creating and working with the test set

./bioc_json.py -b json/collection.json $XML_TARGET/collection.xml
./bioc_json.py -b json/abbr.json $XML_TARGET/abbr.xml
./bioc_json.py -b json/everything.json $XML_TARGET/everything.xml
./bioc_json.py -b json/everything-sentence.json $XML_TARGET/everything-sentence.xml

exit

# ./bioc_json.py -j $XML_SRC/collection.xml json/collection.json
./bioc_json.py -j $XML_SRC/abbr.xml json/abbr.json
# ./bioc_json.py -j $XML_SRC/everything.xml json/everything.json
./bioc_json.py -j $XML_SRC/everything-sentence.xml json/everything-sentence.json

exit

# ./bioc_json.py -b json/collection.json z.xml
# diff xml/collection.xml z.xml

