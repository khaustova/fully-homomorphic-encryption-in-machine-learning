import os
import pandas as pd
import tenseal as ts
from time import time
from zipfile import ZipFile


def encrypt_data(data: pd.DataFrame, filename: str, ctx_training: ts.Context) -> None:
    """
    Зашифровывает и архивирует данные по схеме CKKS.
    """
    
    t_start = time()
    rows = data.shape[0]
    zip_name = f'encrypted data//{filename}.zip'
    
    with ZipFile(zip_name, 'w') as filezip:   
        for i in range(rows):
            vector = ts.ckks_vector(ctx_training, data[i].tolist()).serialize()
            filename_with_num = f'{filename}_{i}.hex'
            
            with open(filename_with_num, 'wb') as file:
                file.write(vector)
                
            filezip.write(filename_with_num)
            os.remove(filename_with_num)
    t_end = time()
    
    print(f'Шифрование заняло {int(t_end - t_start)} секунд')
    

def get_ckks_vector(filename: str, ctx_training: ts.Context) -> list[ts.CKKSVector]:
    """
    Распаковывает и восстаналивает зашифрованные данные из архива.
    """
    t_start = time()
    zip_name = f'encrypted data//{filename}.zip'
    with ZipFile(zip_name, "r") as myzip:
        myzip.extractall(path='encrypted data')
        
    ckks_vectors_list = []  
    i = 1
    while True:
        filename_with_num = f'encrypted data//{filename}_{i}.hex'
        try:
            with open(filename_with_num, 'rb') as file:
                bytes_vector = file.read()
            ckks_vector = ts.ckks_vector_from(ctx_training, bytes_vector)
            ckks_vectors_list.append(ckks_vector)
            os.remove(filename_with_num)
            i += 1
        except:
            break
    t_end = time()
    
    print(f'Распаковка зашифрованных данных заняла {int(t_end - t_start)} секунд')
    
    return ckks_vectors_list