import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# create daily orders dataframe
def create_daily_orders_df(df):
    daily_orders_df = df.resample(rule='w', on='order_delivered_customer_date').agg({
        "order_id": "nunique",
        "payment_value": "sum"})
    daily_orders_df = daily_orders_df.reset_index()
    daily_orders_df = daily_orders_df.rename(columns={
        'order_delivered_customer_date': 'order_date',
        "order_id": "order_count",
        "payment_value": "revenue"})
    
    return daily_orders_df

# create 
def create_sum_order_items_df(df):
    sum_order_items_df = df.groupby('product_category').agg(
        order_count=('order_id', 'count'),
        revenue=('payment_value', 'sum')
    ).reset_index()
    return sum_order_items_df

# grouping customers
def customer_group_df(df, groupby='customer_city'):
    bygender_df = df.groupby(by=groupby).agg(
        customer_count=('customer_unique_id', 'nunique')).reset_index()
    
    return bygender_df

# grouping sellers
def seller_group_df(df, groupby='seller_city'):
    bygender_df = df.groupby(by=groupby).agg(
        seller_count=('seller_id', 'nunique')).reset_index()
    
    return bygender_df

# create RFM dataframe
def create_rfm_df(df):
    rfm_df = df.groupby('customer_unique_id').agg(
        max_order_timestamp=('order_purchase_timestamp', 'max'),
        frequency=('order_id', 'nunique'),
        monetary=('payment_value', 'sum')).reset_index()
    
    # calculate recency
    rfm_df["max_order_timestamp"] = pd.to_datetime(rfm_df["max_order_timestamp"])
    rfm_df["max_order_timestamp"] = rfm_df["max_order_timestamp"].dt.date
    recent_date = df['order_purchase_timestamp'].dt.date.max()
    rfm_df["recency"] = rfm_df["max_order_timestamp"].apply(lambda x: (recent_date - x).days)
    rfm_df = rfm_df.drop("max_order_timestamp", axis=1)
    
    return rfm_df

# create daily orders graph
def create_daily_orders_graph(df):
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(
        df["order_date"],
        df["order_count"],
        marker='o', 
        linewidth=2
    )
    # ax.tick_params(axis='y', labelsize=20)
    # ax.tick_params(axis='x', labelsize=15)
    
    return fig

# create best product category graph
def product_bycategory_graph(df, best=True):
    fig, ax1 = plt.subplots(figsize=(20, 10))
    sns.barplot(
        data=df.sort_values(
            by='order_count', ascending=(not best)).head(8),
        x='product_category',
        y='order_count',
        ax=ax1
    )
    ax1.set_xlabel(None)
    ax1.set_ylabel('Number of Orders', fontsize=25)
    ax1.tick_params(axis='x', labelsize=25, labelrotation=90)
    ax1.tick_params(axis='y', labelsize=25)

    ax2 = ax1.twinx()
    sns.lineplot(
        data=df.sort_values('order_count', ascending=(not best)).head(8),
        x='product_category',
        y='revenue',
        marker='o',
        markersize=20,
        linewidth=4,
        color='#ffcc06',
        ax=ax2
    )
    if best == True:
        ax2.set_ylabel('Total Revenue (Millions R$)', fontsize=30, labelpad=10)
    else:
        ax2.set_ylabel('Total Revenue (R$)', fontsize=25, labelpad=10)
    ax2.tick_params(axis='y', labelsize=25)
    ax2.set_ylim(0, None)

    return fig

# create customer group graph
def customer_group_graph(df, groupby='customer_city', reverse=False):
    fig, ax = plt.subplots(figsize=(20, 12))
    sns.barplot(
        data=df.sort_values(
            by='customer_count', ascending=False).head(8),
        x='customer_count',
        y=groupby,
        ax=ax
    )
    ax.tick_params(axis='y', labelsize=25)
    ax.tick_params(axis='x', labelsize=25)
    if reverse == True:
        ax.invert_xaxis()
        ax.yaxis.set_label_position("right")
        ax.yaxis.tick_right()
    ax.set_xlabel(None)
    ax.set_ylabel(None)

    return fig

# create seller group graph
def seller_group_graph(df, groupby='seller_city', reverse=False):
    fig, ax = plt.subplots(figsize=(20, 12))
    sns.barplot(
        data=df.sort_values(
            by='seller_count', ascending=False).head(8),
        x='seller_count',
        y=groupby,
        ax=ax
    )
    ax.tick_params(axis='y', labelsize=25)
    ax.tick_params(axis='x', labelsize=25)
    if reverse == True:
        ax.invert_xaxis()
        ax.yaxis.set_label_position("right")
        ax.yaxis.tick_right()
    ax.set_xlabel(None)
    ax.set_ylabel(None)

    return fig

# RFM graph
def create_rfm_graph(df, by='recency'):
    fig, ax = plt.subplots(figsize=(5, 5))

    sort_ascending = True if by == 'recency' else False
    sns.barplot(
        data=df.sort_values(by, ascending=sort_ascending).head(8),
        x='customer_unique_id',
        y=by,
        ax=ax)

    ax.set_xlabel('Customer ID', fontsize=15)
    ax.set_ylabel(None)
    ax.tick_params(axis='x', labelrotation=90)
        
    return fig