# Master Handoff v2 — Rich (Himanshu Gullaiya)
## DA Job Prep + Project 1 Complete + Project 2 In Progress
### Last Updated: April 17, 2026

---

## WHO IS RICH

- **Name:** Himanshu Gullaiya (goes by Rich)
- **GitHub:** himanshugullaiya
- **Education:** CSE 2021, MSIT Janakpuri, Delhi
- **Gap:** 5 years — full-time systematic trader (built broker API scalper, tkinter backtesting toolbox, automated Google Drive photo pipeline). Has a trading YouTube channel — 80 subs, 50+ videos. Proof of trading background.
- **Goal:** Data Analyst role — stable hours, low pressure, ~10-12 LPA, product-based company. Job = runway to fund trading.
- **Trading hours:** 6:30–9:30 PM daily
- **Teaching style:** Direct, no fluff, fintech examples, attempt first then correct

---

## CLAUDE BEHAVIOUR RULES

1. Call him Rich, never Himanshu
2. Direct — no fluff, no over-encouragement
3. He writes code himself — guide, hint, provide code only after 2 failed attempts
4. One thing at a time
5. Strict accountability — keep on track with deadlines
6. All measure names prefixed with `_M_` in Power BI
7. Power BI canvas: 1280×720, white background, Samsung aesthetic (#1B2A4A navy)
8. Table name in PostgreSQL for returns is `all_returns` not `returns`

---

## DEADLINE: MAY 1, 2026 (Application Day)

---

## SPRINT PLAN — REMAINING

| Task | Status |
|------|--------|
| Project 1 — HG Analytics D2C Dashboard | ✅ DONE |
| Project 1 — README pushed to GitHub | ✅ DONE |
| Project 1 — GIFs + Video | After Project 2 half done |
| Project 2 — NSE Stock Market Analytics | 🔄 IN PROGRESS |
| Project 2 — Download script | 🔄 IN PROGRESS |
| GitHub READMEs — both projects | P1 done, P2 pending |
| CV + LinkedIn overhaul | NOT STARTED |
| SQL revision — top 100 questions | NOT STARTED |
| Communication prep + mock interview | NOT STARTED |
| First applications sent | May 1, 2026 |

---

## REFERENCES & NETWORK

- Brother — SDE-3 at large MNC (potential referral)
- Friend — Product Analyst at Zomato (potential referral)
- MSIT Janakpuri alumni network
- Target companies: Amex, Mastercard, Airblack, PolicyBazaar, Chegg, Scry AI, similar

---

## GITHUB STATUS

- Profile bio: "Data Analyst | Python · SQL · Power BI | Ex-Derivatives Trader. Long-Term Gain & Self-Discipline"
- Project 1 repo: himanshugullaiya/D2C-ecommerce_analytics — LIVE, README pushed
- Project 2 repo: himanshugullaiya/NSE_Stock_Market_Analytics — LIVE, structure pushed
- .pbix files NOT pushed yet — push both on May 1

---

## GIFs + VIDEO PLAN (After Project 2 half done)

**4 GIFs to record for Project 1 (use ScreenToGif — free):**
1. Map toggle Revenue ↔ Returns (blue/red)
2. Return trend chart conditional coloring by subcategory+reason
3. Field parameter switcher on Products tab
4. Cohort heatmap scroll + YOY Revenue toggle

**YouTube Video:**
- Both projects in one video, facecam
- Upload to trading YouTube channel (80 subs, 50+ videos) — proves trading background is real
- Link in both READMEs

**Power BI Publish to Web:** May 1 morning — File → Publish → Publish to Web (free, public link)

---

## PROJECT 1 — HG ANALYTICS D2C DASHBOARD
### Status: ✅ COMPLETE

**Repo:** himanshugullaiya/D2C-ecommerce_analytics
**Local:** D:\DATA ANALYST JOB PREP\MY PROJECTS\D2C E-Commerce Analytics\
**Branding:** HG Analytics (circular logo on all tabs, transparent horizontal on Executive tab)

### Key Numbers
- Revenue: ₹6.8bn | Orders: 125K | Customers: 13K | AOV: ₹54.6K
- Profit Margin: ~46.8% | Return Rate: 9.96% (orders), 22.88% (revenue)
- Total Return Value: ₹1.56bn | Best Month: December 2025 ₹869M

### Tab Summary
- **Executive** — 6 KPI cards (MOM/MTD/CUR NPM%), Revenue Trend (field param), Time Period Selector, Map toggle (Revenue/Returns), AOV by Category donut, Acquisition Channel donut
- **Products** — "What's Driving The Revenue" — Category donut, field param switcher, subcategory bar, brand treemap, Top 3 products table, High Return Products table
- **Revenue** — "Revenue Trends & Leakage Analysis" — YOY comparison, MOM% trend, bookmark toggle, best month KPIs
- **Cohort** — "Customer Retention Analysis by First Order Month" — heatmap M1-M16, cohort size bar, 5 pre-written insights
- **RFM** — "Customer RFM Segment Analysis" — segment bar, avg revenue bar, top 10 customers, actions table, state distribution
- **Returns** — "Return Patterns & Risk Detection Analysis" — return % KPI (9.96%/22.88%), category donut, reason donut, monthly % trend (conditional green/red), return trend by subcategory+reason (colored by return_condition_flag)

### Key Interview Answers
- **Fan-out:** "Joining orders → order_items (one-to-many) then SUM(order_amount) caused 2x inflation. Fixed by always aggregating from order_items.total_sales_curr_order"
- **Medallion:** "Bronze = raw intact. Silver = clean. Gold = analytical aggregations. Each layer independently rerunnable."
- **Subcategory for returns:** "Product level = noise. Category = too broad. Subcategory+reason = actionable. 'Laptop Damaged worsening' triggers a packaging fix."
- **IQR subcategory-wise:** "Global IQR failed — ₹93K shirt passed because electronics raised upper bound."
- **Repeat Rate 99.92%:** "Poisson lam=10 synthetic artifact. Real D2C = 40-60%."
- **AOV ₹54.6K:** "Electronics at 79% skew overall. Category-level tells real story: clothing ₹2-3K, electronics ₹76K+"

### Known Limitations
1. Revenue pre-discount (~4.5% not deducted)
2. Repeat Rate 99.92% — Poisson artifact
3. Returns at order level not product level
4. Return rate uniform across categories — synthetic artifact
5. 0.004% floating point variance Python vs PostgreSQL

---

## PROJECT 2 — NSE STOCK MARKET ANALYTICS
### Status: 🔄 IN PROGRESS — Download script working, schema designed

**Repo:** himanshugullaiya/NSE_Stock_Market_Analytics
**Local:** D:\DATA ANALYST JOB PREP\MY PROJECTS\Trading Dashboard\

### Folder Structure
```
Trading Dashboard/
├── Scripts/
│   ├── download_data.py      (IN PROGRESS)
│   ├── parse_and_clean.py    (NOT STARTED)
│   └── load_to_postgres.py   (NOT STARTED)
├── DATA/
│   ├── Bhavcopy/             # PD zips + extracted CSVs
│   ├── Market Report/        # MA csv files
│   └── PE Ratio/             # PE csv files
├── POWERBI/
├── SAMPLE DATA/
├── SQL/
├── .gitignore
├── LICENSE
└── README.md
```

### Dashboard Scope — 3 Tabs
1. **Market Overview + Breadth** — Key indices, advance/decline, traded value, top gainers/losers, 52-week highs/lows count
2. **Sector Pulse** — Sector indices performance (green/red), sector PE, best/worst sector, breadth chart if space
3. **Stock Deep Dive** — Dropdown select stock, 1-year price trend, 52-week high/low position, PE ratio, volume trend

**Dropped:** Corporate actions tab, Recommendations/Watchlist tab (too complex, post-May-1)

### Data Source — NSE Bhavcopy
**URL Pattern (confirmed working):**
`https://nsearchives.nseindia.com/archives/equities/bhavcopy/pr/PR{DDMMYY}.zip`

Example: `https://nsearchives.nseindia.com/archives/equities/bhavcopy/pr/PR160425.zip`

**Note:** Direct URL in browser doesn't work — needs requests with headers. Status 200 confirmed working.

**Data Period:** 1 year historical (April 2024 → April 2026) — ~250 trading days

### Files Needed Per Day
| File | Source | Purpose |
|------|--------|---------|
| PD (pdddmmyyyy.csv) | PR zip | Main OHLCV + series + 52WK high/low |
| GL (glddmmyyyy.csv) | PR zip | Gainers/losers (pre-calculated by NSE) |
| HL (hlddmmyyyy.csv) | PR zip | 52-week highs/lows today |
| MA (market activity) | Separate download | All indices OHLCV + sector data |
| PE ratio | Separate download | PE ratios per stock |
| MCAP | PR zip | Market cap (refresh weekly, not daily) |

**Files NOT needed:** BH (price bands), TT (top 25 — too small, use GL instead), corporate bond files, SME files, DAT files

### Confirmed File Columns

**PD file columns:**
`MKT, SERIES, SYMBOL, SECURITY, PREV_CL_PR, OPEN_PRICE, HIGH_PRICE, LOW_PRICE, CLOSE_PRICE, NET_TRDVAL, NET_TRDQTY, IND_SEC, CORP_IND, TRADES, HI_52_WK, LO_52_WK`
- IND_SEC = Y means it's an index row, N means it's a stock row
- SERIES: EQ = normal equity, BE = trade-to-trade, BZ/ST/SM = other categories

**HL file columns:**
`SECURITY, NEW, PREVIOUS, NEW_STATUS`
- NEW_STATUS: H = new 52-week high, L = new 52-week low

**MCAP file columns:**
`Trade Date, Symbol, Series, Security Name, Category, Last Trade Date, Face Value, Issue Size, Close Price, Market Cap`

**TT file columns (top 25 by value):**
`SECURITY, PREV_CL_PR, CLOSE_PRIC, NET_TRDQTY, NET_TRDVAL`

**BH file columns:**
`SYMBOL, SERIES, SECURITY, HIGH/LOW, INDEX FLAG`

**MA file structure:**
- Top section: All NSE indices (Nifty 50, Bank Nifty, sector indices) with OHLCV + Gain/Loss
- Bottom section: All stocks with close price, traded value, volume

### Database Schema — 4 Tables

```sql
-- Main price table (from PD file, stock rows only where IND_SEC = N)
stock_prices_daily (
    date DATE,
    symbol VARCHAR,
    series VARCHAR,          -- EQ, BE, BZ etc.
    security_name VARCHAR,
    prev_close NUMERIC,
    open_price NUMERIC,
    high_price NUMERIC,
    low_price NUMERIC,
    close_price NUMERIC,
    traded_value NUMERIC,
    traded_qty BIGINT,
    trades INTEGER,
    week_52_high NUMERIC,
    week_52_low NUMERIC,
    PRIMARY KEY (date, symbol, series)
)

-- Index data (from PD file, index rows where IND_SEC = Y, or from MA file)
index_daily (
    date DATE,
    index_name VARCHAR,
    prev_close NUMERIC,
    open_price NUMERIC,
    high_price NUMERIC,
    low_price NUMERIC,
    close_price NUMERIC,
    gain_loss NUMERIC,
    PRIMARY KEY (date, index_name)
)

-- Market cap (from MCAP file — refresh weekly not daily)
market_cap (
    trade_date DATE,
    symbol VARCHAR,
    security_name VARCHAR,
    series VARCHAR,
    category VARCHAR,        -- Listed, Permitted etc.
    market_cap NUMERIC,
    close_price NUMERIC,
    PRIMARY KEY (trade_date, symbol)
)

-- 52-week breakouts today (from HL file)
week52_breakouts (
    date DATE,
    security VARCHAR,
    new_price NUMERIC,
    previous_price NUMERIC,
    status VARCHAR           -- H = new high, L = new low
)
```

**Stock metadata table** (to be created manually or from MCAP):
```sql
stock_metadata (
    symbol VARCHAR PRIMARY KEY,
    security_name VARCHAR,
    sector VARCHAR,          -- needs external mapping
    market_cap_category VARCHAR  -- Large/Mid/Small cap
)
```

**Note on sector mapping:** NSE Bhavcopy doesn't include sector names. Need to either:
1. Download NSE sector classification file separately
2. Map manually for Nifty 50/500 stocks
3. Use index membership (Nifty IT stocks = IT sector etc.)

### Download Script — Current Status

```python
import requests
import zipfile
import pandas as pd
import os

# CONFIRMED WORKING
url = "https://nsearchives.nseindia.com/archives/equities/bhavcopy/pr/PR160425.zip"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36",
    "Referer": "https://www.nseindia.com/",
    "Accept": "*/*",
}

response = requests.get(url, headers=headers)
# Returns status 200, content length ~472330 bytes

# Save zip
zip_path = "../DATA/Bhavcopy/PR160425.zip"
with open(zip_path, "wb") as f:
    f.write(response.content)

# Extract
extract_path = "../DATA/Bhavcopy/"
with zipfile.ZipFile(zip_path, 'r') as z:
    z.extractall(extract_path)
```

### NEXT STEPS FOR PROJECT 2

**Immediate next task — complete download_data.py:**

1. Generate list of all trading dates for past 1 year (exclude weekends + NSE holidays)
2. Loop through dates, download PR zip for each date
3. Extract only PD, GL, HL files from each zip (skip the rest)
4. Save to correct folders
5. Download MA and PE files separately (different URL pattern — need to find)
6. Add error handling for holidays (404 = holiday, skip)
7. Test on 5 dates first before running full 1-year loop

**URL patterns to find:**
- MA file URL pattern (market activity report)
- PE ratio file URL pattern
- GL file URL pattern (may be inside PR zip or separate)

**After download complete:**
- parse_and_clean.py — read all CSVs, clean, combine into single dataframes
- Load to PostgreSQL
- Build Power BI on top

### Key Technical Notes

- NSE blocks direct URL — must use requests with browser headers
- Status 200 = success, 404 = holiday or wrong date, handle gracefully
- GL file deleted accidentally — re-download and check columns
- PD file has both index rows (IND_SEC=Y) and stock rows (IND_SEC=N) — filter when loading
- EQ series = main equity stocks to focus on. BE, BZ, ST, SM = other categories
- For Stock Deep Dive tab — need 1 year of daily prices per stock = 250 rows per stock
- 1 year × 3000 stocks = 750K rows in stock_prices_daily — manageable
- SQLAlchemy NOT being used — Rich doesn't know it, not working on his system. Use psycopg2 directly or DBeaver import

---

## BEFORE APPLYING — REVISION CHECKLIST

- [ ] SQL top interview questions + concepts
- [ ] Excel revision
- [ ] Python/Pandas revision
- [ ] Power BI tools revision
- [ ] Business KPIs (must know)
- [ ] Interview narrative — gap explanation (5 years trading, YouTube channel proof)
- [ ] Communication prep
- [ ] Mock interview with Claude

---

## MAY 1 CHECKLIST

- [ ] Push Project 1 .pbix to GitHub
- [ ] Push Project 2 everything to GitHub
- [ ] Power BI Publish to Web — both projects
- [ ] Add YouTube video link to both READMEs
- [ ] Add GIFs to both READMEs
- [ ] Update LinkedIn
- [ ] Send first applications

---

*For next chat: Upload this file at the start. Current task: Complete download_data.py — generate trading date list, loop download all 1-year PR zips, extract PD + GL + HL files only.*
