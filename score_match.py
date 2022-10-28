from glob import glob

import pandas as pd
import numpy as np

def main() -> int:
  df = pd.read_csv("./participantlist.csv")
  df['Points'] = 0

  matches = sorted(glob("./match????.json"))
  for fn in matches:
    m = pd.read_json(fn)
    drivers = list(m.Drivers.keys())
    points = list(m.Drivers)
    for d,p in zip(drivers, points):
      p0 = df.loc[df.Driver == d, 'Points'].values[0]
      df.loc[df.Driver == d, 'Points'] = p0+p

  df = df.sort_values(by='Points', ascending=False, ignore_index=True,)
  df.to_csv("./participantlist.csv", index=False,)
  print(df)

  return 0

if __name__ == '__main__':
  raise SystemExit(main())
