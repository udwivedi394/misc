#https://www.interviewbit.com/problems/gray-code/
import time

def grayCode(A):
    final_arr = []
    return grayCodeUtility(A,0,[0])
    #return final_arr

def grayCodeUtility(A,index,curNum):
    if index >= A:
        return curNum

    reflect_curNum = [curNum[i]|(1<<index) for i in xrange(len(curNum)-1,-1,-1)]
    return grayCodeUtility(A,index+1,curNum+reflect_curNum)

print grayCode(2)
