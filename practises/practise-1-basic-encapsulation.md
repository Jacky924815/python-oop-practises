# 練習 1 － 商品管理
## 練習說明
本練習利用商品買賣行為，練習物件導向「**封裝**」（**Encapsulation**）的概念。在這個練習中先不用 `try-except` 的語法做例外處理 (Exception Handling)。


## 情境說明
一間商店要管理許多的商品，需要一套庫存系統。該系統大致會有下面的使用案例：
- 消費者會店家下訂商品。
- 店家會進貨與出貨。
- 計算消費的總價格。
- 有時候店家會推出促邀活動。
- 客人會和店家估價。


## 設計要求
請利用 Python 設計出一個 class `Produce`，在該類別中包含著以下的**實體屬性**（**Instance Attributes**）：
- `__name: str`: 商品的名稱。
- `__price: int`： 商品的價格，以 1 元為單位。
- `__stock: int = 0`: 商品的庫存量。
- `__discount: [callable|None] = None`: 商品的促銷方式，若為 `None` 表示不折扣；若為 callable（function 或 lambda）其引數（parameters） 必須為 `(x, n)`，分別代表「商品原價」與「購買數量」，該函數會計算出折扣後的價格回傳。

接者你要針對不同的使用行為去定義出商品的**實體方法**（**Instance Methods**）：
- `estimate(n: int) -> int` 對 n 個商品進行估價（不銷售），回傳折扣後的價格。
- `sale(n: int) -> int`: 販售 n 個商品。若 n 大於庫存量，則不變動庫存量，然後回傳 `-1`；若 n 小於等於庫存量，則將目前的庫存量減 n ，然後回傳折扣後的價格。
- `restock(n: int)`: 補充該商品的庫存量，若 n 為負數則不予變更。
- `is_on_sale() -> bool`: 若有促銷方案則回傳 True，否則回傳 Fasle。

寫出 **Getter** 和 **Setter** 控制對於屬性的存取（getter 和 setter 也是一種 Instance Method）：
- `get_name() -> str`: 取得該商品的名稱。
- `get_price() -> int`: 取得該商品的單價。
- `set_price(n: int)`: 變更該商品的單價，若 n 為不合理的數字（負數）則不予更改。
- `get_stock() -> int` 
- `set_discount(func: [callable|None])`: 變更折扣的計算方式，若 `func` 非 callable 也非 None 則不予變更。

> [!NOTE]
> 上列中關於 Attribute 和 Method 的描述格式
> - Attribute 格式為 `<attribute_name>: <type> [=<default_value>]`
> - Method 格式為 `<method_name>(<param_0> [: <type_0>] [,...]) [-> <return_type>]`

> [!WARNING]
> 上述的格式描述並非轉寫 Python 語法。


## Python 語法提示
### Python 特性其一
在 Python 中所有的東西都是物件，包括 int、str、list、class、function、type，所有東西的根源接繼承自 `object`。
> [!TIP]
> 有個有趣的現象是 `object` 和 `type` 是自己本身的實體，也是彼此的實體。

### Python 變數命名通則
- 變數與屬性用全小寫、底線連接，例如 `p1_score`
- 常數用全大寫、底線連接，例如 `MAX_SCORE`
- class 名稱單字第一個大寫，例如 `WaddleDee`
- 若要 class 定義私有（pravited）屬性或方法在前面要名稱前方加上雙底線，例如 `__password`。
- 變數、常數、屬性以名詞作為開頭，例如 `dog`、 `color_code`、`list_len`。
- 函數、方法以動次作為開頭，例如 `add_all`、`is_pressed`、`pop_largest_number`
- 除非是約定成俗的縮寫（如 `i, j ,k` 表示 `index`、`len` 表示 `length`），盡量不要用縮寫。
### 物件的創建子（**Constructor**）與 Instance Method 的宣告
```python
class MyClass:
    def __init__(self, p1, ...):
        self.a1 = p1
        ...

    def an_instance_method(self, ..):
        ...
```

### 帶有預設值的函數／方法宣告
```python
def find_ith_maximum(array, i=1):
    ...
```


## 部分程式碼與模擬流程
請依照下面的程式碼完成流程
```python
# 定義 class `Product`
class Product:
    ...

# 定義打八折
def discount_20_persent_off(x, n):
    return ...

# 定義買三送一
def ...

# 主流程
if __name__ == '__main__':
    
    # 宣告 apple，定價 20 元
    apple = Product('Apple', 20)

    # 印出目前蘋果的庫存量
    # 預期輸出 "Apple stock: 0"
    print("%s stock: %d"%(apple.get_name(), apple.get_stock()))

    # 進貨 20 顆，然後在印一次庫存量
    # 預期輸出 "Apple stock: 20"
    ...

    # 賣蘋果 15 顆，印出所得還有庫存量
    # 預期輸出 "You earn 300 dollar(s)", "Apple stock: 5"
    income = ...
    if income >= 0:
        print("You earn %d dollar(s)."%(income))
    else:
        print("Stock is not enough!")
    ...

    # 賣出 10 顆，因為庫存不足會印出 "Stock is not enough!"
    ...

    # 將 apple 售價訂為 25 元，折扣打八折
    apple.set_price(25)
    ...

    # 估 20 顆蘋果的價格
    # 預期輸出 "Estimation cost: 400"
    print("Estimation cost: %d"%(...))


    # 宣告 orange，定價 30 元，庫存 10，有買三送一的優惠
    orange = ...

    # 賣 5 顆橘子，顯示收益與剩餘庫存
    ...

    # 移除橘子的優惠
    ...

    # 估算 10 蘋果和 12 顆橘子的價格
    # 預期輸出 "Estimation cost: 560"
    ...
    
```