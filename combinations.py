#https://www.interviewbit.com/problems/combinations/

def combinations(A,B):
    final_arr = []
    combinationsUtil(A,B,1,0,[],final_arr)
    return final_arr

def combinationsUtil(A,B,num,level,cur_list,final_arr):
    if level==B:
        final_arr.append(cur_list)
        return

    for i in xrange(num,A+1):
        temp_list = cur_list+[i]
        combinationsUtil(A,B,i+1,level+1,temp_list,final_arr)
    return

print combinations(1,1)
