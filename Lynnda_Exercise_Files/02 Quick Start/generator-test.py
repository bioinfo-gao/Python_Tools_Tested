#!/usr/bin/python3

def isprime(n):
    if n == 1:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
    else:
        return True


# QoderCN can do automatic code generation, explain, debugging, and refactoring, and comment generation.
# 这段代码定义了一个名生成器函数（generator function）**，它的作用是**无限地生成质数（素数）序列**。

# 具体解释如下：

# 1.  **`def primes(n = 1):`**: 定义一个函数 [primes]它有一个默认参数 `n`，初始值为 1。

# 3.  **`if isprime(n): yield n`**: 
#     *   在每次循环中，它会调用一个名为 [isprime(n)]的辅助函数来检查当前的数字 `n` 是否为质数。
#     *   如果 [isprime(n)]返回 `True`（即 `n` 是质数），那么 `yield n` 语句就会被执行。
#     *   `yield` 是生成器的关键字。它会将当前的质数 `n` “产出”（yield）给调用者，然后**暂停**函数的执行，并记住当前的状态（包括变量 `n` 的值）。
#     *   下一次再从这个生成器获取值时，函数会从 `yield` 语句之后的地方恢复执行。 <<<<<<<<<<<<<<<<<<=====================================================================

# 4.  **`n += 1`**: 无论 `n` 是否为质数，在检查完之后，`n` 都会自增 1，以便在下一次循环中检查下一个数字。

# **总结来说**，这个generator 本身并不会一次性计算出所有质数并返回一个巨大的列表（这在内存上是不可行的）。相反，它创建了一个“质数工厂”，你可以通过迭代的方式，一个接一个地、按需地获取质数。

def primes(n = 1):
   while(True):
       if isprime(n): yield n
       n += 1 

for n in primes():
    if n > 100: break
    print(n, end="  ")

