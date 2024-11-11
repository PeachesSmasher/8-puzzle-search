print("EXAMPLE CASE IN REPORT DOC")
    reportDocNode = [
        [1, 2, 3],
        [4, 8, 0],
        [7, 6, 5]
    ]
    reportDoc = Problem(reportDocNode)
    reportDoc.search(1)
    reportDoc.search(2)
    reportDoc.search(3)