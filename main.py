from jinja2 import Environment, FileSystemLoader 

class Comms:
    def __init__(self,s,t,n):
        self.state = s
        self.tp = t
        self.n = n

    def addc(self,c):
        self.c = c

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

class Moves: 
    def __init__(self,s,n):
        self.state = s
        self.n = n
        self.o = None

    def addi(self,i):
        self.i = i
    
    def addc(self,c):
        self.c = c

    def addns(self,ns):
        self.ns = ns

    def addo(self,o):
        self.o = o

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __str__(self):
        return "n{},i{},c{},ns{},o{}".format(self.n,self.i,self.c,self.ns,self.o)

    def __repr__(self):
        return "n{},i{},c{},ns{},o{}".format(self.n,self.i,self.c,self.ns,self.o)

    def __hash__(self):
        return hash((self.__dict__))

def get_ctrl_ids(content):
    a = set(map(lambda x: int(x[0][1]), content))
    return list(a) 

def mk_comms(line, i):
    return Comms(s=int(line[1][1]),t=int(line[2][1]),n=i)

def mk_moves(line, i):
    return Moves(s=int(line[2][1]),n=i)

def toint(lst):
    t = 0
    for i,d in enumerate(lst):
        t += 2**i if d == 1 else 0
    return t

def comms_return(comms):
    lst = []
    for line in c_content:
        if comms.n == int(line[1][1]) and comms.tp == int(line[2][1]):
            lst.append(int(line[-1]))
    comms.addc(toint(lst))
    return comms

def moves_return(move):
    lst = []
    for line in m_content:
        print move
        if move.ns == int(line[2][1]) and move.n == int(line[0][1]):
            lst.append(int(line[-1]))
    move.addo(toint(lst))
    return move 

def moves_tau(move):
    lst = []
    for line in tau_content:
        if (move.state == int(line[1][1]) and move.n == int(line[0][1]) and 
                int(line[-1]) == 1):
            ns = int(line[4][1])
            i = int(line[2][1])
            c = int(line[3][1])
            move.addns(ns)
            move.addi(i)
            move.addc(c)
            lst.append(move)
    return lst


def get_comms(content, index):
    comms = []
    for line in content:
        if int(line[0][1]) == index:
            tmp = mk_comms(line, index) 
            if tmp not in comms:
                comms.append(tmp)
    comms = map(comms_return,comms)
    return comms

def get_moves(content, index):
    moves = []
    for line in content:
        if int(line[0][1]) == index:
            tmp = mk_moves(line,index) 
            if tmp not in moves:
                moves.append(tmp)
    moves = map(moves_tau,moves)
    moves = [item for sublist in moves for item in sublist]
    moves = map(moves_return,moves)
    moves = list(set(moves))
    return moves


def split_(lst):
    return lst.rstrip().split("_")

env = Environment(
    loader=FileSystemLoader("./"),
)

tpl =  env.get_template('template.py')

f = "sample_synth_output.txt"
content = map(split_,open(f).readlines())

c_content = map(lambda x: x[1:], list(filter(lambda x: x[0] == 'c',content)))
m_content = map(lambda x: x[1:], list(filter(lambda x: x[0] == 'o',content)))
tau_content = map(lambda x: x[1:], list(filter(lambda x: x[0] == 'tau',content)))
ctrl_ids = get_ctrl_ids(c_content)
for i in ctrl_ids:
    cs = get_comms(c_content,i)
    ms = get_moves(m_content,i)
    ctrl = tpl.render(ctrl_name="Controller{}".format(i), commsifs=cs, moveifs=ms)
    text_file = open("ctrl{}.py".format(i), "w")
    text_file.write(ctrl)
    text_file.close()



