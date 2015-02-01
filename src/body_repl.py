
hostOnly = re.compile("^(.*):\d+$")

def escape(s):
    return '_'+re.sub('[-.]', '_', s)

def getMembers():
    status = getConn().admin.command("replSetGetStatus")
    return [m for m in status["members"] if m["state"] in (1,2,3)]

def doData():
    print "multigraph mongo_repl_lag"+instance

    members = getMembers()
    master = [m for m in members if m["state"] == 1][0]["optime"].time

    for m in members:
        if m["state"] != 1:
            host = hostOnly.match(m['name']).group(1)
            escaped = escape(host)
            lag = master - m["optime"].time
            print "%s.value %s" % (escaped, lag)

def doConfig():
    print "multigraph mongo_repl_lag"+instance
    print "graph_title Replication lag"
    print "graph_vlabel sec"
    print "graph_category MongoDB"
    print "graph_args --lower-limit 0"
    print "graph_scale no"

    warning = os.environ.get("repl_lag.warning")
    critical = os.environ.get("repl_lag.critical")

    for m in getMembers():
        if m["state"] != 1:
            host = hostOnly.match(m['name']).group(1)
            escaped = escape(host)
            print "%s.label %s" % (escaped, host)
            print "%s.type GAUGE" % escaped
            print "%s.min 0" % escaped
            if warning != None:
                print "%s.warning %s" % (escaped, warning)
            if critical != None:
                print "%s.critical %s" % (escaped, critical)
