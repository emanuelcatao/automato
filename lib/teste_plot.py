def plotar(self):
        G = nx.DiGraph()
        labels = {}
        edge_labels = {}

        for estado in self.estados:
            G.add_node(estado.nome)
            labels[estado.nome] = estado.nome

            if estado.is_inicial:
                G.nodes[estado.nome]['shape'] = '8'
                G.nodes[estado.nome]['color'] = 'green'
            elif estado.is_final:
                G.nodes[estado.nome]['shape'] = 'o'
                G.nodes[estado.nome]['color'] = 'red'
            else:
                G.nodes[estado.nome]['shape'] = 'o'
                G.nodes[estado.nome]['color'] = 'lightblue'

        for origem, transicoes in self.transicoes.items():
            for transicao in transicoes:
                G.add_edge(origem.nome, transicao.destino.nome, label=transicao.simbolo)
                edge_labels[(origem.nome, transicao.destino.nome)] = transicao.simbolo  # Adicionando legenda da aresta


        pos = nx.spring_layout(G, seed=60)
        options = {
            'node_size': 500,
            'node_color': [G.nodes[n]['color'] for n in G.nodes()],
            'edge_color': 'black',
            'width': 2,
            'arrowstyle': '-|>',
            'arrowsize': 12,
            'with_labels': True,
            'font_size': 12,
            'font_color': 'black',
            'font_weight': 'bold'
        }

        nx.draw_networkx(G, pos, labels=labels, **options)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10)  # Adicionando as legendas das arestas
        
        for (u, v), symbols in edge_labels.items():
            for symbol in symbols:
                label = '\n'.join(symbol)
                if u == v:
                    x, y = pos[u]
                    plt.text(x + 0.1, y + 0.1, label, ha='center', fontsize=10)  # Adicionando legenda de autoloop
        
        plt.title('Autômato Finito Determinístico')
        plt.axis('off')
        plt.show()