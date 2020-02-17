dp={}
dp[1]=1
dp[2]=1
dp[3]=1
""" def get_op(m):
    if m in dp.keys():
        return dp[m]+1
    if m%3==0 and m%2==0:
        dp[m]=min(get_op(m/3),get_op(m/2),get_op(m-1))
    if m%3!=0 and m%2==0:
        dp[m]=min(get_op(m/2),get_op(m-1))
    if m%3==0 and m%2!=0:
        dp[m]=min(get_op(m/3),get_op(m-1))
    if m%3!=0 and m%2!=0:
        dp[m]=get_op(m-1)

    return dp[m]+1
get_op(96234) """


def get_op_iter(num):
    path_dic={}
    for m in range(4,num+1):
        path=[]
        ls= []
        if m%2==0:
            path.append(m/2)
            ls.append(dp[m/2])
        if m%3==0:
            path.append(m/3)
            ls.append(dp[m/3])
        path. (m-1)
        ls.append(dp[m-1])
        path_dic[m]=path[ls.index(min(ls))]
        dp[m]=min(ls)+1
    path_dic[1]=1
    path_dic[2]=1
    path_dic[3]=1
    path_list=[]
    path_list.append(1)

    key=num
    for _ in path_dic:
        if key<=1:
            break
        path_list.append(int(key))
        key=path_dic[key]
    print(dp[num])
    print(sorted(path_list))

   #print(dp[m])
num=96234
get_op_iter(num)
        
        

