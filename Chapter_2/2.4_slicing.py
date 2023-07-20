def tuple_slicing():
    l = [10, 20, 30, 40, 50, 60]
    print(l[:2])
    print(l[2:])
    print(l[:3])
    print(l[3:])
    
    print("-----对对象进行切片-----")
    s = "bicycle"
    print("间隔取值" + s[::3])
    print("反向取值：" + s[::-1])
    print("反向间隔取值" + s[::-2])
    print("从下标开始间隔2个数取值：" + s[2::2])
    
    print("-----给切片赋值-----")
    l = list(range(10))
    print(l)
    
    print("把切片放在赋值语句的左边：")
    l[2:5] = [20, 30]
    print(l)
    
    print("切除操作：")
    del l[5:7]
    print(l)
    
    print("就地修改操作：")
    l[3::2] = [11, 22]
    print(l)

if __name__ == '__main__':   

    print("2.3.6 切片")
    
    tuple_slicing()