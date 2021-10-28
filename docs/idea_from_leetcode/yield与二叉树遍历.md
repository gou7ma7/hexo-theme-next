# yield的作用
首先yield就是return，不要想多了，所以搭配`yield func()`能够递归，就是这么简单；

# 几个yield并排你就不会了？
学以致用，看文档的时候自然说：都懂，都懂，结果自己不仅写不来还看不懂。

```python
import sys

def func():
    return 1
    return 2
    return 3

def gen():
    yield 1
    yield 2
    yield 3


it = gen()
while True:
    try:
        print(next(it))
    except StopIteration:
        sys.exit()
```
要遍历一个生成器，自然需要调用next方法到报错为止，实际上行为和遍历序列的时候下标越界同理，只是现代编译器做好了没意识到而已。
## 生成器和迭代器的区别
在python中实现了__iter__和__next__方法，可以迭代操作的对象就叫迭代器；  
构建迭代器的时候，并不一次性加载所有元素到内存，只有调用next方法的时候才会**返回**需要的该元素；


生成器就是一种迭代器，由生成器函数返回；  
生成器函数就是上文中的 return -> yield的函数；  
>普通函数func调用：  
>`print(func())  # 1`  
>`print(func())  # 1`

>生成器函数调用：  
>`it = gen();  # 获得一个生成器` 
>`print(next(it))  # 1`  
>`print(next(it))  # 2`  
## 为啥要用生成器
从上文中可以看到生成器函数一个巨大的优势就是函数写出来是分块的，可以直接剪掉很多的选择分支，让代码更加的整洁接近算法描述。  
尤其是当需要递归的时候，使用yield的代码写出来简直就像是伪代码，曾一度让我无法理解其中的逻辑分支和递归基是如何运行的。

比如使用普通函数实现中序遍历一个BST的伪代码如下
```python
global_res = []

def in_order_visit(node):
    if node is None:
        return None
    in_order_visit(node.left)
    global_res.append(node.value)
    in_order_visit(node.right)

in_order_visit(root)  # root为需要遍历的BST的根节点
print(global_res)
```
### 递归参数只能是对象本身，需要的值无法收集
可以明显的看得出来，遍历函数本身在递归的过程中参数只能是node or None，同时node = None作为递归基；  
那么问题来了，我遍历出来的值如何返回给上层呢？  
我当时的函数设计的无比复杂，进入函数的时候先进行一个逻辑判断，再选择进入node.left还是返回node.value，因此一个函数就可能接受2种数据结构，  
再根据自己的下面的调用结果判断是该继续往下递归还是往上return。
### 需要的值放到递归参数中会导致逻辑十分混乱
代码无比丑陋，逻辑无比复杂。  
不得已，只得引入全局变量（不引入也可以，可以让遍历函数返回一个元组，前面是node后面是node.value，但本质没变）  
让遍历函数只专心访问node，我用一个全局变量来储存访问结果（也就是网上教材都只让你print出来的操作）  
问题是全局变量应该少用，这是破坏结构性的，不管是封装成对象还是闭包还是什么玩意儿。

### 必须将所有节点全部访问到内存

使用生成器函数遍历一个BST的代码如下
```python
def in_order_visit_gen(node):
    # TODO 先写道这里吧，不早了，同时试试git显示效果
```