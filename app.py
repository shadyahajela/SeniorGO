import streamlit as st
import pandas as pd

# Set page config to wide mode
st.set_page_config(layout="wide")

def home_page():
    st.title("SeniorGO")
    st.write("SeniorGO is a revolutionary navigation website dedicated to enhancing the mobility and social engagement of seniors facing mobility challenges. We offer accessible routes, realtime assistance, and community connections to ensure seniors can move freely and interact with their surroundings, fostering independence and well-being.")

    # User information
    user_data = {
        "Name": ["John Doe"],
        "Age": [75],
        "Health Issues": ["Arthritis, Reduced mobility"]
    }
    df = pd.DataFrame(user_data)
    st.dataframe(df, width=800)

    # Navigation buttons
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("M"):
            st.session_state.page = "map"
    with col2:
        if st.button("B"):
            st.session_state.page = "book_buddy"
    with col3:
        if st.button("C"):
            st.session_state.page = "community"

def map_page():
    st.title("Map")
    col1, col2 = st.columns([1, 2])
    with col1:
        st.write("Enter your current location and destination:")
        current_location = st.text_input("Current Location")
        destination = st.text_input("Destination")
        if st.button("Get Route"):
            st.write(f"Route from {current_location} to {destination} (Personalized to your health information)")
            if st.button("Go!"):
                st.session_state.page = "step_by_step"
    with col2:
        st.write("Google Map (Square Shape)")

    if st.button("Back to Home"):
        st.session_state.page = "home"

def book_buddy_page():
    st.title("Book a Buddy")
    st.write("Choose the type of service you need:")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Transportation"):
            st.session_state.page = "transportation"
    with col2:
        if st.button("Personal"):
            st.session_state.page = "personal"

    if st.button("Back to Home"):
        st.session_state.page = "home"

def transportation_page():
    st.title("Transportation")
    st.write("Enter the details for your transportation request:")
    destination = st.text_input("Destination")
    help_walk = st.checkbox("Need help walking to the destination?")
    help_drive = st.checkbox("Need a volunteer to drive you?")
    if st.button("Send Request"):
        st.write("Request sent to volunteers!")

    if st.button("Back to Book a Buddy"):
        st.session_state.page = "book_buddy"

def personal_page():
    st.title("Personal")
    st.write("Enter the details for your personal service request:")
    hours = st.number_input("Number of hours needed", min_value=1, max_value=10)
    personal_work = st.text_area("What personal work do you need help with?")
    if st.button("Send Request"):
        st.write("Request sent to volunteers!")

    if st.button("Back to Book a Buddy"):
        st.session_state.page = "book_buddy"

def community_page():
    st.title("Community")
    st.write("List of social events happening near you:")
    # Dummy data for social events
    events = [
        {"name": "Senior Meetup", "description": "A social gathering for seniors to connect and chat."},
        {"name": "Gentle Exercise Class", "description": "A low-impact exercise class for seniors."},
        {"name": "Book Club", "description": "A book club for seniors to discuss their favorite books."}
    ]
    for event in events:
        st.subheader(event["name"])
        st.write(event["description"])

    if st.button("Back to Home"):
        st.session_state.page = "home"

def step_by_step_page():
    st.title("Step-by-Step Instructions")
    st.write("Detailed instructions on how to get to your destination.")

    if st.button("Back to Map"):
        st.session_state.page = "map"

if "page" not in st.session_state:
    st.session_state.page = "home"

if st.session_state.page == "home":
    home_page()
elif st.session_state.page == "map":
    map_page()
elif st.session_state.page == "book_buddy":
    book_buddy_page()
elif st.session_state.page == "transportation":
    transportation_page()
elif st.session_state.page == "personal":
    personal_page()
elif st.session_state.page == "community":
    community_page()
elif st.session_state.page == "step_by_step":
    step_by_step_page()
