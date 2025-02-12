import streamlit as st

def main():
    st.title("Automated Scene Generation")
    
    # Multi-select for road selection
    road = st.multiselect("Road Type:", ["Single-Lane", "Two-Lane", "Three-Lane", "Highway"])

    # Multi-select for sign selection
    sign = st.multiselect("Sign Type:", ["Rectangle", "Triangle"])

    # Multi-select for environment selection
    environment = st.multiselect("Environment:", ["Fir trees", "Birch trees", "Grassy Plain", "City"])


    

if __name__ == "__main__":
    main()
