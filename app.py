import streamlit as st
import pandas as pd

from balancer_handler import *


st.title('Check Aptos balance')

addresses_str = st.text_area(label='Insert addresses that splitted by ENTER')
addresses = addresses_str.split('\n')

if addresses_str:
    df = pd.DataFrame(index=addresses, columns=['amount in USDT'])

    df = get_balance(df=df)
    st.write(df)
    st.write(
        f"""
        # Total balance ${sum(df['amount in USDT'])}
        """
    )
