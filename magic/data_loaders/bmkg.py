import io
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API
    """
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}

    url = 'https://data.bmkg.go.id/DataMKG/MEWS/DigitalForecast/CSV/kecamatanforecast-jakarta.csv'
    response=requests.get(url,headers=headers).content
    df=pd.read_csv(io.StringIO(response.decode('utf-8')),on_bad_lines='skip', sep=';',names=["ID", "Waktu", "Suhu_Udara_Min", "Suhu_Udara_Max", "Kelembapan_Min", "Kelembapan_Max", "Kelembapan_Dalam", "Suhu_Udara_Dalam", "Cuaca_code", "Arah_Angin", "Kecepatan_Angin"])
    # response = requests.get(url,headers=headers).content
    
    # df = pd.read_csv(io.StringIO(url), sep=';')
    # print(df)
    return df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    print(len(output.columns))
    assert output is not None, 'The output is undefined'
