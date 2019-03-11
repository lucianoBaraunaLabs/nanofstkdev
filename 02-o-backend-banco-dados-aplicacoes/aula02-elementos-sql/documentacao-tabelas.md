# Todas as tabelas no banco de dados do zoológico

### animals
Essa tabela lista animais individuais no zoológico. Cada animal tem apenas uma linha. Pode haver diversos animais com o mesmo nome, ou até mesmo diversos animais com o mesmo nome e a mesma espécie.
- name — o nome do animal (exemplo: 'George')
- species — a espécie do animal (exemplo: 'gorilla')
- birthdate — a data de nascimento do animal (exemplo: '1998-05-18')

### diet
Essa tabela combina as espécie com os alimentos que eles podem consumir. Cada espécie no zoológico come, pelo menos, um tipo de alimento, e muitos deles comem mais de um. Se uma espécie come mais que um alimento, teremos mais que uma linha para cada espécie.
- species — o nome da espécie (exemplo: 'hyena')
- food — o nome do alimento que a espécie consome (exemplo: 'meat')

### taxonomy
Essa tabela dá os nomes taxonômicos biológicos (parciais) para cada espécie no zoológico, que podem ser utilizados para encontrar quais espécies estão relacionadas de maneira mais próxima das outras evolucionalmente.
- name — o nome comum da espécie (exemplo: 'jackal')
- species — o nome taxonômico da espécie (exemplo: 'aureus')
- genus — o nome taxonômico do gênero (exemplo: 'Canis')
- family — o nome taxonômico da família (exemplo: 'Canidae')
- t_order — o nome taxonômico da ordem (exemplo: 'Carnivora')

### ordernames
Esta tabela dá os nomes comuns para cada ordem taxonômica na tabela de taxonomy.
- t_order — o nome taxonômico da ordem (ex. 'Cetacea')
- name — o nome comum (ex. 'whales and dolphins')
