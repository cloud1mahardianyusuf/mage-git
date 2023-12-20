if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    """
    Template code for a transformer block.

    Add more parameters to this function if this block has multiple parent blocks.
    There should be one parameter for each output variable from each parent block.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    # Specify your transformation logic here

    columns = {
        0: "ID", 
        1: "Waktu", 
        2: "Suhu_Udara_Min", 
        3: "Suhu_Udara_Max", 
        4: "Kelembapan_Min", 
        5: "Kelembapan_Max", 
        6: "Kelembapan_Dalam", 
        7: "Suhu_Udara_Dalam", 
        8: "Cuaca_code", 
        9: "Arah_Angin", 
        10: "Kecepatan_Angin"
    }

    df = data.rename(columns=columns)
    # print(df)
    return df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    print(len(output.columns))
    assert output is not None, 'The output is undefined'
