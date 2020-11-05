{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Introduction\n",
    "\n",
    "In this project, you will act as a data visualization developer at Yahoo Finance! You will be helping the \"Netflix Stock Profile\" team visualize the Netflix stock data. In finance, a _stock profile_ is a series of studies, visualizations, and analyses that dive into different aspects a publicly traded company's data. \n",
    "\n",
    "For the purposes of the project, you will only visualize data for the year of 2017. Specifically, you will be in charge of creating the following visualizations:\n",
    "+ The distribution of the stock prices for the past year\n",
    "+ Netflix's earnings and revenue in the last four quarters\n",
    "+ The actual vs. estimated earnings per share for the four quarters in 2017\n",
    "+ A comparison of the Netflix Stock price vs the Dow Jones Industrial Average price in 2017 \n",
    "\n",
    "Note: We are using the Dow Jones Industrial Average to compare the Netflix stock to the larter stock market. Learn more about why the Dow Jones Industrial Average is a general reflection of the larger stock market [here](https://www.investopedia.com/terms/d/djia.asp).\n",
    "\n",
    "During this project, you will analyze, prepare, and plot data. Your visualizations will help the financial analysts asses the risk of the Netflix stock.\n",
    "\n",
    "After you complete your visualizations, you'll be creating a presentation to share the images with the rest of the Netflix Stock Profile team. Your slides should include:\n",
    "\n",
    "- A title slide\n",
    "- A list of your visualizations and your role in their creation for the \"Stock Profile\" team\n",
    "- A visualization of the distribution of the stock prices for Netflix in 2017\n",
    "- A visualization and a summary of Netflix stock and revenue for the past four quarters and a summary\n",
    "- A visualization and a brief summary of their earned versus actual earnings per share\n",
    "- A visualization of Netflix stock against the Dow Jones stock (to get a sense of the market) in 2017\n",
    "\n",
    "Financial Data Source: [Yahoo Finance](https://finance.yahoo.com/quote/DATA/)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 1\n",
    "\n",
    "Let's get our notebook ready for visualizing! Import the modules that you'll be using in this project:\n",
    "- `from matplotlib import pyplot as plt`\n",
    "- `import pandas as pd`\n",
    "- `import seaborn as sns`"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [],
   "source": [
    "from matplotlib import pyplot as plt\n",
    "import pandas as pd\n",
    "import seaborn as sns\n",
    "import numpy as np"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 2"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Let's load the datasets and inspect them."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Load **NFLX.csv** into a DataFrame called `netflix_stocks`. Then, quickly inspect the DataFrame using `print()`.\n",
    "\n",
    "Hint: Use the `pd.read_csv()`function).\n",
    "\n",
    "Note: In the Yahoo Data, `Adj Close` represents the adjusted close price adjusted for both dividends and splits. This means this is the true closing stock price for a given business day."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "          Date        Open        High         Low       Close   Adj Close  \\\n",
      "0   2017-01-01  124.959999  143.460007  124.309998  140.710007  140.710007   \n",
      "1   2017-02-01  141.199997  145.949997  139.050003  142.130005  142.130005   \n",
      "2   2017-03-01  142.839996  148.289993  138.259995  147.809998  147.809998   \n",
      "3   2017-04-01  146.699997  153.520004  138.660004  152.199997  152.199997   \n",
      "4   2017-05-01  151.910004  164.750000  151.610001  163.070007  163.070007   \n",
      "5   2017-06-01  163.520004  166.869995  147.300003  149.410004  149.410004   \n",
      "6   2017-07-01  149.800003  191.500000  144.250000  181.660004  181.660004   \n",
      "7   2017-08-01  182.490005  184.619995  164.229996  174.710007  174.710007   \n",
      "8   2017-09-01  175.550003  189.949997  172.440002  181.350006  181.350006   \n",
      "9   2017-10-01  182.110001  204.380005  176.580002  196.429993  196.429993   \n",
      "10  2017-11-01  197.240005  202.479996  184.320007  195.509995  195.509995   \n",
      "11  2017-12-01  186.990005  194.490005  178.380005  191.960007  191.960007   \n",
      "\n",
      "       Volume Month  \n",
      "0   181772200   Jan  \n",
      "1    91432000   Feb  \n",
      "2   110692700   Mar  \n",
      "3   149769200   Apr  \n",
      "4   116795800   May  \n",
      "5   135675800   Jun  \n",
      "6   185144700   Jul  \n",
      "7   136523100   Aug  \n",
      "8   111427900   Sep  \n",
      "9   208657800   Oct  \n",
      "10  161719700   Nov  \n",
      "11  115103700   Dec  \n"
     ]
    }
   ],
   "source": [
    "netflix_stocks = pd.read_csv('NFLX.csv')\n",
    "netflix_stocks['Month'] = 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'\n",
    "print(netflix_stocks)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Load **DJI.csv** into a DataFrame called `dowjones_stocks`. Then, quickly inspect the DataFrame using `print()`.\n",
    "\n",
    "Note: You can learn more about why the Dow Jones Industrial Average is a industry reflection of the larger stock market [here](https://www.investopedia.com/terms/d/djia.asp). \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "          Date          Open          High           Low         Close  \\\n",
      "0   2017-01-01  19872.859375  20125.580078  19677.939453  19864.089844   \n",
      "1   2017-02-01  19923.810547  20851.330078  19831.089844  20812.240234   \n",
      "2   2017-03-01  20957.289063  21169.109375  20412.800781  20663.220703   \n",
      "3   2017-04-01  20665.169922  21070.900391  20379.550781  20940.509766   \n",
      "4   2017-05-01  20962.730469  21112.320313  20553.449219  21008.650391   \n",
      "5   2017-06-01  21030.550781  21535.029297  20994.220703  21349.630859   \n",
      "6   2017-07-01  21392.300781  21929.800781  21279.300781  21891.119141   \n",
      "7   2017-08-01  21961.419922  22179.109375  21600.339844  21948.099609   \n",
      "8   2017-09-01  21981.769531  22419.509766  21709.630859  22405.089844   \n",
      "9   2017-10-01  22423.470703  23485.250000  22416.000000  23377.240234   \n",
      "10  2017-11-01  23442.900391  24327.820313  23242.750000  24272.349609   \n",
      "11  2017-12-01  24305.400391  24876.070313  23921.900391  24719.220703   \n",
      "\n",
      "       Adj Close      Volume Month  \n",
      "0   19864.089844  6482450000   Jan  \n",
      "1   20812.240234  6185580000   Feb  \n",
      "2   20663.220703  6941970000   Mar  \n",
      "3   20940.509766  5392630000   Apr  \n",
      "4   21008.650391  6613570000   May  \n",
      "5   21349.630859  7214590000   Jun  \n",
      "6   21891.119141  5569720000   Jul  \n",
      "7   21948.099609  6150060000   Aug  \n",
      "8   22405.089844  6342130000   Sep  \n",
      "9   23377.240234  7302910000   Oct  \n",
      "10  24272.349609  7335640000   Nov  \n",
      "11  24719.220703  6589890000   Dec  \n"
     ]
    }
   ],
   "source": [
    "dowjones_stocks = pd.read_csv('DJI.csv')\n",
    "dowjones_stocks['Month'] = 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'\n",
    "print(dowjones_stocks)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Load **NFLX_daily_by_quarter.csv** into a DataFrame called `netflix_stocks_quarterly`. Then, quickly inspect the DataFrame using `print()`.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "           Date        Open        High         Low       Close   Adj Close  \\\n",
      "0    2017-01-03  124.959999  128.190002  124.309998  127.489998  127.489998   \n",
      "1    2017-01-04  127.489998  130.169998  126.550003  129.410004  129.410004   \n",
      "2    2017-01-05  129.220001  132.750000  128.899994  131.809998  131.809998   \n",
      "3    2017-01-06  132.080002  133.880005  129.809998  131.070007  131.070007   \n",
      "4    2017-01-09  131.479996  131.990005  129.889999  130.949997  130.949997   \n",
      "..          ...         ...         ...         ...         ...         ...   \n",
      "246  2017-12-22  188.330002  190.949997  186.800003  189.940002  189.940002   \n",
      "247  2017-12-26  189.779999  189.940002  186.399994  187.759995  187.759995   \n",
      "248  2017-12-27  187.800003  188.100006  185.220001  186.240005  186.240005   \n",
      "249  2017-12-28  187.179993  194.490005  186.850006  192.710007  192.710007   \n",
      "250  2017-12-29  192.509995  193.949997  191.220001  191.960007  191.960007   \n",
      "\n",
      "       Volume Quarter  \n",
      "0     9437900      Q1  \n",
      "1     7843600      Q1  \n",
      "2    10185500      Q1  \n",
      "3    10657900      Q1  \n",
      "4     5766900      Q1  \n",
      "..        ...     ...  \n",
      "246   3878900      Q4  \n",
      "247   3045700      Q4  \n",
      "248   4002100      Q4  \n",
      "249  10107400      Q4  \n",
      "250   5187600      Q4  \n",
      "\n",
      "[251 rows x 8 columns]\n"
     ]
    }
   ],
   "source": [
    "netflix_stocks_quarterly = pd.read_csv('NFLX_daily_by_quarter.csv')\n",
    "print(netflix_stocks_quarterly)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 3"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Let's learn more about our data. The datasets are large and it may be easier to view the entire dataset locally on your computer. Open the CSV files directly from the folder you downloaded for this project.\n",
    " - `NFLX` is the stock ticker symbol for Netflix and `^DJI` is the stock ticker symbol for the Dow Jones industrial Average, which is why the CSV files are named accordingly\n",
    " - In the Yahoo Data, `Adj Close` is documented as adjusted close price adjusted for both dividends and splits.\n",
    " - You can learn more about why the Dow Jones Industrial Average is a industry reflection of the larger stock market [here](https://www.investopedia.com/terms/d/djia.asp). \n",
    " \n",
    "Answer the following questions by inspecting the data in the **NFLX.csv**,**DJI.csv**, and **NFLX_daily_by_quarter.csv** in your computer."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "What year is represented in the data? Look out for the latest and earliest date."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# In the respective files stock data from January 2017 through December 2017 are presented."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "+ Is the data represented by days, weeks, or months? \n",
    "+ In which ways are the files different? \n",
    "+ What's different about the columns for `netflix_stocks` versus `netflix_stocks_quarterly`?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Data in NFLX.csv and DJI.csv is presented on a monthly,  while data in NFLX_daily by quarter.csv is listed \n",
    "# on a daily basis.\n",
    "# Data in NFLX.csv and DJI.csv is equally structured. NFLX_daily_by_quarter.csv adds a column indicating the \n",
    "# quarter the data has been taken from."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 4\n",
    "\n",
    "Great! Now that we have spent sometime looking at the data, let's look at the column names of the DataFrame `netflix_stocks` using `.head()`. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Date</th>\n",
       "      <th>Open</th>\n",
       "      <th>High</th>\n",
       "      <th>Low</th>\n",
       "      <th>Close</th>\n",
       "      <th>Adj Close</th>\n",
       "      <th>Volume</th>\n",
       "      <th>Month</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2017-01-01</td>\n",
       "      <td>124.959999</td>\n",
       "      <td>143.460007</td>\n",
       "      <td>124.309998</td>\n",
       "      <td>140.710007</td>\n",
       "      <td>140.710007</td>\n",
       "      <td>181772200</td>\n",
       "      <td>Jan</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2017-02-01</td>\n",
       "      <td>141.199997</td>\n",
       "      <td>145.949997</td>\n",
       "      <td>139.050003</td>\n",
       "      <td>142.130005</td>\n",
       "      <td>142.130005</td>\n",
       "      <td>91432000</td>\n",
       "      <td>Feb</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2017-03-01</td>\n",
       "      <td>142.839996</td>\n",
       "      <td>148.289993</td>\n",
       "      <td>138.259995</td>\n",
       "      <td>147.809998</td>\n",
       "      <td>147.809998</td>\n",
       "      <td>110692700</td>\n",
       "      <td>Mar</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2017-04-01</td>\n",
       "      <td>146.699997</td>\n",
       "      <td>153.520004</td>\n",
       "      <td>138.660004</td>\n",
       "      <td>152.199997</td>\n",
       "      <td>152.199997</td>\n",
       "      <td>149769200</td>\n",
       "      <td>Apr</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2017-05-01</td>\n",
       "      <td>151.910004</td>\n",
       "      <td>164.750000</td>\n",
       "      <td>151.610001</td>\n",
       "      <td>163.070007</td>\n",
       "      <td>163.070007</td>\n",
       "      <td>116795800</td>\n",
       "      <td>May</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "         Date        Open        High         Low       Close   Adj Close  \\\n",
       "0  2017-01-01  124.959999  143.460007  124.309998  140.710007  140.710007   \n",
       "1  2017-02-01  141.199997  145.949997  139.050003  142.130005  142.130005   \n",
       "2  2017-03-01  142.839996  148.289993  138.259995  147.809998  147.809998   \n",
       "3  2017-04-01  146.699997  153.520004  138.660004  152.199997  152.199997   \n",
       "4  2017-05-01  151.910004  164.750000  151.610001  163.070007  163.070007   \n",
       "\n",
       "      Volume Month  \n",
       "0  181772200   Jan  \n",
       "1   91432000   Feb  \n",
       "2  110692700   Mar  \n",
       "3  149769200   Apr  \n",
       "4  116795800   May  "
      ]
     },
     "execution_count": 44,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "netflix_stocks.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "What do you notice? The first two column names are one word each, and the only one that is not is `Adj Close`! \n",
    "\n",
    "The term `Adj Close` is a confusing term if you don't read the Yahoo Documentation. In Yahoo, `Adj Close` is documented as adjusted close price adjusted for both dividends and splits.\n",
    "\n",
    "This means this is the column with the true closing price, so these data are very important.\n",
    "\n",
    "Use Pandas to change the name of of the column to `Adj Close` to `Price` so that it is easier to work with the data. Remember to use `inplace=True`.\n",
    "\n",
    "Do this for the Dow Jones and Netflix Quarterly pandas dataframes as well.\n",
    "Hint: Use [`.rename()`](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.rename.html)).\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {},
   "outputs": [],
   "source": [
    "netflix_stocks.rename(columns={'Adj Close':'Price'}, inplace=True)\n",
    "netflix_stocks_quarterly.rename(columns={'Adj Close':'Price'}, inplace=True)\n",
    "dowjones_stocks.rename(columns={'Adj Close':'Price'}, inplace=True)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Run `netflix_stocks.head()` again to check your column name has changed."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Date</th>\n",
       "      <th>Open</th>\n",
       "      <th>High</th>\n",
       "      <th>Low</th>\n",
       "      <th>Close</th>\n",
       "      <th>Price</th>\n",
       "      <th>Volume</th>\n",
       "      <th>Month</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2017-01-01</td>\n",
       "      <td>19872.859375</td>\n",
       "      <td>20125.580078</td>\n",
       "      <td>19677.939453</td>\n",
       "      <td>19864.089844</td>\n",
       "      <td>19864.089844</td>\n",
       "      <td>6482450000</td>\n",
       "      <td>Jan</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2017-02-01</td>\n",
       "      <td>19923.810547</td>\n",
       "      <td>20851.330078</td>\n",
       "      <td>19831.089844</td>\n",
       "      <td>20812.240234</td>\n",
       "      <td>20812.240234</td>\n",
       "      <td>6185580000</td>\n",
       "      <td>Feb</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2017-03-01</td>\n",
       "      <td>20957.289063</td>\n",
       "      <td>21169.109375</td>\n",
       "      <td>20412.800781</td>\n",
       "      <td>20663.220703</td>\n",
       "      <td>20663.220703</td>\n",
       "      <td>6941970000</td>\n",
       "      <td>Mar</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2017-04-01</td>\n",
       "      <td>20665.169922</td>\n",
       "      <td>21070.900391</td>\n",
       "      <td>20379.550781</td>\n",
       "      <td>20940.509766</td>\n",
       "      <td>20940.509766</td>\n",
       "      <td>5392630000</td>\n",
       "      <td>Apr</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2017-05-01</td>\n",
       "      <td>20962.730469</td>\n",
       "      <td>21112.320313</td>\n",
       "      <td>20553.449219</td>\n",
       "      <td>21008.650391</td>\n",
       "      <td>21008.650391</td>\n",
       "      <td>6613570000</td>\n",
       "      <td>May</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "         Date          Open          High           Low         Close  \\\n",
       "0  2017-01-01  19872.859375  20125.580078  19677.939453  19864.089844   \n",
       "1  2017-02-01  19923.810547  20851.330078  19831.089844  20812.240234   \n",
       "2  2017-03-01  20957.289063  21169.109375  20412.800781  20663.220703   \n",
       "3  2017-04-01  20665.169922  21070.900391  20379.550781  20940.509766   \n",
       "4  2017-05-01  20962.730469  21112.320313  20553.449219  21008.650391   \n",
       "\n",
       "          Price      Volume Month  \n",
       "0  19864.089844  6482450000   Jan  \n",
       "1  20812.240234  6185580000   Feb  \n",
       "2  20663.220703  6941970000   Mar  \n",
       "3  20940.509766  5392630000   Apr  \n",
       "4  21008.650391  6613570000   May  "
      ]
     },
     "execution_count": 46,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dowjones_stocks.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Call `.head()` on the DataFrame `dowjones_stocks` and `netflix_stocks_quarterly`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {
    "scrolled": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "         Date          Open          High           Low         Close  \\\n",
      "0  2017-01-01  19872.859375  20125.580078  19677.939453  19864.089844   \n",
      "1  2017-02-01  19923.810547  20851.330078  19831.089844  20812.240234   \n",
      "2  2017-03-01  20957.289063  21169.109375  20412.800781  20663.220703   \n",
      "3  2017-04-01  20665.169922  21070.900391  20379.550781  20940.509766   \n",
      "4  2017-05-01  20962.730469  21112.320313  20553.449219  21008.650391   \n",
      "\n",
      "          Price      Volume Month  \n",
      "0  19864.089844  6482450000   Jan  \n",
      "1  20812.240234  6185580000   Feb  \n",
      "2  20663.220703  6941970000   Mar  \n",
      "3  20940.509766  5392630000   Apr  \n",
      "4  21008.650391  6613570000   May  \n",
      "         Date        Open        High         Low       Close       Price  \\\n",
      "0  2017-01-03  124.959999  128.190002  124.309998  127.489998  127.489998   \n",
      "1  2017-01-04  127.489998  130.169998  126.550003  129.410004  129.410004   \n",
      "2  2017-01-05  129.220001  132.750000  128.899994  131.809998  131.809998   \n",
      "3  2017-01-06  132.080002  133.880005  129.809998  131.070007  131.070007   \n",
      "4  2017-01-09  131.479996  131.990005  129.889999  130.949997  130.949997   \n",
      "\n",
      "     Volume Quarter  \n",
      "0   9437900      Q1  \n",
      "1   7843600      Q1  \n",
      "2  10185500      Q1  \n",
      "3  10657900      Q1  \n",
      "4   5766900      Q1  \n"
     ]
    }
   ],
   "source": [
    "print(dowjones_stocks.head())\n",
    "print(netflix_stocks_quarterly.head())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 5\n",
    "\n",
    "In this step, we will be visualizing the Netflix quarterly data! \n",
    "\n",
    "We want to get an understanding of the distribution of the Netflix quarterly stock prices for 2017. Specifically, we want to see in which quarter stock prices flucutated the most. We can accomplish this using a violin plot with four violins, one for each business quarter!\n",
    "\n",
    "\n",
    "1. Start by creating a variable `ax` and setting it equal to `sns.violinplot()`. This will instantiate a figure and give us access to the axes through the variable name `ax`.\n",
    "2. Use `sns.violinplot()` and pass in the following arguments:\n",
    "+ The `Quarter` column as the `x` values\n",
    "+ The `Price` column as your `y` values\n",
    "+ The `netflix_stocks_quarterly` dataframe as your `data`\n",
    "3. Improve the readability of the chart by adding a title of the plot. Add `\"Distribution of 2017 Netflix Stock Prices by Quarter\"` by using `ax.set_title()`\n",
    "4. Change your `ylabel` to \"Closing Stock Price\"\n",
    "5. Change your `xlabel` to \"Business Quarters in 2017\"\n",
    "6. Be sure to show your plot!\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAfYAAAFfCAYAAAC8+O6aAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjMuMSwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/d3fzzAAAACXBIWXMAAAsTAAALEwEAmpwYAAB6z0lEQVR4nO3dd3hTdRfA8e9NuhdtaSkUWjZlQxkFEUFAtigvggPZwwHIUhQZspGloCxlCbKnTAVZggtkLymj7D1aKF1pm9z3j9JI6SAtGR3n8zw8JLk3956M5tzfVlRVVRFCCCFErqCxdQBCCCGEMB9J7EIIIUQuIoldCCGEyEUksQshhBC5iCR2IYQQIheRxJ4L2XKggwyyyHmy82eWnWMT2Y98X5JIYreBjh07EhQUZPxXvnx5atWqRY8ePfj7779T7Ltu3TqCgoIIDw836dgHDx6kb9++z9wvKCiI+fPnAzB9+nSCg4Mz/0Kecu7cOTp37my8v3//foKCgjhx4sRzH9scvvzyS2rUqEG1atU4dOhQmvscPnyYjh07UqNGDerWrcunn37KvXv3Uuxz8OBB2rVrR5UqVWjSpAlr1qxJ95ynTp2ifPnyKT6/5PclvX/Xr19P81jJ34WZM2emuf31119n8ODBz3obUli1ahXTpk1L8djT71NQUBBbt24FzPNdiYqK4quvvqJJkyZUrFiRWrVq0bNnT/bt25diP1O/y5mRlfif/nsNCgqiSpUqvPbaayxZsuSZz2/YsCGjR4/Oashm8eTfu7mFhYUxbNgwGjZsSOXKlWnYsCHDhw/n4sWLFjlfenbs2MGIESOses7sys7WAeRV1apV47PPPgMgMTGRO3fusGLFCrp27cqUKVN49dVXAXj55ZdZuXIlHh4eJh13zZo1Jv1BrVy5En9//6y/gDRs3bo1RRKvUKECK1eupGTJkmY9T1acOXOGhQsX0rlzZxo3bky5cuVS7RMWFkaXLl2oU6cOX331FZGRkXzzzTd0796dNWvWYG9vT1hYGD169KBBgwZ89NFH/PnnnwwdOhQ3NzeaNWuW4ngXLlzggw8+QK/Xp3g8+X15kk6no2/fvlSoUIFChQpl+Fq+++47mjdvTokSJbL4bqQ81ssvv2y8//T79PT3rl27dtSvXz/L51NVlR49enDnzh3ef/99ihUrRmRkJGvXrqVr167MmjWLBg0aAKZ/l63hyb9XgJiYGNatW8eYMWMA6NChQ7rPnTFjhsl/vznNzp07+fjjjylZsiQfffQRhQsX5sqVKyxevJg2bdowderUFN8vS1q0aBEuLi5WOVd2J4ndRjw8PKhatWqKx5o1a0bnzp0ZOXIkL730Evny5cPb2xtvb2+zn//pc1uCm5ubVc5jiocPHwLw6quvUrly5TT3WbJkCb6+vkyfPh17e3sAihYtSrt27fjrr7+oX78+c+bMoXDhwnz99dcoikK9evUIDw9n5syZxsRuMBhYu3YtEydORKNJXSmW1vsybtw4FEVhypQpaT7nSY6OjgwfPpwlS5agKEpm34oMPf0+Xbt2LcX2ggULUrBgwSwf/8CBAxw5coRVq1ZRpUoV4+ONGjXirbfeYubMmcbEnp2k9fdau3ZtTp48yZIlSzJM7OXLl7dwdLZx8+ZNPv30U1544QWmT5+OnV1SOgkJCeG1117jgw8+4JNPPmHz5s3P9Z0RmSdV8dmIRqOhV69ePHr0yFj1+XRV/IULF+jRo4exqrR79+6EhoYCMHjwYH766SfOnTtHUFAQ+/fvZ926ddSqVYt58+ZRq1YtmjZtSmxsbJpVc+vXr6dBgwZUqVKF999/n8uXLxu3DR482FiLkGzHjh0EBQVx7do1pk+fzowZM4iJiSEoKIh169alWRW/fft23njjDapWrUr9+vWZNm0aCQkJxu0NGzZk7ty5jBgxgpCQEGNJKSoqKsP3LjQ0lB49ehASEkJISAiDBg0yVqFPnz6djh07AkklzuTbTytVqhTdunUzJnXAWCpOTnB//fUXL7/8coqE+sorr3D27Flu374NJJV6x4wZQ4cOHfjkk08yjBvg/PnzLF26lP79+5t0Effxxx9z8ODBVKX+tPz444/GKu+WLVvy888/G7c1bNiQ69evs3TpUoKCgkx6n56syv7ll18ICgpi+fLlxu1btmxJUXX/tPv37wNJFz9P0mg0DBgwgDZt2gBpf5ch6XPo168fderUITg4mA8//JBLly6lOFbyd6FatWrUqVOHzz//nAcPHqQZz7FjxwgODmbIkCGZbp/VaDSULVuWGzduAP81saxYsYK6detSv359rl27lqoq/vr16/Tr14+QkBBq1arFRx99ZDxG8nv06aefEhISQnBwMB988AFXr141btfr9UyaNImXX36ZihUr0qJFixSfQXoiIiLo1auXsbp84cKFxm0fffRRqr9vgKZNmzJx4sQ0j7d06VJ0Oh2jRo0yJvVkDg4OjBo1iqioKGNzRXpNczVq1GD69OnG+8ePH6dnz57UqFGDihUr0rRpU1asWGHcntZvWtu2bfnnn3/47bffjL9JAJcvX6ZXr14EBwdTo0YNBg0alKJZbPDgwfTq1YuPP/6YatWqMWDAgGe+jzmBJPZsJiQkBK1Wy5EjR9Lc3rt3b/R6PVOnTmXq1KlERETw/vvvo9fr6dWrF/Xr1ycgIICVK1dSoUIFAB49esS6deuYMmUKAwYMwNnZOdVxY2NjmTJlCn379mXSpElcunSJbt26pUi6GWnXrh1t27bFycmJlStXpln9tnLlSvr06UOlSpWYMWMGHTp0YMGCBXz++ecp9vv++++JjIzk66+/pn///mzZsoXZs2ene+7Tp0/z1ltvkZCQwIQJExgyZAgHDx6kQ4cOxMTE0K5dO7744gsgqf04vXa4d999l3fffTfFY7t27QKSEnxMTAx37tyhaNGiKfYJCAgAMCaYQoUKsX37dvr375/qBy8tU6dOpVixYrz55pvP3BeSfmwbNmzIlClTjBcTaZkxYwYTJ06kRYsWfPfdd9SpU4eBAwfyyy+/GLf7+vrStGlTVq5cafL7lKx58+Y0btyYadOmER4eTnh4OGPHjqVly5apmiWS1axZExcXF/r06cP06dM5duwYiYmJANSpU4f27dsDpPldvnXrFu3atePy5cuMGDGCL7/8kmvXrtG+fXvj+3D9+nXat29PVFQUkyZNYtiwYfz55598/PHHqWIJCwvjvffeo379+owdOzZLtR+XL1+mSJEiKR6bNWsWo0ePZsCAAam2RUVF0b59e86cOWN8DRcuXKBnz57o9Xri4uLo1KkThw4dYtiwYUyaNIl79+7RoUMHY23K/PnzWbt2Lf3792f+/Pm89NJLjBw5kt9//z3DWBcsWICbmxszZ86kadOmfPnll6xevRpI6p9x7tw5zpw5Y9z/+PHjXLp0iddffz3N4/32229UrFiRAgUKpLk9ICCA8uXL89tvv2UY15Nu3LhBp06dcHFx4ZtvvmHmzJkUL16cESNGGAswkPo3bcKECZQvX55q1aqxcuVKChQowL1792jfvj03btxg0qRJjBo1iqNHj9K9e3fi4+ONx9qzZw86nY6ZM2fy1ltvmRxrdiZV8dmMVqvF09MzVYctgPDwcC5cuEDv3r156aWXgKQksnnzZmJiYggMDMTb25sbN26kqDbU6/X07dvX+Jy0qKrK5MmTeeGFF4CkRNaqVSu2bNlC69atnxl3chWtRqNJs/rdYDAwbdo0WrZsyciRIwGoW7cu7u7ujBgxgh49elC2bFnjsZKruuvWrcs///zD3r17GTRoUJrnnjVrFt7e3sydOxcHBwcAKlasSKtWrVi7di0dO3akVKlSAJQuXdp4+1lu3rzJpEmTqFixIrVr1+bu3bsAuLq6ptgv+X5yrYKnp6dJxwe4evUqu3btYvTo0c+sgn/SiBEjaNGiBWPGjGHGjBmptkdGRjJnzhx69OhB//79gaT3Ozo6mq+++ormzZtTvnx5HBwc8PHxMX5mT79PT1fFP+2LL76gZcuWTJs2jejoaLRarfHiIC0+Pj7Mnj2bzz//nBkzZjBjxgxcXFyoXbs27777LnXr1gVI87s8Y8YM4uLiWLBggbFmIyQkhFdeeYUffviBwYMHs2jRIrRaLfPmzcPNzQ1IarqYNGkSERERxjhu3bpF9+7dCQ4OZvLkyc9871VVNV6AqKrK3bt3Wb58Of/++2+qC9POnTvTsGHDNI+zdu1a7t27x9atW40XhIUKFaJ3795cuHCBQ4cOcfHiRTZt2mTsm/LCCy/QoEEDFi9eTJ8+fTh48CAVK1Y0/l3WqlULJyenNC/YnxQcHMykSZMAeOmll7h58ybff/+9sd+Et7c3mzdvJigoCIBNmzZRpkwZ49/l065fv/7MZpMiRYrwxx9/ZLjPk86dO0fVqlWZMmWKseasSpUq1KpVi4MHDxpjSes3zc3NDRcXF+P3ZdGiReh0uhTfl8qVK9O0aVN+/vln4/uXmJjI6NGjLdLkaStSYs9BPD09KVasGMOHD2fIkCFs27aNwoULM3DgQNzd3TN87rOSmbu7uzGpQ9IPe0BAgNl6tIeFhREeHp6qJJdc/Xfw4EHjY5UqVUpReipYsCAxMTHpHvvAgQM0atTImNQh6fUGBQVx4MCBLMV78+ZNunTpgsFgYOrUqSiKYqyqfbpkl/x4ZhJzstWrV+Ph4ZFuqSg9BQsW5OOPP2b79u38+uuvqbYfPXoUnU7Hyy+/TGJiovFfvXr1uHr1aoqq3edRoEABPvvsM1avXs3mzZsZO3bsMy9sateuzY4dO/jhhx/o2rUrRYsWZffu3XTv3p2vv/463ecdOHCAWrVqpfgB9vb25oUXXuCff/4B4MiRI9SsWdOY1CGp/X7btm14eXkBST/k3bt35/bt23zxxRcpml7Ss2fPHipUqECFChWoWLEiDRo04Mcff6RLly6p2tcz+ls7cuQIpUqVMiZ1gHLlyrFr1y5Kly7N/v37KVq0KEWLFjV+Zk5OTlSvXt04aiA4OJg//viDjh07smjRIq5evcqAAQOoUaNGhq+hcePGKe43aNCAq1evEhERgb29PS1btmTLli1AUuL8+eefM/29fJqiKKmaXTJSv359Fi5ciMFgIDQ0lK1btzJ37lyAFKVsePZv2v79+6latSoeHh7G97JQoUKULFkyxegjS/VjsiUpsWczOp2Ohw8f4ufnl2qbRqNh4cKFTJ8+nZ07d7J27VqcnJzo3r07H330UYZVic/64ubPnz/N59y5cyfzLyINydWIT5/Hzc0NR0fHFG3oT5c8nkyqaYmMjEwz/vz58z+zbT4tZ8+epWfPniQmJrJgwQICAwONsQJER0en2D/5ouNZF1dp2bFjB6+88kqKixJTvfPOO2zatInRo0enuCgDjG3Kb7/9dprPvXv3bork8jyaNGnCmDFjsLe3p1q1aiY9R6vVUqdOHerUqQMktZ0PGTKEOXPm0LZtW+N7/qTIyMg0RzPkz5+f8+fPA0nfs/RKmMni4+NxdnbGw8ODadOmGUuxGalevbqxZK4oCi4uLgQEBKR5UZDR39rDhw/T/K4me/DgARcuXDA2oz2pWLFiALz33ns4OzuzZs0axo8fz/jx4wkJCWHKlClp/m4k8/HxSTPOO3fu4OXlRevWrVm8eDFHjhwhKiqK8PBwWrVqle7xChcunO7QzGTXr19/5iiPJ+n1eiZMmMDKlStJSEggMDDQeMHy9G/As37THjx4wLFjx9J8L319fY23M/o8cipJ7NnMwYMHSUxMpHr16mluL1SoEOPHj8dgMHD06FFWr17NzJkzKVWqFC1atMjyeSMjI1M9du/ePcqUKQOkfeX9dILLSHIpLrnz1JPn1el0maq+flq+fPlSHReS4s/sULtjx47Rs2dP3NzcWLRokfHHFJKq3H19fVOVdpPvP7mvKW7cuEFYWFiKYVSZodFoGD16NG3atGHy5MkptiVfZMycOTPNH/vixYtn6ZxpmTRpEm5ubqiqypdffsmXX36Z7r79+vUjMTEx1Vj8IkWKMGTIEF5//XUuXryYZmLPly9fmk1U9+7dM35/3NzcUs35EB8fz99//23s9Ofg4MC8efPYunUrI0aMoE2bNtSuXTvD1+ju7k6lSpUy3McU7u7uXLlyJdXjyTUC7u7ulC1blrFjx6baJ/niT6vV0qVLF7p06cKNGzfYsWMH06dPZ+jQocybNy/dcydfXCdL/ptJfu8qVqxI6dKl2bZtG9HR0dSuXTvDC4UGDRqwYMECbt++bdwv+YIgMDCQGzducPr0ad555x3gv5quJxO0qqrExsYa78+ePZtVq1YxceJE6tevj4uLC7GxsRnOFZEeNzc36tWrl+ZcCE83p+U2UhWfjaiqypw5c/D09KRJkyaptoeGhlK3bl1OnTqFRqOhWrVqjB07Fjs7O2Ov2qxUB0NS+/2pU6eM90+dOsW1a9cICQkBkv4Q7t+/nyK5Pz3JS0bnLl68OF5eXql6Syf30ja1pJeW6tWrs3PnzhRVdWFhYZw9ezZTx7127Ro9e/Ykf/78LF++PM1E/cILL7B79+4UY9N37NhBmTJlUpWInuX48eMA6Q6/M0WZMmXo0aMHq1atSnHBUaVKFezt7bl//z6VKlUy/jt37lyKpJrV70uyffv2sWbNGj777DM+/fRT1q1bx19//ZXu/kWKFGHPnj2cO3cu1bZLly6h0WiMIxGejq169ers378/ReIODw/n77//Nn7O1apV48CBAykuOv/++2/ee+89YyKzs7PD09OTN998k4oVKzJy5MhU1byWEhwczLlz51KUdJM78YWGhlKtWjWuXbtG4cKFjZ9ZxYoVWbhwobETWrdu3YwXT/7+/nTq1IlXXnmFmzdvZnjupzvXbdu2jWLFiqVI3q+99ho7d+7kt99+e2Y1fIcOHXB2dmbEiBHG/gcHDx6kadOmfPHFF4wYMQI7OzvjpFXJNV5P1gIePXrU+Nzk+xUrVqR58+bGMenJcT9r1EJa35cLFy4QFBRkfC/LlCnDjBkz0p2gKreQEruNREZGcvToUSCpze/27dusXr2aAwcOMGXKlBRthMlKlSqFq6srn332GX369CFfvnysX78eRVGMvdA9PDy4desWf/75JxUrVjQ5HgcHBwYOHMgnn3xCQkICU6ZMoWzZsjRt2hSAevXqsXjxYkaNGkWLFi3Yt28fO3bsSHEMDw8PYmNj2bFjR6pkpdVq6dOnD2PGjCFfvnw0atSIM2fOMH36dJo1a2asGciKDz74gLfffpuePXvSpUsXHj16xLRp0yhcuLBJHf+SjRs3jqioKL744gtu3ryZ4ofS39+fAgUK0L17d9q2bUu/fv1o164df//9Nxs3bkw1e5spzp07h5eXl7HtN6t69erF1q1bU0zm4u3tTceOHZkwYQIPHz6kcuXKhIaGMnXqVBo1amT8fnl4eHDq1CkOHDjwzDbap8XGxjJ8+HDjuGVImlRm+PDhbNq0Kc3JQrp3786vv/7Ku+++S6dOnahWrRqKonDo0CEWLFhAhw4djE0ET3+Xu3Tpwk8//US3bt3o1asXqqoye/ZsHBwcjMmjc+fO/PTTT7z//vt069aNmJgYpkyZQpMmTVLVUmg0Gr744gveeust5syZQ58+fTL1+rPijTfeYOHChXzwwQf06dMHrVbLN998Q+XKlalduzZVq1Zl8eLFdOvWjffeew9PT09WrlzJr7/+anyPq1evzuzZs/H19aVSpUqEhYWxdevWFLM+puXvv/9m4sSJ1KtXj+3bt7Nr1y6mTp2aYp/XX3+dqVOn4ujomKpN/ml+fn5MmTKF/v378/bbb9OhQweKFClCly5dWLBgAQBdunQxfp5BQUH4+fnxzTffYGdnR1RUFN9++22KJqxKlSoxd+5clixZQpkyZThx4gQzZ85EURTi4uIyjMfDw4PTp0+zf/9+qlSpQteuXdmwYQM9evSgU6dO2Nvbs2DBAo4ePWrsUJpbSWK3kcOHDxuHVtjb2xv/SJcvX55i4o4n2dnZMXfuXCZOnMjIkSONY8a///57Y0eSt956i927d/P++++b1HaYrHDhwnTp0oVRo0YRHR1N/fr1GT58uLH6r169egwYMIAlS5awfv16XnjhBSZMmEDPnj2Nx2jZsiXr16+nf//+9OvXL1Vy79ChA05OTixYsIDVq1dToEABunbtSq9evTL13j2tYsWKLFq0iK+//pp+/frh7OxM/fr1GTRoUJoXSGlJSEhg79696PX6NIdGffrpp3Tv3p2yZcsye/ZspkyZQp8+ffD39+fLL7+kefPmmY77/v37ZpmRzMHBgTFjxqQadz5o0CC8vb1ZtWoV3377LQUKFKBz584pEtj7779vHJWwbdu2TJ33m2++4ebNm3z33XfGx0aMGMH//vc/pk6dytChQ1M9JzmeOXPmsGXLFmPVccmSJRk8eDDt2rUz7vv0d7lFixYsXbqUyZMn89lnn6HVagkJCWHq1KnGCVACAgJYsmQJkyZNYsCAAbi7u9OsWbN0xydXqVKFN954gzlz5tCqVatUQxnNzcPDgyVLljBhwgQGDx6Mg4MD9erVY/DgwdjZ2eHm5sbSpUuZNGmSsSahdOnSzJo1yzjj3wcffIDBYGD58uVMmzYNHx+fVJ9rWgYMGMDvv//OkiVLKFSoEFOmTEnVfOfn50dQUJCxEPEsL7/8MmvXrmXevHlMmzaN+/fv4+PjQ5s2bShQoADz58/n6tWrTJw4EXd3d6ZNm8a4cePo06cPRYoUYdCgQSmGsr733nvcvXuXGTNmoNPpjJ2FN2/enO4Q4GRdunRhwIAB9OjRg0WLFlGtWjWWLVvG5MmTGTRoEIqiUKFCBX744Yc0+2rkJooqs+YLIYQgqZr85ZdfZt68ecaOjc/jwoULrF27lk8++cTssySK9EliF0KIPO7KlSts3LiRHTt2oNfr2bhxoyTiHEw6zwkhRB6nqiqLFi0iLi6OyZMnS1LP4aTELoQQQuQiUmIXQgghchFJ7EIIIUQuIoldCCGEyEUksQshhBC5iCR2IYQQIheRxC6EEELkIpLYhRBCiFxEErsQQgiRi0hiF0IIIXIRSexCCCFELiKJXQghhMhFJLELIYQQuYgkdiGEECIXkcQuhBBC5CKS2IUQQohcxM7WAZjD0aNHcXR0tHUYQgghhFXodDqqVq2a5rZckdgdHR0pV66crcMQQgghrOL06dPpbpOqeCGEECIXkcQuhBBC5CKS2IUQQohcRBK7EEIIkYtIYhdCCCFyEUnsQgghRC4iiV0IIYTIRSSxCyGEELmIJHYhhBAiF5HELoQQQuQiktiFEELkOrNmzaJrly7ExsbaOhSrk8QuhBAi11mxYgVhFy5w48YNW4didZLYhRBC5FoRERG2DsHqJLELIYTIVeLi4oy379y5Y8NIbEMSuxBCiFzl2rVrxttXrlyxYSS2IYldCCFErnLu3DkgKcGdf3w7L5HELoQQIlc5ceIEToqGYODkyZMkJibaOiSrksQuhBAi1zAYDOz76y9KqAZKATGxsZw8edLWYVmVJHYhhBC5xrFjx7gXHk55oDTgoChs377d1mFZlSR2IYQQucaaNWtw1mgoBziiUFFV+XXbNh4+fGjr0KxGErsQQohcITQ0lN9//51aBgMOKADUAeLj41m6dKltg7MiSexCCCFyPL1ez9dTpuCq0fDiE4/7oRAMrFm9mgsXLtgqPKuSxC6EECLHW7RoEaFnz9LCYMDpcWk9WRPAUVUZPWoUOp3ONgFakSR2IYQQOdqePXtYuHAhwUDlx0n9CCpHUAFwRaGNwcCFixf5cvx4DAaDDaO1PEnsQgghcqyDBw8yetQoAhSFVk88fvjxv2RlUGgC7Nq9m2+++QZVVa0bqBXZ2ToAIYQQIiv+/vtvhg8bRn69ng6qiv1TVfBPqwtEAz/99BN6vZ4BAwag1WqtEqs1SWIXQgiR42zYsIGpU6dSUFXppKq4PCOpAygoNEVFC2zcuJHw+/cZ/sUXODs7Wz5gK5KqeCGEEDlGfHw8U6ZM4auvvqKUwUA3VcXVhKSeTEGhMQotgT///JMP338/xaIxuYEkdiGEEDnC9evX6d2rFxs3bqQu0J6kSWiyojYKnYBbV67Qo3t3du3aZc5QbcoqVfEJCQkMGTKE69evEx8fz4cffkipUqUYPHgwiqJQunRpRowYgUajYdWqVaxYsQI7Ozs+/PBDGjRoYI0QhRBCZFOqqvLLL7/wzdSpEJ/AO0D5LCb0J5VC4UODgVVxcYwcOZJ9+/bRr18/XF1dnz9oG7JKYt+4cSOenp5MnjyZiIgI/ve//1G2bFn69+9PrVq1+OKLL9i5cydVq1Zl8eLFrF27Fp1OR/v27XnxxRdxcHCwRphCCCGymXv37jFl8mT++vtviisKbVQVTzMk9WSeKHRXVXYD27Zu5fDBQwwe8jk1atQw2zmszSqJvVmzZjRt2tR4X6vVcurUKUJCQgCoV68ef/75JxqNhuDgYBwcHHBwcCAwMJDQ0FAqV65sjTCFEEJkE6qq8vPPPzNz+nR0sbE0B2qrKhozJvVkWhReAcqg8tP9+wwcOJCWLVvSq1cv3N3dzX4+S7NKYk+u1oiKiqJv377079+fiRMnoiiKcfujR4+IiopK8Sa6uroSFRX1zOPrdDpOnz5tmeCFEEJY1e3bt1m6ZAlnzp6lGAqvo+JjgYT+tEAUeqkGdgG/bNnC73v28Obbb1OjRg1jvsoJrDbc7ebNm/Tu3Zv27dvTqlUrJk+ebNwWHR2Nh4cHbm5uREdHp3jclKslR0dHypUrZ5G4hRBCWIdOp2PZsmUsXrwYO72e14DqWKaUnh57FJoClVDZEB3NvHnzOHH8OAMGDsTf399qcTxLRoVZq/SKv3fvHt26dWPQoEG0bdsWgPLly7N//34A9u7dS40aNahcuTKHDh1Cp9Px6NEjwsLCKFOmjDVCFEKIFFRV5fbt2yQmJto6lDzhn3/+oUvnzvzwww+US0ykr6pSE8WqSf1J/ii8p6q0AI4eOECnjh1ZtGgR8fHxNoknMxTVCvPqjR07ll9++YUSJUoYHxs6dChjx44lISGBEiVKMHbsWLRaLatWrWLlypWoqsr777+fom0+PadPn5YSuxDCrBYsWMDChQtp1KgRI0aMsHU4udbdu3eZMWMGu3fvJr9Gw6sGA6XMkMznP54nvrsZjhWJys/AKaBI4cJ8/MknVK9e/bmP+zwyyntWSeyWJoldCGFuo0ePZseOHZQJKsO8ufNsHU6uo9fr+emnn5g7Zw4JOh31VJW68MxpYU1lzsSe7BwqmzUawg0GXnnlFfr06YO3t7fZjp8ZGeU9mVJWCCHS8PDhQwAiHkTYOJLc5/z580ycMIEzZ89SCoVWqHjbqMo9M0qj0MdgYC+we+dO9v31F7369KFly5bZqnOdzDwnhBBpuHf/HgAPIh7k6pXArCkhIYH58+fTs0cPrp8/z5tApxyS1JPZo9AIhd6qik9MLJMmTWLAgAHcunXL1qEZSWIXQog03LuXlNgT4hNMGnYrMnb16lXef+89Fi1aREWDgY8MBiqhoOSgpP4kXxS6ovIacOrIETp36sSvv/5q67AASexCCJGKTqfjUeQjVM+kkvqdO3dsHFHOtnfvXnp068aNixd5B2iLYtJqbNmdBoWaj0vvBXQ6xo4dy5QpU2w+kkISuxBCPOXmzZsAqD5Jif3GjRu2DCdHW7t2LcOHD8cnPp5eBoNZ5nh/FhWVSOAu8A8qKpZtSvFCoauq8hJJU6h/OmgQcXFxFj1nRiSxCyHEU5KX8VQLJiWE69ev2zKcHGvLli188803lFVVuqoq+axUSj8AhAPRwKbH9y1Ni0ITFP4HHDp0iGHDhqHX661w5tQksQshxFOuXLmSdCM/aJw0XL582bYB5UCXL1/m66++oiTwJuYbxmaK0Gfct6RqKLQiacKd5cuXW/HM/5HELoQQT7lw4QIaFw04gN5DT1hYmK1DynGWLl2KRq/nDcDOyu3pCc+4b2k1gLLA0iVLiI2NtfLZJbELIUQqp0NPo8+XVI2q5lMJCwuzeYeonObA/v0EqSruuaCTXGYpKNQEomNiOHPmjNXPL4ldCCGeEBMTw7Wr11C9H3e48k4af33hwgXbBpbD6HQ6HG0dhA3ZP/5fp9NZ/dwZJvaDBw9iMBisFYsQQtjciRMnUFUVNX9SYk/+/8SJE7YMK8cpW64c5zQa9BbukZ5dhQIajYbSpUtb/dwZJvYOHTrQtWtXwsPDrRWPEELY1JEjR5J+GfM/fsAVFFeFw4cP2zKsHOett9/mgcHAbhucOw5wdnambdu2ODs7Y+2BZzdQ2a8oNG7c2CZzyT+zKv7Ro0c0a9aMFStWyLSKQohcb9/+fUlJ/YmVNPQF9Bw8dFDa2TOhVq1atGjRgj3AISuX2uOAli1b0rdvX1q2bGnVxB6OyhKNBm9vb/r06WPFM/8nw8SuKArff/89PXr0YNKkSTRt2pTVq1fbpJefEEJY2t27d7kQdgFDwZRNkGpBldiYWI4fP26jyHKmgQMHUrNmTdYDf1sxuTuRNIb+22+/ZcuWLThZ6bw3UZmn0YCLC1O+/pp8+fJZ6cwpZZjYVVVFo9Hw3nvv8euvv/Lyyy8zceJE6tSpw8CBA1m1ahVHjx7l0qVLVgpXCCEsZ+/evQCohZ9KQgVB0Sr8/vvvNogq53JwcGD8+PG89NJL/AxsRrVKm7sTEBsby5o1a4iNjbVKYj+DynxFwdHTkxkzZ1K8eHErnDVtJveK9/HxYciQIezZs4eRI0ei1+v59ttvefvtt2nevLklYxRCCKvYuWsnSj4F3J/aYAeGggZ27tpps9nEcipHR0dGjx7NW2+9xX5gkaIQnYs61Kmo7EFlKRBYsiTfzZlj06QOWViP3dXVlddff53XX38dSKq6unv3rtkDE0IIa7px4wYnT5zEUDHtkUCGQAMP/n7AoUOHCAkJsXJ0OZtWq6V3796ULFmSyZMm8Z3BwLsGAwVz+Bj3eFTWAaeAV155hU8//RQnJ2tV/KcvwxJ7zZo1sbe3z2gXfH19KV++vFmDEkIIa9uyZQsAatF0SpOFQHFUjPuJzGvWrBkzZs5Em8+TeYrC2Rxccn+EygJF4V9F4cMPP2T48OHZIqnDMxL74sWL8fDwsFYsQghhE4mJiWzeshm1kAou6eykBX2gnr1798oQ4OdQrlw55s6fR0CJEiwFTuTA5P4AlfkaDffs7Rk/fjzvvPMOipJ9ah9k5jkhRJ7322+/EREegaFkxhNyqSVV9Ho9GzZssFJkuZOPjw8zZs6kYqVKrAZO56DkHoXKDxoNcY6OTPvmG1588UVbh5SKJHYhRJ6mqiorVq5AcVeg4DN2dge1kMq6n9bZZKrQ3MTFxYXJU6YQVKYMqxWFOzkguRtQWaEoRGu1TPn6aypUqGDrkNKUYee5rl27mly9sGDBArMEJIQQ1nT48GHOnjmLoZoBU/pyGcoYeLjnIVu3bjV2IhZZ4+zszPgJE+jauTProqJ4T1XRZOMOdX8Dl1WVoZ9+mm2TOjyjxF67dm327dvHrVu38PPzy/CfEELkRD/++COKs4JazMQSoy/gDUuWLpGZ6MzAx8eH3h99xHVVteq66ZkVj8oeRUNISAhNmjSxdTgZyrDE/v777+Pp6cmECRP47rvvCAwMtFZcQghhcUePHuXIkSMYqhhAa+KTFNCX03P7z9ts3bqVV1991aIx5gWNGzdm7vffc/j+fbLrGKvTQKxqoEOHDtmqo1xantnG/tZbb1G3bl2mTJlijXiEEMIqVFVl3vx5SaX1Epls3y0EeMMPC38gPj7eIvHlJVqtljp163JJUTBk07b2i4CbqyuVK1e2dSjPZFLnudGjR9OpUydLxyKEEFZz4MABjh87jr6sPvNTdSmgr6Dn7p27bNq0ySLx5TUlS5ZEp6pE2TqQdNwHipcogUaT/fucmxShl5cXNWrUsHQsQghhFQaDge/nfI/iqqAWT7uEqFxSUC5lUOXqB/jCwkULiYmJsUygeUjynCnZdYmxOI0GT09PW4dhEpOuUxMSEjh9+jS3bt1Cp9Ph7OyMn58f5cqVw84u07PSCiGETe3evZtzZ89hCEm/bT05qafbqU4BfSU9D3c9ZNWqVXTp0sUyweYRySXh7FkRDwaSmgxyggyzssFg4Ntvv2XJkiVERSVVkCiKYlyX3c3Nja5du9K7d2/LRyqEEGaQkJCQVFr3VFADnzON5E9aCW7psqW8/vrreHl5mSdIkS0l577sLsPE/vXXX7Nu3TqGDRtGSEgIBQoUwM7OjsTERO7cucO+ffv46quvSEhIoH///lYKWQghsm7Dhg3cunkL/Ut6k8atP4uhkgHdNh0LFy5kwIABz3/APCq5p7k5UufTK5xkvOKJ6bJ7b/hkGbaxr1u3jgkTJtC6dWv8/f2N1e52dnb4+/vTpk0bxo8fz5o1a6wSrBBCPI+oqCgW/LAACpDURm4O7mAobmDDxg1cu3bNTAfNe5ydnQEwx3x+ZZ9xPyt0/BdjdpdhYk9ISKBgwYznWPT19SU6OtqsQQkhhCWsWLGCqEdR6CuZp7SeTK2goioqc+fNNd9B85gCBQoAEGGGY9UEvAFXoNXj+88jAZVIgwFfX9/njs0aMkzsderUYcyYMdy4cSPN7bdv32bMmDHUrVvXIsEJIYS5REREsHLVSgxFDEm/+ubkBPrSenbv2s25c+fMfPC8oUiRIjg7OXHFDMdSUPAgaZLAEBSU57yKu0ZSE0FQUJAZorO8DNvYR4wYQZ8+fWjUqBH+/v74+fnh6OhIfHw8d+/e5erVq1SpUoWRI0daKVwhhMiapUuXotPpUCtapgOUWkZFCVOYO3cukyZNssg5cjM7Oztqv/AC+/fsoYXBgH02mjP+GOBob0/16tVtHYpJMkzs3t7eLFu2jCNHjnDo0CFu3bpFXFwcTk5ONGjQgOrVqxMcHGytWIUQIkvu37/PTz/9hCHQAO4WOokD6Mvo2bdvH6GhoZQta46W3byldevW7N69mwNAHVsH81gEKkcVhZbNm+Pi4mLrcExi0iD04OBgSeBCiBxr1apVJCQmoJaz7HAltZSKck5h4aKFTPhygkXPlRsFBwdTs2ZNdh08SDlVxcvGpXYVlY0o2Nnb56jZV58589zGjRvp0qULbdq0YerUqcbx7MkiIiJo2rSpxQIUQojnERUVxU/rf0pqW7dUaT2ZPehL6vnrz7+4csUcrcV5zyeffILG0ZGVikKCjaer2QucR6VX797Gzn05QYaJffXq1QwZMoTChQtToUIFfvzxR9544w2uX79u3Eev18sXWAiRbW3ZsoW42DjUIOskCbWkiqJVWL16tVXOl9sUKlSIYcOHc11VWQXobZTcj6GyA3jllVdo3bq1TWLIqgwT+6JFixgxYgTjxo1jzJgxbNmyBQcHBzp27Mjt27etFaMQQmSJqqr8tP4n8AGsNSmcE+gD9GzdtlXmkM+il156iX79+hEKrMH6yf0EKuuA4KpV+eyzz3LMxDTJMkzs169fp3bt2sb7/v7+LFq0CHt7e7p3705kZKTFAxRCiKw6fvw4N67fwFDCYNXzqiVUdHE6du3aZdXz5iZvvPEGH374ISeB5WC1avmDqKwGKlWqxJcTJuDo6GiV85pThom9YMGCHDt2LMVj3t7ezJs3j4iICN577z2ZnEYIkW3t2LEDxU5BLWzl6lxvUNwVduzYYd3z5jLvvPMOAwcO5Kyi8IOiEG3B5K6isguVDUBISAiTv/oqx/SCf1qGif3dd99l+PDhfP311yna1QMCApg7dy4XL17MUT0FhRB5h8Fg4Lc9v6EvmIX11p+XAvoieo4cOSI1m8+pdevWjBo1iltaLXM1Gu5bILknovITsBto1qwZX06YgJOTk9nPYy0ZJvYOHTowaNAg9uzZw82bN1NsK1++PMuWLcsxU+wJIfKW8+fP8/DBQyhkm/OrhVRUVeXgwYO2CSAXefnll5n2zTckuLgwR6PhihmTeywqi1E4AnTt2pXPP/88xy9H/szhbu3bt2fDhg3UqFEj1baSJUuyZs0afvnlF4sEJ4QQWXX06FEAVD8bDZnyBsVB4ciRI7Y5fy5TqVIlvpszBy8/PxYqCqfNkNwjUZmvaLisURgyZAhdu3bNcR3l0vLMxG6KYsWKmeMwQghhNqdPn0bjqoGsLMilArFAJChhStbWElXA4Gng39P/ZuHJIi1FihRh9vffU7JMGZYDR54jud9HZa5GQ6SDPZOnTKFZs2bmC9TGzJLYhRAiuwm7EIbeQ5+l5yoXFJQoBUWnoDmsQbmQtVKc6qly6dIlVNW2E63kJp6ennzz7bdUr16ddcChLCT3+6gs0GgwuLjw7YwZadZI52SS2IUQuY6qqty8eRPVLWsJVbmhZHjfZK6QEJ/A/fv3s/Z8kSZnZ2cmTJxISEgIG4CTmUjuj1BZqNGguLry7YwZOWbFtsyQxC6EyHV0Oh26OB1ktWPz0wX9rBX8UZ2TEk5EhDlWGRdPcnBwYNy4cZQvX551isINE5J7IirLFIU4e3umfP01JUqUsEKk1peprn9xcXGcP3+ehISEVFVL1apVM2tgQgiRVcY1LextG0fy+Z9eY0OYh6OjI19OmEC3Ll1Y9eABvQwGHDJYOGYHcE1VGTNsWK4sqSczObHv2LGDzz//nKioqFRJXVEUTp8+bfbghBAiK/T6x0VsW3dwfnx+g8G6M9/lJZ6engwfMYJ+/fqxB2iczn43UfkLeO2116hfv74VI7Q+kxP7jMcdDPr164e7u6WXSBJCiKwzjkO2dZ+1x/lcq9XaNo5cLjg4mFdeeYU9O3fygqrilsYV3U7A1dWV999/3/oBWpnJbeyXLl3i448/pmzZshQuXDjVP1McO3aMjh07AklDUd58803eeecdPv/8c+MV7apVq2jTpg1vvvkmu3fvzsJLEkLkdW5ubkk34m0bBwlJ/0lhyPI6depEgqpyOI1tEaicBdq2a5cnPguTE3uJEiWea0W3uXPnMmzYMHQ6HZBUA9C7d2+WL19OfHw8v/32G3fv3mXx4sWsWLGC+fPn8/XXXxMfb+u/TCFETuPo6IijkyPE2TYOJS6p5JgvXz7bBpIHFCtWjPLlynEqjQlm/iWp8iY3jVXPiMmJ/YMPPmDkyJGsXLmSffv2cfjw4RT/niUwMJDp06cb75crV44HDx6gqirR0dHY2dlx/PhxgoODcXBwwN3dncDAQEJDQ7P2yoQQeVqhQoVQom3cyB4N9vb2eHt72zaOPKJW7drcVFXinmqDuQgEFC6Mv7+/bQKzMpPb2Pv27QvAiBEjUm0zpfNc06ZNuXbtmvF+sWLFGD16NLNnz8bd3Z1atWqxdevWFNUkrq6uJvUm1el00nlPCJGCt5c3l89dxoDtOq4pjxR8fHw4c+aMzWLIS1xdXVGBp+uWb2k0BBUunGfyhMmJfefOnWY98bhx41i6dCmlS5dm6dKlTJgwgbp166ZYBjY6Otqk9hBHR0fKlStn1viEEDlbcHBwUm1iItZf3e0x7UMtlepWkt8nK3F1dWXGjBk8OWtAIiqRBpXy5cvnqs8ho4sUk7/upnaQM1W+fPmMHVwKFCjA4cOHqVy5MtOmTUOn0xEfH09YWBhlypQx63mFEHmD8bcjArDFIpSxYIgxULp0aRucPG/y8fEB4Ml63miS2tfz589vi5BsIsPE3rRpU1auXImnpydNmjTJcNWbbdu2ZerEY8eOZcCAAdjZ2WFvb8+YMWPw9fWlY8eOtG/fHlVVGTBgAI6Ojpk6rhBCQNLS0gDKPQXVN5Pj3hKSpi1t2bIlW7ZsISYhJvMBPJ5FtlKlSpl/rsgSZ2dntBoNsU/MGxD7+H8PDw/bBGUDGSb2Vq1aGRPra6+99twnK1KkCKtWrQKgRo0arFixItU+b775Jm+++eZzn0sIkbfly5ePwKKBXL57GbVc5hN7y5YtjX2LVv+yOtPnV+4qODg6SIndihRFwdXFhbgn+mbpHv/v6upqm6BsIMPE3qdPnzRvCyFETlCjeg2ubryaNE9GZlbGsIctW7YAj//PQsWh9q6WKpWrYG9v63lt8xZXV9cUiT15xKNxboM8QBaBEULkWtWrV0dNVI3V4iazh9jYWNasWUNsbGzm55yPBfWhmuuWA80J3D08jNXv8F9VfF6YmCaZJHYhRK5VrVo1NFoNyi3rjmdXbiedr2bNmlY9rwBPLy9inugPljzOytPT0ybx2IIkdiFEruXq6kqFChXQ3LbyT90t8PTypGTJktY9r8DHx4dHTyT2SMDR3l6q4oUQIreoFVIracibtaaXVUF7R0vtWrUzHEkkLMPPz49HBgNVgGrAA5KGVOelzyJTif3gwYOEh4cDSR1K3n//fWbNmiVLEgohsq2QkBDgv+pxi4sAVacazyusq3DhwqhAIBCMQoSi4F+kiK3DsiqTE/vSpUvp1KkT586dIzQ0lM8++wxVVVm2bBnffPONJWMUQogsK1OmDO4e7qnnGbUQ5baCoijScc5GijxO4vcAAyr3SVqrJC8xObH/+OOPjB49mlq1arFx40bKlCnDnDlzmDx5Mhs3brRkjEIIkWUajYYa1Wtgd9fOKuuza25rKFGyRJ7qrJWdFC1aFIC7wEMgXlWNj+UVJif2Gzdu8OKLLwLwxx9/UK9ePSDpTbx/P7NjSYQQwnqqVauGIcaQcq5RS9CDcl+hRnUprduKq6srPvnzcwe48/ix4sWL2zIkqzM5sfv5+XHlyhWuXLnC2bNnqVu3LgCHDh2iUKFCFgtQCCGeV9WqVYGk2eAsKhxUg2o8n7CNEiVKcFdRuPv4frFixWwZjtWZvAjMm2++Sd++fXFwSJoisUaNGixdupRJkybRv39/C4YohBDPJzAwEI98Hjy49wBKWO48yr2kCweZH962ihUvzpGDB7kDeHl65qnJaSATib1bt26ULl2ay5cvG+eN9/LyYtSoUbRu3dpS8QkhxHNTFIWKFSry98m/SSTRcue5r1AkoEieWnAkOwoICCBBVbkAFM9j7euQiar4119/nYIFC9KlSxe8vb0BaNGihSR1IUSOUL58edRIFRIsdAIVtBFaKlaoaKETCFMl94x/CBTOY0PdIBOJPSIiAmdnZ0vGIoQQFhMUFJR0I8JCJ4gDQ5zhv/MIm3my31de7ANmclV8586d6du3Lx07dqRIkSKp1kmvVq2a2YMTQghzKVWqFADKQwW1gAXGvT1M+k+mkbU9Hx8f421fX18bRmIbJif2qVOnAjB8+PBU2xRF4fTp0+aLSgghzMzb2xs3dzciH0Za5PjKw6SOcyVKWLB3njCJg4OD8Xb+/PltGIltmJzYd+7cack4hBDCohRFoVjRYpy8dRI9evOf4BF45POQjnPZTL58+WwdgtWZnNgLFy5svH3t2jUKFiyIqqrY22d2oWIh8o67d++iKEqKqkFhO4GBgfwb9q9FErvmkSbPzXCWE+S1oW6Qic5zqqoyc+ZMqlatSpMmTbh58yaffvopQ4YMISHBUt1Mhci5Tp48yRtvvEGbNm0ICwuzdTiCpN7ShlgDlhjxponREFAkwPwHFlkybNgwWrdujZ+fn61DsTqTE/sPP/zAmjVrGDNmjLH9okWLFvz2229MmzbNUvEJkWOdPXvWePv8+fM2jEQk8/f3T7ph7qll9WCIMeTJHtjZVZMmTRg4cCBardbWoVidyYl9zZo1fPHFF7Rq1cq4rm3jxo0ZP348W7ZssViAQuRUly5dwkELWgUuXLhg63AEULBgwaQbMWY+cHTSf5LYRXZgchv7tWvXjMNFnlS8eHHjGu1CiP+Env6XEu6JxBk0nDkTautwBP8ldiVaQTXnUm8xKY8vhC2ZXGIvXrw4Bw8eTPX4tm3b8tzKOUI8S0xMDOfOn6e0ZwKlPeL599S/0hclG/Dy8krq8GvmErsSk1SLmRfbc0X2Y3KJ/aOPPmLQoEGcP38evV7Pxo0buXz5Mlu2bGHSpEmWjFGIHOfw4cPo9QYqeCUSp1fYfk3HyZMnCQ4OtnVoeZqiKBTwK8C16GvmLbFHg0arkdEPIlswucT+yiuvMG3aNI4cOYJWq2XRokVcu3aN7777jpYtW1oyRiFynL179+Jsr1DWK5GK3gnYaxX27Nlj67AE4F/IHyXWzMu3xkB+n/x5sqOWyH5MLrEfOHCAF198kfr166d4PD4+nu3bt9O4cWOzBydEThQbG8vePb9RwycOOw3YaSA4v45dO3fQu3dvmfvBxgoWLIjmhMasY9k10RoKBxR+9o5CWIHJJfZOnToRGZl6Ksbr16/z8ccfmzUoIXKyHTt2EBMbR33/eONj9f11PHgYyd69e20YmYCknuuGOINZV3nTxGj+G0onhI1lWGJftmwZ8+fPB5ImqHnjjTfQaFJeC0RGRkrnOSEeMxgMrFq5gkB3A0Ge/82CUil/In4uKitXLKdhw4bGIaPC+oyzaEYDnmY4YCIYYg2S2EW2kWFib9OmDZGRkRgMBr799lteffVVXFxcjNsVRcHV1ZUmTZpYPFAhcoK9e/dy+cpVelWM4cncrVGgRWAMP4Se5cCBA4SEhNguyDwuea1uojBPYn882c2T024LYUsZJnYnJyc++OADIGmYSOPGjaXXpxDpSExMZN7cOfi7qdT2S13PW88/nk2XXZkz53tq1KiRqvZLWEdyYlceZTCW/ek+cBn0iVMeJV3ByTzxIrsw+Zfl66+/5tGjR5aMRYgcbfPmzVy5eo12JaLRpFHTbq+BN4pHc/bsOXbs2GH9AAUAzs7O+Pj6QAart6r+aob3U4hMqr001gQIYWMmJ/Zy5crx119/WTIWIXKsyMhI5s2dQ1kvPTV80++V9WKheIp7GPhu9ixiYsw9r6kwVckSJdFGpl8MV0uoqG4qqqOKoZoBtUT6iV2JVChYqCBOTk6WCFWITDN5uFv+/PkZO3Ys3333HQEBAam+xAsWLDB7cELkFHPmzCEqKopOIdFk1C9Oo0CnMlGMOqhh0aJFfPjhh9YLUhiVLFmS/Qf2g4G0izcK4Jz0Ty2Z8UQ2mkgNJSuXtECUQmSNyYndycmJ1q1bWzAUIXKm06dPs2nTRpoUiSPQ/dljo0t76qnvr2PVqpU0a9ZMRpXYQOnSpZOSeiTP14EuEdRIlaCgIPMEJoQZmJzYv/zyS0vGIUSOpNfr+WrKZPI5whslY01+3tulYjl0z4mvpkxh+owZMvzNysqUKQOAEqGgej7H1LIRSf+VLl3aDFEJYR4mJ3aA0NBQzp49i8FgAJLGtsfHx3PixAnGjh1rkQCFyM7Wr1/P2XPn6VMpCpen/pp+v+EAwEtPTFSTzN1B5a2SUcw/cYKtW7fSvHlza4QrHitcuDDOLs5Eh0fDc1SYKBFJF2Rly5Y1U2RCPD+TE/v8+fOZPHkyGo0GVVVRFAWDwYCiKNSqVcuSMQqRLYWHhzN37hwqeidSq0DqDnN7MkjsAPX949l704nZs2ZSt25d3N3dLRqv+I9Go6F8ufIcvnCYRBKf/YT03AcfXx+8vb3NF5wQz8nkXvFLly6ld+/enDhxAm9vb3bv3s3PP/9MmTJlqFevniVjFCJb+v7779HFxdIpKOMOc+nRKNC5TDQPH0ZK51MbqFChAuoDlefJ63YRdlSuVNl8QQlhBiYn9jt37tC6dWu0Wi1ly5bl+PHjlChRgsGDB7NmzRpLxihEtnPmzBl++eUXmgXE4e9qyPJxinnoaVBYx08//cTly5fNGKF4lgoVKoAKhGfxADFgiDYkHUeIbMTkxO7m5oZOpwOgWLFinD17FkiabenGjRuWiU6IbEhVVWbNnIm7A7xe3PQOc+lpWzIWR43Kd9/NNkN0wlQVK1YEQLmXtY6Lyv2k51WqVMlsMQlhDiYn9pCQEL766ivu3LlDpUqV2LZtG48ePWLXrl14enpaMEQhspcDBw5w5OhR/lcsJlWHuazwcFB5tWgMf/75FydPnnz+AwqTuLu7U7RY0Swndu6Bg6MDpUqVMm9gQjwnkxP7Z599xrVr1/j5559p0aIFGo2GkJAQxo0bR+fOnS0ZoxDZhqqqzJs7Bx9naFBEZ7bjNg2MI58jzJs712zHFM9WtUpVNOEa0psyPiPa+1oqVqiInZ0Zru6EMCOTv5GFCxdm06ZN6HQ6HBwcWL58Of/88w9eXl5UriydR0TesG/fPkLPnKV7uWjszbiGi5MWXg2MYemRIxw7dowqVaqY7+AiXZUrV2bDhg3wAPDKxBMTQI1QqdJaPieR/Zj803T79m1u377NgwcPuH37NpGRkZQtWxY/Pz9u375tyRiFyBZUVWXhwh/wcYaXCqU9hO15NCyiw8MRFi1aaPZji7QlF0oyXR1/P+k/aV8X2ZHJJfb69etnODvW6dOnzRKQENnV4cOHOX06lK5lo7GzwIqrjlpoERDDioOH+Pfffylfvrz5TyJS8PPzI79vfu7evwuZmDxOuackjYWXz0hkQyYn9h9//DHFfb1ez8WLF1m4cCGDBw82e2BCZDeLFi3E08kypfVkjYro2HTFlcWLf+TLLydY7DziP1UrV2X337tJIP1V+Z6m3FcoXqI4Li4uFoxMiKwxObGHhISkeuyFF16gSJEizJgxg4YNG5o1MCGyk+PHj3P06DHeLR2DQ/qrfT43ZztoWiSGdX/+xblz52QOciuoUKECO3fuhBjAlDxtAE24hsovSt8ikT09d4Vi8eLFCQ0NNUcsQmRbPyxYgIdjUju4pTUN0OFir/DDDz9Y/FyC/yaYMXWimkhQE1WZmEZkWyaX2NPqIBcVFcX3339PkSJFzBqUENnJoUOHOHT4MO+WjsHRgqX1ZK72Ks0DYlj7xx/S1m4FJUuWxM7ODkO4AbXIs8e9KeFJfY3KlStn6dCEyJLn6jynqiouLi5MnjzZ7IEJkR0YDAZmz55Ffuek9m9raRYYx6/XnPnuu9l88823sqyrBTk4OFCiZAnORJxBNWVAewS4uLpIgUZkWyYn9kWLFqX6cbG3t6dMmTK4urqaPTAhsoPt27dz9uw53i8fbdG29ac520Gb4jEsOnqMP/74g5deesl6J8+DygaV5dzWcxhUAzzjGkrzQENQUJBcbIlsy+TEntHSrLGxsTg7Oz/zGMeOHWPKlCksXryY+/fvM2zYMCIjI9Hr9UyaNInAwEBWrVrFihUrsLOz48MPP6RBgwamhiiEWUVHR/Pd7FmUzGfgRQv2hE9Pw8I6dl53Zsb0bwkJCcHR0dHqMeQVpUuXRt2oJnWgy6icooLyUKF0KenUKLIvkxL7wYMHWbp0KUeOHCE8PBwPDw8qV65Mx44deeGFFxg9ejQlSpSgZ8+e6R5j7ty5bNy40XgBMHnyZFq1akWLFi3Yt28fFy5cwNnZmcWLF7N27Vp0Oh3t27fnxRdfxMHBwTyvVohMmD9/PuHhEfStGYXGBoUzrQY6lYli/OHbLFmyhO7du1s/iDyiRIkSSTceknFijwJVr1KyZElrhCVEljwzsc+aNYvp06dTrFgx6tevj6enJ5GRkRw8eJBu3brRokUL9uzZw88//5zhcQIDA5k+fTqffvopkDTZR1BQEF26dKFw4cIMHTqUv//+m+DgYBwcHHBwcCAwMJDQ0NBnTlmr0+lkghxhVleuXGHt2rU0LKyjZD69zeIo751InYI6lixZTIkSJShYsKDNYsnN4uOTamSUSAXVP4N29sj/bspvjsiuMkzse/fuZebMmYwZM4a2bdum2r527VqGDRtG9+7dKVCgQIYnatq0KdeuXTPev379Oh4eHixcuJAZM2Ywd+5cihUrhru7u3EfV1dXoqKinvkiHB0dpYeqMJvExES+mjKZfI4qb5Z6/mVZn9e7ZWI5Fu7E2jVr+Hb6dDQaC0x7J/D08iT8UcZj3pTIpKqb+vXry+Q0wqYyurDM8Bdi0aJFdOvWLc2kDknJ2cnJKUtLTXp6ehontWnYsCEnT57Ezc2N6Oho4z7R0dEpEr0Q1rBu3TrOnjtPh9JRuNpnYdkvM8vnoPJOySiOnzjxzJoxkXWBgYFoop5x0RQFnt6ektRFtpbht/jUqVO0atUq3e2//vorI0eOzFKVVPXq1dmzZw+QtL51qVKlqFy5MocOHUKn0/Ho0SPCwsIoU6ZMpo8tRFbduXOH+fPmUsUngVoFTJ9i1NLq+8dT1iuR2bNm8uDBA1uHkysVKVwETXTGiV0TpSGgSICVIhIiazL8FsfHx2d4Zbpp0yaqV69OQkLmfwA/++wzNmzYwNtvv83vv//OBx98gK+vLx07dqR9+/Z07tyZAQMGSE9gYVWzZs0kMSGezkExPM9oJlWFCJ2GG9Fadl5zQH3Ogr+iQNegaGKio5kzZ87zHUykqVChQhhiDZBBlwpNrAb/Qv7WC0qILMiwjb148eIcOHAg3YkYFEVh//79//UofYYiRYqwatUqIGl997SmzHzzzTd58803TTqeEOZ04sQJdu3azf+Kx1LA2fBcx9p53YHbsUkD338IdUUFXinyfEPmCrsZaBIQx5Ytm3njjTekZ7aZGTsmxgBptQAawBBjwM/Pz5phCZFpGZbYW7duzdSpU7l+/Xqa269cucK0adN44403LBKcENY0d873eDpCy2Jxz32sI3cdMryfVa2Lx+FirzBnzvdmOZ74j6+vb9KN9PpLxgEqz+woLIStZVhif/fdd9m5cyetW7embdu2VKtWDXd3dx4+fMihQ4dYt24dNWrU4J133rFWvEJYxIkTJzh67DgdysTgZIYZ5nT6jO9nlau9SrMiMaz9ex9hYWFSajcjHx8fAJRYJe2pZeNS7idEdpVhYtdoNMybN4/vvvuOFStWpKg69/X1pUePHhlOSiNETrFu3Tpc7RVeLmy9+eCzqnGAjk2XXVi3bh2DBg2ydTi5hpeXV9KN9Cps4p7aT4hs6pkT1NjZ2dGnTx969+7NlStXiIiIwMvLi4CAABlPK3KFmJgYft+7l3p+sWYprVuam71KiG8cu3ftpH///tjb29s6pFzBzc0NrVaLQZd2/wpFl9SbUhK7yO5MzsyKolC0aFGqVq1K0aJFJamLXOPIkSPEJyRQMxsNb3uWGgUSiIqOydIcEiJtiqLg5uEG6fVxfFyZ4+HhYbWYhMgKyc4izzt58iRaBUrnS7R1KCYr55UU66lTp2wcSe7i4e6BEp/OOMcE0Gg1Ji14JYQtSWIXed6VK1co6KpadVnW5+Vqr+LtrHD58mVbh5KruLu7Q3oVNwlJ01zLcq0iu5PELvK8iPBw8tnnnNJ6Mk/7RJmFzszcXN1QEtMvsctUsiInyHJiDw8PZ+vWrVy9etWc8QhhdQaD3uzLssYmKjg7O9O2bVucnZ2JTS9ZPAeNAnq97Vaey41cXFzQJKb9s6gkKji7SDW8yP5MTuyhoaE0adKEAwcO8OjRI9q1a0f//v1p0aIFf/zxhyVjFMKiXN3ciUnnxzyrYhIVWrZsSd++fWnZsiUxFkjs0Xotrq4ZLR4uMsvJySn9KWUTwdVZ3m+R/T1zuFuyiRMnUqZMGUqWLMn69euJjY3lr7/+YsWKFUybNo26detaMk4hLKZgwYL8e8wOVeW55od/koudypYtWwDYsmULBezMu0qc3gD3YqB+oUJmPW5el1FiV/RK0nYhsjmTiylHjx7lk08+wdvbm7179/Lyyy/j7e3Na6+9xrlz5ywZoxAWVaZMGaLjVW7Hmq/U7mynEhsby5o1a4iNjcXZzIn9SpSWBAOy+qGZOTg4oOrT/qwUgyKLUokcweRfMgcHB1RVJT4+ngMHDvDiiy8CSW3tUh0ocrLq1asDcPRezpno5djjWKtWrWrbQHKZZyV2mQxI5AQmV8WHhIQwadIk4+QM9evXJzQ0lHHjxvHCCy9YLEAhLK1IkSKULFGcv26H0Sww+08pq6rw1x0nKlWsIPOWm5mdnR0YIK2p4jEgiV3kCCaX2EeOHImdnR2hoaFMmjQJNzc3NmzYgJOTE0OGDLFkjEJYXMtXW3HhoYawh9l/MPupcDtuRCm82uo1W4eS6xgTd1qzyhoeJ34hsjmTv6X58+dn+vTpKR4bNGiQTC0rcoUWLVqwYP481l9M4OOqUbYOJ12qCusvOePt5UmjRo1sHU6uY0zcUmIXOZjJWVlVVTZs2MCtW7cAmD9/Pq+99hpDhw4lJibGYgHmdf/88w8zZ86U+QIszMXFhXfav8uRe/aERmTfUtnR+3aERtjRsVNnHBzMs8a7+I8xsadTYtdqs3+NjhAmJ/YZM2YwcuRIbt26xcGDB/nqq6+oWbMmR44cYfLkyZaMMU+bOXMWK1euZN26dbYOJddr164dBXx9+PGsK4lpL/BlU/F6WHrOjYAihXntNamGtwRj4k6rxK5KYhc5g8mJ/aeffmLy5MlUrVqVX375hapVqzJixAjGjRvH9u3bLRljnpWQkMCVK1cACAsLs3E0uZ+TkxN9+/XnyiMNv1zJfsOa1l904la0woCBH0uVsIUYE3caF3aqQZU2dpEjmJzY7969S8WKFQH4448/eOmllwDw9fUlKir7tknmZKGhoej1iRjsXfj39GkSEnLOsqI5Vb169ahX7yXWXXThelT26T9yIVLL5svONGvWjBo1atg6nFxLquJFbmDyL1dAQAAnT57k33//5fLly9SrVw+A3bt3ExAQYLEA87I//vgDFIWEgJrE63QcPnzY1iHlCQMHfoyLqzuz/3XPFlXyOj1896873t7efPTRR7YOJ1fLqCpeSuwipzA5sffo0YMBAwbwzjvvULNmTSpUqMCsWbOYMGECPXr0sGSMeVJCQgJbt/2KPl8REvOXQLF3NE5RKizL29ubTz8bzKVIDWsv2H4K0RXnnLkRpTBk6LCkZUWFxaRbYlef2i5ENmbyt7RNmzaUL1+ea9euGavhq1atysKFC6lZs6bFAsyrtm3bRkT4fRKCaoBGi86nDHv27OHy5csULVrU1uHlei+99BItWrRgyy8/U9UngSBP26yidvy+HduvOdGuXTupgreCdIe7GZ7aLkQ2lqlGxLJly1K1alWOHj1KXFwcQUFBktQtIDIyku++n4PB3Q99viIAJBSqDFp7pn3zDapq3nnHRdr69u2Ln58fc/51R2eDvB6doDDvtDvFAgN47733rB9AHmTslPj05y2JXeQgJif2+Ph4hgwZQt26denatSt3797liy++oHPnzjx69MiSMeYpBoOBCRMmEPkoEl3ROv8tN2bvTFyRGhw6eJDVq1fbNsg8wsXFhc+HDOV2jMLasMytw+2ozfi+KVacd+aBTuHzocNk8RErSXfmuceJXuYOEDlBpsaxnzhxgmXLlhl/ZHr06MGtW7dkHLuZqKrK999/zx9//IGuSAgG1/wpticWKIfeqyizZs3izz//tFGUeUvVqlV59dVX2XrViauZ6CUf7Buf4f1nCXuoZfd1R9q9+SblypXL1HNF1hkTdzoldknsIicw+Zfql19+YdiwYVSrVs34WHBwMGPGjGHXrl0WCS4vUVWVOXPmsHz5chIKlCOxYIXUOykKcSXro3fJz/DhX/D7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\n",
      "text/plain": [
       "<Figure size 576x360 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize=(8, 5))\n",
    "ax1 = sns.violinplot(x = 'Quarter', y = 'Price', data = netflix_stocks_quarterly)\n",
    "sns.set_style('whitegrid')\n",
    "ax1.set_title('Distribution of 2017 Netflix Stock Prices by Quarter', fontsize = 16, y=1.05)\n",
    "ax1.set_xlabel('Closing Stock Price', fontsize = 15)\n",
    "ax1.set_ylabel('Business Quarters in 2017', fontsize = 15)\n",
    "\n",
    "plt.savefig(\"netflix_quarterly_stock_price_violindia.png\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Graph Literacy\n",
    "- What are your first impressions looking at the visualized data?\n",
    "\n",
    "- In what range(s) did most of the prices fall throughout the year?\n",
    "\n",
    "- What were the highest and lowest prices? "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    " # Steady increase in stock price. High fluctuation in Q3 (Cooperation with Disney cancelled)\n",
    " # $140 - $150 and $180 - $190\n",
    " # lowest ~$122; highest ~$205 "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 6\n",
    "\n",
    "Next, we will chart the performance of the earnings per share (EPS) by graphing the estimate Yahoo projected for the Quarter compared to the actual earnings for that quarters. We will accomplish this using a scatter chart. \n",
    "\n",
    "1. Plot the actual EPS by using `x_positions` and `earnings_actual` with the `plt.scatter()` function. Assign `red` as the color.\n",
    "2. Plot the actual EPS by using `x_positions` and `earnings_estimate` with the `plt.scatter()` function. Assign `blue` as the color\n",
    "\n",
    "3. Often, estimates and actual EPS are the same. To account for this, be sure to set your transparency  `alpha=0.5` to allow for visibility pf overlapping datapoint.\n",
    "4. Add a legend by using `plt.legend()` and passing in a list with two strings `[\"Actual\", \"Estimate\"]`\n",
    "\n",
    "5. Change the `x_ticks` label to reflect each quarter by using `plt.xticks(x_positions, chart_labels)`\n",
    "6. Assing \"`\"Earnings Per Share in Cents\"` as the title of your plot.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAfkAAAFfCAYAAABN87UXAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjMuMSwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/d3fzzAAAACXBIWXMAAAsTAAALEwEAmpwYAAA6wUlEQVR4nO3deViU9f7/8Se7IC64pphrgZYi7ifT3ELL1IqjoSnu5MkWczmluYaGmEuaih2XnyBagYqWZVp2UtNKTxah30ArNbdCU1zYt/n9QU6OwIgKg9y+HtfFxdz7e4bPxWvuz73ZmUwmEyIiImI49qVdgIiIiJQMhbyIiIhBKeRFREQMSiEvIiJiUAp5ERERg1LIi4iUIbogSm6GQl7KrMDAQLy9vQv9Wb58eYnXcOrUKby9vdm2bVuJb+tOc+7cOd544w26dOlC06ZNad++PS+//DLx8fEW83l7e7Nq1apSqjK/mJgYvL29uXDhwm2v688//2Tu3Ln06NGD5s2b06lTJ8aNG8fPP/9cDJXmFx0dzcKFC0tk3WJMjqVdgMjtaNmyJa+99lqB02rVqlXi269RowZRUVHUr1+/xLd1J0lJSeHZZ5/F1dWVMWPGULt2bf7880/Wrl1L//79WbduHU2bNi3tMgvUuXNnoqKiqFix4m2tJyEhgZEjR+Lq6srQoUNp2LAhFy5cICIigmeeeYaVK1fSqlWrYqo6z7vvvkvnzp2LdZ1ibAp5KdMqVqyIr69vqW3f2dm5VLdfWj777DNOnjzJV199RfXq1c3ju3btyuOPP86KFStYtGhRKVZYuCpVqlClSpXbWkdmZiZjx46lUqVKvP/++xZfGB599FECAgJ4/fXX+fTTT7G3V4eplB61PrkrxMXFERQUROvWrWnatCk9evTggw8+ME+PiYmhXbt2rFy5knbt2tGjRw/S0tLw9vYmJiaGsWPH0qJFC9q1a8ebb75JdnY2kL+7fuLEibz88stERETQpUsXfHx8CAwM5Ndff7WoZ926dfj5+eHj48PQoUPZtGkT3t7enDp1CsjrCh8zZgzt2rWjefPmPPvss+zfv7/Q97dv3z68vb3Zs2cPTz/9ND4+Pvj7+/PNN99YzHf+/HleffVV2rZtS4sWLfjXv/7FyZMnzdMXL16Mv78/ISEhtG7dmv79+xe4vfPnzwOQm5trMb5cuXJMnDiRRx991GL8xYsXGTdunPkzDAkJISsryzz97NmzTJo0iQ4dOvDggw/SoUMH3nzzTTIzMy0+54iICLp27crDDz/M999/D8DevXvp168fPj4+PPLIIyxatIicnJxCP6vru+u7du3KihUrmD59Om3btjX3DiUnJxe6ji+//JKjR4/yyiuv5OsRcHFx4dVXX6Vnz54W6/j444/p3bs3zZo149FHHyUyMtJiuRu1ta5du3L69GnWrVuHt7c3AKmpqUyePJkOHTrg4+PD008/zWeffVZo3XL3UchLmWYymcjOzi7w56ozZ84wePBg3NzcWLRoEUuXLqVBgwZMnz6dhIQE83xXrlwhJiaGefPmMXbsWFxdXQEICQmhSpUqhIWFMXDgQNasWUN0dHShNX399dds3ryZyZMnM3fuXH777TcmTpxonh4VFcXMmTN59NFHWbp0KXXr1mXatGkW65g0aRInTpxg9uzZhIWF4erqyqhRo7h48aLVz2P8+PF069aNxYsXU6VKFYKCgjhy5AgA6enpDB48mAMHDjBlyhTeeust/vzzTwYNGsSlS5fM6zh8+DAHDx5k8eLF/Otf/ypwOx06dMDe3p6BAweycuVKEhISzIHfo0cPevfubTH/ypUr8fDwICwsjP79+xMREWH+kpWbm8vIkSP56aefmD59OitXruTJJ59kzZo1REVFWaxn0aJFTJgwgX//+980bdqUb775hqCgIOrUqcOSJUsYMWIEq1evZtasWVY/p+v95z//4fLlyyxYsIBXXnmFTz75hGXLlhU6/969e3FwcODhhx8ucHr79u0ZM2aM+QvApk2bGD9+PG3atGHZsmU89dRTzJ49m5UrV1osZ62tLVmyhOrVq9OjRw/z5zJnzhy+/fZbJk+ezH/+8x8aNWrEmDFj8n2plLuYSaSMGjRokMnLy6vQn/T0dJPJZDLt3LnTNGTIEFNmZqZ52aSkJJOXl5cpMjLSZDKZTBs3bjR5eXmZPv30U4tteHl5mUaOHGkx7qmnnjKNGjXKZDKZTCdPnrRY7rXXXjM1btzYlJiYaJ4/IiLC5OXlZbpw4YLJZDKZOnbsaHrttdcs1jlq1CiTl5eX6eTJkyaTyWRq3ry56d133zVPT0xMNIWGhprOnDlT4Gfx7bffmry8vExz5841j8vIyDB17NjRNHHiRJPJZDK9//77piZNmph++eUX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\n",
      "text/plain": [
       "<Figure size 576x360 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "x_positions = [1, 2, 3, 4]\n",
    "chart_labels = [\"Q1\",\"Q2\",\"Q3\",\"Q4\"]\n",
    "earnings_actual =[.4, .15,.29,.41]\n",
    "earnings_estimate = [.37,.15,.32,.41 ]\n",
    "\n",
    "plt.figure(figsize=(8, 5))\n",
    "ax2 = plt.subplot()\n",
    "sns.set_style('whitegrid')\n",
    "ax2.set_title('Earnings per Share in Cents', fontsize = 16, y=1.05)\n",
    "plt.scatter(range(len(x_positions)), earnings_actual, color='blue', marker='+')\n",
    "plt.scatter(range(len(x_positions)), earnings_estimate, color='red', alpha=0.5)\n",
    "ax2.set_xticks(range(len(x_positions)))\n",
    "ax2.set_xticklabels(chart_labels)\n",
    "ax2.set_ylabel('Cent', fontsize = 15)\n",
    "ax2.set_xlabel('Quarter in 2017', fontsize = 15)\n",
    "\n",
    "plt.legend(['Actual', 'Estimate'], loc='lower right', fontsize = 15)\n",
    "plt.savefig(\"netflix_quarterly_earnings_per_share_sctatterdia.png\")\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "collapsed": true
   },
   "source": [
    "## Graph Literacy\n",
    "\n",
    "+ What do the purple dots tell us about the actual and estimate earnings per share in this graph? Hint: In color theory red and blue mix to make purple.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# actual and estimate values are the same. For better readability I have changed one of the markers."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    " "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    " "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 7"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Next, we will visualize the earnings and revenue reported by Netflix by mapping two bars side-by-side. We have visualized a similar chart in the second Matplotlib lesson [Exercise 4](https://www.codecademy.com/courses/learn-matplotlib/lessons/matplotlib-ii/exercises/side-by-side-bars).\n",
    "\n",
    "As you may recall, plotting side-by-side bars in Matplotlib requires computing the width of each bar before hand. We have pasted the starter code for that exercise below. \n",
    "\n",
    "1. Fill in the `n`, `t`, `d`, `w` values for the revenue bars\n",
    "2. Plot the revenue bars by calling `plt.bar()` with the newly computed `x_values` and the `revenue_by_quarter` data\n",
    "3. Fill in the `n`, `t`, `d`, `w` values for the earnings bars\n",
    "4. Plot the revenue bars by calling `plt.bar()` with the newly computed `x_values` and the `earnings_by_quarter` data\n",
    "5. Create a legend for your bar chart with the `labels` provided\n",
    "6. Add a descriptive title for your chart with `plt.title()`\n",
    "7. Add labels to each quarter by assigning the position of the ticks through the code provided. Hint:  `plt.xticks(middle_x, quarter_labels)`\n",
    "8. Be sure to show your plot!\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 576x360 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# The metrics below are in billions of dollars\n",
    "revenue_by_quarter = [2.79, 2.98,3.29,3.7]\n",
    "earnings_by_quarter = [.0656,.12959,.18552,.29012]\n",
    "quarter_labels = [\"Q1\",\"Q2\",\"Q3\",\"Q4\"]\n",
    "\n",
    "plt.figure(figsize=(8, 5))\n",
    "plt.xlabel('Quarter in 2017', fontsize = 15)\n",
    "plt.ylabel('Billions of Dollars', fontsize = 15)\n",
    "# Revenue\n",
    "n = 1  # This is our first dataset (out of 2)\n",
    "t = 2 # Number of dataset\n",
    "d = 4 # Number of sets of bars\n",
    "w = 0.8 # Width of each bar\n",
    "bars1_x = [t*element + w*n for element\n",
    "             in range(d)]\n",
    "plt.bar(bars1_x, revenue_by_quarter, label='Revenue')\n",
    "\n",
    "# Earnings\n",
    "n = 2  # This is our second dataset (out of 2)\n",
    "t = 2 # Number of dataset\n",
    "d = 4 # Number of sets of bars\n",
    "w = 0.8 # Width of each bar\n",
    "bars2_x = [t*element + w*n for element\n",
    "             in range(d)]\n",
    "plt.bar(bars2_x, earnings_by_quarter, label='Earnings')\n",
    "sns.set_style('whitegrid')\n",
    "\n",
    "\n",
    "middle_x = [ (a + b) / 2.0 for a, b in zip(bars1_x, bars2_x)]\n",
    "labels = [\"Revenue\", \"Earnings\"]\n",
    "plt.legend(labels, fontsize = 15)\n",
    "plt.title('Netflix Revenue and Earnings by Quarter in 2017', fontsize = 16, y=1.05)\n",
    "plt.xticks(middle_x, quarter_labels)\n",
    "plt.savefig(\"netflix_quarterly_revenue_and_earnings_blockdia.png\")\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Graph Literacy\n",
    "What are your first impressions looking at the visualized data?\n",
    "\n",
    "- Does Revenue follow a trend?\n",
    "- Do Earnings follow a trend?\n",
    "- Roughly, what percentage of the revenue constitutes earnings?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# both revenue and earnings show an increasing trend. \n",
    "# Increase in earnings is generally higher than increase in revenue.\n",
    "# Earnings percentage is increasing from ~2% to ~8%"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 8\n",
    "\n",
    "In this last step, we will compare Netflix stock to the Dow Jones Industrial Average in 2017. We will accomplish this by plotting two line charts side by side in one figure. \n",
    "\n",
    "Since `Price` which is the most relevant data is in the Y axis, let's map our subplots to align vertically side by side.\n",
    "- We have set up the code for you on line 1 in the cell below. Complete the figure by passing the following arguments to `plt.subplots()` for the first plot, and tweaking the third argument for the second plot\n",
    "    - `1`-- the number of rows for the subplots\n",
    "    - `2` -- the number of columns for the subplots\n",
    "    - `1` -- the subplot you are modifying\n",
    "\n",
    "- Chart the Netflix Stock Prices in the left-hand subplot. Using your data frame, access the `Date` and `Price` charts as the x and y axes respectively. Hint: (`netflix_stocks['Date'], netflix_stocks['Price']`)\n",
    "- Assign \"Netflix\" as a title to this subplot. Hint: `ax1.set_title()`\n",
    "- For each subplot, `set_xlabel` to `\"Date\"` and `set_ylabel` to `\"Stock Price\"`\n",
    "- Chart the Dow Jones Stock Prices in the left-hand subplot. Using your data frame, access the `Date` and `Price` charts as the x and y axes respectively. Hint: (`dowjones_stocks['Date'], dowjones_stocks['Price']`)\n",
    "- Assign \"Dow Jones\" as a title to this subplot. Hint: `plt.set_title()`\n",
    "- There is some crowding in the Y axis labels, add some space by calling `plt.subplots_adjust(wspace=.5)`\n",
    "- Be sure to `.show()` your plots.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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u3Zl165dBAUFcfXqVe655x5cXV0B+PXXX/n0009xcXFhxowZ+Y7Vu3dvvvvuO2rVqsXZs2extbXF2dmZfv364eDgQMWKFbl48WK+40DWL+bbb7+d/bWzszPdu3fn66+/5ttvv2XJkiU4Ozvz9ttvc/To0QKJ+bc7uc5+/fpx991389133+Up1j9/lnr27Mlzzz3H7t2783zXqbjGvtX3tEqVKrz++utUrVqVSpUqAVC/fn3uuusuAgMDKVeuHPb29tjZ3fnHS/fu3YmIiGDAgAGUKVMGi8XCSy+9RJUqVRg3bhwZGRkATJ8+nYsXL5Kens6TTz5JXFwcI0eOxNPTM0/X6uLiwvz583njjTeIi4sjIyOD+vXrM3PmTK5cucKkSZP48MMPcXJy4p133uHcuXN8+OGHNG7cmPvuuy9PMa/36quvsmPHDlxcXOjVqxeDBw8mMzOTFi1acM899wAwYMAAhg8fzhtvvJGvWDt27CA4OBgbGxsyMjIYM2YM9957L2+99dYNn0uvvfYa48ePx8bGhooVK/LEE0/k+1rl1opLW1Va2ykwrq1SO6V2qqS3U1B0bZVR7ZTJcv2tJ5ECFhwczJQpU7K7No0WHR3NSy+9xKeffmp0KqVKbGws69at45FHHiE1NZX77ruPTz/9lGrVqhVazJ07d7J8+fLsGWpERPKqOLVVaqcKh9opuR2r6CkSAfjpp5+YO3cu06dPNzqVUqdcuXIcOnSIhx9+GJPJxIABAwq1oRERKY3UThUetVNyO+opEhERERERq2YVEy2IiIiIiIjciooiERERERGxaiqKRERERETEqqkoEsmjrl27Ur9+fZYuXXrT14cNG0b9+vXzPK3qP50/f561a9dmfx0cHMyrr75aIOcWEZHSR+2USO6pKBLJB3t7e3766acbtsfFxbFz584CjTV+/Hg2b95coOcUEZHSTe2USO6oKBLJh7Zt27J7924uX76cY/svv/xCs2bNCjSWJooUEZE7pXZKJHdUFInkg7+/PxUqVODXX3/Nsf3HH3+kd+/eObatX7+efv360axZM+6++27mzJlDeno6kLXAW9OmTfn111/p2bMnzZs3JzAwkD179gDw8ssvs337dr799lvq16+ffc6kpCReeukl/P39adOmDdOnT89eTVtERETtlEjuqCgSyQeTyUT37t1zDE24fPkyu3fvpkePHtnbfv75Z8aMGUOvXr1YtWoVL730EiEhIbz55pvZ+6SlpTF37lymTZuWPf57/PjxWCwWXn31VVq2bEmvXr3YsmVL9jHr1q2jRo0arF69mpdffpmQkBDWrFlTBFcuIiIlgdopkdxRUSSSTz179mTnzp3Ex8cDWQ1LQEAAFSpUyN5nwYIF9OrViyeffJJatWrRu3dvnnvuOZYvX05iYiKQNexg7NixtGzZkkaNGjFixAhOnz7NlStXcHNzw97eHicnJypWrJh9Xn9/f0aNGoW3tzcPPfQQvr6+HDp0qGjfABERKdbUToncnooikXxq0aIF5cqVY/369cDNhyQcO3aMgICAHNtatWpFeno6J06cyN5Wq1at7P93c3MDsu7M3cr1+wOULVuWlJSUvF2IiIiUSmqnRG5PRZFIPplMJnr06MFPP/3E5cuX2bdvH/fee2+OfZycnG447u8x1XZ2dtnbHBwcbtjv3x5ctbG58VdYD7qKiMj11E6J3J6KIpEC0LNnT7Zt28aqVato3bo1np6eOV6vU6cOe/fuzbFt79692Nvb4+Pjk6sYJpOpwPIVERHronZK5N+pKBIpAAEBAZQtW5a5c+feMCQBYOTIkfz4448sXLiQU6dO8eOPPzJ79mwGDBiQPfzgdlxcXIiMjCQqKqqg0xcRkVJO7ZTIv1NRJFIAbGxs6NGjB6mpqdxzzz03vN6pUydmzJjBqlWruP/++3nnnXd47LHH7mil70ceeYSTJ0/Su3dvYmJiCjJ9EREp5dROifw7k0UDO0VERERExIqpp0hERERERKyaiiIREREREbFqKopERERERMSqqSgSERERERGrpqJIRERERESsmooiERERERGxaiqKRERERETEqqkoEhERERERq/b/HYN4uIFkF6YAAAAASUVORK5CYII=\n",
      "text/plain": [
       "<Figure size 1008x360 with 2 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Left plot Netflix\n",
    "plt.figure(figsize=(14, 5))\n",
    "\n",
    "\n",
    "ax1 = plt.subplot(1,2,1)\n",
    "sns.lineplot(data = netflix_stocks, x = netflix_stocks['Month'], y = netflix_stocks['Price'], sort=False)\n",
    "sns.set_style('whitegrid')\n",
    "ax1.set_title('Netflix', fontsize = 16, y=1.05)\n",
    "ax1.set_xlabel('Month', fontsize = 15)\n",
    "ax1.set_ylabel('Stock Price', fontsize = 15)\n",
    "\n",
    "\n",
    "# Right plot Dow Jones\n",
    "ax2 = plt.subplot(1, 2, 2)\n",
    "sns.lineplot(data = dowjones_stocks, x = dowjones_stocks['Month'], y = dowjones_stocks['Price'], sort=False)\n",
    "sns.set_style('whitegrid')\n",
    "ax2.set_title('Dow Jones', fontsize = 16, y=1.05)\n",
    "ax2.set_xlabel('Month', fontsize = 15)\n",
    "ax2.set_ylabel('Stock Price', fontsize = 15)\n",
    "\n",
    "\n",
    "plt.subplots_adjust(wspace=.2)\n",
    "plt.savefig(\"netflix_dow-jones_stock_price_linedia.png\")\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- How did Netflix perform relative to Dow Jones Industrial Average in 2017?\n",
    "- Which was more volatile?\n",
    "- How do the prices of the stocks compare?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# both had more or less steady trends upward. Netflix increased by ~40%, Dow Jones by ~25%\n",
    "# Netflix stocks were more volatile\n",
    "# Dow Jones is an index, therefore an aggregation of stock prices"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    " "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Step 9\n",
    "\n",
    "It's time to make your presentation! Save each of your visualizations as a png file with `plt.savefig(\"filename.png\")`.\n",
    "\n",
    "As you prepare your slides, think about the answers to the graph literacy questions. Embed your observations in the narrative of your slideshow!\n",
    "\n",
    "Remember that your slideshow must include:\n",
    "- A title slide\n",
    "- A list of your visualizations and your role in their creation for the \"Stock Profile\" team\n",
    "- A visualization of the distribution of the stock prices for Netflix in 2017\n",
    "- A visualization and a summary of Netflix stock and revenue for the past four quarters and a summary\n",
    "- A visualization and a brief summary of their earned versus actual earnings per share\n",
    "- A visualization of Netflix stock against the Dow Jones stock (to get a sense of the market) in 2017\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
