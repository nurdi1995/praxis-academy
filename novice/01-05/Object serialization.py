#1.
#python program to illustrate
#pickle.dump()

import pickle
from StringIO import StringIO

class SimpleObject(object):

    def __init__(self, name):
        self.name = name
        l = list(name)
        l.reverse()
        self.name_backwards = ''.join(l)
        return

    data = []
    data.append(SimpleObject('pickle')) 
    data.append(SimpleObject('cPickle'))
    data.append(SimpleObject('last'))

    #Simulasi a file with StringIO
    out_s =StringIO()

    #Write to the stream
    for o in data:
        print ('writing: %s (%s)') % (o.name, o.nume_backwards)
        pickle.dump(o, out_s)
        out_s.flush()
    
   
   
#2.
#Python program to illustrate 
#picle.dumps()
data1 = [ {'a':'A', 'b':2, 'c':3.0} ]
data_string = pickle.dump(data1)
print('PICKLE: ', data_string)  


#3.
#Python program to illustrate
#pickle.load()

class SimpleObject(object):
    self.name = name
    l = list(name)
    l.reverse()
    self.name_backwards = ''.join(l)

data = []
data.append(SimpleObject('pickle'))
data.append(SimpleObject('cPickle'))
data.append(SimpleObject('last'))

#simulate a file with StringIO
out_s = StringIO()


#Write to the stream
for o in data:
    print('WRITING : %s (%s)' % (o.name, o.name_backwards))
    pickle.dump(o,out_s)
    out_s.flush()

#Set up read-able stream
in_s = StringIO(out_s.getvalue())


#Read the data 
while True:
    try:
        o = pickle.load(in_s)
    except EOFError:
        break
    else:
        print ('READ: %s (%s)' %(o.name, o.name_backswards))


#4.
import pprint

data2 = [{'a':'A', 'b' :2, 'c':3.0}]
pprint 'BEFORE',
pprint.pprint(data2)

data2_string = pickle.dumps(data2)

data3 = pickle.load(data2_string)
print('AFTER :'),
pprint.pprint(data3) 

print('SAME:',(data2 is data3))
print('EQUAL',(data2 == data3))


#5. 
class TextReader: 
    def __init__(self, filename):
        self.filename = filename
        self.file  = open(filename)
        self.lineo= 0
    
    def readline(self):
        self.lineno +=1
        line = self.file.readline()
        if not line:
            return None
        if line.endswith('\n'):
            line = line[:-1]
        return "%i: %s" % (self.lineno, line)

    def ___getstate__(self):
        state = self.__dict__.copy()
        del state['file']
        return state
    
    def __setstate_(self, state):
        self.__dict__.update(state)
        file = open(self.lineno)
        for _ in range(self.lineno):
            file.readline()
        self.file = file
reader = TextReader("hello.txt")
print(reader.readline())
print(reader.readline())
new_reader = pickle.loads(pickle.dump(reader))
print(new_reader.readline())


