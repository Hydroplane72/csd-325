``` mermaid
---
config:
  theme: redux
---
flowchart TD
 subgraph s1["For each Element in list"]
        n2["Print Property Values"]
  end
    A(["Main Start"]) --> n1["Load JSON in file to Class List"]
    n1 --> n10["Call PrintClassList(ClassList)"]
    n3@{ label: "Print 'Above is original List'" } --> n17["Call CreateNewClassObject( Your Firstname, Your Lastname, Fake ID, Your Email)"]
    n4["Create new class object named NewObject"] --> n5["Assign Your Name to NewObject"]
    n5 --> n6["Assign FictionalID to NewObject"]
    n6 --> n7["Assign Your email to NewObject"]
    n8["Append NewObject to ClassList"] --> n9["Call PrintClassList(ClassList)"]
    n10 --> n3
    n11(["PrintClass List Start"]) --> s1
    s1 --> n12["Finish PrintClassList"]
    n13["Rectangle"] --> n11
    n14["Start"] --> A
    n15["Start"] --> n16(["CreateNewClassObject(Firstname, Lastname, ID, Email)"])
    n16 --> n4
    n17 --> n8
    n7 --> n18["Return NewObject"]
    n18 --> n19["Untitled Node"]
    n9 --> n20["Print to user object was updated"]
    n20 --> n21["Export ClassList to Json file"]
    n21 --> n22["Untitled Node"]
    n3@{ shape: rect}
    n12@{ shape: stop}
    n13@{ shape: start}
    n14@{ shape: start}
    n15@{ shape: start}
    n19@{ shape: stop}
    n22@{ shape: stop}

```