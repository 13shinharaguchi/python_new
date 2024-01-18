# 計算に使う変数を用意
tax = 0.10 # 0.10は10%のこと
cost_a = 100

# 税込み価格の合計を計算
cost_a_taxin = cost_a + cost_a * tax

# 税込み価格の合計をprint関数で表示
print(cost_a_taxin)
