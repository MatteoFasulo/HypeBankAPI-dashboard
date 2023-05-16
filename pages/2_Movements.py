import streamlit as st
import pandas as pd
import plotly.express as px
import altair as alt

import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)

@st.cache_data
def load_balance():
    balance = pd.read_json('json/balance.json', orient='index').transpose()
    balance = balance.iloc[0]
    return balance

@st.cache_data
def load_movements():
    movements = pd.read_json('json/movements.json', orient='columns')
    month_movements = movements["month"]
    movements_data = [movement for month in month_movements for movement in month["movements"]]
    movements = pd.json_normalize(movements_data)
    movements = movements.sort_values('date')
    movements.date = pd.to_datetime(movements.date, utc=False, format='%Y-%m-%dT%H:%M:%SZ').dt.date
    movements['month'] = pd.to_datetime(movements.date).dt.month
    movements['month_name'] = pd.to_datetime(movements.date).dt.month_name()
    movements['year'] = pd.to_datetime(movements.date).dt.year
    movements.rename(
        columns={
            'additionalInfo.category.id': 'category_id', 
            'additionalInfo.category.name': 'category',
            },
        inplace=True,
    )
    return movements

st.set_page_config(
    page_title="Hype Personal Dashboard",
    page_icon="🏠",
    layout='wide',
    initial_sidebar_state='expanded',
    menu_items={
        'Get Help': 'https://github.com/MatteoFasulo/HypeAPI',
        'Report a bug': "https://github.com/MatteoFasulo/HypeAPI/issues",
        'About': 
            """
            # Hype Personal Dashboard
            This webapp was created with the aim of allowing Hype users to better analyze their account through the use of aggregated statistics and graphs.
            Any contribution to this project is welcome to improve the quality of work!

            GitHub Repository: https://github.com/MatteoFasulo/HypeAPI
            """
        }
)

movements = load_movements()
balance = load_balance()
filtered_movements = movements.copy()

with st.sidebar:
    st.sidebar.title('Hype Account Dashboard')
    movement_types = movements.subType.unique().tolist()
    movement_types.insert(0, 'All')
    transaction_type = st.selectbox('Transaction Type', options=movement_types, index=movement_types.index('All'), help='None (Imposta di Bollo)')
    date_range = st.date_input('Date Range', value=[movements.date.min(), movements.date.max()], min_value=movements.date.min(), max_value=movements.date.max(), help='Date range of transactions')
    if transaction_type != 'All':
        filtered_movements = filtered_movements[filtered_movements['subType'] == transaction_type]
    try:
        filtered_movements = filtered_movements[(filtered_movements['date'] >= date_range[0]) & (filtered_movements['date'] <= date_range[1])]
    except IndexError:
        pass
    
st.title('Hype Bank Account Dashboard')
st.subheader('Summary')
left, midleft, midright, right = st.columns(4)
with left:
    st.metric('Total Balance', balance.balance)
with midleft:
    st.metric('Spendable', balance.spendable)
with midright:
    st.metric('Scheduled Activities', balance.scheduledActivities)
with right:
    st.metric('Saved for Goals', balance.savedAmountForGoals)

st.divider()
st.subheader('Transactions')
st.dataframe(filtered_movements)

st.divider()
st.subheader('Charts')
left, right = st.columns(2)

with left:
    # barchart
    chart = alt.Chart(
        filtered_movements[['subType','amount']].groupby('subType').sum().reset_index().sort_values(by='amount', ascending=False)
        ).mark_bar().encode(
            x=alt.X('subType', title='Transaction Type', axis=alt.Axis(labelAngle=-45)),
            y=alt.Y('amount', title='Total Amount ($/EUR)'),
            color='subType'
        ).properties(title='Total amount per transaction type')
    
    st.altair_chart(chart, use_container_width=True)

with right:
    # sunburst
    subtype_count = filtered_movements.groupby(['subType', 'income']).size().reset_index(name='count')
    subtype_count['label'] = subtype_count['income'].map({True: 'In', False: 'Out'})
    fig = px.sunburst(subtype_count, path=['subType', 'label'], values='count',
                    color='subType',
                    hover_data=['count'])
    fig.update_layout(
    title=dict(text='Movements SubType Sunburst Chart'), 
    title_x=0.5,
    title_y=0.95,
    )
    st.plotly_chart(fig, use_container_width=True)

# scatterplot
filtered_movements['color'] = filtered_movements['income'].map({True: 'green', False: 'red'})

chart = alt.Chart(
    filtered_movements
    ).mark_circle().encode(
        x=alt.X('date:T', title='Transaction Date', axis=alt.Axis(labelAngle=-45)),
        y=alt.Y('amount:Q', title='Total Amount ($/EUR)'),
        size=alt.Size('amount:Q'),
        color=alt.Color('income:N', scale=alt.Scale(domain=[True, False], range=['green', 'red'])),
    ).properties(
        title='Bank Transactions Scatter Plot',
    ).configure_title(
        fontSize=20,
        anchor='start',
        align='left'
    )

st.altair_chart(chart, use_container_width=True)

# BarChart income for each month
grouped_df = filtered_movements.groupby(['year', 'month', 'month_name', 'income'])['amount'].sum().reset_index()
grouped_df['month_year'] = grouped_df['month_name'] + ' ' + grouped_df['year'].astype(str)
color_map = {True: 'green', False: 'red'}

fig = px.bar(grouped_df, x='month_year', y='amount', color='income',
            barmode='group', labels={'income': 'Income'}, title='Monthly Income', color_discrete_map=color_map)
fig.update_layout(
    legend=dict(itemclick='toggle'),
    clickmode='event+select'
)
st.plotly_chart(fig, use_container_width=True)

left, right = st.columns(2)

with left:
    # PieChart facet wrap for each year
    grouped_data = filtered_movements.groupby(['year', 'income'])['amount'].sum().reset_index()

    chart = alt.Chart(grouped_data).mark_arc(innerRadius=40, outerRadius=100).encode(
        theta=alt.Theta('amount:Q'),
        color=alt.Color('income:N', scale=alt.Scale(domain=[False, True], range=['red', 'green'])),
        facet=alt.Facet('year:N', columns=2)
    ).properties(
        title='Income by Year',
        width=250,
        height=250
    ).configure_title(
        fontSize=20,
        anchor='start',
        align='left'
    )

    st.altair_chart(chart, use_container_width=False)

with right:
    # PieChart transaction category (all years)
    grouped_data = filtered_movements[['year', 'amount', 'income', 'category']].groupby(['year','category'])['amount'].sum().reset_index()

    fig = px.pie(grouped_data,
                values='amount',
                names='category',
                color='category',
                title='Amount spent per transaction category',
                facet_col='year', 
                facet_col_wrap=2,
                facet_col_spacing=.22,
                facet_row_spacing=.2,
                height=700, 
                width=700,
    )
    fig.update_traces(
        textposition='inside', 
        textinfo='percent', 
        showlegend=True
    )
    fig.for_each_annotation(lambda a: a.update(text=a.text.split("=")[-1]))
    st.plotly_chart(fig, use_container_width=True)
