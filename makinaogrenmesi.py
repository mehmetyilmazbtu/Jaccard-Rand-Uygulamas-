import pandas as pd
xls = pd.ExcelFile('kumeleme_sonucu.xls')
df1 = pd.read_excel(xls, 'Sınıf Etiketleri')
df2 = pd.read_excel(xls, 'Hangi örnek hangi kümede')

x=df2["Unnamed: 2"]
Kume1=[]

Kume2_1=[]
Kume2_2=[]

Kume3_1=[]
Kume3_2=[]
Kume3_3=[]

Kume4_1=[]
Kume4_2=[]
Kume4_3=[]
Kume4_4=[]

Kume5_1=[]
Kume5_2=[]
Kume5_3=[]
Kume5_4=[]
Kume5_5=[]

Kume6_1=[]
Kume6_2=[]
Kume6_3=[]
Kume6_4=[]
Kume6_5=[]
Kume6_6=[]

Kume7_1=[]
Kume7_2=[]
Kume7_3=[]
Kume7_4=[]
Kume7_5=[]
Kume7_6=[]
Kume7_7=[]

Kume8_1=[]
Kume8_2=[]
Kume8_3=[]
Kume8_4=[]
Kume8_5=[]
Kume8_6=[]
Kume8_7=[]
Kume8_8=[]

Kume9_1=[]
Kume9_2=[]
Kume9_3=[]
Kume9_4=[]
Kume9_5=[]
Kume9_6=[]
Kume9_7=[]
Kume9_8=[]
Kume9_9=[]

Kume10_1=[]
Kume10_2=[]
Kume10_3=[]
Kume10_4=[]
Kume10_5=[]
Kume10_6=[]
Kume10_7=[]
Kume10_8=[]
Kume10_9=[]
Kume10_10=[]


def diziyeAtama(Kume,clusterNo,cluster):
    sinif1=0
    sinif2=0
    sinif3=0
    for i in range(1, len(df2[cluster])):
        if df2[cluster][i]==clusterNo:
            Kume.append(i)
    for i in range(0,len(Kume)):
        if(Kume[i]<=50):
            sinif1=sinif1+1
        elif(Kume[i]>50 and Kume[i]<=100):
            sinif2=sinif2+1
        elif(Kume[i]>100):
            sinif3=sinif3+1
    Kume.append(sinif3)
    Kume.append(sinif2)
    Kume.append(sinif1)

diziyeAtama(Kume1,1,'Küme Sayısı')

diziyeAtama(Kume2_1,1,'Unnamed: 2')
diziyeAtama(Kume2_2,2,'Unnamed: 2')

diziyeAtama(Kume3_1,1,'Unnamed: 3')
diziyeAtama(Kume3_2,3,'Unnamed: 3')
diziyeAtama(Kume3_3,3,'Unnamed: 3')

diziyeAtama(Kume4_1,1,'Unnamed: 4')
diziyeAtama(Kume4_2,3,'Unnamed: 4')
diziyeAtama(Kume4_3,3,'Unnamed: 4')
diziyeAtama(Kume4_4,4,'Unnamed: 4')

diziyeAtama(Kume5_1,1,'Unnamed: 5')
diziyeAtama(Kume5_2,2,'Unnamed: 5')
diziyeAtama(Kume5_3,3,'Unnamed: 5')
diziyeAtama(Kume5_4,4,'Unnamed: 5')
diziyeAtama(Kume5_5,5,'Unnamed: 5')

diziyeAtama(Kume6_1,1,'Unnamed: 6')
diziyeAtama(Kume6_2,2,'Unnamed: 6')
diziyeAtama(Kume6_3,3,'Unnamed: 6')
diziyeAtama(Kume6_4,4,'Unnamed: 6')
diziyeAtama(Kume6_5,5,'Unnamed: 6')
diziyeAtama(Kume6_6,6,'Unnamed: 6')

diziyeAtama(Kume7_1,1,'Unnamed: 7')
diziyeAtama(Kume7_2,2,'Unnamed: 7')
diziyeAtama(Kume7_3,3,'Unnamed: 7')
diziyeAtama(Kume7_4,4,'Unnamed: 7')
diziyeAtama(Kume7_5,5,'Unnamed: 7')
diziyeAtama(Kume7_6,6,'Unnamed: 7')
diziyeAtama(Kume7_7,7,'Unnamed: 7')

diziyeAtama(Kume8_1,1,'Unnamed: 8')
diziyeAtama(Kume8_2,2,'Unnamed: 8')
diziyeAtama(Kume8_3,3,'Unnamed: 8')
diziyeAtama(Kume8_4,4,'Unnamed: 8')
diziyeAtama(Kume8_5,5,'Unnamed: 8')
diziyeAtama(Kume8_6,6,'Unnamed: 8')
diziyeAtama(Kume8_7,7,'Unnamed: 8')
diziyeAtama(Kume8_8,8,'Unnamed: 8')

diziyeAtama(Kume9_1,1,'Unnamed: 9')
diziyeAtama(Kume9_2,2,'Unnamed: 9')
diziyeAtama(Kume9_3,3,'Unnamed: 9')
diziyeAtama(Kume9_4,4,'Unnamed: 9')
diziyeAtama(Kume9_5,5,'Unnamed: 9')
diziyeAtama(Kume9_6,6,'Unnamed: 9')
diziyeAtama(Kume9_7,7,'Unnamed: 9')
diziyeAtama(Kume9_8,8,'Unnamed: 9')
diziyeAtama(Kume9_9,9,'Unnamed: 9')

