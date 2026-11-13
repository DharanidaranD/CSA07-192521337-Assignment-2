INF=99; names='ABCDE'
cost={('A','B'):2,('A','C'):7,('B','C'):3,('B','D'):8,('C','D'):1,('D','E'):4}
def run(cost):
    link={}
    for (u,v),c in cost.items(): link[u,v]=link[v,u]=c
    t={u:{v:(0 if u==v else link.get((u,v),INF)) for v in names} for u in names}
    rounds=0
    while True:
        rounds+=1; old={u:dict(t[u]) for u in names}; changed=False
        for u in names:
            for n in names:
                if (u,n) not in link: continue
                for d in names:
                    cand=link[u,n]+old[n][d]
                    if cand<t[u][d]: t[u][d]=cand; changed=True
        if not changed: break
    print('converged after',rounds,'rounds')
    for u in names: print(u,[t[u][v] for v in names])
    return t
print('NORMAL'); run(cost)
print('AFTER C-D FAILURE'); c=dict(cost); c[('C','D')]=99; run(c)
