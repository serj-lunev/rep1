
# coding: utf-8

# In[ ]:

while True:
    code = int(raw_input())
    if code == 0:
        break
    line = raw_input()
    segments = []
    j = 0
    for i in xrange(0, len(line), code):
        if j % 2 == 1:
            # reverse every odd segment
            tmp = list(line[i:i + code])
            tmp.reverse()
            segments.append("".join(tmp))
        else:
            segments.append(line[i:i+code])
        j += 1
    out = []
    for i in xrange(0, code):
        for f in segments:
            out.append(f[i])
    print "".join(out)

