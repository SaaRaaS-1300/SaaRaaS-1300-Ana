import streamlit as st


# HTML内容
html_content = """
<iframe
	src="https://while-nalu-secretary-ana.hf.space"
	frameborder="0"
	width="850"
	height="450"
></iframe>
"""
 
# 将HTML内容传递给st.markdown()函数进行展示
st.markdown(html_content)
