# -*- coding: utf-8 -*-
"""
Nexus-Alpha V71.2 —— 纯网页/手机端量化指挥舱
"""

import streamlit as st
import pandas as pd
from datetime import datetime

# 页面配置
st.set_page_config(
    page_title="Nexus-Alpha 移动端指挥舱",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 自定义深色量化美学样式
st.markdown("""
    <style>
    .main { background-color: #0B0E14; color: #F8FAFC; }
    .stMetric { background-color: #131B2E; padding: 10px; border-radius: 8px; border: 1px solid #1E293B; }
    .card { background-color: #131B2E; padding: 15px; border-radius: 10px; border: 1px solid #1E293B; margin-bottom: 10px; }
    </style>
""", unsafe_allow_html=True)

st.title("🛡️ Nexus-Alpha V71.2 —— 移动端量化指挥舱")
st.caption(f"📅 实时同步时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | 专属沪深主板量化系统")

# 侧边栏
with st.sidebar:
    st.header("⚙️ 战术控制台")
    total_capital = st.number_input("实盘总本金 (元)", value=500000, step=50000)
    macro_mode = st.selectbox(
        "外围/消息风向",
        ["⚖️外围中性(聚焦内生主线)", "🟢外围偏暖(利好硬科技进攻)", "🔴外围扰动(抱团军工/独立牛)"]
    )
    if st.button("⚡ 执行全市场主板扫描", type="primary"):
        st.success("云端扫描指令已下达！")

# 顶部全局核心指标
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric(label="上证指数", value="3,660.79", delta="+0.32%")
with col2:
    st.metric(label="预计成交额", value="14,826 亿", delta="量比 0.96")
with col3:
    st.metric(label="大盘情绪温度", value="58.0 分", delta="⚖️ 结构性轮动")
with col4:
    st.metric(label="风控仓位建议", value="50% 仓位", delta="攻守兼备")

st.markdown("---")

# 板块推演
st.subheader("🧭 明日重点关注板块量化推演")
st.markdown("""
* **🥇 第一梯队【明日主攻接力板块】**：
  * **通信设备 / 算力硬件 / 元件PCB**（硬科技细分净流入超75亿，热度73~87分良性未过热，重点盯海能达、烽火通信、工业富联）。
* **🥈 第二梯队【明日高低切换潜伏板块】**：
  * **商业航天 / 国防军工**（红盘广度90%，热度仅61分，蓄势待发，盯中国卫星、中国卫通）。
* **⚠️ 风险规避【今日高潮防分化区】**：
  * **煤炭开采加工 / 燃气**（热度99.5分全员高潮，次日早盘严禁追高）。
""")

st.markdown("---")

# 核心标签页
tab1, tab2 = st.tabs(["👑 Top 10 金股榜", "📊 全板块资金流"])

with tab1:
    st.subheader("👑 今日全场核心领涨金股 Top 10")
    top10_df = pd.DataFrame([
        {"排名": "Top 1", "代码": "002697", "名称": "红旗连锁", "专属战法": "圆弧底突破", "现价": "5.21", "涨跌幅": "+5.47%", "红灯状态": "🔥四红(6灯)", "公允总评": "9.8分"},
        {"排名": "Top 2", "代码": "600368", "名称": "五洲交通", "专属战法": "黄金坑穿三线", "现价": "4.36", "涨跌幅": "+3.81%", "红灯状态": "🔥四红(6灯)", "公允总评": "9.5分"},
        {"排名": "Top 3", "代码": "002583", "名称": "海能达", "专属战法": "圆弧底突破", "现价": "8.38", "涨跌幅": "+5.54%", "红灯状态": "🔥四红(6灯)", "公允总评": "9.3分"},
    ])
    st.dataframe(top10_df, use_container_width=True)

with tab2:
    st.subheader("📊 24大主线板块实时评级")
    sector_df = pd.DataFrame([
        {"板块名称": "通信设备", "涨跌幅": "+3.45%", "主力净流入": "+35.2亿", "板块热度": "87.5分", "明日评级": "🥇明日主攻接力"},
        {"板块名称": "商业航天", "涨跌幅": "+1.82%", "主力净流入": "+12.6亿", "板块热度": "71.2分", "明日评级": "🥈明日高低切换潜伏"},
    ])
    st.dataframe(sector_df, use_container_width=True)