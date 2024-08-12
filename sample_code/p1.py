# 定義 class `Product`
class Product:
    
    def __init__(self, name, price, stock=0, discount=None):
        self.__name = name
        self.__price = price
        self.__stock = stock
        self.__discount = discount
        
    def estimate(self, n):
        if self.__discount is not None:
            return self.__discount(self.__price, n)
        else:
            return self.__price * n
        
    def sale(self, n):
        if n > self.__stock:
            return -1
        else:
            self.__stock -= n
            return self.estimate(n)
        
    def restock(self, n):
        if n > 0:
            self.__stock += n
            
    def is_on_sale(self):
        return self.__discount is not None
    
    # getter and setter
    def get_name(self):
        return self.__name
    
    def get_price(self):
        return self.__price
    
    def set_price(self, n):
        if n > 0:
            self.__price = n
            
    def get_stock(self):
        return self.__stock
    
    def set_discount(self, discount):
        if callable(discount) or discount is None:
            self.__discount = discount
    

# 定義打八折
def discount_20_percent_off(x, n):
    return int(x * n * 0.8)


# 定義買三送一
def buy_3_get_1(x, n):
    num = n // 4 * 3 + n % 4
    return int(x * num)


# 主流程
if __name__ == '__main__':
    
    # 宣告 apple，定價 20 元
    apple = Product('Apple', 20)

    # 印出目前蘋果的庫存量
    # 預期輸出 "Apple stock: 0"
    print("%s stock: %d"%(apple.get_name(), apple.get_stock()))

    # 進貨 20 顆，然後在印一次庫存量
    # 預期輸出 "Apple stock: 20"
    apple.restock(20)
    print("%s stock: %d"%(apple.get_name(), apple.get_stock()))

    # 賣蘋果 15 顆，印出所得還有庫存量
    # 預期輸出 "You earn 300 dollar(s)", "Apple stock: 5"
    income = apple.sale(15)
    if income >= 0:
        print("You earn %d dollar(s)."%(income))
    else:
        print("Stock is not enough!")    
    print("%s stock: %d"%(apple.get_name(), apple.get_stock()))

    # 賣出 10 顆，因為庫存不足會印出 "Stock is not enough!", "Apple stock: 5"
    income = apple.sale(10)
    if income >= 0:
        print("You earn %d dollar(s)."%(income))
    else:
        print("Stock is not enough!")
    print("%s stock: %d"%(apple.get_name(), apple.get_stock()))

    # 將 apple 售價訂為 25 元，折扣打八折
    apple.set_price(25)
    apple.set_discount(discount_20_percent_off)

    # 估 20 顆蘋果的價格
    # 預期輸出 "Estimation cost: 400"
    print("Estimation cost: %d"%(apple.estimate(20)))


    # 宣告 orange，定價 30 元，庫存 10，有買三送一的優惠
    orange = Product('orange', 30, stock=10, discount=buy_3_get_1)

    # 賣 5 顆橘子，顯示收益與剩餘庫存
    # 預期輸出 "You earn 120 dollar(s)
    income = orange.sale(5)
    if income >= 0:
        print("You earn %d dollar(s)."%(income))
    else:
        print("Stock is not enough!")

    # 移除橘子的優惠
    orange.set_discount(None)

    # 估算 10 蘋果和 12 顆橘子的價格
    # 預期輸出 "Estimation cost: 560"
    estimation = apple.estimate(10) + orange.estimate(12)
    print("Estimation cost: %d"%(estimation))
    