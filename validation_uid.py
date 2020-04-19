# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    #n =int(input())
    uids=[]
    for _ in range(int(input())):
        uid = input()
        uids.append(uid)
    print(uids)    
    for text in uids:
        matrix ={}
        num_chars=0
        num_digits=0
        for char in text:
            if (char.isdigit()):
                num_digits +=1
            if char in matrix:
                print("Invalid")
                break
            else:
                matrix[char]=1
        else:
            print("Valid")



  