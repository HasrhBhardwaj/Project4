{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "d25ab3e5-0cd3-4d73-8c24-8b2b5148313a",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Original Dataset:\n",
      "   Unique ID  Indicator ID                    Name Measure Measure Info  \\\n",
      "0     172653           375  Nitrogen dioxide (NO2)    Mean          ppb   \n",
      "1     172585           375  Nitrogen dioxide (NO2)    Mean          ppb   \n",
      "2     336637           375  Nitrogen dioxide (NO2)    Mean          ppb   \n",
      "3     336622           375  Nitrogen dioxide (NO2)    Mean          ppb   \n",
      "4     172582           375  Nitrogen dioxide (NO2)    Mean          ppb   \n",
      "\n",
      "  Geo Type Name  Geo Join ID                      Geo Place Name  \\\n",
      "0         UHF34          203  Bedford Stuyvesant - Crown Heights   \n",
      "1         UHF34          203  Bedford Stuyvesant - Crown Heights   \n",
      "2         UHF34          204                       East New York   \n",
      "3         UHF34          103                  Fordham - Bronx Pk   \n",
      "4         UHF34          104                Pelham - Throgs Neck   \n",
      "\n",
      "           Time Period  Start_Date  Data Value  Message  \n",
      "0  Annual Average 2011  12/01/2010       25.30      NaN  \n",
      "1  Annual Average 2009  12/01/2008       26.93      NaN  \n",
      "2  Annual Average 2015  01/01/2015       19.09      NaN  \n",
      "3  Annual Average 2015  01/01/2015       19.76      NaN  \n",
      "4  Annual Average 2009  12/01/2008       22.83      NaN  \n",
      "\n",
      "Missing Values:\n",
      "Unique ID             0\n",
      "Indicator ID          0\n",
      "Name                  0\n",
      "Measure               0\n",
      "Measure Info          0\n",
      "Geo Type Name         0\n",
      "Geo Join ID           0\n",
      "Geo Place Name        0\n",
      "Time Period           0\n",
      "Start_Date            0\n",
      "Data Value            0\n",
      "Message           16218\n",
      "dtype: int64\n",
      "\n",
      "Cleaned and Preprocessed Dataset:\n",
      "   Unique ID  Indicator ID                    Name Measure Measure Info  \\\n",
      "0     172653           375  Nitrogen dioxide (NO2)    Mean          ppb   \n",
      "1     172585           375  Nitrogen dioxide (NO2)    Mean          ppb   \n",
      "2     336637           375  Nitrogen dioxide (NO2)    Mean          ppb   \n",
      "3     336622           375  Nitrogen dioxide (NO2)    Mean          ppb   \n",
      "4     172582           375  Nitrogen dioxide (NO2)    Mean          ppb   \n",
      "\n",
      "  Geo Type Name  Geo Join ID                      Geo Place Name  \\\n",
      "0         UHF34          203  Bedford Stuyvesant - Crown Heights   \n",
      "1         UHF34          203  Bedford Stuyvesant - Crown Heights   \n",
      "2         UHF34          204                       East New York   \n",
      "3         UHF34          103                  Fordham - Bronx Pk   \n",
      "4         UHF34          104                Pelham - Throgs Neck   \n",
      "\n",
      "           Time Period Start_Date  Data Value  Message  \n",
      "0  Annual Average 2011 2010-12-01       25.30      NaN  \n",
      "1  Annual Average 2009 2008-12-01       26.93      NaN  \n",
      "2  Annual Average 2015 2015-01-01       19.09      NaN  \n",
      "3  Annual Average 2015 2015-01-01       19.76      NaN  \n",
      "4  Annual Average 2009 2008-12-01       22.83      NaN  \n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "# Load the dataset from the uploaded file in JupyterLab\n",
    "file_path = 'Air_Quality.csv'\n",
    "df = pd.read_csv(file_path)\n",
    "\n",
    "# Display the first few rows of the dataset\n",
    "print(\"Original Dataset:\")\n",
    "print(df.head())\n",
    "\n",
    "# Check for missing values\n",
    "print(\"\\nMissing Values:\")\n",
    "print(df.isnull().sum())\n",
    "\n",
    "# Fill missing values for specific columns\n",
    "columns_to_fill = ['Data Value']  # Add other column names as needed\n",
    "for col in columns_to_fill:\n",
    "    df[col] = df[col].fillna(df[col].mean())\n",
    "\n",
    "# Convert Date column to datetime format\n",
    "df['Start_Date'] = pd.to_datetime(df['Start_Date'], format='%m/%d/%Y')\n",
    "\n",
    "# Display cleaned and preprocessed dataset\n",
    "print(\"\\nCleaned and Preprocessed Dataset:\")\n",
    "print(df.head())\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "a7b3781c-41ab-4473-84ba-5a97996afa6b",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting streamlit\n",
      "  Obtaining dependency information for streamlit from https://files.pythonhosted.org/packages/9b/ea/7219c01b5e92d02d2bc994a36245d99331cd66eb12d284707a2060a013d0/streamlit-1.32.2-py2.py3-none-any.whl.metadata\n",
      "  Downloading streamlit-1.32.2-py2.py3-none-any.whl.metadata (8.5 kB)\n",
      "Requirement already satisfied: pandas in ./anaconda3/lib/python3.11/site-packages (2.0.3)\n",
      "Requirement already satisfied: plotly in ./anaconda3/lib/python3.11/site-packages (5.9.0)\n",
      "Requirement already satisfied: altair<6,>=4.0 in ./anaconda3/lib/python3.11/site-packages (from streamlit) (5.2.0)\n",
      "Collecting blinker<2,>=1.0.0 (from streamlit)\n",
      "  Obtaining dependency information for blinker<2,>=1.0.0 from https://files.pythonhosted.org/packages/fa/2a/7f3714cbc6356a0efec525ce7a0613d581072ed6eb53eb7b9754f33db807/blinker-1.7.0-py3-none-any.whl.metadata\n",
      "  Downloading blinker-1.7.0-py3-none-any.whl.metadata (1.9 kB)\n",
      "Collecting cachetools<6,>=4.0 (from streamlit)\n",
      "  Obtaining dependency information for cachetools<6,>=4.0 from https://files.pythonhosted.org/packages/fb/2b/a64c2d25a37aeb921fddb929111413049fc5f8b9a4c1aefaffaafe768d54/cachetools-5.3.3-py3-none-any.whl.metadata\n",
      "  Downloading cachetools-5.3.3-py3-none-any.whl.metadata (5.3 kB)\n",
      "Requirement already satisfied: click<9,>=7.0 in ./anaconda3/lib/python3.11/site-packages (from streamlit) (8.0.4)\n",
      "Requirement already satisfied: numpy<2,>=1.19.3 in ./anaconda3/lib/python3.11/site-packages (from streamlit) (1.24.3)\n",
      "Requirement already satisfied: packaging<24,>=16.8 in ./anaconda3/lib/python3.11/site-packages (from streamlit) (23.1)\n",
      "Requirement already satisfied: pillow<11,>=7.1.0 in ./anaconda3/lib/python3.11/site-packages (from streamlit) (9.4.0)\n",
      "Collecting protobuf<5,>=3.20 (from streamlit)\n",
      "  Obtaining dependency information for protobuf<5,>=3.20 from https://files.pythonhosted.org/packages/f3/bf/26deba06a4c910a85f78245cac7698f67cedd7efe00d04f6b3e1b3506a59/protobuf-4.25.3-cp37-abi3-macosx_10_9_universal2.whl.metadata\n",
      "  Downloading protobuf-4.25.3-cp37-abi3-macosx_10_9_universal2.whl.metadata (541 bytes)\n",
      "Requirement already satisfied: pyarrow>=7.0 in ./anaconda3/lib/python3.11/site-packages (from streamlit) (11.0.0)\n",
      "Requirement already satisfied: requests<3,>=2.27 in ./anaconda3/lib/python3.11/site-packages (from streamlit) (2.31.0)\n",
      "Collecting rich<14,>=10.14.0 (from streamlit)\n",
      "  Obtaining dependency information for rich<14,>=10.14.0 from https://files.pythonhosted.org/packages/87/67/a37f6214d0e9fe57f6ae54b2956d550ca8365857f42a1ce0392bb21d9410/rich-13.7.1-py3-none-any.whl.metadata\n",
      "  Downloading rich-13.7.1-py3-none-any.whl.metadata (18 kB)\n",
      "Requirement already satisfied: tenacity<9,>=8.1.0 in ./anaconda3/lib/python3.11/site-packages (from streamlit) (8.2.2)\n",
      "Requirement already satisfied: toml<2,>=0.10.1 in ./anaconda3/lib/python3.11/site-packages (from streamlit) (0.10.2)\n",
      "Requirement already satisfied: typing-extensions<5,>=4.3.0 in ./anaconda3/lib/python3.11/site-packages (from streamlit) (4.7.1)\n",
      "Collecting gitpython!=3.1.19,<4,>=3.0.7 (from streamlit)\n",
      "  Obtaining dependency information for gitpython!=3.1.19,<4,>=3.0.7 from https://files.pythonhosted.org/packages/e9/bd/cc3a402a6439c15c3d4294333e13042b915bbeab54edc457c723931fed3f/GitPython-3.1.43-py3-none-any.whl.metadata\n",
      "  Downloading GitPython-3.1.43-py3-none-any.whl.metadata (13 kB)\n",
      "Collecting pydeck<1,>=0.8.0b4 (from streamlit)\n",
      "  Obtaining dependency information for pydeck<1,>=0.8.0b4 from https://files.pythonhosted.org/packages/10/4b/2fc80540e2d3903452245bb657c7f758ec7342420507d1e4091b0161856e/pydeck-0.8.1b0-py2.py3-none-any.whl.metadata\n",
      "  Downloading pydeck-0.8.1b0-py2.py3-none-any.whl.metadata (3.9 kB)\n",
      "Requirement already satisfied: tornado<7,>=6.0.3 in ./anaconda3/lib/python3.11/site-packages (from streamlit) (6.3.2)\n",
      "Requirement already satisfied: python-dateutil>=2.8.2 in ./anaconda3/lib/python3.11/site-packages (from pandas) (2.8.2)\n",
      "Requirement already satisfied: pytz>=2020.1 in ./anaconda3/lib/python3.11/site-packages (from pandas) (2023.3.post1)\n",
      "Requirement already satisfied: tzdata>=2022.1 in ./anaconda3/lib/python3.11/site-packages (from pandas) (2023.3)\n",
      "Requirement already satisfied: jinja2 in ./anaconda3/lib/python3.11/site-packages (from altair<6,>=4.0->streamlit) (3.1.2)\n",
      "Requirement already satisfied: jsonschema>=3.0 in ./anaconda3/lib/python3.11/site-packages (from altair<6,>=4.0->streamlit) (4.17.3)\n",
      "Requirement already satisfied: toolz in ./anaconda3/lib/python3.11/site-packages (from altair<6,>=4.0->streamlit) (0.12.0)\n",
      "Collecting gitdb<5,>=4.0.1 (from gitpython!=3.1.19,<4,>=3.0.7->streamlit)\n",
      "  Obtaining dependency information for gitdb<5,>=4.0.1 from https://files.pythonhosted.org/packages/fd/5b/8f0c4a5bb9fd491c277c21eff7ccae71b47d43c4446c9d0c6cff2fe8c2c4/gitdb-4.0.11-py3-none-any.whl.metadata\n",
      "  Downloading gitdb-4.0.11-py3-none-any.whl.metadata (1.2 kB)\n",
      "Requirement already satisfied: six>=1.5 in ./anaconda3/lib/python3.11/site-packages (from python-dateutil>=2.8.2->pandas) (1.16.0)\n",
      "Requirement already satisfied: charset-normalizer<4,>=2 in ./anaconda3/lib/python3.11/site-packages (from requests<3,>=2.27->streamlit) (2.0.4)\n",
      "Requirement already satisfied: idna<4,>=2.5 in ./anaconda3/lib/python3.11/site-packages (from requests<3,>=2.27->streamlit) (3.4)\n",
      "Requirement already satisfied: urllib3<3,>=1.21.1 in ./anaconda3/lib/python3.11/site-packages (from requests<3,>=2.27->streamlit) (1.26.16)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in ./anaconda3/lib/python3.11/site-packages (from requests<3,>=2.27->streamlit) (2023.7.22)\n",
      "Requirement already satisfied: markdown-it-py>=2.2.0 in ./anaconda3/lib/python3.11/site-packages (from rich<14,>=10.14.0->streamlit) (2.2.0)\n",
      "Requirement already satisfied: pygments<3.0.0,>=2.13.0 in ./anaconda3/lib/python3.11/site-packages (from rich<14,>=10.14.0->streamlit) (2.15.1)\n",
      "Collecting smmap<6,>=3.0.1 (from gitdb<5,>=4.0.1->gitpython!=3.1.19,<4,>=3.0.7->streamlit)\n",
      "  Obtaining dependency information for smmap<6,>=3.0.1 from https://files.pythonhosted.org/packages/a7/a5/10f97f73544edcdef54409f1d839f6049a0d79df68adbc1ceb24d1aaca42/smmap-5.0.1-py3-none-any.whl.metadata\n",
      "  Downloading smmap-5.0.1-py3-none-any.whl.metadata (4.3 kB)\n",
      "Requirement already satisfied: MarkupSafe>=2.0 in ./anaconda3/lib/python3.11/site-packages (from jinja2->altair<6,>=4.0->streamlit) (2.1.1)\n",
      "Requirement already satisfied: attrs>=17.4.0 in ./anaconda3/lib/python3.11/site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (22.1.0)\n",
      "Requirement already satisfied: pyrsistent!=0.17.0,!=0.17.1,!=0.17.2,>=0.14.0 in ./anaconda3/lib/python3.11/site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.18.0)\n",
      "Requirement already satisfied: mdurl~=0.1 in ./anaconda3/lib/python3.11/site-packages (from markdown-it-py>=2.2.0->rich<14,>=10.14.0->streamlit) (0.1.0)\n",
      "Downloading streamlit-1.32.2-py2.py3-none-any.whl (8.1 MB)\n",
      "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m8.1/8.1 MB\u001b[0m \u001b[31m19.8 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m00:01\u001b[0m00:01\u001b[0m\n",
      "\u001b[?25hDownloading blinker-1.7.0-py3-none-any.whl (13 kB)\n",
      "Downloading cachetools-5.3.3-py3-none-any.whl (9.3 kB)\n",
      "Downloading GitPython-3.1.43-py3-none-any.whl (207 kB)\n",
      "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m207.3/207.3 kB\u001b[0m \u001b[31m15.5 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
      "\u001b[?25hDownloading protobuf-4.25.3-cp37-abi3-macosx_10_9_universal2.whl (394 kB)\n",
      "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m394.2/394.2 kB\u001b[0m \u001b[31m18.2 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
      "\u001b[?25hDownloading pydeck-0.8.1b0-py2.py3-none-any.whl (4.8 MB)\n",
      "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m4.8/4.8 MB\u001b[0m \u001b[31m42.1 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0ma \u001b[36m0:00:01\u001b[0m\n",
      "\u001b[?25hDownloading rich-13.7.1-py3-none-any.whl (240 kB)\n",
      "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m240.7/240.7 kB\u001b[0m \u001b[31m19.2 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
      "\u001b[?25hDownloading gitdb-4.0.11-py3-none-any.whl (62 kB)\n",
      "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m62.7/62.7 kB\u001b[0m \u001b[31m6.3 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
      "\u001b[?25hDownloading smmap-5.0.1-py3-none-any.whl (24 kB)\n",
      "Installing collected packages: smmap, protobuf, cachetools, blinker, rich, pydeck, gitdb, gitpython, streamlit\n",
      "Successfully installed blinker-1.7.0 cachetools-5.3.3 gitdb-4.0.11 gitpython-3.1.43 protobuf-4.25.3 pydeck-0.8.1b0 rich-13.7.1 smmap-5.0.1 streamlit-1.32.2\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install streamlit pandas plotly"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "dd31e496-115a-49a5-a4fb-22f3bbc439b3",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "DeltaGenerator()"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import streamlit as st\n",
    "import pandas as pd\n",
    "import plotly.express as px\n",
    "\n",
    "# Define a function to load the data\n",
    "def load_data():\n",
    "    file_path = 'Air_Quality.csv'\n",
    "    df = pd.read_csv(file_path)\n",
    "    return df\n",
    "\n",
    "# Load the dataset\n",
    "df = load_data()\n",
    "\n",
    "# Title and description\n",
    "st.title('Air Quality Dashboard')\n",
    "st.write('Explore air quality data and key insights.')\n",
    "\n",
    "# Sidebar for user input\n",
    "st.sidebar.header('Filters')\n",
    "selected_measure = st.sidebar.selectbox('Select Measure', df['Measure'].unique())\n",
    "selected_geo_type = st.sidebar.selectbox('Select Geo Type', df['Geo Type Name'].unique())\n",
    "\n",
    "# Filter the data based on user input\n",
    "filtered_df = df[(df['Measure'] == selected_measure) & (df['Geo Type Name'] == selected_geo_type)]\n",
    "\n",
    "# Display filtered data\n",
    "st.write(f\"Showing data for {selected_measure} in {selected_geo_type}:\")\n",
    "st.write(filtered_df.head())\n",
    "\n",
    "# Data visualization\n",
    "st.header('Data Visualizations')\n",
    "\n",
    "# Line chart\n",
    "line_chart = px.line(filtered_df, x='Start_Date', y='Data Value', color='Geo Place Name',\n",
    "                     title=f'{selected_measure} Over Time')\n",
    "st.plotly_chart(line_chart)\n",
    "\n",
    "# Bar chart\n",
    "bar_chart = px.bar(filtered_df, x='Geo Place Name', y='Data Value', color='Geo Place Name',\n",
    "                    title=f'{selected_measure} by Location')\n",
    "st.plotly_chart(bar_chart)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "1d34611d-c05a-41b1-9f38-65bfffcfbd9d",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[Errno 2] No such file or directory: 'path/to/directory'\n",
      "/Users/harshbhardwaj\n"
     ]
    }
   ],
   "source": [
    "cd path/to/directory"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
