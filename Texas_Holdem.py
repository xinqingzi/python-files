class Card():
	values = (None, None, "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace")
	suits = ("spades", "hearts", "diamonds", "clubs")
	
	def __init__(self, value, suit):
		self.value = value
		self.suit = suit
		
	def __gt__(self, card2):
		if self.value > card2.value:
			return True
		return False
			
	def __lt__(self, card2):
		if self.value < card2.value:
			return True
		return False
			
	def __repr__(self):
		return self.values[self.value] + " of " + self.suits[self.suit]
		
class Hand():
	def __init__(self, list):
		self.list = list
	
	def is_there_a_number(self, value):
		list = []
		for i in self.list:
			if i.value == value:
				list.append(i)
		return list
		
	def is_there_a_suit(self, suit):
		list = []
		for i in self.list:
			if i.suit == suit:
				list.append(i)
		return list
		
	def is_there_a_straight(self, n):
		result = []
		firstlist = self.is_there_a_number(n)
		secondlist = self.is_there_a_number(n + 1)
		thirdlist = self.is_there_a_number(n + 2)
		fourthlist = self.is_there_a_number(n + 3)
		fifthlist = self.is_there_a_number(n + 4)
		for a in firstlist:
			for b in secondlist:
				for c in thirdlist:
					for d in fourthlist:
						for e in fifthlist:
							list = [a, b, c, d, e]
							result.append(list)													
		return result
		
	def same_suit(self, list):
		for i in list:
			if list[0].suit != i.suit:
				return False
		return True
								
	def is_royal_flush(self):
		list = self.is_there_a_straight(10)
		for i in list:
			if self.same_suit(i):
				return True
		return False
		
	def is_straight_flush(self):
		for i in range(2, 11):
			list = self.is_there_a_straight(i)
			for j in list:
				if self.same_suit(j):
					return True
		return False
		
	def is_four_of_a_kind(self):
		for i in range(2, 15):
			list = self.is_there_a_number(i)
			if len(list) == 4:
				return True
		return False		
		
	def is_full_house(self):
		for i in range(2, 15):
			list = self.is_there_a_number(i)
			if len(list) >= 3:
				from itertools import chain
				rest = chain(range(2, i), range(i+1, 15))
				for j in rest:
					list = self.is_there_a_number(j)
					if len(list) >= 2:
						return True
		return False
	
	def is_flush(self):
		for i in range(0, 3):
			list = self.is_there_a_suit(i)
			if len(list) >= 5:
				return True
		return False
		
	def is_straight(self):
		for i in range(2, 11):
			list = self.is_there_a_straight(i)
			if list != []:
				return True
		return False
		
	def is_three_of_a_kind(self):
		for i in range(2, 15):
			list = self.is_there_a_number(i)
			if len(list) >= 3:
				return True
		return False
		
	def is_two_pairs(self):
		for i in range(2, 15):
			list = self.is_there_a_number(i)
			if len(list) >= 2:
				from itertools import chain
				rest = chain(range(2, i), range(i+1, 15))
				for j in rest:
					list = self.is_there_a_number(j)
					if len(list) >= 2:
						return True
		return False
		
	def is_one_pair(self):
		for i in range(2, 15):
			list = self.is_there_a_number(i)
			if len(list) >= 2:
				return True
		return False
		
	def is_high_card(self):
		return True
			
	def biggest_value(self):
		for i in range(14, 1, -1):
			if self.is_there_a_number(i) != []:
				return i		
			
	def assign_points(self):
		if self.is_royal_flush():
			return 23
		elif self.is_straight_flush():
			return 22
		elif self.is_four_of_a_kind():
			return 21
		elif self.is_full_house():
			return 20
		elif self.is_flush():
			return 19
		elif self.is_straight():
			return 18
		elif self.is_three_of_a_kind():
			return 17
		elif self.is_two_pairs():
			return 16
		elif self.is_one_pair():
			return 15
		else:
			return self.biggest_value()		
								
	def __gt__(self, hand2):	
		if self.assign_points() > hand2.assign_points():
			return True
		return False
	
	def __lt__(self, hand2):
		if self.assign_points() < hand2.assign_points():
			return True
		return False
	
	def __repr__(self):
		if self.assign_points() == 23:
			return "royal flush"
		elif self.assign_points() == 22:
			return "straight flush"
		elif self.assign_points() == 21:
			return "four of a kind"
		elif self.assign_points() == 20:
			return "full house"
		elif self.assign_points() == 19:
			return "flush"
		elif self.assign_points() == 18:
			return "straight"
		elif self.assign_points() == 17:
			return "three of a kind"
		elif self.assign_points() == 16:
			return "two pairs"
		elif self.assign_points() == 15:
			return "one pair"
		elif self.assign_points() < 15:
			return "high card"

from random import shuffle	
class Deck():
	def __init__(self):
		self.cards = []
		for i in range(2, 15):
			for j in range(0, 4):
				self.cards.append(Card(i, j))
		shuffle(self.cards)
				
	def remove_a_card(self):
		if self.cards == 0:
			return
		return self.cards.pop()
		
