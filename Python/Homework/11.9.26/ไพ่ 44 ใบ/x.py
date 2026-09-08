"""ไพ่ 44 ใบ"""
card = input().upper()
rank = card[:-1]
suit = card[-1]
rank_name = {
    "A": "Ace",
    "J": "Jack",
    "Q": "Queen",
    "K": "King"
}
suit_name = {
    "D": "Diamonds",
    "H": "Hearts",
    "S": "Spades",
    "C": "Clubs"
}
if rank in rank_name:
    rank = rank_name[rank]
print(rank, "of", suit_name[suit])
