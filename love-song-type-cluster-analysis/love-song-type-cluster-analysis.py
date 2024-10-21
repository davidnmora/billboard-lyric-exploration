import marimo

__generated_with = "0.8.0"
app = marimo.App(width="medium")


@app.cell
def __():
    import marimo as mo
    import pandas as  pd
    import numpy as np
    return mo, np, pd


@app.cell
def __(pd):
    FINALIZED_LOVE_SONG_DATA_PATH = './data/full data with love song types.csv' # note: assume you're in the root directory
    df = pd.read_csv(FINALIZED_LOVE_SONG_DATA_PATH)
    df
    return FINALIZED_LOVE_SONG_DATA_PATH, df


@app.cell
def __(pd):
    LYRICS_PATH = './data/lyric-fetching-datasets/2.6 OUTPUT lyrics for all songs.csv'
    lyrics = pd.read_csv(LYRICS_PATH)
    lyrics
    return LYRICS_PATH, lyrics


@app.cell
def __(mo):
    mo.md(r"""# Merge lyrics and data""")
    return


@app.cell
def __(df, lyrics):
    merged = lyrics.merge(
        on=['song_id'],
        right=df,
        how="inner"
    )
    len(df) - len(merged)
    return merged,


@app.cell
def __(merged):
    merged
    return


@app.cell
def __(merged):
    merged
    return


@app.cell
def __(merged):
    embed_df = merged[
        ['song_id', 'lyrics', 'love_song_sub_type']
    ]
    embed_df
    return embed_df,


@app.cell
def __(embed_df):
    embed_df.to_csv('./data/lyrics-with-love-song-types-for-NOMIC.csv', index=False)
    return


@app.cell
def __():
    return


if __name__ == "__main__":
    app.run()
