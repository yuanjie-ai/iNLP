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

### 3. 繁简体汉字拆字
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
