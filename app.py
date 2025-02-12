import streamlit as st

def main():
    st.title("Automated Scene Generation")
    st.subheader("Select what you would like in your scene, selecting multiple otpions will generate multiple scenes.")

    # Multi-select for road selection
    road = st.multiselect("Road Type:", ["Single-Lane", "Two-Lane", "Three-Lane", "Highway"])

    # Multi-select for variations on roads
    road_variations = st.multiselect("Variations on Roads:", ["Potholes", "Cracks", "Uneven Surface", "Fresh Pavement"])

    # Multi-select for number of trees
    num_trees = st.multiselect("Number of Trees:", ["Few", "Moderate", "Dense", "No Trees"])

    # Multi-select for environment selection
    environment = st.multiselect("Environment:", ["Fir Trees", "Birch Trees", "Grassy Plain", "City"])

    # Multi-select for light changes
    light_changes = st.multiselect("Light Changes:", ["Sunny", "Cloudy", "Dusk", "Dawn", "Artificial Lighting"])

    # Multi-select for camera position and rotation
    camera_settings = st.multiselect("Camera Position & Rotation:", ["Front View", "Side View", "Top View", "Low Angle", "Tilted"])

    # Multi-select for time of day
    time_of_day = st.multiselect("Time of Day:", ["Morning", "Noon", "Evening", "Night"])

    # Multi-select for sign type
    sign = st.multiselect("Sign Type:", ["Rectangle", "Triangle", "Circle", "Octagon"])

    # Multi-select for sign quality/damage
    sign_quality = st.multiselect("Sign Quality/Damage:", ["New", "Faded", "Bent", "Covered with Dirt", "Partially Missing"])

    # Multi-select for weather conditions
    weather = st.multiselect("Weather:", ["Clear", "Overcast", "Rain", "Snow", "Fog", "Storm"])

    # Display the selected options
    st.write("### Selected Options:")
    st.write("Road Type:", road)
    st.write("Variations on Roads:", road_variations)
    st.write("Number of Trees:", num_trees)
    st.write("Environment:", environment)
    st.write("Light Changes:", light_changes)
    st.write("Camera Settings:", camera_settings)
    st.write("Time of Day:", time_of_day)
    st.write("Sign Type:", sign)
    st.write("Sign Quality/Damage:", sign_quality)
    st.write("Weather Conditions:", weather)


    

if __name__ == "__main__":
    main()
