import pandas as pd
import datetime
import joblib
import streamlit as st
def main():
    html_tag="""
    <div style = "background-color:grey;padding:15px">
    <h2 style="color:red;text-align:center;">Car Selling Price Prediction World</h2>
    <ul>
        <li style="color:red;">
        <h5 style="color:blue;text-align:centre;">Welcome to Car Prediction System Made by Machine Learning </h5>
        </li>
        <li style="color:red;"> 
        <h5 style="color:blue;text-align:centre;">     Predict Your Car selling Price at best price</h5>
        </li>
        <li style="color:red;">
        <h5 style="color:blue;text-align:centre;">Fill the details Carefully!!!</h5></li>
    </ul>   
    
    <h5 style="color:black;text-align:left;">Incase of Clarifiction or doubts Contact me:-> 
    <ul>
      <li style="color:yellow;">
      <a href="https://www.linkedin.com/in/neeraj-kumar-9a75811a2" style="color:#36AE7C;">Linkdin Profile</a>
      </li>
      <li style="color:yellow;">
      <a href="https://github.com/neerajcodes888" style="color:#36AE7C;">Github Profile</a
      </li>
   </ul>
    </h5> 
      </div>
    """
    model=joblib.load('Car_price_Prediction_model')
    
    st.markdown(html_tag,unsafe_allow_html=True)
    st.write('')
    st.write('')
    arg1=st.number_input("What is the present price according to the market(in Lakhs)",2.0,30.0,step=0.5)
    arg2=st.number_input("How much distance covered till now(in Kilometers)",100,50000,step=100)
    arg3=st.selectbox("Which fuel is used for the car",('Petrol','Diesel','CNG'))
    if arg3=="Petrol":
        s1=0
    elif arg3=="Diesel":
        s1=1
    elif arg3=="Diesel":
        s1=2
    arg4=st.selectbox("Whether you are a Dealer or Indivisual",('Dealer','Indivisual'))
    if arg4=="Dealer":
        s2=0
    elif arg4=="Indivisual":
        s2=1
    arg5=st.selectbox("What is the transmission Mode",('Mannual','Automatic'))
    if arg5=="Mannual":
        s3=0
    elif arg5=="Automatic":
        s3=1
    arg6=st.slider("How many owners had for the car Previously",0,5)
    current_date=datetime.datetime.now()
    year_old=st.number_input("Which Year have you purchased the car",2000,current_date.year)
    s4=current_date.year-year_old
    new_data = pd.DataFrame({
    'Present_Price':arg1,
    'Kms_Driven':arg2,
    'Fuel_Type':s1,
    'Seller_Type':s2,
    'Transmission':s3,
    'Owner':arg6,
    'Age':s4
    },index=[0])
    try:
        if st.button('Predict'):
         prediction=model.predict(new_data)
         st.balloons()
         st.success("Final selling price for your car will be  {:.2f} lakhs".format(prediction[0]))
        # else:
        #  st.warning("OOPS....Unable to predict selling Price")
    except:
        st.warning("Some error occured! Please Try again!!!")



if __name__ == '__main__':
    main()
    
