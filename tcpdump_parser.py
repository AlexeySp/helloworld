import os
import sys
import re

fileName = sys.argv[1]
dump = open(fileName, 'r')
clearDumpName ="{0}_sp".format(str(os.path.basename(dump.name)))
clearDump = open(clearDumpName, "w")
new_line = ""
for line in dump:
   if re.match(r'\s', line):
      line = line[51:]
      new_line = new_line + line.strip("\n")
   else:
      clearDump.write(new_line)
      clearDump.write("\n\n" + line)
      new_line = ""
clearDump.write(new_line)
dump.close()
clearDump.close()
print("Cleared Dump: {0}".format(clearDumpName))