diziyeAtama(Kume10_1,1,'Unnamed: 10')
diziyeAtama(Kume10_2,2,'Unnamed: 10')
diziyeAtama(Kume10_3,3,'Unnamed: 10')
diziyeAtama(Kume10_4,4,'Unnamed: 10')
diziyeAtama(Kume10_5,5,'Unnamed: 10')
diziyeAtama(Kume10_6,6,'Unnamed: 10')
diziyeAtama(Kume10_7,7,'Unnamed: 10')
diziyeAtama(Kume10_8,8,'Unnamed: 10')
diziyeAtama(Kume10_9,9,'Unnamed: 10')
diziyeAtama(Kume10_10,10,'Unnamed: 10')

Kumeler1=[Kume1]
Kumeler2=[Kume2_1,Kume2_2]
Kumeler3=[Kume3_1,Kume3_2,Kume3_3]
Kumeler4=[Kume4_1,Kume4_2,Kume4_3,Kume4_4]
Kumeler5=[Kume5_1,Kume5_2,Kume5_3,Kume5_4,Kume5_5]
Kumeler6=[Kume6_1,Kume6_2,Kume6_3,Kume6_4,Kume6_5,Kume6_6]
Kumeler7=[Kume7_1,Kume7_2,Kume7_3,Kume7_4,Kume7_5,Kume7_6,Kume7_7]
Kumeler8=[Kume8_1,Kume8_2,Kume8_3,Kume8_4,Kume8_5,Kume8_6,Kume8_7,Kume8_8]
Kumeler9=[Kume9_1,Kume9_2,Kume9_3,Kume9_4,Kume9_5,Kume9_6,Kume9_7,Kume9_8,Kume9_9]
Kumeler10=[Kume10_1,Kume10_2,Kume10_3,Kume10_4,Kume10_5,Kume10_6,Kume10_7,Kume10_8,Kume10_9,Kume10_10]
a=0
b=0
c=0
d=0
aToplam=0
bToplam=0
cToplam=0
dToplam=0


def Kombinasyon(kumeler,K,a,b,c,d):
    a1=0
    a2=0
    a3=0
    b1=0
    b2=0
    b3=0
    c1=0
    c2=0
    c3=0
    d1=0
    d2=0
    d3=0

    for i in range(0,K):
        a1=(kumeler[i][-1]*(kumeler[i][-1]-1))/2
        a2=(kumeler[i][-2]*(kumeler[i][-2]-1))/2
        a3=(kumeler[i][-3]*(kumeler[i][-3]-1))/2
        a=a+a1+a2+a3
    ##print(a)
    for i in range(0,len(kumeler)):
        
        for j in range(i,len(kumeler)):
            if(i==j):
                continue
            b1=b1+kumeler[i][-1]*kumeler[j][-1]
            b2=b2+kumeler[i][-2]*kumeler[j][-2]
            b3=b3+kumeler[i][-3]*kumeler[j][-3]
    b=b1+b2+b3
    ##print(b)

    for i in range(0,K):
        c1=kumeler[i][-1]*kumeler[i][-2]
        c2=kumeler[i][-2]*kumeler[i][-3]
        c3=kumeler[i][-3]*kumeler[i][-1]
        c=c+c1+c2+c3
    ##print(c)
    for i in range(0,len(kumeler)):
        
        for j in range(i,len(kumeler)):
            if(i==j):
                continue
            d1=d1+kumeler[i][-1]*kumeler[j][-2]
            d2=d2+kumeler[i][-2]*kumeler[j][-3]
            d3=d3+kumeler[i][-3]*kumeler[j][-1]
    d=d1+d2+d3
    ##print(d)
    return a,b,c,d

a,b,c,d=Kombinasyon(Kumeler1,1,a,b,c,d)
aToplam=aToplam+a
bToplam=bToplam+b
cToplam=cToplam+c
dToplam=dToplam+d
a,b,c,d=Kombinasyon(Kumeler2,2,a,b,c,d)
aToplam=aToplam+a
bToplam=bToplam+b
cToplam=cToplam+c
dToplam=dToplam+d
a,b,c,d=Kombinasyon(Kumeler3,3,a,b,c,d)
aToplam=aToplam+a
bToplam=bToplam+b
cToplam=cToplam+c
dToplam=dToplam+d
a,b,c,d=Kombinasyon(Kumeler4,4,a,b,c,d)
aToplam=aToplam+a
bToplam=bToplam+b
cToplam=cToplam+c
dToplam=dToplam+d
a,b,c,d=Kombinasyon(Kumeler5,5,a,b,c,d)
aToplam=aToplam+a
bToplam=bToplam+b
cToplam=cToplam+c
dToplam=dToplam+d
a,b,c,d=Kombinasyon(Kumeler6,6,a,b,c,d)
aToplam=aToplam+a
bToplam=bToplam+b
cToplam=cToplam+c
dToplam=dToplam+d
a,b,c,d=Kombinasyon(Kumeler7,7,a,b,c,d)
aToplam=aToplam+a
bToplam=bToplam+b
cToplam=cToplam+c
dToplam=dToplam+d
a,b,c,d=Kombinasyon(Kumeler8,8,a,b,c,d)
aToplam=aToplam+a
bToplam=bToplam+b
cToplam=cToplam+c
dToplam=dToplam+d
a,b,c,d=Kombinasyon(Kumeler9,9,a,b,c,d)
aToplam=aToplam+a
bToplam=bToplam+b
cToplam=cToplam+c
dToplam=dToplam+d
a,b,c,d=Kombinasyon(Kumeler10,10,a,b,c,d)
aToplam=aToplam+a
bToplam=bToplam+b
cToplam=cToplam+c
dToplam=dToplam+d
print("a: ",a," b: ",b," c: ",c," d: ",d)

jaccard=a/(a+b+c)
rand=(a+d)/(a+b+c+d)

print("Jaccard: ",jaccard)
print("Rand: ",rand)







