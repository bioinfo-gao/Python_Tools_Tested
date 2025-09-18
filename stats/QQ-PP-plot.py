import numpy as np
import scipy.stats as stats 
import matplotlib.pyplot as plt
 
plt.rcParams['font.sans-serif'] = ['SimHei'] # 用来正常显示中文标签 
plt.rcParams['axes.unicode_minus'] = False # 用来正常显示负号 

# 设置随机种子以保证结果可重现 
np.random.seed(42) 

# 生成样本数据 
n_samples = 10000 # 100
normal_data = np.random.normal(loc=0, scale=1, size=n_samples) 
skewed_data = np.random.chisquare(df=1, size=n_samples) # 卡方分布=3，右偏 
heavy_tailed_data = np.random.standard_t(df=2, size=n_samples) # t分布=5，重尾 

# 创建画布 
fig, axes = plt.subplots(2, 3, figsize=(15, 10)) 
fig.suptitle('QQ图与PP图对比', fontsize=16) 

# 为每个数据集绘制QQ图和PP图 
datasets = [normal_data, skewed_data, heavy_tailed_data] 
titles = ['正态数据', '右偏数据', '重尾数据'] 

for i, (data, title) in enumerate(zip(datasets, titles)): 
    # 绘制QQ图 \
    stats.probplot(data, dist="norm", plot=axes[0, i]) 
    
    axes[0, i].set_title(f'QQ图 - {title}') 
    axes[0, i].get_lines()[0].set_markerfacecolor('C0') # 设置散点颜色 
    axes[0, i].get_lines()[0].set_markeredgecolor('C0') 
    axes[0, i].get_lines()[1].set_color('red') # 设置参考线颜色 
    axes[0, i].get_lines()[1].set_linewidth(2) 
    
    # 绘制PP图 
    # 计算理论累积概率和样本累积概率 
    sorted_data = np.sort(data) 
    sample_cdf = np.arange(1, len(data) + 1) / len(data) # 经验累积概率 
    theory_cdf = stats.norm.cdf(sorted_data) # 理论累积概率 
    
    axes[1, i].plot(theory_cdf, sample_cdf, 'o', alpha=0.8) 
    
    axes[1, i].plot([0, 1], [0, 1], 'r-', linewidth=2) # 绘制y=x的参考线
    
    axes[1, i].set_xlabel('理论累积概率 (Normal)') 
    axes[1, i].set_ylabel('样本累积概率') 
    
    axes[1, i].set_title(f'PP图 - {title}') 
    axes[1, i].set_aspect('equal') 
    axes[1, i].set_xlim(0, 1) 
    axes[1, i].set_ylim(0, 1) 
    axes[1, i].grid(True) 


plt.tight_layout() 
plt.show()