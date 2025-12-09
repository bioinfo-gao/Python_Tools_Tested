#pip install rpy2

import rpy2.robjects as ro
from rpy2.robjects import pandas2ri
from rpy2.robjects.conversion import localconverter
from rpy2.robjects.packages import importr
import pandas as pd

# 启用 pandas ↔ R DataFrame 自动转换
pandas2ri.activate()

# 导入 R 包
ggplot2 = importr('ggplot2')
dplyr = importr('dplyr')

# 示例数据（pandas DataFrame）
df = pd.DataFrame({
    'x': range(1, 11),
    'y': [i**2 for i in range(1, 11)],
    'group': ['A']*5 + ['B']*5
})

# 将 pandas df 转为 R DataFrame
with localconverter(ro.default_converter + pandas2ri.converter):
    r_df = ro.conversion.py2rpy(df)

# 创建 ggplot 图形对象
p = ggplot2.ggplot(r_df) + \
    ggplot2.aes_string(x='x', y='y', color='group') + \
    ggplot2.geom_point(size=3) + \
    ggplot2.geom_line() + \
    ggplot2.labs(title="Python 用 rpy2 + ggplot2 画图", x="X轴", y="Y轴") + \
    ggplot2.theme_minimal()

# 显示图形（弹出窗口或 Jupyter 内嵌）
from rpy2.robjects.lib import grdevices
grdevices = importr('grDevices')

# 在 Jupyter 中显示（推荐）
from rpy2.ipython.ggplot import image_png
from IPython.display import Image

with grdevices.png(filename="plot.png", width=800, height=600):
    p.plot()

Image("plot.png")