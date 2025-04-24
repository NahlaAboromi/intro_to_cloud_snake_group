import pandas as pd
import ipywidgets as widgets
from IPython.display import display
from plotly.offline import iplot
import plotly.graph_objs as go
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import plotly.express as px
import requests
import pandas as pd
import matplotlib.pyplot as plt


# Create a simple DataFrame
url = 'https://data.gov.il/api/3/action/datastore_search?resource_id=053cea08-09bc-40ec-8f7a-156f0677aff3'
response = requests.get(url)
data = response.json()

# שלב 2: הפיכת הנתונים ל-DataFrame
records = data['result']['records']
df = pd.DataFrame(records)

# הגדרה להצגת כל העמודות
pd.set_option("display.max_columns", None)


# Tab 1: Data Overview
tab1_content = widgets.Output()
with tab1_content:
    print("Data Overview:")
    display(df.describe())  # Summary statistics

# Tab 2: Raw Data
tab2_content = widgets.Output()
with tab2_content:
    print("Raw Data:")
    display(df)  # Full DataFrame
# Tab 3: Charts
tab3_content = widgets.Output()
with tab3_content:
    print("Charts:")
    plt.clf()  # Clear the current figure
    plt.figure(figsize=(10, 8))  # Increased figure size to accommodate labels
    side_length = 10
    data = 5 + np.random.randn(side_length, side_length)
    data += np.arange(side_length)
    data += np.reshape(np.arange(side_length), (side_length, 1))




      # המרת שנת ייצור למספרים
    df['shnat_yitzur'] = pd.to_numeric(df['shnat_yitzur'], errors='coerce')

    # ספירת כמות רכבים לפי שנת ייצור
    year_counts = df['shnat_yitzur'].value_counts().sort_index()

    # שמות השנים
    years = year_counts.index.astype(str).tolist()

    # כמות הרכבים שיוצרו בכל שנה
    count = year_counts.values

    # יצירת הגרף
    plt.figure(figsize=(10, 6))
    plt.bar(years, count)
    plt.xticks(rotation=45)
    plt.title("num ber year")
    plt.xlabel("year")
    plt.ylabel("count")
    plt.tight_layout()
    plt.show()
    plt.close()

# Create Tabs
tabs = widgets.Tab(children=[tab1_content, tab2_content,tab3_content])
tabs.set_title(0, 'Tab 1: Data Overview')
tabs.set_title(1, 'Tab 2: Raw Data')
tabs.set_title(2, 'Tab 3: Charts')



# Display Tabs
display(tabs)
