``` mermaid
---
config:
  theme: redux
---
flowchart TD
    A(["Open sitka file"]) --> n1["Convert contents of file as CSV"]
    n1 --> n2["Read first row as header row"]
    n2 --> n3["Read next row"]
    n3 --> n4["End of Rows?"]
    n4 -- Yes --> n5["Initialize graph"]
    n4 -- No --> n6["Set current date"]
    n6 --> n7["Append current date to dates list"]
    n7 --> n8["Set high"]
    n8 --> n9["Append high to highs list"]
    n9 --> n3
    n5 --> n10["Plot the dates and highs in the graph"]
    n10 --> n11["Set graph title"]
    n11 --> n12["Set X Axis label"]
    n12 --> n14["Format the X Axis as date"]
    n14 --> n13["Set Y Axis Label"]
    n13 --> n15["Change tick marks on graph"]
    n15 --> n16["Show the graph"]
    n4@{ shape: diam}

```