import streamlit as st


st.write('# Cyclophosphamide for allo prescription')

st.write('## This tool has NOT been validated any conclusions drawn ' + \
         'are done at the risk of the user')

weight = st.number_input('Enter weight in kg')

height = st.number_input('Enter height in cm')

gender = st.radio('Select gender', ('Male', 'Female'))

button = st.button('click to calculate!')

if button:
    if any([weight, height, gender]) == None:
            st.write('## Please make sure all fields are entered')
    else:
        if gender == 'Male':
            ibw = 2.3*(height-152.4)/2.54 + 50
        else:
            ibw = 2.3*(height-152.4)*0.9/2.54 + 45.5
        st.write(f'Ideal body weight is {round(ibw,1)}kg')

        if weight/ibw > 1.25:
            cdw = ibw + 0.4*(weight - ibw)
            st.write('Weight is more than 125% ideal body weight, therefore using adjusted body weight')
            st.write(f'This is {round(cdw, 1)}kg')
        else:
            cdw = ibw
            st.write('Weight is less than 125% ideal body weight, therefore using ideal body weight as above')

        dose = 50*cdw
        st.write(f'50mg/kg cyclophosphamide dose should therefore be: {round(dose)}mg')
        st.write('Note: this does not take dose banding into account')