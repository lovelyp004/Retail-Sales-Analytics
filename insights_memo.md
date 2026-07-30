# Retail Sales Analysis — Insights Memo

## Problem Statement
This analysis explores four years (2015-2018) of retail order data to identify 
which product categories, regions, and time periods drive revenue, and whether 
sales spikes are driven by higher-value orders or simply higher order volume.

## Key Findings

1. **Technology leads category revenue, but by a narrow margin.**
   Technology ($827,456), Furniture ($728,659), and Office Supplies ($705,422) 
   are far closer in total sales than their product breadth suggests — no single 
   category dominates the business.

2. **Phones and Chairs are the two biggest sub-category earners**, at $327,782 
   and $322,823 respectively — together outselling the next three sub-categories 
   (Storage, Tables, Binders) combined.

3. **Nov/Dec revenue spikes are volume-driven, not value-driven.**
   November and December consistently post the highest total sales each year 
   (e.g. Nov 2018: $117,938), but average order value in these months is 
   unremarkable (Nov: $241.66, Dec: $232.62 — both mid-pack across the year). 
   Order *count*, however, jumps sharply: November averages ~1,449 orders vs. 
   a low of 297 in February. This points to a seasonal ordering-frequency 
   effect (e.g. holiday shopping) rather than customers spending more per order.

4. **West and East regions drive ~70% of total revenue** ($710,220 and 
   $669,519 respectively), while South lags at $389,151 — less than half of 
   West's total, and worth investigating for regional strategy.

5. **Revenue is concentrated in a small customer base.** The top 10 customers 
   each spent $12,000-$25,000, led by Sean Miller ($25,043) — a potential 
   starting point for a customer-loyalty or account-management analysis.

6. **1,145 orders (~11.7% of all orders) were flagged as statistical outliers** 
   in Sales value using the IQR method, suggesting a meaningful share of 
   transactions are either bulk/high-value orders or possible data anomalies 
   worth a closer look.

## Recommendations
1. Investigate the South region's underperformance — is it a market-size 
   issue, a lower-density sales team, or a product-mix mismatch?
2. Since Nov/Dec growth is volume-driven, focus holiday-season strategy on 
   order-acquisition tactics (promotions, ad spend) rather than upsell/AOV tactics.