class Player():
	def __init__(self, name, money):
		self.name = name
		self.money = money
		self.gain = 0
		self.bet = 0
		self.cards = []
		
class Texas_Holdem():
	def __init__(self):
		self.deck = Deck()
		name1 = input("Player1 name: ")
		print()
		money1 = input("{}, How much money do you have for Texas Hold'em?".format(name1))
		print()
		name2 = input("Player2 name: ")
		print()
		money2 = input("{}, How much money do you have for Texas Hold'em?".format(name2))
		print()
		name3 = input("Player3 name: ")
		print()
		money3 = input("{}, How much money do you have for Texas Hold'em?".format(name3))
		
		self.player1 = Player(name1, int(money1))
		self.player2 = Player(name2, int(money2))
		self.player3 = Player(name3, int(money3))
			
	def draw_cards_to_players(self):
		self.player1.cards = []
		self.player2.cards = []
		self.player3.cards = []
		card1 = self.deck.remove_a_card()
		self.player1.cards.append(card1)
		card2 = self.deck.remove_a_card()
		self.player2.cards.append(card2)
		card3 = self.deck.remove_a_card()
		self.player3.cards.append(card3)
		card4 = self.deck.remove_a_card()
		self.player1.cards.append(card4)
		card5 = self.deck.remove_a_card()
		self.player2.cards.append(card5)
		card6 = self.deck.remove_a_card()
		self.player3.cards.append(card6)
		
		print("{} draw {}.".format(self.player1.name, self.player1.cards))
		for i in range(50):
			print()
		print("{} draw {}.".format(self.player2.name, self.player2.cards))
		for i in range(50):
			print()
		print("{} draw {}.".format(self.player3.name, self.player3.cards))
		for i in range(50):
			print()
		
	def fold(self, player):
		self.remainingPlayers.remove(player)
		
		
		
	def call(self, player):
		m = self.betrecord - player.bet
		self.betting(player, m)
		
		
	def Raise(self, player):
		m = 0
		while m < 2 * self.betrecord:
			print()
			m = input("{}, You have to double at least, how much do you want to raise?".format(player.name))
			m = int(m)
		if player.money < m:
			print()
			print("Unfortunately, you don't have enough money, and you only have{}. Please choose again.".format(player.money))
			self.choice_supplement(player)
		else:		
			self.betrecord = m
			m = m - player.bet
			self.betting(player, m)		
		
		
	def bet_list(self, list):
		a = []
		for i in list:
			a.append(i.bet)
		return a
		
	def same_value_in_the_list(self,list):
		result = all(element == list[0] for element in list)
		return result
			
						
	def choice_supplement(self, player):
		c = input("{}, please choose 'call', 'raise' or 'fold': ".format(player.name))
		if c == "fold":
			self.fold(player)
		elif c == "call":
			self.call(player)
		elif c == "raise":
			self.Raise(player)
			if len(self.remainingPlayers) == 3:
				index = self.remainingPlayers.index(player)
				if index == 1:
					self.remainingPlayers.insert(0, self.remainingPlayers.pop())
			l = self.remainingPlayers[:]
			l.remove(player)
			for i in l:
				if self.same_value_in_the_list(self.bet_list(self.remainingPlayers)):
					break
				self.choice_supplement(i)
		else:
			self.invalid_message()
			self.choice_supplement(player)
		
	
	def choice(self, player):
		if player not in self.remainingPlayers:
			pass
		else:
			self.choice_supplement(player)
		
		
	def betting(self, player, money):
		player.money -= money
		self.communityMoney += money
		player.bet += money
		print("{} put ${}.".format(player.name, money))
		print()		
	
	def first_round_of_betting(self):
		self.choice(self.player3)
		
	def check(self):
		print()
		self.rearrange_order_of_players_for_new_bettings()
		for i in self.remainingPlayers:
			a = 'start'
			while a != 'yes' and a!= 'no':
				a = input("{}, you have the option to check. Do you want to check or not? Please type 'yes' or 'no': ".format(i.name))
				print()
				if a == 'yes':
					pass
				elif a =='no':
					return i
				else:
					self.invalid_message()
					
	def invalid_message(self):
		print("You respond is invalid, please type again.")		
		
	def rearrange_order_of_players_for_new_bettings(self):
		list = [self.player1, self.player2, self.player3]
		for i in list:
			if i not in self.remainingPlayers:
				list.remove(i)
		self.remainingPlayers = list
		
	def next_player(self, player):
		if player == self.remainingPlayers[-1]:
			return self.remainingPlayers[0]
		else:
			index = self.remainingPlayers.index(player)
			index += 1
			return self.remainingPlayers[index]
		
	def check_fold(self):
		self.rearrange_order_of_players_for_new_bettings()
		print(len(self.remainingPlayers))
		l = self.remainingPlayers[:]
		for i in l:
			c = "start"
			if self.only_one_player():
				break
			while c != 'yes' and c != 'no':
				c = input("{}, do you want to fold or not? Please type'yes' or 'no': ".format(i.name))
				if c == "yes":
					self.fold(i)
				elif c == 'no':
					pass
				else:
					self.invalid_message()		
	
	def second_to_fourth_round_of_betting(self):
		self.player1.bet = 0
		self.player2.bet = 0
		self.player3.bet = 0
		self.check_fold()
		if self.only_one_player():
			pass
		else:
			player = self.check()
			if player == None:
				pass
			else:
				m = 0
				while m < 10:
					print()
					m = input("{}, how much do you want to bet? This is a 5-10 game, so minimum will be $10.".format(player.name))
					m = int(m)
					if m >= 10:
						self.betting(player, m)
						self.betrecord = m
					else:
						self.invalid_message()
						
				player = self.next_player(player)
				self.choice(player)
				
				for i in self.remainingPlayers:
					if i.bet == 0:
						self.choice(i)
						
	def flop(self):
		self.deck.remove_a_card()
		print()
		print("Dealer drop a card.")
		for i in range(3):
			i = self.deck.remove_a_card()
			self.communityCards.append(i)
		print("Dealer then draw three community cards. They are: {}.".format(self.communityCards))
		
	def turn(self):
		self.deck.remove_a_card()
		print()
		print("Dealer drop a card.")
		card = self.deck.remove_a_card()
		self.communityCards.append(card)
		print("Dealer then draw the fourth community cards which is: {}. The community cards we know are: {}".format(card, self.communityCards))
		
	def river(self):
		self.deck.remove_a_card()
		print()
		print("Dealer drop a card.")
		card = self.deck.remove_a_card()
		self.communityCards.append(card)
		print("Dealer then draw the fifth community cards which is: {}. The total five community cards are: {}".format(card, self.communityCards))
		
	def only_one_player(self):
		if len(self.remainingPlayers) == 1:
				winner = self.remainingPlayers[0]
				winner.money += self.communityMoney
				print("{} won this round, got ${} back, and hold ${} now.".format(winner.name, self.communityMoney, winner.money))
				return True		
					
	def play_the_game(self):
		while len(self.deck.cards) >= 14:
			print()
			print("The game starts! Remember this is a 5-10 game!")
			print()
			self.communityMoney = 0
			self.player1.bet = 0
			self.player2.bet = 0
			self.player3.bet = 0
			self.remainingPlayers = [self.player1, self.player2, self.player3]
			self.communityCards = []
			for i in self.remainingPlayers:
				print("{} have ${} left.".format(i.name, i.money))
			self.betting(self.player1, 5)
			self.betting(self.player2, 10)
			self.betrecord = 10
			self.draw_cards_to_players()
			self.first_round_of_betting()
			if self.only_one_player():
				continue
			self.flop()
			self.second_to_fourth_round_of_betting()
			if self.only_one_player():
				continue
			self.turn()
			self.second_to_fourth_round_of_betting()
			if self.only_one_player():
				continue
			self.river()
			self.second_to_fourth_round_of_betting()
			if self.only_one_player():
				continue
			
			self.winning_message()
	
	def winner(self):
		cardsList = []
		playerList = []
		for i in self.remainingPlayers:
			cards = i.cards + self.communityCards
			print("{} hold {}.".format(i.name, Hand(cards)))
			
			cardsList.append(cards)
			playerList.append(i)
				
		if len(self.remainingPlayers) == 3:
			list0 = cardsList[0]
			list1 = cardsList[1]
			list2 = cardsList[2]
			if Hand(list0) > Hand(list1) and Hand(list0) > Hand(list2):
				p = playerList[0]
				p.money += self.communityMoney 
				return p
			elif Hand(list1) > Hand(list0) and Hand(list1) > Hand(list2):
				p = playerList[1]
				p.money += self.communityMoney 
				return p
			elif Hand(list2) > Hand(list1) and Hand(list2) > Hand(list0):
				p = playerList[2]
				p.money += self.communityMoney 
				return p
		else:
			list0 = cardsList[0]
			list1 = cardsList[1]
			if Hand(list0) > Hand(list1):
				p = playerList[0]
				p.money += self.communityMoney 
				return p
			elif Hand(list1) > Hand(list0):
				p = playerList[1]
				p.money += self.communityMoney 
				return p
			
			
				
	def winning_message(self):
		winner = self.winner()
		if winner == None:
			print("it was a tie.")
			n = len(self.remainingPlayers)
			m = self.communityMoney / n
			for i in self.remainingPlayers:
				i.money += m
				print("{} got ${} back, now hold ${}.".format(i.name, m, i.money))
			for i in [self.player1, self.player2, self.player3]:
				if i in self.remainingPlayers:
					pass
				else:
					print("{} now hold ${}".format(i.name, i.money))
			
		else:
			print("{} won this round, got ${} back, and hold${} now.".format(winner.name, self.communityMoney, winner.money))
			for i in [self.player1, self.player2, self.player3]:
				if i == winner:
					pass
				else:
					print("{} have ${} left.".format(i.name, i.money))
			
				
			
				
				
				
				 
				
				
			
			

game1 = Texas_Holdem()
game1.play_the_game()				
						
								
																							
																		
