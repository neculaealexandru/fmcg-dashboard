import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

st.set_page_config(page_title="FMCG Analytics · Romania", page_icon="📊", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Space+Grotesk:wght@400;500;700&display=swap');
html, body, [class*="css"] { font-family: 'Inter', sans-serif; background-color: #0a0f1e; color: #e8eaf0; }
.stApp { background-color: #0a0f1e; }
.hero { background: linear-gradient(135deg, #0d1b3e 0%, #0a0f1e 60%); border: 1px solid #1e2d5a; border-radius: 16px; padding: 48px 40px 36px; margin-bottom: 32px; }
.hero-label { font-family: 'Space Grotesk', sans-serif; font-size: 11px; font-weight: 500; letter-spacing: 3px; text-transform: uppercase; color: #3b82f6; margin-bottom: 12px; }
.hero-title { font-family: 'Space Grotesk', sans-serif; font-size: 42px; font-weight: 700; color: #f0f4ff; line-height: 1.1; margin-bottom: 12px; }
.hero-sub { font-size: 15px; color: #8892b0; font-weight: 300; max-width: 560px; }
.kpi-card { background: #0d1b3e; border: 1px solid #1e2d5a; border-radius: 12px; padding: 24px 20px; text-align: center; }
.kpi-value { font-family: 'Space Grotesk', sans-serif; font-size: 32px; font-weight: 700; color: #60a5fa; line-height: 1; margin-bottom: 6px; }
.kpi-label { font-size: 12px; color: #8892b0; text-transform: uppercase; letter-spacing: 1.5px; }
.kpi-delta { font-size: 13px; color: #34d399; margin-top: 4px; }
.section-title { font-family: 'Space Grotesk', sans-serif; font-size: 20px; font-weight: 600; color: #e8eaf0; margin: 32px 0 16px; padding-bottom: 8px; border-bottom: 1px solid #1e2d5a; }
</style>
""", unsafe_allow_html=True)

years = list(range(2010, 2025))
fmcg_market = pd.DataFrame({"year": years, "market_size_bn_eur": [8.2,8.7,9.1,9.6,10.3,10.9,11.6,12.4,13.5,14.1,12.8,14.9,16.2,17.8,19.1], "confectionery_bn_eur": [0.82,0.87,0.93,0.99,1.07,1.14,1.23,1.34,1.48,1.55,1.41,1.61,1.79,1.98,2.14], "beverages_bn_eur": [1.31,1.39,1.46,1.54,1.65,1.75,1.86,1.99,2.16,2.26,2.05,2.39,2.59,2.85,3.06], "personal_care_bn_eur": [1.23,1.31,1.37,1.44,1.55,1.64,1.74,1.86,2.03,2.12,1.92,2.24,2.43,2.67,2.87]})
consumer = pd.DataFrame({"year": years, "avg_monthly_spend_eur": [142,148,153,159,168,176,186,199,218,228,207,241,263,289,311], "online_channel_pct": [1,1,2,2,3,4,5,7,9,12,18,21,25,29,33], "private_label_pct": [8,9,9,10,11,11,12,13,14,14,16,16,17,18,19], "consumer_confidence": [72,68,71,74,78,81,84,87,89,85,79,83,81,79,82]})
regions = pd.DataFrame({"region": ["Bucharest-Ilfov","Nord-Vest","Centru","Sud-Est","Sud-Muntenia","Nord-Est","Sud-Vest","Vest"], "market_share_pct": [28,14,13,11,11,10,7,6], "growth_yoy_pct": [6.8,5.2,4.9,4.1,3.8,3.2,2.9,5.6], "avg_basket_eur": [38,29,27,23,21,19,18,28]})

C = {"blue":"#3b82f6","indigo":"#6366f1","teal":"#14b8a6","amber":"#f59e0b","green":"#34d399","grid":"#1e2d5a","text":"#8892b0"}

def T(fig):
    fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", font=dict(family="Inter", color=C["text"], size=12), title_font=dict(family="Space Grotesk", color="#e8eaf0", size=16), xaxis=dict(gridcolor=C["grid"], linecolor=C["grid"]), yaxis=dict(gridcolor=C["grid"], linecolor=C["grid"]), legend=dict(bgcolor="rgba(0,0,0,0)"), margin=dict(t=40,b=20,l=10,r=10))
    return fig

latest = fmcg_market["market_size_bn_eur"].iloc[-1]
prev = fmcg_market["market_size_bn_eur"].iloc[-2]
yoy = (latest - prev) / prev * 100

st.markdown(f'<div class="hero"><div class="hero-label">Romania · FMCG Intelligence</div><div class="hero-title">Consumer Market<br>Analytics Dashboard</div><div class="hero-sub">End-to-end analysis of Romania\'s FMCG market — 2010–2024.</div></div>', unsafe_allow_html=True)

k1,k2,k3,k4 = st.columns(4)
k1.markdown(f'<div class="kpi-card"><div class="kpi-value">€{latest:.1f}B</div><div class="kpi-label">Total Market 2024</div><div class="kpi-delta">↑ {yoy:.1f}% YoY</div></div>', unsafe_allow_html=True)
k2.markdown(f'<div class="kpi-card"><div class="kpi-value">€{fmcg_market["confectionery_bn_eur"].iloc[-1]:.2f}B</div><div class="kpi-label">Confectionery</div><div class="kpi-delta">↑ 8.1% YoY</div></div>', unsafe_allow_html=True)
k3.markdown(f'<div class="kpi-card"><div class="kpi-value">{consumer["online_channel_pct"].iloc[-1]}%</div><div class="kpi-label">Online Channel</div><div class="kpi-delta">↑ from 1% in 2010</div></div>', unsafe_allow_html=True)
k4.markdown(f'<div class="kpi-card"><div class="kpi-value">€{consumer["avg_monthly_spend_eur"].iloc[-1]}</div><div class="kpi-label">Avg Monthly Spend</div><div class="kpi-delta">↑ 7.6% YoY</div></div>', unsafe_allow_html=True)

st.markdown('<div class="section-title">Market Size & Category Breakdown</div>', unsafe_allow_html=True)
c1,c2 = st.columns([3,2])
with c1:
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=fmcg_market["year"], y=fmcg_market["market_size_bn_eur"], mode="lines", fill="tozeroy", line=dict(color=C["blue"], width=2.5), fillcolor="rgba(59,130,246,0.10)", name="Total FMCG"))
    fig.add_trace(go.Scatter(x=fmcg_market["year"], y=fmcg_market["confectionery_bn_eur"], mode="lines+markers", line=dict(color=C["amber"], width=2, dash="dot"), marker=dict(size=5), name="Confectionery"))
    fig.add_trace(go.Scatter(x=fmcg_market["year"], y=fmcg_market["beverages_bn_eur"], mode="lines+markers", line=dict(color=C["teal"], width=2, dash="dot"), marker=dict(size=5), name="Beverages"))
    fig.update_layout(title="Romania FMCG Market (€ Billion)", hovermode="x unified")
    st.plotly_chart(T(fig), use_container_width=True)
with c2:
    row = fmcg_market.iloc[-1]
    other = row["market_size_bn_eur"]-row["confectionery_bn_eur"]-row["beverages_bn_eur"]-row["personal_care_bn_eur"]
    fig2 = go.Figure(go.Pie(labels=["Confectionery","Beverages","Personal Care","Other Food"], values=[row["confectionery_bn_eur"],row["beverages_bn_eur"],row["personal_care_bn_eur"],other], hole=0.55, marker_colors=[C["amber"],C["teal"],C["indigo"],C["blue"]]))
    fig2.update_layout(title="Category Mix 2024")
    st.plotly_chart(T(fig2), use_container_width=True)

st.markdown('<div class="section-title">Consumer Behaviour Trends</div>', unsafe_allow_html=True)
c1,c2 = st.columns(2)
with c1:
    fig3 = make_subplots(specs=[[{"secondary_y": True}]])
    fig3.add_trace(go.Bar(x=consumer["year"], y=consumer["avg_monthly_spend_eur"], name="Monthly Spend (€)", marker_color=C["blue"], opacity=0.8), secondary_y=False)
    fig3.add_trace(go.Scatter(x=consumer["year"], y=consumer["online_channel_pct"], name="Online %", mode="lines+markers", line=dict(color=C["green"], width=2)), secondary_y=True)
    fig3.update_layout(title="Monthly Spend & Online Channel Growth", hovermode="x unified")
    fig3.update_yaxes(title_text="€ / month", secondary_y=False, gridcolor=C["grid"])
    fig3.update_yaxes(title_text="Online %", secondary_y=True, color=C["green"])
    st.plotly_chart(T(fig3), use_container_width=True)
with c2:
    fig4 = go.Figure()
    fig4.add_trace(go.Scatter(x=consumer["year"], y=consumer["private_label_pct"], mode="lines+markers", fill="tozeroy", line=dict(color=C["indigo"], width=2), fillcolor="rgba(99,102,241,0.12)", name="Private Label %"))
    fig4.add_trace(go.Scatter(x=consumer["year"], y=consumer["consumer_confidence"], mode="lines", line=dict(color=C["amber"], width=2, dash="dot"), name="Consumer Confidence", yaxis="y2"))
    fig4.update_layout(title="Private Label vs Consumer Confidence", yaxis=dict(title="Private Label %", gridcolor=C["grid"]), yaxis2=dict(title="Confidence Index", overlaying="y", side="right", color=C["amber"]), hovermode="x unified")
    st.plotly_chart(T(fig4), use_container_width=True)

st.markdown('<div class="section-title">Regional Market Intelligence</div>', unsafe_allow_html=True)
r1,r2 = st.columns(2)
with r1:
    fig5 = px.bar(regions.sort_values("market_share_pct"), x="market_share_pct", y="region", orientation="h", color="growth_yoy_pct", color_continuous_scale=[[0,"#1e3a6e"],[0.5,"#3b82f6"],[1,"#34d399"]], labels={"market_share_pct":"Market Share (%)","region":"","growth_yoy_pct":"YoY Growth"}, title="Regional Market Share & Growth Rate", text="market_share_pct")
    fig5.update_traces(texttemplate="%{text}%", textposition="outside")
    st.plotly_chart(T(fig5), use_container_width=True)
with r2:
    fig6 = px.scatter(regions, x="growth_yoy_pct", y="avg_basket_eur", size="market_share_pct", color="region", labels={"growth_yoy_pct":"YoY Growth (%)","avg_basket_eur":"Avg Basket (€)"}, title="Growth vs Basket Size by Region", color_discrete_sequence=px.colors.qualitative.Set2)
    fig6.update_traces(marker=dict(opacity=0.85, line=dict(width=1, color="#1e2d5a")))
    st.plotly_chart(T(fig6), use_container_width=True)

st.markdown('<div style="text-align:center; margin-top:48px; padding-top:24px; border-top:1px solid #1e2d5a; color:#4a5568; font-size:12px; letter-spacing:1px;">ROMANIA FMCG ANALYTICS · BUILT BY ALEXANDRU NECULAE · DATA: EUROSTAT / INS</div>', unsafe_allow_html=True)
