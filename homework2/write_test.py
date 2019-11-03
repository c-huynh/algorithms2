outfile = open("test_clustering_big.txt", "w")
outfile.write("1000\n")

# write binary representation of first 1000 nodes
with open("clustering_big.txt") as infile:
    next(infile)
    for i in range(0,1000):
        outfile.write(infile.readline())

outfile.close()
