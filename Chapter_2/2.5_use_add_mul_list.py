'''
Author: FEIFEI SUN
Description: 
Detail: 
Date: 2023-07-20 17:26:06

'''
def new_list_ref():
    print("创建不含引用的列表")
    board = [['_'] * 3 for i in range(3)]
    print(board)
    board[1][2] = 'X'
    print(board)

    
    print("-----含有3个指向同一对象的引用的列表是毫无用处的-----")
    weird_board = [['_'] * 3] * 3
    print(weird_board)
    
    print("想要标记第一行第二列的元素时，马上暴露出列表内的3个引用指向同一个对象的事实")
    weird_board[1][2] = 'X'
    print(weird_board)
    
if __name__ == '__main__':   

    print("将一个序列复制几份再拼接起来，更快的方法是乘法")
    l = [1, 2, 3]
    print(l * 5)
    
    print("拼接和乘操作，都会产生一个新序列")
    
    print(5 * 'abcd ')
    
    new_list_ref()
    
    
    