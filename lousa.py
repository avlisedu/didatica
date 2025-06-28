import streamlit as st
import random

st.set_page_config(page_title="Lousa Interativa - UPE Salgueiro", layout="wide")
st.markdown("## Lousa Interativa - UPE Salgueiro")
st.markdown("## Disciplina: **Gestão de Projetos**")


alunos = [
    'Lucas', 'Mariana', 'Rafael', 'Beatriz', 'Fernando',
    'Camila', 'João', 'Ana', 'Gabriel', 'Larissa',
    'Vinicius', 'Paula', 'Rodrigo', 'Jéssica', 'Thiago'
]

ideias = [
    ('Lucas', 'Produtividade é alcançar metas com eficiência.'),
    ('Mariana', 'Saber priorizar tarefas importantes.'),
    ('Rafael', 'Buscar sempre melhoria contínua.'),
    ('Beatriz', 'Reduzir desperdícios no processo.'),
    ('Fernando', 'Focar nos resultados entregues.'),
    ('Camila', 'Organização do tempo é essencial.'),
    ('João', 'A colaboração da equipe aumenta a produtividade.'),
    ('Ana', 'Automatizar atividades rotineiras.'),
    ('Gabriel', 'Ter clareza dos objetivos.'),
    ('Larissa', 'Manter disciplina nas entregas.'),
    ('Vinicius', 'Saber delegar é fundamental.'),
    ('Paula', 'Adaptação às mudanças é chave.'),
    ('Rodrigo', 'Comunicação eficaz melhora resultados.'),
    ('Jéssica', 'Planejamento evita retrabalho.'),
    ('Thiago', 'Gestão do tempo faz a diferença.')
]

cores = [
    '#FFF176', '#AED581', '#81D4FA', '#CE93D8', '#FFAB91',
    '#FFD54F', '#4DD0E1', '#F06292', '#FFF59D', '#A5D6A7',
    '#B0BEC5', '#FFE082', '#E1BEE7', '#FFCDD2', '#C5E1A5'
]

def get_rotacao():
    return random.choice([-6, -3, -2, 0, 2, 4, 7])

n_rows, n_cols = 4, 4  # Grid para até 16 cartões

# Estado inicial
if 'embaralhados' not in st.session_state:
    # Embaralha as ideias uma vez, junto com cor e rotação
    cartoes = list(zip(
        [i[0] for i in ideias],
        [i[1] for i in ideias],
        cores,
        [get_rotacao() for _ in range(len(ideias))]
    ))
    random.shuffle(cartoes)
    st.session_state.embaralhados = cartoes
    st.session_state.quantos_mostrar = 0

# Sorteia posições só uma vez
if 'posicoes' not in st.session_state or len(st.session_state.posicoes) != len(ideias):
    todas_posicoes = random.sample([(i, j) for i in range(n_rows) for j in range(n_cols)], len(ideias))
    st.session_state.posicoes = todas_posicoes

# Mostra mais cartões a cada clique
def avancar():
    # Grupo pode ser 2 ou 3, sorteando sempre que possível
    if st.session_state.quantos_mostrar < len(ideias):
        restante = len(ideias) - st.session_state.quantos_mostrar
        proximo_grupo = random.choice([2, 3]) if restante > 2 else restante
        st.session_state.quantos_mostrar += proximo_grupo

if st.button('Mostrar próximos cartões'):
    avancar()

# Resetar mural (opcional)
if st.button('Reiniciar mural'):
    cartoes = list(zip(
        [i[0] for i in ideias],
        [i[1] for i in ideias],
        cores,
        [get_rotacao() for _ in range(len(ideias))]
    ))
    random.shuffle(cartoes)
    st.session_state.embaralhados = cartoes
    st.session_state.quantos_mostrar = 0
    todas_posicoes = random.sample([(i, j) for i in range(n_rows) for j in range(n_cols)], len(ideias))
    st.session_state.posicoes = todas_posicoes

def exibir_cartoes(cartoes, posicoes):
    grid = [[None for _ in range(n_cols)] for _ in range(n_rows)]
    for idx, (aluno, texto, cor, rotacao) in enumerate(cartoes):
        i, j = posicoes[idx]
        grid[i][j] = (aluno, texto, cor, rotacao)
    for i in range(n_rows):
        cols = st.columns(n_cols)
        for j in range(n_cols):
            if grid[i][j] is not None:
                aluno, texto, cor, rotacao = grid[i][j]
                with cols[j]:
                    st.markdown(
                        f"""
                        <div style='
                            background:{cor};
                            border-radius:20px;
                            box-shadow:4px 6px 16px #aaa;
                            padding:38px 26px 28px 26px;
                            margin:24px 6px 18px 6px;
                            min-width:230px;
                            max-width:320px;
                            min-height:170px;
                            max-height:280px;
                            font-size:19px;
                            font-family: "Segoe UI", Arial, sans-serif;
                            display:inline-block;
                            transform:rotate({rotacao}deg);
                            position:relative;
                            transition: all 0.2s ease;
                            cursor: pointer;
                        '
                        onmouseover="this.style.boxShadow='0 8px 32px #666';this.style.zIndex='9999';this.style.transform='scale(1.07) rotate({rotacao}deg)';"
                        onmouseout="this.style.boxShadow='4px 6px 16px #aaa';this.style.zIndex='0';this.style.transform='rotate({rotacao}deg)';"
                        >
                        <span style='
                            font-size:26px;
                            position:absolute;
                            top:-22px; left:50%; transform:translateX(-50%);
                            '>
                            📌
                        </span>
                        <b>{aluno}</b>
                        <br><br>
                        {texto}
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
            else:
                with cols[j]:
                    st.markdown("&nbsp;")

# Exibir os cartões já liberados
qt = st.session_state.quantos_mostrar
if qt > 0:
    exibir_cartoes(st.session_state.embaralhados[:qt], st.session_state.posicoes)

# Dica de navegação
if qt < len(ideias):
    st.info("")
else:
    st.success("")

