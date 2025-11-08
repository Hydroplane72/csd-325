```mermaid
flowchart TD
%% --- Node Definitions and Connections ---
Start((Start)):::terminatorStart --> p1[Import Libraries]:::process
p1 --> d1{Bext Installed?}:::decision
d1 -- No --> io1[/Display Error - Install Bext/]:::inputOutput
io1 --> End((Exit)):::terminatorFinish
d1 -- Yes --> p2[Set up constants]:::process
p2 --> p3[Set up settings]:::process
p3 ---> mainF((Main)):::terminatorStart

%% --- Class Definitions ---
%% Process Rectangle: Blue (white text)
classDef process fill:#0066cc,stroke:#333,color:#fff;

%% Decision Diamond: Orange (White Text)
classDef decision fill:#ff9900,stroke:#333,color:#fff;

%% Database Can: Yellow (Black Text)
classDef database fill:#ffeb3b,stroke:#333,color:#000;

%% Input/Output Parallelagram: Purple (White Text)
classDef inputOutput fill:#9933cc,stroke:#333,color:#fff;

%% Terminator Circle: Green for Start, Red for Finish (White Text)
classDef terminatorStart fill:#4CAF50,stroke:#333,color:#fff;
classDef terminatorFinish fill:#F44336,stroke:#333,color:#fff;
```

```mermaid
flowchart TD
    Start(("Main Start")) --> createForest(("Create New Forest"))
    createForest --> p1["Clear Screen"]
    p1 --> p2["Initalize While Loop"]
    p2 --> displayForest(("displayForest"))
    displayForest --> p3@{ label: "Initalize 'nextForest' dictionary" }
    p3 --> p4["For each x,y in nextForest"]
    d4{"does x,y already exist"} -- no --> d1{"is x,y EMPTY and RAND &lt;= GrowChance"}
    d1 -- no --> d2{"is x,y TREE and RAND &lt;= FireChance"}
    d2 -- no --> d3{"is x,y FIRE"}
    d3 -- no --> p5["Set x,y to same value as last forest"]
    d4 -- yes --> p11{"All x,y done?"}
    d1 -- yes --> p6["Set x,y to TREE"]
    d2 -- yes --> p7["Set x,y to FIRE"]
    p5 --> p11
    p6 --> p11
    p7 --> p11
    p8["Set x,y to EMPTY"] --> p11
    d8{"neighbor Cell= Tree?"} -- Yes --> p9["Set neighbor to FIRE"]
    p9 --> n2["Done Iterating NeigborCells?"]
    p11 -- no --> p4
    p11 -- yes --> p12["Sleep"]
    p12 --> displayForest
    io1[/"Press Cntr-C"/] --> End(("Exit"))
    n1["For EAch Neighbor Cell"] --> d8
    n2 -- No --> n1
    n2 -- YEs --> p8
    d3 -- Yes --> n1
    d8 -- No --> n2
    p4 --> d4

    p3@{ shape: rect}
    n2@{ shape: diam}
    n1@{ shape: rect}
     Start:::terminatorStart
     createForest:::terminatorStart
     p1:::process
     p2:::process
     displayForest:::terminatorStart
     p3:::process
     p4:::process
     d4:::decision
     d1:::decision
     d2:::decision
     d3:::decision
     p5:::process
     p11:::decision
     p6:::process
     p7:::process
     p8:::process
     d8:::decision
     p9:::process
     n2:::decision
     p12:::process
     io1:::inputOutput
     End:::terminatorFinish
     n1:::process
    classDef database fill:#ffeb3b,stroke:#333,color:#000
    classDef inputOutput fill:#9933cc,stroke:#333,color:#fff
    classDef terminatorStart fill:#4CAF50,stroke:#333,color:#fff
    classDef terminatorFinish fill:#F44336,stroke:#333,color:#fff
    classDef process fill:#0066cc, stroke:#333, color:#fff
    classDef decision fill:#ff9900, stroke:#333, color:#fff



```

```mermaid
flowchart TD
    Start(("Start createNewForest")) --> n1["Initialize Forest Variable using global setting values"]
    p1["For x,y"] --> d1{"Rand * 100 &lt;= Initial Tree Density"}
    d1 -- no --> p2["x,y=EMPTY"]
    d1 -- yes --> p3["x,y=TREE"]
    p2 --> n2["Done iterating?"]
    p4["return=Forest"] --> End(("End"))
    n1 --> p1
    p3 --> n2
    n2 -- No --> p1
    n2 -- Yes --> p4

    n2@{ shape: diam}
     Start:::terminatorStart
     n1:::process
     p1:::process
     d1:::decision
     p2:::process
     p3:::process
     n2:::decision
     p4:::process
     End:::terminatorFinish
    classDef database fill:#ffeb3b,stroke:#333,color:#000
    classDef inputOutput fill:#9933cc,stroke:#333,color:#fff
    classDef terminatorStart fill:#4CAF50,stroke:#333,color:#fff
    classDef terminatorFinish fill:#F44336,stroke:#333,color:#fff
    classDef process fill:#0066cc, stroke:#333, color:#fff
    classDef decision fill:#ff9900, stroke:#333, color:#fff



```

```mermaid
flowchart TD
    Start(("Start displayForest")) --> n6["Initialize Bext(0,0)"]
    p1["For x,y"] --> d1{"is x,y TREE"}
    d1 -- no --> d2{"is x,y FIRE"}
    d2 -- no --> d3{"is x,y EMPTY"}
    d1 -- yes --> p2["Set bext fg = green"]
    d2 -- yes --> p3["Set bext fg = red"]
    d3 -- yes --> p4["Log Console = {space}"]
    p4 --> d4{"all x,y done?"}
    d4 -- no --> p1
    io1[/"Display Grow Chance"/] --> n4[/"Display Lightning Chance"/]
    p2 --> n1@{ label: "<span style=\"color:\">Log console = A</span>" }
    p3 --> n2["Log console = @"]
    n1 --> d4
    n2 --> d4
    n4 --> n5["Display How to stop program"]
    n5 --> End(("End"))
    n6 --> p1
    d4 -- Yes --> n7["Reset Bext fg"]
    n7 --> io1

    n1@{ shape: rect}
    n2@{ shape: rect}
    n5@{ shape: lean-r}
     Start:::terminatorStart
     n6:::process
     p1:::process
     d1:::decision
     d2:::decision
     d3:::decision
     p2:::process
     p3:::process
     p4:::inputOutput
     d4:::decision
     io1:::inputOutput
     n4:::inputOutput
     n1:::inputOutput
     n2:::inputOutput
     n5:::inputOutput
     End:::terminatorFinish
     n7:::process
    classDef decision fill:#ff9900,stroke:#333,color:#fff
    classDef database fill:#ffeb3b,stroke:#333,color:#000
    classDef terminatorStart fill:#4CAF50,stroke:#333,color:#fff
    classDef terminatorFinish fill:#F44336,stroke:#333,color:#fff
    classDef inputOutput fill:#9933cc, stroke:#333, color:#fff
    classDef process fill:#0066cc, stroke:#333, color:#fff



```