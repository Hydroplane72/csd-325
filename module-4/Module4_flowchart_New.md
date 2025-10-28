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
    n9 --> n17["Set low"]
    n5 --> n19["Was Lows input?"]
    n10["Plot the dates and highs in the graph"] --> n11["Set graph High title"]
    n11 --> n12["Set X Axis label"]
    n12 --> n14["Format the X Axis as date"]
    n14 --> n13["Set Y Axis Label"]
    n13 --> n15["Change tick marks on graph"]
    n15 --> n16["Show the graph"]
    n17 --> n18["Set Low to lows list"]
    n18 --> n3
    n19 -- No --> n10
    n19 -- Yes --> n20["Plot the dates and lows in the graph"]
    n20 --> n21["Set graph low title"]
    n21 --> n12
    n22["Get User Input with prompt"] --> n23["Is user input exit?"]
    n23 -- No --> n25["Is input Highs or Lows?"]
    n25 -- Yes --> A
    n26["Output that the input was bad"] --> n22
    n25 -- No --> n27["Clear Console"]
    n27 --> n26
    n23 -- Yes --> n28["Show exit message"]
    n28 --> n24["Exit program"]
    n4@{ shape: diam}
    n19@{ shape: diam}
    n23@{ shape: diam}
    n25@{ shape: diam}


```