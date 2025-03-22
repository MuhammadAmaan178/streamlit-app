import streamlit as st
import module as md


st.title('Cryptogram')

option = st.radio("Select what do you want?", ('Encode The Message', 'Decode The Message'))
if option == 'Encode The Message':
    msg= st.text_input("Enter your Message:").upper()
    st.subheader("Type Your Key Here: -")
    x11 = st.number_input("Type Value For First Row and First Column", min_value=-100, max_value=100, value=0)
    x12 = st.number_input("Type Value For First Row and Second Column", min_value=-100, max_value=100, value=0)
    x21 = st.number_input("Type Value For Second Row and First Column", min_value=-100, max_value=100, value=0)
    x22 = st.number_input("Type Value For Second Row and Second Column", min_value=-100, max_value=100, value=0)
    if st.button("Encode It!!!"):
        if md.is_valid_input(msg) == True:
            new_list = md.take_string(msg)
            key = [[x11, x12], [x21, x22]]
            # checking if the key is inversable
            temp = ((key[0][0]) * (key[1][1])) - ((key[0][1]) * (key[1][0]))
            if temp == 0:
                st.text("Key Is Non-Inversable")
            else:
                encoded_msg = md.key_msg(new_list, x11, x12, x21, x22)
                result_string = " ".join(map(str, encoded_msg))
                st.text(f"Your Encoded Message Is {result_string} and key is {key}")
        else:
            st.warning("Message Can Only Contains Alphabets and Spaces")

elif option == 'Decode The Message':
    msg = st.text_input("Enter your Code With Gap Like This (34 2 55 8):")
    st.subheader("Type Your Key Here: -")
    x11 = st.number_input("Type Value For First Row and First Column", min_value=-100, max_value=100, value=0)
    x12 = st.number_input("Type Value For First Row and Second Column", min_value=-100, max_value=100, value=0)
    x21 = st.number_input("Type Value For Second Row and First Column", min_value=-100, max_value=100, value=0)
    x22 = st.number_input("Type Value For Second Row and Second Column", min_value=-100, max_value=100, value=0)

    if st.button("Decode It!!!"):
        if md.check_numeric_input(msg) == True:
            split = msg.split(" ")
            result = []
            for i in split:
                result.append(int(i))
            key = [[x11, x12], [x21, x22]]
            temp = ((key[0][0]) * (key[1][1])) - ((key[0][1]) * (key[1][0]))
            if temp == 0:
                st.text("Martix Is Non-Inversable")
            else:
                inverse_key = md.inverse(key)
                f_result = md.inversekey_msg(result, inverse_key)
                message = md.decode(f_result)
                st.text(f"According To Your Key {key}, Your Final Decoded Message Is {message}")
        else:
            st.warning("Please enter only numeric values and spaces!")
