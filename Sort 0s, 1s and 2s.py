class Solution:
    def sort012(self, arr):
        zero,one,two=[],[],[]
        for i in range(len(arr)):
            if arr[i] == 0:
                zero.append(arr[i])
            elif arr[i]== 1:
                one.append(arr[i])
            else:
                two.append(arr[i])
        arr[:] = zero + one + two

class Solution:
    def sort012(self, arr):
        n= len(arr)
        l,m =0,0
        h = n-1
        
        while m<=h:
            if arr[m] == 0:
                arr[l],arr[m] = arr[m], arr[l]
                l+=1
                m+=1
            elif arr[m] == 1:
                m+=1
            else:
                arr[m],arr[h] = arr[h], arr[m]
                h-=1
                
        return arr 
