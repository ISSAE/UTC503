def _filter(p,l):
    if l:
        if (p(l[0])): return [l[0], *filter(p,l[1:])]
        else: return filter(p,l[1:])
    else:
        return []

filterlnl= lambda p, l: [l[0], *filterl(p,l[1:])] if p(l[0]) else filterl(p,l[1:])

filterl= lambda p, l: filterlnl(p,l) if l else []