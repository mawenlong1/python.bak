k近邻算法的python实现
===== 
### 核心代码

```
#inX：要分类的数据信息

#dataSet：训练数据集

#labels：标签向量

def classify0(inX, dataSet, labels, k):

    dataSetSize = dataSet.shape[0]

    diffMat = tile(inX, (dataSetSize,1)) - dataSet

    sqDiffMat = diffMat**2

    sqDistances = sqDiffMat.sum(axis=1)

    distances = sqDistances**0.5

    sortedDistIndicies = distances.argsort()    

    classCount={}          

    for i in range(k):

        voteIlabel = labels[sortedDistIndicies[i]]

        classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1

    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)

    return sortedClassCount[0][0]

```
### python的tile函数简单介绍(使用tile要from numpy import*)
格式：tile(A,reps)
* A:输入的数组<br>
* reps：A沿各纬度重复的次数（tile（A,(2,2,3)）表示A沿第一纬度重复3遍，第二纬度重复2遍，第二纬度重复2遍）<br>
* A的类型众多，几乎所有类型都可以：array, list, tuple, dict, matrix以及基本数据类型int, string, float以及bool类型。

```
>>> A = [1,2,3]
>>> tile(A,3)
array([1, 2, 3, 1, 2, 3, 1, 2, 3])
>>> tile(A,(2,3))
array([[1, 2, 3, 1, 2, 3, 1, 2, 3],
       [1, 2, 3, 1, 2, 3, 1, 2, 3]])
>>> tile(A,(2,3,4))
array([[[1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3],
        [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3],
        [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]],

       [[1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3],
        [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3],
        [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]]])
```




