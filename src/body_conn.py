
name = "connections"


def doData():
    print "multigraph mongo_conn"+instance
    print name + ".value " + str( getServerStatus()["connections"]["current"] )

def doConfig():
    print "multigraph mongo_conn"+instance
    print "graph_title MongoDB current connections"
    print "graph_args --base 1000 -l 0"
    print "graph_vlabel connections"
    print "graph_category MongoDB"

    print name + ".label " + name





