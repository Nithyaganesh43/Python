while(1):
    try:
        i=input()
        i=int(i)
        if i==0:
            raise Exception("zero error")
        if i<0:
            raise Exception("index")
        if i==3:
            raise ValueError("pesama sethuru ni ")
        else:
            print("seri kelambu !!")
              
    except Exception as e:
            if str(e)=='index':
                print("index ededed ")
            if str(e)[0]=='p':
                print("mithu inonu")
            if str(e)[0]=='e':
                print("ithu vera")
    