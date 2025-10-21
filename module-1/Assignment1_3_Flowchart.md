# Main Function
``` mermaid
flowchart TD
        A(["Start"]) --> n1["Ask User for number of bottles"]
    n1 --> n2{"Is Value Valid?"}
    n2 -- No --> n1
    n2 -- Yes --> n3["Call OutputBeers function"]
    n3 --> n4["Remind user to buy more beer"]
    n4 --> n5(["Finish"])
```

# OutputBeers Function
``` mermaid
flowchart TD
    A(["Start"]) --> n1["Save Input pNumberBeers to localVariable NumberBeers"]
    n1 --> n2{"Is NumberBeers = 1"}
    n5["Output Number of beers on wall"] --> n6["Subtract 1 beer from NumberBeers"]
    n2 -- No --> n5
    n2 -- Yes --> n7["Output 1 beer on the wall"]
    n6 --> n10["Output subtracting 1 beer"]
    n7 --> n8["Output subtracting 1 beer"]
    n8 --> n9(["Finish Function"])
    n10 --> n2
```