import sys
import subprocess

# Usage:
# $ python3 siteWatcher.py url.txt new last

DUMMY = '---dummy---'

def repIDwDummy(line):
    search_begin = 0
    while search_begin < len(line):
        #print(line[search_begin:])
        id_begin = line[search_begin:].find(' id="')
        if id_begin != -1:
            end_search_begin = search_begin + id_begin + 5
            id_end = line[end_search_begin:].find('"')
            line = line[0:search_begin + id_begin+5] + DUMMY + line[end_search_begin + id_end:]
            search_begin = search_begin + id_begin + 5 + len(DUMMY)
            #print("search_begin = " + str(search_begin))
        else:
            return line

def replaceIDwithDummy(page):
    f = open(page)
    lines = []
    for line in f:
        if len(line) != 0:
            lines.append(repIDwDummy(line))
    f.close()
    #print(str(lines))
    f = open(page, mode="w")
    for line in lines:
        if(line != None):
            f.write(line)
    f.close()

infile = sys.argv[1]
lines = open(infile).readlines()

for url in lines:
    print("URL: " + url)
    filename = url.replace('https://', '').replace('/', '_').replace('\n', '') + ".html"
    out = open(sys.argv[2] + '/' + filename, mode='w')
    out_err = open("stderr", mode='a')
    http_get = "curl " + url
    subprocess.run([http_get], stdout=out, stderr=out_err, shell=True)
    out.close()
    out_err.close()
    replaceIDwithDummy(sys.argv[2] + '/' + filename)

subprocess.run(["diff -r " + sys.argv[2] + " " + sys.argv[3]], shell=True)
