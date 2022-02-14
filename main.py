# import pendulum
# import pandas._libs.algos

# import pyximport
# pyximport.install()

from datetime import timedelta
import pandas as pd


def experiment():
    t = pd.Timestamp("2022-02-03 11:10:05.400")
    # duration = pendulum.duration(milliseconds=200)
    duration = timedelta(milliseconds=200)
    print('\n>>> C function')
    test = t.__sub__(duration)

    print('\n>>> Result inspection')
    print(f'{type(t)=} , {type(duration)=} , {type(test)=}')
    print(f'{t=} , {duration=} , {test=}')


if __name__ == '__main__':
    experiment()

# if __name__ == '__main__':
#     df = pd.DataFrame({'a': [1, 2, 3], 'v': [1, 1, 1]})
#     print("hello there")
# print(df.head())
