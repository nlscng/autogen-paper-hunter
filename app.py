import streamlit as st
import asyncio
from agents import get_team_config, orchestrate 

st.title('Literature Review Assistant')

desc = st.text_area('Enter a description to conduct a literature review:')

clicked = st.button('Search', type='primary')

chat_container = st.container()

if clicked:
    async def main(desc):
        team = get_team_config()
        async for one_msg in orchestrate(team, task=desc):
            with chat_container:
                if one_msg.startswith('ArxivAgent'):
                    with st.chat_message('human'):
                        st.markdown(one_msg[12:])
                elif one_msg.startswith('researcher'):
                    with st.chat_message('assistant'):
                        st.markdown(one_msg[10:])
                else:
                    with st.expander('Tool Call'):
                        st.markdown(one_msg)

    asyncio.run(main(desc))