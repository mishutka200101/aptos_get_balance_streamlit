# from starknet_balancer import *
from aptos_balancer import *
from file_handler import *
from multiprocessing import Pool


def get_balance(df: pd.DataFrame):
    # logger.info(f"Начата обработка аккаунтов {filename.split('.')[0]}...")

    items = df.index.values

    processes = 40 if len(items) >= 40 else len(items)

    with Pool(processes=processes) as p:
        result = p.map(func=get_aptos_ballance, iterable=items)

    # for i in items:
    #     balance = get_aptos_ballance(address=i)
    #     logger.success(f"{i} : {balance}")
    #     dfpd.at[i, 'amount in USDT'] = balance

    # write_to_excel(dfpd, filename=filename)

    for i in result:
        df.at[i[0], 'amount in USDT'] = i[1]

    return df


# if __name__ == "__main__":
#     get_balance('aptos.xlsx')
