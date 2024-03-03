# import packages
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from tools import metric_graph as mg
from babel.numbers import format_currency
sns.set(style='dark')
st.set_page_config(layout="wide")

# load dataset
df_path = "https://github.com/tmrafif/data-analysis-project/blob/8bb4adfc3acd5db9a51500d1bcdcf63752eaaf2e/dashboard/main_data.csv"
main_df = pd.read_csv(df_path)

# datetime columns
datetime_columns = ['order_purchase_timestamp', 'order_approved_at', 'order_delivered_carrier_date',
                    'order_delivered_customer_date', 'order_estimated_delivery_date']

# convert dtype to "datetime"
for column in datetime_columns:
    main_df[column] = pd.to_datetime(main_df[column], format='%Y-%m-%d %H:%M:%S')

daily_orders_df = mg.create_daily_orders_df(main_df)
sum_order_items_df = mg.create_sum_order_items_df(main_df)
customer_bycity_df = mg.customer_group_df(main_df, groupby='customer_city')
customer_bystate_df = mg.customer_group_df(main_df, groupby='customer_state')
seller_bycity_df = mg.seller_group_df(main_df, groupby='seller_city')
seller_bystate_df = mg.seller_group_df(main_df, groupby='seller_state')
rfm_df = mg.create_rfm_df(main_df)

# Daily Orders
st.subheader('Daily Orders')

col1, col2 = st.columns(2)

with col1:
    total_orders = daily_orders_df['order_count'].sum()
    st.metric("Total Orders", value=total_orders)

with col2:
    total_revenue = format_currency(daily_orders_df['revenue'].sum(), 'R$', locale='es_CO') 
    st.metric("Total Revenue", value=total_revenue)

st.pyplot(mg.create_daily_orders_graph(daily_orders_df))

# Best & Worst Product Category
st.header('Best & Worst Performing Product')

col1, col2 = st.columns(2)

with col1:
    st.subheader('Best Performing Product Category')
    st.pyplot(mg.product_bycategory_graph(sum_order_items_df, best=True))

with col2:
    st.subheader('Worst Performing Product Category')
    st.pyplot(mg.product_bycategory_graph(sum_order_items_df, best=False))

# Customer and Seller Demographics
st.header('Customer and Seller Demographics')

col1, col2 = st.columns(2)

with col1:
    st.subheader('Top Cities by Number of Customers')
    st.pyplot(mg.customer_group_graph(customer_bycity_df, groupby='customer_city'))

with col2:
    st.subheader('Top States by Number of Customers')
    st.pyplot(mg.customer_group_graph(customer_bystate_df, groupby='customer_state', reverse=True))

col1, col2 = st.columns(2)

with col1:
    st.subheader('Top Cities by Number of Sellers')
    st.pyplot(mg.seller_group_graph(seller_bycity_df, groupby='seller_city'))

with col2:
    st.subheader('Top States by Number of Sellers')
    st.pyplot(mg.seller_group_graph(seller_bystate_df, groupby='seller_state', reverse=True))

# Best Customer Based on RFM Parameters
st.header('Best Customer Based on RFM Parameters')

col1, col2, col3 = st.columns(3)

with col1:
    avg_recency = round(rfm_df.recency.mean(), 1)
    st.metric("Average Recency (days)", value=avg_recency)
    st.subheader('By Recency (Days)')
    st.pyplot(mg.create_rfm_graph(rfm_df, by='recency'))

with col2:
    avg_frequency = round(rfm_df.frequency.mean(), 2)
    st.metric("Average Frequency", value=avg_frequency)
    st.subheader('By Frequency')
    st.pyplot(mg.create_rfm_graph(rfm_df, by='frequency'))

with col3:
    avg_frequency = format_currency(rfm_df.monetary.mean(), 'R$', locale='es_CO') 
    st.metric("Average Monetary", value=avg_frequency)
    st.subheader('By Monetary (R$)')
    st.pyplot(mg.create_rfm_graph(rfm_df, by='monetary'))
