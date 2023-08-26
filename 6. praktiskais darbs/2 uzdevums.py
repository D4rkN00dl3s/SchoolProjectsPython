def dienas():
    d=0
    pat=5
    c=200
    while c > 0:
        #Iztereja viena diena
        pat+=pat*20/100
        #Cik cementu palika
        c=c-pat
        #Saskaitam dienas
        d+=1
    
    print(f"200 tonnu cementa pietiks uz: {d} dienas")
        
dienas()