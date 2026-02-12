# Paradex BTC 秒开关配置 - 多号轮换版
# ⚠️ 使用前请复制此文件为 config.py，并填写你的账号信息

import os

# ==================== API 配置 ====================
# Paradex 环境
PARADEX_ENV = "MAINNET"  # MAINNET 或 TESTNET

# Paradex API URLs
API_BASE_URL = "https://api.prod.paradex.trade"
WS_URL = "wss://ws.api.prod.paradex.trade/v1"

# ==================== 多账号配置 ====================
# 多账号列表，依次轮换
ACCOUNTS = [
    {
        "name": "账号1",
        "L2_ADDRESS": "",          # ⬅️ 填写你的 L2 地址
        "L2_PRIVATE_KEY": "",      # ⬅️ 填写你的 L2 私钥
    },
    {
        "name": "账号2",
        "L2_ADDRESS": "",          # 填写账号2的L2_ADDRESS
        "L2_PRIVATE_KEY": "",      # 填写账号2的L2_PRIVATE_KEY
    },
    {
        "name": "账号3",
        "L2_ADDRESS": "",
        "L2_PRIVATE_KEY": "",
    },
    {
        "name": "账号4",
        "L2_ADDRESS": "",
        "L2_PRIVATE_KEY": "",
    },
    {
        "name": "账号5",
        "L2_ADDRESS": "",
        "L2_PRIVATE_KEY": "",
    },
    {
        "name": "账号6",
        "L2_ADDRESS": "",
        "L2_PRIVATE_KEY": "",
    },
]

# ==================== 轮换切换条件 ====================
SWITCH_COST_PER_10K = 0.4  # 磨损切换阈值：元/万

# ==================== 交易配置 ====================
MARKET = "BTC-USD-PERP"
ORDER_SIZE_BTC = 0.008
MAX_SPREAD_PERCENT = 0.0005
MAX_CYCLES = 800

# ==================== 波动率过滤配置 ====================
VOLATILITY_FILTER_ENABLED = True
MAX_VOLATILITY_PCT = 0.07
VOLATILITY_WINDOW_SECONDS = 15

# ==================== 日志配置 ====================
LOG_FILE = "scalper.log"
LOG_LEVEL = "INFO"

# ==================== 安全配置 ====================
MAX_CONSECUTIVE_FAILURES = 5
EMERGENCY_STOP_FILE = "STOP"

# ==================== 定时配置 ====================
SCHEDULE_ENABLED = True
SCHEDULE_START_HOUR = 0
SCHEDULE_START_MINUTE = 0
SCHEDULE_END_HOUR = 23
SCHEDULE_END_MINUTE = 59

# ==================== Telegram 通知配置 ====================
TG_ENABLED = False                # 改为 True 启用通知
TG_BOT_TOKEN = ""                 # ⬅️ 填写你的 Bot Token
TG_CHAT_ID = ""                   # ⬅️ 填写你的 Chat ID

TG_NOTIFY_START_STOP = True
TG_NOTIFY_FEE_PAUSE = True
TG_NOTIFY_SCHEDULE = True
TG_NOTIFY_REPORT_INTERVAL = 60
