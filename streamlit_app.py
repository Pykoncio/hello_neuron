import streamlit as st

st.image("img/neurona.jpg", width=400)
st.title("Hello Neuron!")

tab1, tab2, tab3 = st.tabs(["One Input", "Two Inputs", "Three Inputs and a Bias"])

def calculate_output(weights, input_values, bias=0):
    return sum(w * x for w, x in zip(weights, input_values)) + bias

with tab1:
    st.header("One Neuron with an Input and a Weight")
    w0 = st.slider("Weight", min_value=0.00, max_value=5.00, value=0.00, step=0.01)
    x0 = st.number_input("Insert an Input Value", value=0.00, step=0.01)
    if st.button("Calculate the output", key="tab1"):
        output = calculate_output([w0], [x0])
        st.write(f"The output value is {output}")

with tab2:
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("Weight w<sub>0</sub>", unsafe_allow_html=True)
        w0 = st.slider("s1", min_value=0.00, max_value=5.00, value=0.00, step=0.01, label_visibility="collapsed")
        st.markdown("Input x<sub>0</sub>", unsafe_allow_html=True)
        x0 = st.number_input("n1", value=0.00, step=0.01, label_visibility="collapsed")

    with col2:
        st.markdown("Weight w<sub>1</sub>", unsafe_allow_html=True)
        w1 = st.slider("s2", min_value=0.00, max_value=5.00, value=0.00, step=0.01, label_visibility="collapsed")
        st.markdown("Input x<sub>1</sub>", unsafe_allow_html=True)
        x1 = st.number_input("n2", value=0.00, step=0.01, label_visibility="collapsed")

    if st.button("Calculate the output", key="tab2"):
        output = calculate_output([w0, w1], [x0, x1])
        st.write(f"The output value is {output}")

with tab3:
    st.header("One Neuron with Three Inputs, Weights, and a Bias")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("Weight w<sub>0</sub>", unsafe_allow_html=True)
        w0 = st.slider("s3", min_value=0.00, max_value=5.00, value=0.00, step=0.01, label_visibility="collapsed")
        st.markdown("Input x<sub>0</sub>", unsafe_allow_html=True)
        x0 = st.number_input("n3", value=0.00, step=0.01, label_visibility="collapsed")

    with col2:
        st.markdown("Weight w<sub>1</sub>", unsafe_allow_html=True)
        w1 = st.slider("s4", min_value=0.00, max_value=5.00, value=0.00, step=0.01, label_visibility="collapsed")
        st.markdown("Input x<sub>1</sub>", unsafe_allow_html=True)
        x1 = st.number_input("n4", value=0.00, step=0.01, label_visibility="collapsed")

    with col3:
        st.markdown("Weight w<sub>2</sub>", unsafe_allow_html=True)
        w2 = st.slider("s5", min_value=0.00, max_value=5.00, value=0.00, step=0.01, label_visibility="collapsed")
        st.markdown("Input x<sub>2</sub>", unsafe_allow_html=True)
        x2 = st.number_input("n5", value=0.00, step=0.01, label_visibility="collapsed")

    b = st.number_input("Insert Bias", value=0.00, step=0.01)

    if st.button("Calculate the output", key="tab3"):
        output = calculate_output([w0, w1, w2], [x0, x1, x2], b)
        st.write(f"The output value is {output}")