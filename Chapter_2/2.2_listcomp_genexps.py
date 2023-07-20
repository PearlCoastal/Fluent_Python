if __name__ == '__main__':
    colors = ['black', 'white']
    sizes = ['S', 'M', 'L']
    
    print("方式一：列表推导方式")
    tshirts = [(color, size) for color in colors for size in sizes]
    print(tshirts)
    
    print("方式二：不采用列表推导方式")
    for color in colors:
        for size in sizes:
            print((color, size))
    
    print("切换排列方式：先尺码后颜色")
    tshirts_size_color = [(color, size) for size in sizes for color in colors]
    print(tshirts_size_color)
    
    print("利用生成式表达式实现了一个笛卡尔积：")
    for tshirt in ('%s %s' % (c, s) for c in colors for s in sizes):
        print(tshirt)
    print("生成器表达式逐个产出元素，不会一次性产出一个包含多个元素的列表，节省内存开销")