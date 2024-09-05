# 練習 4 - 矩陣運算
在這個練習中，藉由矩陣運算，我們會練習**例外**（exception）的使用。

## 矩陣說明
以下是關於矩陣的定義：

### 1. **基本符號**
$A_{m \times n}$ 表示該矩陣有 m 行(row) n 列(column)。

$a_{i,j}$ 表示第 i 行、第 j 列的元素，為配合程式碼的撰寫，
  定義 $i \in \{0, ..., m-1\}, j \in \{0, ..., n-1\}$。

下列的例子為 $3 \times 2$ 矩陣的表示方式

$$ A_{3\times2} = \begin{bmatrix}
    a_{0,0} & a_{0,1} \\
    a_{1,0} & a_{1,1} \\
    a_{2,0} & a_{2,1} \\
\end{bmatrix}  $$

### 2. 矩陣的加減法
$A, B$ 必須有相同的行數與列數才能加／減。
#### 加法
- $C_{m \times n} = A_{m \times n} + B_{m \times n}$
- $\forall (i,j), c_{i,j} = a_{i,j} + b_{i,j}$

 例：

$$\begin{bmatrix}
    1 & 2\\
    3 & 4\\
    5 & 6\\
\end{bmatrix} + 
\begin{bmatrix}
    1 & 1\\
    2 & 2\\
    -1 & -1\\
\end{bmatrix} = 
\begin{bmatrix}
    2 & 3\\
    5 & 6\\
    4 & 5\\
\end{bmatrix}$$

#### 減法
- $C_{m \times n} = A_{m \times n} - B_{m \times n}$
- $\forall (i,j), c_{i,j} = a_{i,j} - b_{i,j}$

例：

$$\begin{bmatrix}
    1 & 2\\
    3 & 4\\
    5 & 6\\
\end{bmatrix} -
\begin{bmatrix}
     1 & 1\\
     2 & 2\\
     -1 & -1\\
\end{bmatrix} = 
\begin{bmatrix}
     0 & 1\\
     1 & 2\\
     7 & 8\\
\end{bmatrix}$$

### 3. 純量乘法
令 $c$ 為常數，則
- $B_{m \times n} = cA_{m \times n}$
- $\forall (i,j), b_{i,j} = ca_{i,j}$

例：

$$3 \times \begin{bmatrix}
     1\\
     2\\
     3\\
\end{bmatrix} = \begin{bmatrix}
     3\\
     6\\
     9\\
\end{bmatrix}$$

### 4. 矩陣乘法
$AB$ 能夠運算表示 $A$ 列數與 $B$ 的行數相同。
- $C_{m \times n} = A_{m \times p}B_{p \times n}$
- $c_{i,j} = \sum_{k=0}^{p-1} a_{i,k}b_{k,j} $
例：

$$\begin{bmatrix}
     1 & 0 & 2\\
     -1 & 3 & 1
\end{bmatrix} \begin{bmatrix}
     3 & 1\\
     2 & 1\\
     1 & 0
\end{bmatrix} =\begin{bmatrix}
     5 & 1\\
     4 & 2\\
\end{bmatrix}$$ 


### 5. 轉置矩陣
將行跟列的順序對調極為轉置矩陣 $A^T$
- $B_{n \times m} = A_{m \times n}^T, b_{i,j} = a_{j_i}$

### 6. 行列式
$A_{n \times n}$ 的行列式可用以下算式計算：
- $det(A) = |A| = \sum_{i=0}^{n-1} (-1)^ia_{0, i}C_{0,i}$

其中 $C_{0, i}$ 定義為扣除第 0 行、第 $i$ 列的行列式。

假設 $A = \begin{bmatrix} 1&2&3 \\ 4&5&6 \\ 7&8&9\end{bmatrix}$，則
$C_{0,0} = \begin{vmatrix} 5&6 \\ 6&9 \end{vmatrix}$, 
$C_{0,1} = \begin{vmatrix} 4&6 \\ 7&9 \end{vmatrix}$, 
$C_{0,2} = \begin{vmatrix} 4&5 \\ 7&8 \end{vmatrix}$。

若 $A = \begin{bmatrix} a&b \\ c&d\end{bmatrix}$，則 $det(A) = ad - bc$；若 $A = \begin{bmatrix} a \end{bmatrix}$，則 $det(A) = a$。

例：

$det(\begin{bmatrix} 1&2&3 \\ 4&5&6 \\ -3&1&2\end{bmatrix})$
$ = \begin{vmatrix} 1&2&3 \\ 4&5&6 \\ -3&1&2\end{vmatrix}$

$= (-1)^0 \cdot 1 \cdot \begin{vmatrix} 5&6 \\ 1&2\end{vmatrix} + $
$= (-1)^1 \cdot 2 \cdot \begin{vmatrix} 4&6 \\ -3&2\end{vmatrix} + $
$= (-1)^2 \cdot 3 \cdot \begin{vmatrix} 4&5 \\ -3&1\end{vmatrix}$

$= 4 - 52 + 57$

$= 9$


## 程式要求
定義 `class Matrix`，該物件具有以下的屬性：
- `__values`: 紀錄數值的 2D tuple。

`Matrix` 的生成式格式為 `Matrix(values)`，
其中 $values$ 為包含 m 個「包含 n 個元素的 `tuple|list`」 的 `tuple|list`。
若是不符合格式，應該要拋出 `ValueError: not a form of matrix.` 
``` python
# correct
m1 = (
    (1, 2, 3),
    (4, 5, 6)
)

# not correct
m2 = (
    (1, 2, 3),
    (4, 5)
)
```

> [!NOTE]
> 在程式運行中可能會遇到意料之外的狀況，物件導向中有「拋出例外」(Exception)的機制。
> 
> python 拋出例外的格式為：
> ``` python
> raise Exception(message)
> ```
> 其中的 `Exception` 有子類別表示不同種類的例外，
> 例如 `ValueError` 表示型態正確（如：要 int）但
> `message` 通常用來提示外部發生意外的原因。
>
> 若發生意外，通常要去處理，但在本次只會練習拋出例外。

接著，請實作以下**實體方法**：

### `add(self, that) -> Matrix`
與另外一個矩陣相加並回傳計算結果。
#### Parameter
`that: Matrix`: 要加的矩陣。
#### Returns
與 `that` 相加的結果。
#### Raises
- 若 `that` 非 `Matrix`，拋出 `TypeError`。
- 若無法相加，拋出 `ArithmeticError`。

### `sub(self, that) -> Matrix`
與另外一個矩陣相減並回傳計算結果。
#### Parameter
`that: Matrix`: 要減的矩陣。
#### Returns
與 `that` 相減的結果。
#### Raises
- 若 `that` 非 `Matrix`，拋出 `TypeError`。
- 若無法相減，拋出 `ArithmeticError`。


### `mul(self, that) -> Matrix`
與純量（數字）或另外一個矩陣相乘並回傳計算結果。
#### Parameter
`that: int|float|Matrix`: 要乘的數字或矩陣。
#### Returns
與 `that` 相乘的結果。
#### Raises
- 若 `that` 非 `Matrix`，拋出 `TypeError`。
- 若無法相乘，拋出 `ArithmeticError`。
