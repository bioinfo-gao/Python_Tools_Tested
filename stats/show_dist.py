import numpy as np 
import scipy.stats as stats 
import matplotlib.pyplot as plt 


plt.rcParams['font.sans-serif'] = ['SimHei'] # 用来正常显示中文标签 
plt.rcParams['axes.unicode_minus'] = False # 用来正常显示负号 

# 设置随机种子以保证结果可重现 
np.random.seed(42) 
# 生成样本数据 
n_samples = 10000 # 1000 

# 增加样本量使图形更平滑 
normal_data = np.random.normal(loc=0, scale=1, size=n_samples) 
skewed_data = np.random.chisquare(df=1, size=n_samples) # 卡方分布=3，右偏 
heavy_tailed_data = np.random.standard_t(df=2, size=n_samples) # t分布=5，重尾 

# 创建画布 
fig, axes = plt.subplots(2, 3, figsize=(15, 8)) 
fig.suptitle('示例数据分布可视化', fontsize=16) 
# 数据列表和标题 
datasets = [normal_data, skewed_data, heavy_tailed_data] 
titles = ['正态数据', '右偏数据', '重尾数据'] 
colors = ['skyblue', 'lightgreen', 'salmon'] 

# 为每个数据集绘制直方图+密度图和箱线图 

for i, (data, title, color) in enumerate(zip(datasets, titles, colors)): 
    # 子图1：直方图与核密度估计 
    axes[0, i].hist(data, bins=30, density=True, alpha=0.6, color=color, edgecolor='black', linewidth=0.5) 
    # 计算并绘制核密度估计曲线 
    kde = stats.gaussian_kde(data) 
    x_vals = np.linspace(min(data), max(data), 200) 
    axes[0, i].plot(x_vals, kde(x_vals), 'k-', linewidth=2) 
    axes[0, i].set_title(f'{title} - 直方图与密度曲线') 
    axes[0, i].set_ylabel('密度') 
    axes[0, i].grid(True, alpha=0.3) 
    
    # 子图2：箱线图 
    axes[1, i].boxplot(data, vert=True, patch_artist=True, boxprops=dict(facecolor=color, color='black'), medianprops=dict(color='red'), whiskerprops=dict(color='black'), capprops=dict(color='black'), flierprops=dict(marker='o', markerfacecolor='darkred', markersize=4, markeredgecolor='none', alpha=0.6)) 
    axes[1, i].set_title(f'{title} - 箱线图') 
    axes[1, i].grid(True, alpha=0.3) 
    axes[1, i].set_ylabel('值') 
    
plt.tight_layout() 
plt.show()