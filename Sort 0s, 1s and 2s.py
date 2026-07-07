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
