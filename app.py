import streamlit as st
from crewai import Crew, Agent, Task
from langchain_openai import ChatOpenAI
import time

# Set up OpenAI model
llm = ChatOpenAI(temperature=0.7)

# Create Travel Planner Agent
travel_planner = Agent(
    role="Travel Planner",
    goal="Create a daily travel itinerary with top tourist attractions",
    backstory="An expert in planning beautiful, balanced, and fun daily itineraries in any city or country.",
    verbose=True,
    llm=llm
)

# Streamlit UI Configuration
st.set_page_config(
    page_title="Travel Itinerary Planner",
    page_icon="✈️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS for styling
st.markdown("""
    <style>
    .main {
        background-color: white !important;
        padding: 2rem;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
    }
    h1 {
        color: #c6d1e0;
        font-family: 'Helvetica Neue', sans-serif;
        font-weight: 700;
        margin-bottom: 1.5rem;
    }
    .stButton > button {
        background-color: #4C9AFF;
        color: white;
        padding: 0.75rem 1.5rem;
        border-radius: 8px;
        font-size: 16px;
        font-weight: 600;
        border: none;
        transition: all 0.3s ease;
        width: 100%;
        margin-top: 1rem;
    }
    .stButton > button:hover {
        background-color: #2684FF;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        transform: translateY(-2px);
    }
    .stTextInput > div > div > input,
    .stNumberInput > div > div > input {
        background-color: #F7F9FC;
        border: 1px solid #E6E8EB;
        padding: 0.75rem;
        font-size: 16px;
        border-radius: 8px;
        color: #c6d1e0;
    }
    .stTextInput > div > div > input:focus,
    .stNumberInput > div > div > input:focus {
        border: 1px solid #4C9AFF;
        box-shadow: 0 0 0 2px rgba(76, 154, 255, 0.2);
    }
    .stMarkdown {
        font-size: 16px;
        color: #c6d1e0;
        line-height: 1.6;
    }
    .result-container {
        background-color: #F7F9FC;
        padding: 1.5rem;
        border-radius: 8px;
        border-left: 4px solid #4C9AFF;
        margin-top: 1.5rem;
        color: #c6d1e0;  /* Ensuring text color is dark and readable */
    }
    .result-container p, .result-container li, .result-container h1, 
    .result-container h2, .result-container h3, .result-container h4 {
        color: #c6d1e0 !important;  /* Force dark color for all text elements */
    }
    .subheader {
        color: #c6d1e0;
        font-size: 20px;
        font-weight: 600;
        margin-top: 0;
        margin-bottom: 1rem;
    }
    .label {
        font-weight: 600;
        color: #c6d1e0;
        margin-bottom: 0.5rem;
    }
    .divider {
        margin: 1.5rem 0;
        border-top: 1px solid #E6E8EB;
    }
    .icon-text {
        display: flex;
        align-items: center;
        gap: 0.5rem;
        font-size: 14px;
        color: #c6d1e0;
    }
    .stTextInput > div > div > input {
        color: black;
    }
  
            

    </style>
""", unsafe_allow_html=True)

# Header with custom styling
st.markdown('<h1>✈️ Travel Itinerary Planner</h1>', unsafe_allow_html=True)
st.markdown('<p class="icon-text">🌍 Plan your perfect trip with AI assistance</p>', unsafe_allow_html=True)

# Input Container
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
st.markdown('<p class="label">Where are you going?</p>', unsafe_allow_html=True)
destination = st.text_input("", placeholder="Enter your destination (e.g., Paris, Tokyo, Bali)", label_visibility="collapsed")

col1, col2 = st.columns(2)
with col1:
    st.markdown('<p class="label">How many days?</p>', unsafe_allow_html=True)
    days = st.number_input("", min_value=1, max_value=14, value=3, label_visibility="collapsed")
with col2:
    st.markdown('<p class="label">Travel style</p>', unsafe_allow_html=True)
    travel_style = st.selectbox("",
        options=["Balanced", "Cultural", "Adventure", "Relaxed", "Budget-friendly", "Luxury"],
        index=0,
        label_visibility="collapsed")

# Additional preferences (collapsible)
with st.expander("Additional preferences"):
    interests = st.multiselect(
        "Select your interests",
        ["History", "Art", "Food", "Nature", "Shopping", "Local experiences", "Architecture", "Photography", "Nightlife"],
        ["History", "Food"]
    )
    avoid = st.text_area("Anything you want to avoid?", "", placeholder="E.g., crowded places, long walks, etc.")

# Generate Button
if st.button("✨ Generate My Itinerary"):
    if not destination:
        st.error("Please enter a destination to continue.")
    else:
        # Show loading spinner with custom message
        with st.spinner("🧠 Planning your perfect itinerary..."):
            time.sleep(2)  # Simulate processing time
            
            # Create the itinerary task for CrewAI
            planner_task = Task(
                description=f"Create a detailed daily travel itinerary for {days} days in {destination}. Focus on {travel_style.lower()} experiences and include interests like {', '.join(interests)}. Each day should include 3-4 places to visit with short descriptions. Make sure it's well-paced and covers various attractions. {avoid if avoid else ''}",
                expected_output="A day-by-day travel plan with carefully selected places per day and brief descriptions.",
                agent=travel_planner
            )
            
            # Run CrewAI to generate the itinerary
            crew = Crew(
                agents=[travel_planner],
                tasks=[planner_task],
                verbose=True
            )
            result = crew.kickoff()
            
            # Convert the CrewOutput object to string
            itinerary_text = str(result)
            
            # Display Results in a beautifully styled container
            # st.markdown('<div class="result-container">', unsafe_allow_html=True)
            st.markdown(f'<p class="subheader">✨ Your {travel_style} Itinerary for {destination} ({days} Days)</p>', unsafe_allow_html=True)
            
            # Add download option with the string version
            st.download_button(
                label="📥 Download Itinerary",
                data=itinerary_text,
                file_name=f"{destination}_itinerary.txt",
                mime="text/plain",
            )
            
            # Display the result as markdown with proper styling to ensure visibility
            st.markdown(f'<div style="color: #c6d1e0;">{itinerary_text}</div>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
            
            # Post-generation feedback
            st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
            st.markdown('<p class="icon-text">💡 Pro tip: Save this itinerary and modify it as needed during your trip!</p>', unsafe_allow_html=True)

# Footer
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
st.markdown('<p class="icon-text">🛠️ Built with Streamlit and CrewAI</p>', unsafe_allow_html=True)