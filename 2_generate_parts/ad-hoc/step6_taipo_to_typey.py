# Input example:
"""
R,S,N,I,A,O,T,E,0,1,sendText
1,0,0,0,0,0,0,0,0,0,r
0,1,0,0,0,0,0,0,0,0,s
0,0,1,0,0,0,0,0,0,0,n
"""

# Output example:

# LHS
"""
SLT,SLB,TL,K,PL,W,H,RL,A,O,*,E,U,F,RR,PR,B,L,G,TR,SR,D,Z,sendText
1,0,0,0,0,0,0,0,0,0,*,0,0,0,0,0,0,0,0,0,0,0,0,r
0,0,1,0,0,0,0,0,0,0,*,0,0,0,0,0,0,0,0,0,0,0,0,s
"""

# RHS
"""
SLT,SLB,TL,K,PL,W,H,RL,A,O,*,E,U,F,RR,PR,B,L,G,TR,SR,D,Z,sendText
0,0,0,0,0,0,0,0,0,0,*,0,0,0,0,0,0,0,0,1,0,0,0,r
0,0,0,0,0,0,0,0,0,0,*,0,0,0,0,1,0,0,0,0,0,0,0,s
"""
