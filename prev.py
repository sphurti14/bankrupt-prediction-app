    
#Importing Libraries:
import numpy as np
import streamlit as st 
from keras.models import load_model
from PIL import Image
import time
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import preprocessing
#-------------------------------------------------------------------------------------------------------------------------------
st.set_page_config(page_title="App-Streamlit",page_icon="random",layout="wide",
                       menu_items={'Get Help': 'http://www.quickmeme.com/img/54/547621773e22705fcfa0e73bc86c76a05d4c0b33040fcb048375dfe9167d8ffc.jpg',
                                   'Report a bug': "https://w7.pngwing.com/pngs/839/902/png-transparent-ladybird-ladybird-bug-miscellaneous-presentation-insects-thumbnail.png",
                                   'About': "# This is a Bankruptcy Prevention App. Very Easy to use!"})

@st.cache(allow_output_mutation=True) #For Autoupdate in app.

def loading_model():
    model = load_model('bankr.h5')
    return model
with st.spinner('Model is being loaded..'):
    model=loading_model()     #Model is loaded.

# Reading File:
bank_data=pd.read_csv("bankruptcy_prevention.csv",sep=";")
label_encoder = preprocessing.LabelEncoder()
bank_data[" class"] = label_encoder.fit_transform(bank_data[" class"])
features=bank_data.columns[0:6]
#-------------------------------------------------------------------------------------------------------------------------------
st.write("""
         # BANKRUPTCY PREVENTION
         """)

# Model Prediction func:
def predict_bankruptcy(i,m,f,cr,co,o):
    pred = model.predict(np.array([[i, m, f, cr, co, o]]))

    # DEBUG (optional, can remove later)
    st.write("Raw prediction:", pred)

    try:
        val = pred[0][0]
    except:
        val = pred[0]

    return int(val)
#-------------------------------------------------------------------------------------------------------------------------------



# Graph function:
def graph1(choice):
    plt.rcParams.update({'font.size': 6})
    
    # Clean column names
    bank_data.columns = bank_data.columns.str.strip()
    choice = choice.strip()

    if choice == 'None':
        return 0, 0

    # -------- Graph 1 --------
    g = sns.catplot(
        x="class",
        hue=choice,
        data=bank_data,
        kind="count",
        height=2,
        aspect=1.25,
        palette={0: "yellow", 0.5: "orange", 1: "red"}
    )
    
    g.legend.set_title(choice, prop={"size": 7})
    g.set_xticklabels(["Bankrupted", "Not Bankrupted"])
    g.fig.suptitle(f"{choice} vs Bankruptcy")
    plt.gcf().set_size_inches(3, 3)

    # -------- Graph 2 --------
    h = sns.catplot(
        x=choice,
        hue="class",
        data=bank_data,
        kind="count",
        height=2,
        aspect=1.25,
        palette={1: "blue", 0: "green"}
    )
    
    h.legend.set_title("Bankruptcy", prop={"size": 7})
    h.set_xticklabels(["Low", "Medium", "High"])
    h.fig.suptitle(f"{choice} vs Bankruptcy")
    plt.gcf().set_size_inches(3, 3)

    return g, h
            
#-------------------------------------------------------------------------------------------------------------------------------    

# Blog func:
def myinfo():
    st.write("My name is Sphurtis Patil and I am a Data Science enthusiast.")
#-------------------------------------------------------------------------------------------------------------------------------

#Input func:
def input_data():
    industrial_risk = st.sidebar.number_input("Industrial Risk",min_value=0.0, max_value=1.0, value=0.0, step=0.5,help="low = 0.0, medium = 0.50, high = 1.0")
    management_risk = st.sidebar.number_input("Management Risk",min_value=0.0, max_value=1.0, value=0.0, step=0.5,help="low = 0.0, medium = 0.50, high = 1.0")
    financial_flexibility = st.sidebar.number_input("Financial Flexibility",min_value=0.0, max_value=1.0, value=0.0, step=0.5,help="low = 0.0, medium = 0.50, high = 1.0")
    credibility = st.sidebar.number_input("Credibility",min_value=0.0, max_value=1.0, value=0.0, step=0.5,help="low = 0.0, medium = 0.50, high = 1.0")
    competitiveness=st.sidebar.number_input("Competitiveness",min_value=0.0, max_value=1.0, value=0.0, step=0.5,help="low = 0.0, medium = 0.50, high = 1.0")
    operating_risk=st.sidebar.number_input("Operating Risk",min_value=0.0, max_value=1.0, value=0.0, step=0.5,help="low = 0.0, medium = 0.50, high = 1.0")
    return(industrial_risk,management_risk,financial_flexibility,credibility,competitiveness,operating_risk)

#-------------------------------------------------------------------------------------------------------------------------------

# Decor Func:    
def decor():
    html_temp = """
    <div style="background-color:Chocolate;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Bankruptcy Prevention App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    image = Image.open('prev.png')
    st.image(image, caption='')    

#--------------------------------------------------------------------------------------------------------------------------------

def main():
    
    decor()
    name=st.sidebar.text_input("Enter your name :")
    if name:
        st.write("# %s's Company"%name)
    col3,col4,col5=st.columns(3)
# taking Inputs:
    with col3:
        check=st.checkbox("Input Values for Features",value=False)
        if check:
            i,m,f,cr,co,o=input_data()
        
    #---------------------------------------------------------------------------------------------------------------------------

# Result:       
    result = ""

# ---------------- INPUT SECTION ----------------
col1, col2, col3 = st.columns(3)

with col1:
    i = st.selectbox("Industrial Risk", [0.0, 0.5, 1.0])

with col2:
    m = st.selectbox("Management Risk", [0.0, 0.5, 1.0])

with col3:
    f = st.selectbox("Financial Flexibility", [0.0, 0.5, 1.0])

col4, col5, col6 = st.columns(3)

with col4:
    cr = st.selectbox("Credibility", [0.0, 0.5, 1.0])

with col5:
    co = st.selectbox("Competitiveness", [0.0, 0.5, 1.0])

with col6:
    o = st.selectbox("Operating Risk", [0.0, 0.5, 1.0])


# ---------------- PREDICT SECTION ----------------
if st.button("Predict"):
    with st.spinner('Wait for it...'):
        time.sleep(3)

    result = predict_bankruptcy(i, m, f, cr, co, o)

    if result == 1:
        st.error("### You are BANKRUPTED!!")
    else:
        st.balloons()
        st.success("### You are NOT BANKRUPTED!!")

else:
    st.write("Whenever you're ready..!")

st.markdown("---")


# ---------------- GRAPH SECTION ----------------
if st.checkbox("Show Graphs", value=False):
    choice = st.selectbox(
        "Choose Feature Values :",
        ('None', 'industrial_risk', 'management_risk', 'financial_flexibility',
         'credibility', 'competitiveness', 'operating_risk')
    )

    col1, col2 = st.columns(2)
    plot1, plot2 = graph1(choice)

    if plot1 != 0:
        with col1:
            st.pyplot(plot1)
        with col2:
            st.pyplot(plot2)
    else:
        st.write("No Feature chosen!")

    st.markdown("---")


# ---------------- BOTTOM SECTION ----------------
col4, col5 = st.columns(2)

with col4:
    st.write("")

with col5:
    expander = st.expander("My info", expanded=False)
    with expander:
        st.info("My name is Sphurti Patil and I am a Data Science enthusiast.")


# ---------------- MAIN ----------------
if __name__ == '__main__':
    main()