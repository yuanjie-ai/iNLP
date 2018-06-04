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
