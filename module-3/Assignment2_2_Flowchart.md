``` mermaid
---
config:
  theme: redux
---
flowchart TD
    A(["Initialize Numbers"]) --> n1["Output game description"]
    n1 --> n2["Initialize purse amount"]
    n5["Output: Asking how much to bet"] --> n6["Take user input"]
    n6 --> n7["Did user ask to quit?"]
    n7 -- No --> n9["Is user input a decimal?"]
    n7 -- Yes --> n4["End program"]
    n9 -- Yes --> n10["Is user input larger than purse amount"]
    n9 -- No --> n11["Output: Please enter a number"]
    n11 --> n6
    n10 -- No --> n12["Set user input to int variable named pot"]
    n10 -- Yes --> n13["Output: You do not have enough to make that bet"]
    n13 --> n6
    n12 --> n14["Roll dice 1"]
    n14 --> n15["Roll disc 2"]
    n15 --> n16["Output: Game description of dice rolling"]
    n16 --> n17["Get user input and assign to bet variable"]
    n17 --> n18["Is bet equal to CHO or HAN?"]
    n18 -- Yes --> n19["Output Game description of cup dice reveal"]
    n18 -- No --> n20["Output: Please enter CHO or HAN"]
    n20 --> n17
    n19 --> n21["Is roll even?"]
    n21 --> n22["Set variable CorrectBet = HAN"] & n23["Set variable CorrectBet = CHO"]
    n23 --> n24["Is CorrectBet equal to userBet?"]
    n22 --> n24
    n24 -- No --> n25["Output: Player Lost"]
    n24 -- Yes --> n26["Output: Player Won"]
    n26 --> n27["Has user ran out of money?"]
    n25 --> n27
    n27 -- Yes --> n28["Output: You have run out of money"]
    n28 --> n4
    n2 --> n5
    n27 -- No --> n5
    n7@{ shape: diam}
    n9@{ shape: diam}
    n4@{ shape: terminal}
    n10@{ shape: diam}
    n18@{ shape: diam}
    n21@{ shape: diam}
    n24@{ shape: diam}
    n27@{ shape: diam}

```