import  matplotlib.pyplot as plt
def main ():
    segitiga_samasisi()
    persegi()
    belah_ketupat()
    layang2()
    trapesium()
    segitiga_terserah()
    segitigaSamaKaki()
    segitigaSiku()
    PersegiPanjang()
    plt.show()

def segitiga_samasisi():
    plt.figure(figsize=(5,4))
    plt.xlabel('Segitiga Sama Sisi')
    line1=plt
    line2=plt
    line1.plot([0,8],[0,0],c='b')
    line1.plot([8,4],[0,5],c='b')
    line1.plot([0,4],[0,5],c='b')
    line2.plot([0,6],[0,2.5],c='r',ls='--')
    line2.plot([8,2],[0,2.5],c='r',ls='--')
    line2.plot([4,4],[5,0],c='r',ls='--')

def segitiga_terserah():
    plt.figure(figsize=(5,4))
    plt.xlabel('Segitiga terserah')
    line1=plt
    line1.plot([0,8],[0,3],c='b')
    line1.plot([8,4],[3,5],c='b')
    line1.plot([0,4],[0,5],c='b')


def persegi():
    plt.figure(figsize=(4,4))
    plt.xlabel('Persegi')
    line1=plt
    line2=plt
    line1.plot([0,6],[0,0],c='b')
    line1.plot([0,0],[0,6],c='b')
    line1.plot([6,6],[0,6],c='b')
    line1.plot([0,6],[6,6],c='b')
    line2.plot([0,6],[3,3],c='r',ls='--')
    line2.plot([3,3],[0,6],c='r',ls='--')
    line2.plot([3,3],[0,6],c='r',ls='--')
    line2.plot([0,6],[0,6],c='r',ls='--')
    line2.plot([0,6],[6,0],c='r',ls='--')
def trapesium():
    plt.figure(figsize=(4,4))
    plt.xlabel('Trapesiem')
    line1=plt
    line2=plt
    line1.plot([-2,8],[0,0],c='b')
    line1.plot([-2,0],[0,6],c='b')
    line1.plot([8,6],[0,6],c='b')
    line1.plot([0,6],[6,6],c='b')
    line2.plot([3,3],[0,6],c='r',ls='--')


def belah_ketupat():
    plt.figure(figsize=(4,4))
    plt.xlabel('Belah Ketupat')
    line1=plt
    line2=plt
    line1.plot([0,2],[2,0],c='b')
    line1.plot([0,2],[2,4],c='b')
    line1.plot([2,4],[4,2],c='b')
    line1.plot([2,4],[0,2],c='b')
    line2.plot([0,4],[2,2],c='r',ls='--')
    line2.plot([2,2],[4,0],c='r',ls='--')

def layang2():
    plt.figure(figsize=(4,4))
    plt.xlabel('Belah Ketupat')
    line1=plt
    line2=plt
    line1.plot([0,2],[2,0],c='b')
    line1.plot([0,2],[2,4],c='b')
    line1.plot([2,6],[4,2],c='b')
    line1.plot([2,6],[0,2],c='b')
    line2.plot([0,6],[2,2],c='r',ls='--')
    line2.plot([2,2],[4,0],c='b',ls='--')

def segitigaSamaKaki():
    line1 = plt
    line1.figure(7)
    line1.plot([1, 5], [1, 1], color='blue')  # base
    line1.plot([1, 3], [1, 9], color='blue')
    line1.plot([5, 3], [1, 9], color='blue')
    line1.plot([3, 3], [1, 9], color='red', linestyle='--')
    line1.plot([8, 8], [1, 1], color='white')
    line1.xlabel('Segitiga Sama Sisi')

def PersegiPanjang():
    line2 = plt
    line2.figure(8)
    line2.plot([1, 8], [1, 1], color='blue')
    line2.plot([8, 8], [1, 4], color='blue')
    line2.plot([1, 8], [4, 4], color='blue')
    line2.plot([1, 1], [1, 4], color='blue')
    line2.plot([1, 8], [2.5, 2.5], color='red', linestyle='--')
    line2.plot([4.5, 4.5], [1, 4], color='red', linestyle='--')
    line2.xlabel('Persegi Panjang')

def segitigaSiku():
    line3 = plt
    line3.figure(9)
    line3.plot([1, 6], [1, 1], color='blue')  # base
    line3.plot([1, 1], [1, 6], color='blue')
    line3.plot([1, 6], [6, 1], color='blue')
    line3.plot([1, 3.5], [1, 3.5], color='red', linestyle='--')
    line3.plot([7, 7], [1, 1], color='white')
    line3.xlabel('Segitiga Siku-Siku')

if __name__ == '__main__':
    main()