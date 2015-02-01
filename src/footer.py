
m = re.search("mongo(_.*)_(.*)$", sys.argv[0])
if (m):
    instance = m.group(1)

if len(sys.argv) > 1 and sys.argv[1] == "config":
    doConfig()
else:
    doData()
