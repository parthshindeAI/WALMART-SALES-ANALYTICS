-- =========================================
-- Walmart Sales Analytics — Core KPIs
-- =========================================

-- Assumed table: walmart_sales
-- Columns:
-- store, date, weekly_sales, dept, is_holiday, type, size, markdown1-5

-- 1. Total revenue per store per month
SELECT
    store,
    DATE_TRUNC('month', date) AS month,
    SUM(weekly_sales) AS total_sales
FROM walmart_sales
GROUP BY store, month
ORDER BY month, total_sales DESC;

-- 2. Top 10 departments by total revenue
SELECT
    dept,
    SUM(weekly_sales) AS total_revenue
FROM walmart_sales
GROUP BY dept
ORDER BY total_revenue DESC
LIMIT 10;

-- 3. Average weekly sales per store
SELECT
    store,
    AVG(weekly_sales) AS avg_weekly_sales
FROM walmart_sales
GROUP BY store
ORDER BY avg_weekly_sales DESC;

-- 4. Holiday vs Non-holiday average sales
SELECT
    is_holiday,
    AVG(weekly_sales) AS avg_sales
FROM walmart_sales
GROUP BY is_holiday;

-- 5. Promotion vs non-promotion sales
SELECT
    CASE
        WHEN (markdown1 + markdown2 + markdown3 + markdown4 + markdown5) > 0
        THEN 'Promotion'
        ELSE 'No Promotion'
    END AS promotion_flag,
    AVG(weekly_sales) AS avg_sales
FROM walmart_sales
GROUP BY promotion_flag;

-- 6. Revenue by store type
SELECT
    type,
    SUM(weekly_sales) AS total_revenue
FROM walmart_sales
GROUP BY type
ORDER BY total_revenue DESC;

-- 7. Rank stores by total revenue
SELECT
    store,
    SUM(weekly_sales) AS total_revenue,
    RANK() OVER (ORDER BY SUM(weekly_sales) DESC) AS revenue_rank
FROM walmart_sales
GROUP BY store;

-- =========================================
-- Notes:
-- These queries replicate the KPIs developed
-- in the Python EDA notebook using SQL.
-- They are designed for analytical workloads
-- and can be executed directly using DuckDB.
-- =========================================
