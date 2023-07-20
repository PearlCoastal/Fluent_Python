'''
Author: FEIFEI SUN
Description: 
Detail: 
Date: 2023-07-20 14:58:23

'''
def tuple4record(traveler_ids):
    
    print('迭代的过程中，passport 变量被绑定到每一个元组上')
    for passport in sorted(traveler_ids):
        print('%s/%s' % passport)
    
    print('拆包 unpacking for 循环分别提取元组里的元素，第二个元素没什么用 赋值给"_"占位符') 
    
    print('拆包让元组可以完美的被当作记录来使用')
    for country, _ in traveler_ids:
        print('country is %r' % country)

def tuple_unpacking(lax_coordinates):
    
    print('元组拆包')
    latitude, longitude = lax_coordinates
    
    print('latitude = %r' % latitude)
    print('longitude = %r' % longitude)
    
    print('优雅的交换两个变量的值：不适用中间变量')
    latitude, longitude = longitude, latitude
    
    print('latitude = %r' % latitude)
    print('longitude = %r' % longitude)
    
    print("用*运算符，将一个可迭代的对象拆开作为函数的参数")
    print(divmod(20, 8))
    
    t = (20, 8)
    print(divmod(*t))
    
    quotient, remainder = divmod(*t)
    print('quotient = %r' % quotient)
    print('remainder = %r' % remainder)
    
    print("元组拆包，让一个函数永远组的形式返回多个值")
    import os
    print("os.path.split() 返回一个（path, last_part）组成的元组")
    _, filename = os.path.split('/home/luciano/.ssh/idrsa.pub')
    print('filename = %r' % filename)
    
    print("用 * 来处理剩下的元素")
    a, b, *rest = range(5)
    print('(%r %r %r)' % (a, b, rest))
    
    a, b, *rest = range(2)
    print('(%r %r %r)' % (a, b, rest))
    
    print("平行赋值中， *前缀只能用在一个变量名前，但可以出现在任意位置")
    a, *body, c, d = range(5)
    print('(%r %r %r %r)' % (a, body, c, d))

def tuple_recur_unpacking():
    metro_areas = [('Tokyo','JP',36.933,(35.689722,139.691667)),
                    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
                    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
                    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
                    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833))
                    ]
    
    print("学习一下format()格式化函数")
    print("^ 居中，< 左对齐 > 右对齐")
    print(":后面带填充的字符，不指定默认用空格填充")
    print("{:15} = 填充15个空格")
    print("{:^9} = 居中填充9个空格")
    print("{:9.4f} = 填充9个空格，保留小数点后四位")
    
    print('{:15} | {:^9} | {:^9}'.format('', 'lat.', 'long.'))
    fmt = '{:15} | {:9.4f} | {:9.4f}'
    
    for name, cc, pop, (latitude, longitude) in metro_areas:
        if longitude <= 0:
            print(fmt.format(name, latitude, longitude))

def tuple_namedtuple():
    
    print("-----定义和使用一个具名元组-----")
    from collections import namedtuple
    City = namedtuple('City', 'name country population coordinates')
    
    tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
    
    print(tokyo)
    
    print("可以通过字段名和位置获取一个字段的信息")
    
    print('population = %r' % (tokyo.population))
    
    print('coordinates = (%r, %r)' % (tokyo.coordinates))
    
    print('City index 1 = %r' % tokyo[1])
    
    print("-----namedtuple的一些专有属性-----")
    print("展示几个最有用的：")
    
    print("1. 类属性 _fields属性是一个包含这个类所有字段名称的元组")
    print(City._fields)
    
    print("2. 类方法： _make(iterable)")
    print("2. 实例方法：_asdict()")
    LatLong = namedtuple('LatLong', 'lat long')
    
    delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))
    print("-----_make()生成实例方法-----")
    delhi = City._make(delhi_data)
    print(delhi._asdict)
    
    print("-----City()类生成实例方法-----")
    delhi_city = City(*delhi_data)
    print(delhi_city._asdict)
    
    for key, value in delhi._asdict().items():
        print(key + ":", value)

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

    # 机场的经纬度
    lax_coordinates = (33.9425, -118.408056)
    
    # 东京市的一些信息
    city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
    
    # 元组列表 （country code， passport numbers）
    traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]
    
    print("2.3.1 元组和记录")
    # tuple4record(traveler_ids)
    
    print('2.3.2 元组拆包')
    # tuple_unpacking(lax_coordinates)
    
    print("2.3.3 嵌套元组拆包")
    # tuple_recur_unpacking()
    
    print("2.3.4 具名元组")
    # tuple_namedtuple()
    
    print("2.3.6 切片")
    tuple_slicing()
    