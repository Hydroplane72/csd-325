``` mermaid
flowchart TD
 subgraph s1["Get User Input"]
        n1["Ask for a positive integer"]
        n2["Is value less than or = 0"]
  end
 subgraph s2["Recursive function calls"]
        n3["Pass User input to recursive function"]
        n4["Is number less than or = 0?"]
        n6["Pass target number and currentNumber +1 to recursive function"]
        n8["Init current number = 1 if not already set"]
        n9["Output Current call info"]
        n10["Is current number less than target number?"]
        n11["Return function"]
  end
 subgraph s3["Non recursive function"]
        n15["Is target number less than or = 0"]
        n16["Return"]
        n17["Add 1 to current number"]
        n18["Init current number"]
        n19["Output current number"]
        n20["Is current number &lt;= targetNumber?"]
        n21["Return function"]
  end
    A(["Start"]) --> n1
    n1 --> n2
    n2 -- Yes --> n1
    n2 -- No --> n13["Output Calling Recursive function"]
    n3 --> n8
    n4 -- Yes --> n11
    n4 -- No --> n9
    n8 --> n4
    n9 --> n10
    n10 -- Yes --> n6
    n10 -- No --> n11
    n11 --> n12["output Done calling recursive function"]
    n13 --> n3
    n12 --> n14["Output Calling non recursive function"]
    n14 --> n15
    n15 --> n16 & n18
    n6 --> n8
    n18 --> n17
    n17 --> n19
    n19 --> n20
    n20 -- No --> n21
    n20 -- Yes --> n17
    n21 --> n22["Output finished non recursive function"]

    n2@{ shape: diam}
    n4@{ shape: diam}
    n10@{ shape: diam}
    n20@{ shape: diam}



```