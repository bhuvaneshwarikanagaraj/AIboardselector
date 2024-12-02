import streamlit as st

# Title of the Application
st.title('Edge AI Board Selection Guide')

# Introduction
st.write("""
Welcome to the Edge AI Board Selector!  
Use this app to find the most suitable NVIDIA Jetson device based on your project needs.
""")

# Step 1: Select the use case
use_case = st.selectbox('What is your application?', ['Robotics', 'Autonomous Vehicles', 'Drones', 'AI Cameras', 'Edge Computing', 'AI at the Edge'])

# Step 2: Define requirements for each use case
if use_case == 'Robotics':
    st.write("""
    Robotics applications require powerful GPUs, fast processing, and low power consumption.
    The ideal Jetson board for robotics applications would be one that handles sensor integration, AI tasks, and real-time decision-making.
    """)
    board_choice = st.selectbox('Do you need lightweight or heavy computational power?', ['Lightweight', 'Heavy Computational Power'])
    
    if board_choice == 'Lightweight':
        st.write("**Recommended Board:** Jetson Nano (Ideal for lightweight robotics tasks)")
    else:
        st.write("**Recommended Board:** Jetson AGX Xavier (For more heavy-duty robotic AI applications)")

elif use_case == 'Autonomous Vehicles':
    st.write("""
    Autonomous vehicles require high computational power for real-time decision-making and advanced perception algorithms like object detection.
    """)
    complexity = st.selectbox('What is the complexity of your vehicle?', ['Basic', 'Advanced'])

    if complexity == 'Basic':
        st.write("**Recommended Board:** Jetson Xavier NX (Great for entry-level autonomous vehicles)")
    else:
        st.write("**Recommended Board:** Jetson AGX Xavier (Powerful for full autonomy and real-time perception)")

elif use_case == 'Drones':
    st.write("""
    Drones need lightweight, powerful boards that can process images, video, and sensor data in real-time.
    """)
    requirements = st.selectbox('What level of AI processing do you need?', ['Basic Image Processing', 'Advanced AI/Computer Vision'])

    if requirements == 'Basic Image Processing':
        st.write("**Recommended Board:** Jetson Nano (Perfect for basic drone applications with image processing)")
    else:
        st.write("**Recommended Board:** Jetson Xavier NX (Ideal for advanced computer vision and AI capabilities for drones)")

elif use_case == 'AI Cameras':
    st.write("""
    AI cameras require high-speed image processing and AI inferencing, typically involving deep learning models for object detection or facial recognition.
    """)
    processing_power = st.selectbox('What type of AI processing do you need?', ['Low power', 'High power'])

    if processing_power == 'Low power':
        st.write("**Recommended Board:** Jetson Nano (For lightweight AI camera applications)")
    else:
        st.write("**Recommended Board:** Jetson Xavier NX (For heavy image processing and real-time AI inferencing)")

elif use_case == 'Edge Computing':
    st.write("""
    Edge computing requires high-performance computing at the edge of the network for processing and analyzing data locally, often with AI and machine learning tasks.
    """)
    edge_task = st.selectbox('What type of edge AI applications are you working on?', ['Basic AI', 'Advanced AI', 'Real-time Processing'])

    if edge_task == 'Basic AI':
        st.write("**Recommended Board:** Jetson Nano (For simple edge AI tasks with low power consumption)")
    elif edge_task == 'Advanced AI':
        st.write("**Recommended Board:** Jetson Xavier NX (For advanced edge AI applications with moderate power consumption)")
    else:
        st.write("**Recommended Board:** Jetson AGX Xavier (For real-time edge AI processing and heavy workloads)")

elif use_case == 'AI at the Edge':
    st.write("""
    AI at the edge involves using powerful devices to run AI models and analyze data in real-time, reducing latency and reliance on cloud services.
    """)
    edge_application = st.selectbox('What’s the scale of your AI application?', ['Small', 'Medium', 'Large'])

    if edge_application == 'Small':
        st.write("**Recommended Board:** Jetson Nano (For smaller-scale AI applications at the edge)")
    elif edge_application == 'Medium':
        st.write("**Recommended Board:** Jetson Xavier NX (For medium-scale AI applications at the edge)")
    else:
        st.write("**Recommended Board:** Jetson AGX Xavier (For large-scale, high-performance AI at the edge)")

# Ending message
st.write("Choose the board that best suits your project and start building your AI solution today!")

# Available Jetson Boards (Moved to the end)
st.write("### Available Jetson Boards:")
st.write("""
- Jetson Nano
- Jetson Xavier NX
- Jetson AGX Xavier
- Jetson Orin Nano
- Jetson Orin AGX
""")
