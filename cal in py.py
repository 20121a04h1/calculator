class calculator:
    def add(self,a,b):
        print(a+b)
    def sub(self,a,b):
        print(a-b)
    def mul(self,a,b):
        print(a*b)
    def di(self,a,b):
        print(a/b)
while 1:
    cal=calculator()
    a,c,b=input()
    a,b=int(a),int(b)
    if c=="+":
        cal.add(a,b)
    elif c=="-":
        cal.sub(a,b)
    elif c=="*":
        cal.mul(a,b)
    elif c=="/":
        cal.di(a,b)
    else:
        print("oops..! wrong operator")
    


        
