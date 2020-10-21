import networkx as nx

infile = open("input.txt", "r")
outfile = open('enzinna.txt', 'w')
# number of sets
number_sets = int(infile.readline())

for a in range(0, number_sets, 1):

    infile.readline()

    G = nx.DiGraph()

    n = int(infile.readline())

    count = 0
    for b in range(n):
        temp = infile.readline().rstrip()
        temp = temp.replace("0", "C-G")
        temp = temp.replace("-", " ")
        temp = temp.replace('\n', "")
        temp = temp.split(" ")
        if (temp[-1] == ""):
            del temp[-1]

        for i in range(len(temp)):
            if((i % 2) == 0):
                G.add_node(count, direction=temp[i], color=temp[i+1])
                count = int(count + 1)

    for t in range(0, (n*n), 1):
        if(G.node[t]["direction"] == "E"):
            for w in range(t, ((t/n)*n)+n, 1):
                if G.node[t]["color"] != G.node[w]["color"]:
                    G.add_edge(t, w)
        elif (G.node[t]["direction"] == "N"):
            for w in range(t, -1, -n):
                if G.node[t]["color"] != G.node[w]["color"]:
                    G.add_edge(t, w)
        elif (G.node[t]["direction"] == "S"):
            for w in range(t, (n*n), n):
                if G.node[t]["color"] != G.node[w]["color"]:
                    G.add_edge(t, w)
        elif (G.node[t]["direction"] == "W"):
            for w in range(t, ((t/n)*n)-1, -1):
                if G.node[t]["color"] != G.node[w]["color"]:
                    G.add_edge(t, w)
        elif (G.node[t]["direction"] == "NE"):
            if ((t % n) != (n-1)):
                for w in range(t, -1, -n+1):
                    if G.node[t]["color"] != G.node[w]["color"]:
                        G.add_edge(t, w)
                    if ((w % n) == (n-1)):
                        break
        elif (G.node[t]["direction"] == "NW"):
            if ((t % n) != (0)):
                for w in range(t, -1, -n-1):
                    if G.node[t]["color"] != G.node[w]["color"]:
                        G.add_edge(t, w)
                    if ((w % n) == 0):
                        break
        elif (G.node[t]["direction"] == "SE"):
            if ((t % n) != (n-1)):
                for w in range(t, (n*n), n+1):
                    if G.node[t]["color"] != G.node[w]["color"]:
                        G.add_edge(t, w)
                    if ((w % n) == (n-1)):
                        break
        elif (G.node[t]["direction"] == "SW"):
            if ((t % n) != (0)):
                for w in range(t, (n*n)-1, n-1):
                    if G.node[t]["color"] != G.node[w]["color"]:
                        G.add_edge(t, w)
                    if ((w % n) == 0):
                        break

    goal = int(0)
    for a in range(0, (n*n), 1):
        if G.node[a]["direction"] == "C":
            goal = int(a)
            break
    path = nx.shortest_path(G, 0, goal)

    for c in range(len(path)-1):

        outfile.write(G.node[path[c]]["direction"] + "-")
        xo = int(path[c]/n)
        yo = int(path[c] % n)

        xn = int(path[c+1]/n)
        yn = int(path[c+1] % n)

        if xn == xo:
            d = int(abs(yn-yo))
        elif yn == yo:
            d = int(abs(xn-xo))
        else:
            d = int(max(abs(xn-xo), abs(xn-xo)))

        outfile.write(str(d))

        outfile.write(" ")

    outfile.write('\n\n')

outfile.flush()
outfile.close()
