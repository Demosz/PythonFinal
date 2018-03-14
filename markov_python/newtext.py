from cc_markov import MarkovChain

lil = MarkovChain()
lil.add_file('markov_chain/Amilli.txt')
lil.add_file('markov_chain/6ft.txt')
lil.add_file('markov_chain/Lollipop.txt')

with open('finalcut.txt', 'w') as f:
    for i in range(10):
        f.write(' '.join(lil.generate_text()) + '\n')
