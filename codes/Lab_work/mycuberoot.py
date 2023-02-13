def mycubrt(x, debug=False):
    if x==0.:
       return 0.
       
     s=1.
     kmax=125
     tol=1.0e-14
     for k in range(kmax):
        if debug:
             print("At itertaion no.%s, s= %15.8f" %(k,s))
             s0=s
             s=(1/3)*((2*s)+(x/(s*s)))
             delta_s=s-s0
             if(abs(delta_s/x))<tol:
               break
      if debug:
           print("after %s iterations, s=%15.10f" %(k+1,s)
      return s
   
   #define test cases
def test_main():
    from numpy import cbrt
    xvalues=[0. , 8., 1000, 1e9, 1000]
    for x in xvalues:
        print("Testing with x=%10.12e" %x)
        c_nt=cbrtNewton(x)
        c_numpy=cbrt(x)
        print("cbrtNewton s=%15.7e, numpy s=%15.7e" %(c, c_numpy))
        assert  abs(c_nt-c_numpy)< 1e-14,"Cube root calculated does not agree with newton raphson method "
    
       
