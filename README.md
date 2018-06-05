<h1 align = "center">:rocket: iNLP :facepunch:</h1>

---


## Install
- `pip install iNLP` **or** `pip install git+https://github.com/Jie-Yuan/iNLP.git`
---


## Usage
### 1. 中文繁简体转换
```python
from inlp.convert import chinese

chinese.s2t('忧郁的台湾乌龟') # chinese.simple2tradition('忧郁的台湾乌龟')
chinese.t2s('憂郁的臺灣烏龜') # chinese.tradition2simple('憂郁的臺灣烏龜')
```

### 2. 全角半角字符转换
```python
from inlp.convert import char

char.half2full("0123456789")
char.full2half("０１２３４５６７８９")
```

### 3. 繁简体汉字拆解

- 拆成字
```python
from inlp.convert.char import split

[split.simple[i] for i in '忧郁的台湾乌龟']
'''简体版
[['心 尤'], ['有 邑'], ['白 勺'], ['厶 口'], ['水 弯'], ['勹 ㇉ 一'], ['刀 电']]
'''

[split.tradition[i] for i in '憂郁的臺灣烏龜']
'''繁體版
[['一 白 冖 心 夕'],
 ['有 邑'],
 ['白 勺'],
 ['吉 冖 至'],
 ['水 彎'],
 ['户 一 ㇆ 火'],
 ['刀 □ 丨 乚 彐 彐 囗 乂']]
'''
```

- 拆成笔画
```python
```


### 4. 相似度
- 基于词库的相似度
```python
from inlp.similarity import thesaurus

s1 = ['周杰伦', '是', '一个', '歌手']
s2 = ['刘若英', '是', '个', '演员']

# 基于词林的相似度
thesaurus.cilin(s1, s2)
"""
0.65
"""

# 基于知网的相似度
thesaurus.hownet(s1, s2)
"""
0.5714285714285714
"""
```
- 基于`hash`的相似度
```python
from inlp.similarity import simhash

simhash(s1, s2)
"""
0.59375
"""
```
---
> 计划

### 相似词
### 相似句
