def minimize_transactions(bill):
    net = {}

    for u, d in bill["payments"].items():
        net[u] = (d["due"] if d["paid"] else 0) - d["due"]

    creditors, debtors = [], []

    for u, amt in net.items():
        if amt > 0: creditors.append([u, amt])
        if amt < 0: debtors.append([u, -amt])

    res = []

    while creditors and debtors:
        c = creditors.pop()
        d = debtors.pop()

        m = min(c[1], d[1])
        res.append({"from": d[0], "to": c[0], "amount": m})

        if c[1] > m: creditors.append([c[0], c[1]-m])
        if d[1] > m: debtors.append([d[0], d[1]-m])

    return res