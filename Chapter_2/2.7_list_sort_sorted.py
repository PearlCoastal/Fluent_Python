'''
Author: FEIFEI SUN
Description: 
Detail: 
Date: 2023-07-25 14:36:56

'''
if __name__ == '__main__': 
    fruits = ['grape', 'raspberry', 'apple', 'banana']
    
    # 打印的是sorted函数的返回值
    print(sorted(fruits))
    
    print(fruits)
    
    print(sorted(fruits, reverse=True))
    
    print(sorted(fruits, ken=len))
    
    # fruits 被原地修改，返回值None被print忽略
    print(fruits.sort())
    
    print(fruits)
    