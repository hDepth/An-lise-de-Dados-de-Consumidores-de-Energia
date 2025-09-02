# CHECKPOINT 01 – Data Science e Machine Learning (Python & Orange)

Repositório preparado para a atividade "Checkpoint 01: Análise de Dados de Consumidores de Energia" da disciplina de **DISRUPTIVE ARCHITECTURES - IOT, IOB And GENERATIVE**.
Proposta pelo professor ANDRÉ TRITIACK

## 📦 Estrutura
```
.
├── notebooks/
│   └── iot_power_assignment.ipynb      # Notebook com todas as 4 partes (40 exercícios)
├── src/
│   └── utils.py                        # Funções auxiliares
├── requirements.txt                    # Dependências (ambiente sugerido)
├── .gitignore
└── README.md
```

---

## 🗂️ Conjuntos de dados (UCI Machine Learning Repository)

1) **Individual Household Electric Power Consumption**  
Link: https://archive.ics.uci.edu/dataset/235/individual+household+electric+power+consumption  
Arquivo principal: `household_power_consumption.txt` (≈ 20+ MB)

2) **Appliances Energy Prediction**  
Link: https://archive.ics.uci.edu/dataset/374/appliances+energy+prediction  
Arquivo principal: `energydata_complete.csv`

> **Importante**: coloque os arquivos na pasta `data/` (crie-a na raiz do projeto) com os nomes acima.
> O notebook já está configurado para procurar nesses caminhos:
> - `data/household_power_consumption.txt`
> - `data/energydata_complete.csv`

---

## ▶️ Como rodar

1. Crie e ative um ambiente (conda ou venv).
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Abra o Jupyter Lab/Notebook e execute `notebooks/iot_power_assignment.ipynb`.

> **Dica**: a base de energia doméstica é grande; as células já usam *tipos otimizados* e *parse incremental*.
> Em máquinas modestas, priorize reamostrar/agrupar antes de visualizações pesadas.

---

## 🧪 O que está implementado

- **Parte 1 (1–20)**: limpeza, EDA, séries temporais, correlações, *feature engineering*, K-Means, decomposição de série temporal, regressão linear.
- **Parte 2 (21–25)**: reamostragem horária, autocorrelação (1h/24h/48h), PCA 2D + *clusters*, comparação Regressão Linear vs Polinomial (grau 2).
- **Parte 3 (26–35)**: *EDA* e modelagem no dataset **Appliances** (Regressão Linear Múltipla, Random Forest; binarização e classificação com avaliação).
- **Parte 4 (36–40)**: instruções de *workflow* no **Orange Data Mining** (com respostas orientadas para as perguntas do enunciado).

Cada exercício possui um **título numerado** e células de código/markdown.  
Onde aplicável, métricas e gráficos são gerados automaticamente.

---

## 🧡 Orange Data Mining (Parte 4)
- Baixe: https://orangedatamining.com/download/  
- Catálogo de widgets: https://orangedatamining.com/widget-catalog/  
- Siga o passo-a-passo no fim do notebook para replicar o fluxo solicitado (CSV Import → Sample Data → Distribution → Scatter Plot → k-Means).

---

## Devs

- Desenvolvido por:
Pedro Henrique Jorge de Paula 
RM:558833


Obrigado! ✨
