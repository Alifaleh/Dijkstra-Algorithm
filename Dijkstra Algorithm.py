import prettytable

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'



#######################################################################

#######################################################################

nodes=["a","b","c","d","e","f","g","z"]

links=[[nodes.index("a"),nodes.index("b"),4],
       [nodes.index("a"),nodes.index("c"),3],
       [nodes.index("b"),nodes.index("c"),2],
       [nodes.index("b"),nodes.index("d"),5],
       [nodes.index("c"),nodes.index("e"),6],
       [nodes.index("c"),nodes.index("d"),3],
       [nodes.index("d"),nodes.index("e"),1],
       [nodes.index("d"),nodes.index("f"),5],
       [nodes.index("e"),nodes.index("g"),5],
       [nodes.index("f"),nodes.index("g"),2],
       [nodes.index("f"),nodes.index("z"),7],
       [nodes.index("g"),nodes.index("z"),4],]

#[nodes.index(""),nodes.index(""),],


start=nodes.index("a")
end=nodes.index("z")

#######################################################################

#######################################################################

n_table=[]
l_table=[]
fixed_table=[]
cr_n=[]
cr_l=[]
fixed=[]
v=[]
v.append(start)

for n in nodes:
    cr_n.append(float("inf"))
    cr_l.append(start)
    fixed.append(0)
fixed[start]=1
cr_n[start]=0


for l in links:
    if start in l[0:-1]:
        cts=l[0:-1][(l[0:-1].index(start)+1)%2]
        cr_n[cts]=l[-1]


n_table.append(list(cr_n))
l_table.append(list(cr_l))
fixed_table.append(list(fixed))
for i in nodes[:-1]:
    tr=[]
    tri=[]
    for ii,let in enumerate(n_table[-1]):
        if fixed[ii]==0:
            tr.append(let)
            tri.append(ii)
    cil=tri[tr.index(min(tr))]
    v.append(cil)
    fixed[cil]=1
    fixed_table.append(list(fixed))
    for l in links:
        if cil in l[0:-1]:
            cts = l[0:-1][(l[0:-1].index(cil) + 1) % 2]
            if fixed[cts]==0 and ((n_table[-1][cil]+l[-1])<(cr_n[cts])):
                cr_n[cts] = n_table[-1][cil]+l[-1]
                cr_l[cts] = cil
    n_table.append(list(cr_n))
    l_table.append(list(cr_l))

ntp=[]
for n in nodes:
    ntp.append(color.RED+n+color.END)
x = prettytable.PrettyTable([color.YELLOW+"V"+color.END]+ntp)
for i,cv in enumerate(v):
    crtp=[]
    crtp.append(color.YELLOW+nodes[cv]+color.END)
    crft=[]
    for ii,n in enumerate(n_table[i]):
        if fixed_table[i][ii]==1:
            crft.append(color.BLUE+str(n)+"-"+nodes[l_table[i][ii]]+color.END)
        else:
            crft.append(str(n)+"-"+nodes[l_table[i][ii]])
    crtp=crtp+crft
    x.add_row(crtp)
print("\n\n")
print(x)


print("\n\nthe shortest path from ("+nodes[start]+") to ("+nodes[end]+") is :\n")

lit=l_table[-1]
pl=[]
pl.append(end)
p=lit[end]
end=p
while p!=start:
    pl.append(end)
    p = lit[end]
    end = p
pl.append(start)
pl.reverse()
for i,cn in enumerate(pl):
    if i!=0:
        print(" => "+nodes[cn],end="")
    else:
        print(nodes[cn], end="")
print("\n\n\n")