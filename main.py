import streamlit as st
# import numpy as np
# import pandas as pd
# from PIL import Image
import time

st.title('Streamlit 超入門')

# st.write('DataFrame')

# df = pd.DataFrame(
#   np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
#   columns=['lat', 'lon']
# )

# 動的なTable
# st.dataframe(df.style.highlight_max(axis=0))

# 静的なTable
# st.table(df.style.highlight_max(axis=0))

# 折れ線グラフ
# st.line_chart(df)

# 折れ線塗りつぶしグラフ
# st.area_chart(df)

# 棒グラフ
# st.bar_chart(df)

# マッピング
# st.map(df)

st.write('Display Image')

# checkbox
# if st.checkbox('Show Image'):
  # 画像
  # img = Image.open('sample.jpeg')
  # st.image(img, caption='hayato Image', use_column_width=True)

# selectbox
# option = st.selectbox(
#   'あなたが好きな数字を教えて下さい',
#   list(range(1, 11))  
# )
# 'あなたの好きな数字は', option, 'です'

# input
# text = st.text_input('あなたの趣味を教えてください。')
# 'あなたの趣味：', text

# slider(min, max, start)
# sidebar
# condition = st.sidebar.slider('あなたの今の調子は?', 0, 100, 50)
# condition = st.slider('あなたの今の調子は?', 0, 100, 50)
# 'コンディション：', condition

# プログレスバー(終わるまで次のプログラムが実行されない)
st.write('プログレスバーの表示')
'Start!!'
bar = st.progress(0)
latest_iteration = st.empty()

for i in range(100):
  latest_iteration.text(f'Iteration {i + 1}')
  bar.progress(i + 1)
  time.sleep(0.01)
'Done'

# ２columnレイアウト
left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
  right_column.write('ここは右カラムです')

# expander
expander = st.expander('問い合わせ1')
expander.write('問い合わせ1の回答')
expander = st.expander('問い合わせ2')
expander.write('問い合わせ2の回答')
expander = st.expander('問い合わせ3')
expander.write('問い合わせ3の回答')