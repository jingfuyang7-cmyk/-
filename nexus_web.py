# -*- coding: utf-8 -*-
"""
Nexus-Alpha V71.2 —— 手机网页端（Web App）看板
随时随地通过手机浏览器查看 Top10 金股、战法池与明日重点板块推演
"""

import streamlit as st
import pandas as pd
from datetime import datetime

# 页面基础配置（针对手机端优化）
st.set_page_config(
    page_title="Nexus-Alpha 移动端指挥舱",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 自定义深色量化美学 CSS 样式
st.markdown("""
    <style>
    .main { background-color: #0B0E14; color: #F8FAFC; }
    .stMetric { background-color: #131B2E; padding: 10px; border-radius: 8px; border: 1px solid #1E293B; }
    .highlight-card { background-color: #131B2E; padding: 15px; border-radius: 10px; border-left: 5px solid #F43F5E; margin-bottom: 10px; }
    </style>
""", unsafe_allow_html=True)

# 标题栏
st.title("🛡️ Nexus-Alpha V71.2 移动端指挥舱")
st.caption(f"📅 实时行情同步时间: {datetime.now().strftime('%Y-%m-%d %H:%M')} | 专属沪深主板量化系统")

# 侧边栏控制
with st.sidebar:
    st.header("⚙️ 移动端控制中心")
    total_capital = st.number_input("总本金 (元)", value=500000, step=50000)
    macro_mode = st.selectbox(
        "外围/消息风向",
        ["⚖️外围中性(聚焦内生主线)", "🟢外围偏暖(利好硬科技进攻)", "🔴外围扰动(抱团军工/航天/独立牛)"]
    )
    if st.button("⚡ 触发云端全维扫描", type="primary"):
        st.success("云端扫描指令已下达，正在通过腾讯原生接口计算...")

# 模拟看板核心数据展示（实际部署时可直接读取您的 nexus_snapshot_v71.json 或运行扫描函数）
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="上证指数", value="3,660.79", delta="+0.32%")
with col2:
    st.metric(label="市场预计成交额", value="14,826亿", delta="量比 0.96")
with col3:
    st.metric(label="大盘情绪温度", value="58.0 分", delta="⚖️ 结构性轮动")

st.markdown("---")

# 标签页：手机端优化的三大核心模块
tab1, tab2, tab3 = st.tabs(["👑 Top10 领涨金股", "🧭 明日板块推演", "💼 我的实盘持仓"])

with tab1:
    st.subheader("👑 今日全场核心领涨金股 Top 10")
    st.info("💡 手机端提示：点击下方股票卡片可查看详细买卖点与止损位。")
    
    # 模拟 Top10 数据展示
    top10_data = [
        {"排名": "Top 1", "代码": "002697", "名称": "红旗连锁", "战法": "圆弧底突破", "现价": "5.21", "涨幅": "+5.47%", "状态": "🔥四红(6灯)", "总评": "9.8分"},
        {"排名": "Top 2", "代码": "600368", "名称": "五洲交通", "战法": "黄金坑穿三线", "现价": "4.36", "涨幅": "+3.81%", "状态": "🔥四红(6灯)", "总评": "9.5分"},
        {"排名": "Top 3", "代码": "002583", "名称": "海能达", "战法": "圆弧底突破", "现价": "8.38", "涨幅": "+5.54%", "状态": "🔥四红(6灯)", "总评": "9.3分"}
    ]
    
    for item in top10_data:
        with st.container():
            st.markdown(f"""
            <div class="highlight-card">
                <b>{item['排名']}：{item['名称']} ({item['代码']})</b> | 战法：<code>{item['战法']}</code><br>
                💰 现价：<b>{item['现价']}</b> ({item['涨幅']}) | 状态：{item['状态']} | 评分：<b>{item['总评']}</b>
            </div>
            """, unsafe_allow_html=True)

with tab2:
    st.subheader("🧭 明日重点关注板块量化推演")
    st.markdown("""
    * **🥇 第一梯队【明日主攻接力板块（大资金爆买 + 情绪未透支）】**：
      * **通信设备 / 算力硬件 / 元件PCB**（硬科技细分合计净流入超75亿，热度73~87分良性未过热，重点盯海能达、烽火通信、工业富联）。
    * **🥈 第二梯队【明日高低切换潜伏板块（红盘广度>70%群庄协同抬轿）】**：
      * **商业航天 / 国防军工**（红盘广度高达90%，热度仅61分，蓄势待发，盯中国卫星、中国卫通、中航沈飞）。
      * **人形机器人 / 自动化设备**（72家红盘协同，高低切换首选，盯拓普集团、三花智控）。
    * **⚠️ 风险规避【今日高潮防分化区】**：
      * **煤炭开采加工 / 燃气**（热度99.5分全员高潮，平量市场次日早盘严禁追高）。
    """)

with tab3:
    st.subheader("💼 移动端实盘持仓简报")
    st.write("当前暂无录入持仓。您可在 PC 端录入后，在手机端实时监控税后净盈亏与三态做T气象指令。")