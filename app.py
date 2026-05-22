import streamlit as st
import requests
import datetime
import random

st.set_page_config(page_title="Kingsley's API App", page_icon="🎭")

st.title("🎭 Joke Generator")
st.write("This app fetches live jokes from an API!")

# Add your name
st.subheader(f"Built by Kingsley 🎉")

# Create tabs for different features
tab1, tab2, tab3 = st.tabs(["📖 Random Joke", "🔍 Search Jokes", "ℹ️ About APIs"])

with tab1:
    st.header("Get a Random Dad Joke")
    
    # Button to fetch a joke
    if st.button("😂 Tell me a joke!", use_container_width=True):
        with st.spinner("Searching for a funny joke..."):
            # Make the API call
            headers = {"Accept": "application/json"}
            response = requests.get(
                "https://icanhazdadjoke.com/",
                headers=headers
            )
            
            if response.status_code == 200:
                joke_data = response.json()
                st.success(f"**{joke_data['joke']}**")
                st.balloons()
            else:
                st.error("Sorry, the joke API isn't responding!")

with tab2:
    st.header("Search for Specific Jokes")
    
    search_term = st.text_input("Enter a topic (e.g., 'pizza', 'computer', 'dog'):")
    
    if search_term:
        with st.spinner(f"Searching for jokes about {search_term}..."):
            headers = {"Accept": "application/json"}
            response = requests.get(
                f"https://icanhazdadjoke.com/search?term={search_term}",
                headers=headers
            )
            
            if response.status_code == 200:
                search_results = response.json()
                jokes = search_results['results']
                
                if len(jokes) > 0:
                    st.success(f"Found {len(jokes)} joke(s)!")
                    for joke in jokes:
                        st.info(f"📢 {joke['joke']}")
                else:
                    st.warning(f"No jokes found about '{search_term}'. Try something else!")
            else:
                st.error("API search failed!")

with tab3:
    st.header("📚 How This Works")
    st.markdown("""
    **What is an API?**
    An API is like a waiter in a restaurant - you ask for something, and it brings you the data.
    
    **This app uses:**
    - `requests.get()` - Asks the API for data
    - `headers` - Tells the API what format we want (JSON)
    - `response.json()` - Turns the API response into Python data
    
    **Try other free APIs:**
    - `https://api.chucknorris.io/jokes/random` - Chuck Norris jokes
    - `https://catfact.ninja/fact` - Random cat facts
    - `https://api.kanye.rest` - Kanye West quotes
    """)