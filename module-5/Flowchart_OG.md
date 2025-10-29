``` mermaid
---
config:
  theme: redux
  layout: dagre
---
flowchart TD
    A(["Set constants"]) --> n1["Create new currentForest"]
    n1 --> n3["Display Forest"]
    n6["Is Cell Empty?"] -- Yes --> n7["Is Grow chance larger than random number?"]
    n6 -- No --> n8["Is cell a Tree?"]
    n7 -- Yes --> n9["Grow tree in cell"]
    n7 -- No --> n16["Have all cells been examined?"]
    n8 -- Yes --> n11["Is fire chance larger than random number?"]
    n8 -- No --> n12["Is cell on fire?"]
    n11 -- Yes --> n13["Set tree as on fire"]
    n11 -- No --> n16
    n12 -- Yes --> n14["Find trees nearby and set on fire"]
    n12 -- No --> n16
    n14 --> n15["Set current cell as empty"]
    n16 -- No --> n5["Next Forest Cell"]
    n16 -- Yes --> n3
    n5 --> n6
    n9 --> n16
    n13 --> n16
    n15 --> n16
    n3 --> n5
    n6@{ shape: diam}
    n7@{ shape: diam}
    n8@{ shape: diam}
    n16@{ shape: diam}
    n11@{ shape: diam}
    n12@{ shape: diam}

```