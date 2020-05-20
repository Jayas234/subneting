print("what is ur IP address")
ip=input()
l=ip.split('/')
ip_address=l[0].split('.')
pre_len=int(l[1])
x=ip_address[0:3]
sd='.'.join(x)+'.'
print(sd,"d value")
if int(ip_address[0])>=0 and int(ip_address[0])<=127:
    p=8
    print("class A")
elif int(ip_address[0])>=128 and int(ip_address[0])<=191:
    p=16
    print("class B")
elif int(ip_address[0])>=192 and int(ip_address[0])<=223:
    p=24
    print("class C")
    n_b=pre_len-p
    h_b=8-n_b
    i=0
    main=[]
    m=[]
    for j in range(1,2**n_b+1):
        for d in range(2**h_b):
            ipval=str(sd)+str(i)
            m.append(str(ipval))
            i+=1
            ipval=''
        print("Network :",j)    
        print("Network ID :",m[0])
        print("Usable IP Range :",m[1],"-",m[-2])
        print("Broadcast ID:",m[-1])
    
        main.append(m)
        m=[]

"""n_b=pre_len-p
h_b=8-n_b
i=0
main=[]
m=[]
for j in range(1,2**n_b+1):
    for d in range(2**h_b):
        ipval=str(sd)+str(i)
        m.append(str(ipval))
        i+=1
        ipval=''
    print("Network :",j)    
    print("Network ID :",m[0])
    print("Usable IP Range :",m[1],"-",m[-2])
    print("Broadcast ID:",m[-1])
    
    main.append(m)
    m=[]"""

    
    
    
