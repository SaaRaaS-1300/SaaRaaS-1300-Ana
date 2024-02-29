import streamlit as st

# html
ana_html = """
<iframe
	src="https://while-nalu-secretary-ana.hf.space"
	frameborder="0"
	width="850"
	height="450"
></iframe>
"""

# 使用st.markdown函数显示iframe
st.markdown(ana_html, unsafe_allow_html=True)
