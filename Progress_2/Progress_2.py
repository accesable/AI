# %%
import os
import itertools
from pysat.solvers import Glucose3

from colorama import Back

# %%
class ColorTable:
    def __init__(self):
        self.rows = 0
        self.columns = 0
        self.matrix = []
        self.matrix1d = []
        
    def load_table(self,filename):
        #load file into matrix
        if not os.path.exists(filename):
            raise Exception("No file Founded")
        f = open(filename,'r')
        firstline = f.readline()
        self.rows,self.columns = int(firstline.split()[0]),int(firstline.split()[1])
        self.transform_matrix_to_1d_array()
        for line in f:
            l=[]
            for i in line:
                if i =='\n' or i==" " or i==None:
                    continue
                if i.isnumeric() :
                    l.append(int(i))
                else:
                    l.append(i)
            self.matrix.append(l)
            
    def transform_matrix_to_1d_array(self):
        for i in range(self.columns):
            sublist = []
            for num in range((i * self.rows) + 1, (i + 1) * self.rows + 1):
                sublist.append(num)
            self.matrix1d.append(sublist)
            
    def printMatrix(self):
      for i in self.matrix:
        print(i)
        
    def get_surrounding(self,i:int,j:int):
        surrounding_elements =[self.matrix1d[i][j]]
        for k in range(i-1,i+2):
            if (k < 0 or k >= len(self.matrix1d)):
                continue
            for h in range(j-1,j+2):
                if (h < 0 or h >= len(self.matrix1d[0])):
                    continue
                else:
                    if not(k==i and h==j):
                        surrounding_elements.append(self.matrix1d[k][h])    
        return surrounding_elements
                    
    def generate_clause(self,surrounding_list:list,element_value:int):
        result=[]
        for i in itertools.combinations(surrounding_list,element_value+1):
            k=[]
            for j in i:
                k.append(-j)
            result.append(k)
        for i  in itertools.combinations(surrounding_list,len(surrounding_list)-element_value+1):
            result.append(list(i))
        return result
    
    def solve(self):
        cnf=Glucose3()
        for i in range(self.rows):
            for j in range(self.columns):
                if isinstance(self.matrix[i][j],int):
                    surrounds=self.get_surrounding(i,j)
                    clauses = self.generate_clause(surrounds,self.matrix[i][j])
                    for k in clauses:
                        cnf.add_clause(k)
        if cnf.solve():
            result=cnf.get_model()
            counter=0
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[0])):
                    item= self.matrix[i][j]
                    if isinstance(item,int) or item=='.':
                        if result[counter] >0:
                            print(Back.GREEN+str(item),end='')
                        else:
                            print(Back.RED+str(item),end='')
                    counter+=1
                print()
        else :
            return "Not good"

                

# %%
foo = ColorTable()
foo.load_table("test1.txt")
print(foo.solve())



