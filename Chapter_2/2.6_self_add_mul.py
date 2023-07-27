'''
Author: FEIFEI SUN
Description: 

Detail: 
Date: 2023-07-25 14:13:18

'''
def puzzel_self_add():
    t = (1, 2, [10, 20])
    # t[2] += [50, 60]
    print(t)
    # 直接运行程序会报错：TypeError，但是控制台再输出t时，他已经被更改
    
if __name__ == '__main__': 
    
    puzzel_self_add()
    
    import dis
    dis.dis('s[a] += b')