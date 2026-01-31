""
'Andreco_script' 
""

""
'This script reads a file and extracts floating values to compute average'
""

fname = input("Enter file name: ")
fh = open(fname)
count = 0
num = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count = count + 1
    num = float(line.replace('X-DSPAM-Confidence: ','').strip()) + num
mean = num / count 
print ('Average spam confidence:',mean) 
                        