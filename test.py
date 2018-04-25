import pandas as pd

df = pd.read_csv("sample.csv")


def oneway(g):
    return(
        pd.Series({
            "measure1": g.measure1.sum(),
            "measure2": g.measure2.sum(),
            "count": len(g),
            "measure1_percent": g.measure1.sum()/df.measure1.sum(),
            "ratio": g.measure1.sum()/g.measure2.sum(),
            "ratio_relativity":
            (g.measure1.sum() / g.measure2.sum()) /
            (df.measure1.sum()/df.measure2.sum())
            })
    )


df.groupby("dimension1").apply(oneway)

list(df)

df.head()

df_reshape = pd.melt(df,
                     id_vars=['dimension1', 'dimension2'],
                     value_vars=['measure1', 'measure2'])

df_index = (df_reshape.groupby(['dimension1', 'dimension2', 'variable'])
                      .agg({'value': 'sum'}))

df_index.pivot(index=['dimension1', 'dimension2'],
               columns='variable', values='value')
