#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv
import pandas as pd
import ipaddress
from typing import List, Dict, Any, Optional


# In[2]:


class FileReader:
    """
    Base class for file readers
    """
    def __init__(self, file_path: str):
        self.file_path = file_path

    """
    Reads the file and returns a pandas dataframe.
    Must be implemented by subclass.
    """
    def read(self) -> pd.DataFrame:
        raise NotInplementedError("Subclass must implement read method")


# In[3]:


class CSVReader(FileReader):
    """
    Reads CSV files and returns a pandas dataframe
    """
    def read(self) -> pd.DataFrame:
        return pd.read_csv(self.file_path)
    
        


# In[4]:


class ExcelReader(FileReader):
    """
    Reads Excel files and returns a pandas dataframe
    """
    def read(self, sheet_name: Optional[int] = 0) -> pd.DataFrame:
        return pd.read_excel(self.file_path, sheet_name=sheet_name)


# In[5]:


class DataProcessor:
    """
    Class containing static methods for processing data.
    """
    @staticmethod
    def extract_columns(df: pd.DataFrame, columns: List[str]) -> pd.DataFrame:
        """
        Extracts specified columns from a DataFrame
        Returns an empty DataFrame if columns are not found.
        """
        return df[columns] if set(columns).issubset(df.columns) else pd.DataFrame()


    @staticmethod
    def unique_column_value(df1: pd.DataFrame, df2: pd.DataFrame, column: str) -> pd.DataFrame:
        """
        Compares a specified column between two DataFrames and returns unique values as a new DataFrame
        """
        if column in df1.columns and column in df2.columns:
            unique_values = set(df1[column]) - set(df2[column])
            return pd.DataFrame({column: list(unique_values)})
        return pd.DataFrame

    @staticmethod
    def count_event_occurrence(df: pd.DataFrame, event_column: str, event_value: str) -> int:
        """
        Counts occurrences of a specified event in a given column of a DataFrame.
        """
        if event_column in df.columns:
            return (df[event_column] == event_value).sum()
        return 0


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




