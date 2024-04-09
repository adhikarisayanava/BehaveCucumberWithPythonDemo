Feature: The dealer hand total

Scenario Outline: Get hand total
  Given a <hand>
  When the dealer sums the cards
  Then the <total> is correct

  Examples: Hands
  | hand          | total |
  | 5,7           | 12    |
  | 5,Q           | 17    |
  | Q,Q,A         | 25    |
  | Q,A           | 13    |
  | A,A,A         | 3     |