import sys
B=[None]*64;T=['w'];D=[3]
P={'P':(100,[],[8,16,9,7]),'N':(300,[],[10,11,-11,-10,-10,-11,11,10]),'B':(320,[9,7,-7,-9],[]),'R':(500,[8,1,-8,-1],[]),'Q':(900,[8,1,-8,-1,9,7,-7,-9],[]),'K':(9000,[8,1,-8,-1,9,7,-7,-9],[])}
def f(s):return s%8
def rk(s):return s//8
def o(s):return 0<=s<64
def pv(p):return P[p.upper()][0] if p else 0
def co(p):return 'w' if p and p.isupper() else ('b' if p else None)
def oc(c):return 'b' if c=='w' else 'w'
def mk(fen):
 d=[None]*64
 for ri,x in enumerate(fen.split()[0].split('/')[::-1]):
  s=ri*8
  for ch in x:
   if ch.isdigit():s+=int(ch)
   else:d[s]=ch;s+=1
 return d,fen.split()[1]
def ik(b,c):
 t='K' if c=='w' else 'k'
 return next((i for i,x in enumerate(b) if x==t),None)
def ic(b,c):
 k=ik(b,c)
 if k is None:return True
 e=oc(c)
 for i,p in enumerate(b):
  if p is None or co(p)!=e:continue
  for _,t in mf(b,i,p):
   if t==k:return True
 return False
def mf(b,s,p):
 c=co(p);sg=1 if c=='w' else -1;u=p.upper();rs=[]
 for d in P[u][1]:
  t=s
  while 1:
   t+=d
   if not o(t) or (f(t)==0 and d in (-1,7,-9)) or (f(t)==7 and d in (1,9,-7)):break
   q=b[t]
   if q is None:rs.append((s,t))
   else:
    if co(q)!=c:rs.append((s,t))
    break
 for d in P[u][2]:
  t=s+d
  if o(t) and abs(f(t)-f(s))<=2:
   q=b[t]
   if q is None or co(q)!=c:rs.append((s,t))
 if u=='P':
  t=s+sg*8
  if o(t) and b[t] is None:
   rs.append((s,t))
   if rk(s)==(6 if c=='w' else 1) and b[s+2*sg*8] is None:rs.append((s,s+2*sg*8))
  for d in (sg*9,sg*7):
   t=s+d
   if o(t) and abs(f(t)-f(s))==1:
    q=b[t]
    if q is not None and co(q)!=c:rs.append((s,t))
 elif u=='K':
  for d in P[u][1]:
   t=s+d
   if o(t):
    q=b[t]
    if q is None or co(q)!=c:rs.append((s,t))
 return rs
def lm(b,c):
 o=[]
 for i,p in enumerate(b):
  if p is None or co(p)!=c:continue
  for fs,ts in mf(b,i,p):
   n=list(b);n[ts]=n[fs];n[fs]=None
   if not ic(n,c):o.append((fs,ts))
 return o
TT={}
def sc(b,c,d,a,be):
 k=(tuple(b),c)
 if k in TT and TT[k][0]>=d:return TT[k][1]
 if d==0:
  v=sum(pv(p) if co(p)==c else -pv(p) for p in b if p)
  return v
 ms=lm(b,c)
 if not ms:return -20000 if ic(b,c) else 0
 ms.sort(key=lambda m:-pv(b[m[1]]) if b[m[1]] else 0)
 be_=-999999
 for fs,ts in ms:
  n=list(b);n[ts]=n[fs];n[fs]=None
  v=-sc(n,oc(c),d-1,-be,-be_)
  if v>be_:be_=v
  if v>a:a=v
  if a>=be:break
 TT[k]=(d,be_)
 return be_
def pm(b,c,d=3):
 ms=lm(b,c)
 if not ms:return None
 bm=ms[0];bv=-999999;a=-999999;be=999999
 ms.sort(key=lambda m:-pv(b[m[1]]) if b[m[1]] else 0)
 for fs,ts in ms:
  n=list(b);n[ts]=n[fs];n[fs]=None
  v=-sc(n,oc(c),d-1,-be,-a)
  if v>bv:bv=v;bm=(fs,ts)
  if v>a:a=v
 return bm
def sn(fs,ts):return chr(97+f(fs))+str(rk(fs)+1)+chr(97+f(ts))+str(rk(ts)+1)
def main():
 b,turn=mk("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1");c=turn
 while 1:
  try:l=sys.stdin.readline()
  except:break
  if not l:break
  l=l.strip()
  if not l:continue
  p=l.split();x=p[0]
  if x in('quit','stop'):break
  if x=='uci':print('id name tiny-chess-01\nid author ratman4080\nuciok',flush=True)
  elif x=='isready':print('readyok',flush=True)
  elif x=='ucinewgame':
   b,turn=mk("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1");c=turn;TT.clear()
  elif x=='position':
   if 'startpos' in p:b,turn=mk("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1");c=turn
   elif 'fen' in p:
    i=p.index('fen');b,turn=mk(' '.join(p[i+1:i+7]));c=turn
   if 'moves' in p:
    for mv in p[p.index('moves')+1:]:c=oc(c)
   TT.clear()
  elif x=='go':
   mv=pm(b,c,D[0])
   if mv is None:print('bestmove 0000',flush=True)
   else:print('bestmove '+sn(*mv),flush=True)
   c=oc(c)
  elif x=='depth':D[0]=int(p[1])
if __name__=='__main__':main()
