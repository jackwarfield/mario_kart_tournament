import subprocess
from itertools import combinations

import numpy as np
import pandas as pd

def main() -> int:
  subprocess.call("rm -f match????.json", shell=True,)

  df = pd.read_csv("./participantlist.csv")
  drivers = df.Driver.values

  matches = []
  for match in combinations(drivers, r=4):
    matches += [np.array(match)]
  matches = np.array(matches)
  np.random.shuffle(matches)

  for i,match in enumerate(matches):
    with open(f"match{i+1:0>4}.json", "w") as f:
      print("{", file=f)
      print("\t\"Drivers\":{", file=f)
      for name in match:
        if name != match[-1]:
          print("\t\t\""+name+"\": 0,", file=f)
        else:
          print("\t\t\""+name+"\": 0", file=f)
      print("\t}\n}", file=f)

  return 0

if __name__ == '__main__':
  raise SystemExit(main())
