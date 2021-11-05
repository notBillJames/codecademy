import pandas as pd
pd.options.display.max_colwidth = None

df = pd.read_csv("jeopardy.csv")
df = df.rename(columns={col: '_'.join(col.strip().lower().split()) for col in df.columns})
df['value'] = df.value.apply(lambda x: ''.join(x.strip("$").split(',')))
df['value'] = pd.to_numeric(df.value, errors='coerce')
df


def keyword_filter(df, match, search):
    return df.loc[df[search].apply(lambda x: all(word.lower() in x.lower() for word in match))].reset_index()


yuma = keyword_filter(df, ['King'], 'question')
len(yuma) == len(df)


def get_answer_counts(data):
    return data["answer"].value_counts()


obj = get_answer_counts(yuma).reset_index()
len(obj)
