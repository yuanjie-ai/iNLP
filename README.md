<h1 align = "center">:rocket: iNLP :facepunch:</h1>

---


## Install
- `pip install iNLP` **or** `pip install git+https://github.com/Jie-Yuan/iNLP.git`
---


## Usage
### **`inlp.convert`**
- 简繁体转换
```python
from inlp.convert import chinese

chinese.s2t('忧郁的台湾乌龟') # chinese.simple2tradition('忧郁的台湾乌龟')
chinese.t2s('憂郁的臺灣烏龜') # chinese.tradition2simple('憂郁的臺灣烏龜')
```

- 全角半角转换
```python
from inlp.convert import char

char.half2full("0123456789")
char.full2half("０１２３４５６７８９")
```

### **`inlp.explode`**
- 汉字拆成字
```python
from inlp.explode import Chars

Chars().get_chars('袁') # ['土 口 衣']
```

- 汉字拆成笔画
```python
from inlp.explode import Strokes

Strokes().get_strokes('袁') # ['一', '丨', '一', '丨', 'フ', '一', 'ノ', 'フ', 'ノ', '丶']
```


### **`inlp.similarity`**
- 基于词库的相似度
```python
from inlp.similarity import thesaurus

s1 = ['周杰伦', '是', '一个', '歌手']
s2 = ['刘若英', '是', '个', '演员']

thesaurus.cilin(s1, s2) # 基于词林的相似度
thesaurus.hownet(s1, s2) # 基于知网的相似度
```
- 基于`hash`的相似度
```python
from inlp.similarity import simhash

simhash(s1, s2)
```

---
> 计划：增加基于词向量相似词相似句的方法
