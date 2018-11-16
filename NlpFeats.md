[<h1 align = "center">:rocket: NlpFeats :facepunch:</h1>][1]

---
## [1. Baseline][2]
- LSTM
- CNN

https://www.kaggle.com/rethfro/1d-cnn-single-model-score-0-14-0-16-or-0-23

---
## 2. 特征工程

- question(leak): 
  - tf: q1/q2/q1+q2
  - tfidf: q1/q2/q1+q2
  
- words(chars): 针对字符串计算
  - 词数
  - 词数差
  - 重叠词数：`len(set(q1) & set(q2))`
  - 相同度（相异度 = 1 - 相同度）: com / (q1 + q2 - com)每个状态分量根据目标设置最优权重
  - simhash
  - jaccard: `jaccard = lambda a, b: len(set(a).intersection(b))/(len(set(a).union(b))+0.)`
  - 对目标影响大的词（lstm状态差等）
  - 编辑距离
    - fuzz.QRatio
    - fuzz.WRatio
    - fuzz.partial_ratio
    - fuzz.token_set_ratio
    - fuzz.token_sort_ratio
    - fuzz.partial_token_set_ratio
    - fuzz.partial_token_sort_ratio
    - ...

  
- [doc2num][3]: 针对tf/tfidf/wordVectors等计算
  - n-grams: 结合tf/tfidf使用
  - gensim
    - wmd
    - norm_wmd(l2): norm_model.init_sims(replace=True)
  - skew/kurtosis: `from scipy.stats import skew, kurtosis`
  - scipy.spatial.distance: `import braycurtis, canberra, cityblock, cosine, euclidean, jaccard, minkowski`
  - cosine（修正）

- lda
- bleu（机器翻译指标）：对两个句子的共现词频率计算`torchtext`



---
[1]: https://ai.ppdai.com/mirror/goToMirrorDetail?mirrorId=1
[2]: https://github.com/Jie-Yuan/PpdaiQuestionPairsMatching/tree/master/Baseline
[3]: https://www.kaggle.com/kardopaska/fast-how-to-abhishek-s-features-w-o-cray-xk7
