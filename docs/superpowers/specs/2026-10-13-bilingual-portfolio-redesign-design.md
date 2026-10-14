# Especificação de design — Portfólio bilíngue de Carlos França

## Objetivo

Remodelar completamente a landing page publicada em `francasense.github.io/francajr/`, substituindo a estrutura visual antiga do Mobirise por um portfólio editorial escuro, inspirado na linguagem visual de `gugamazzotti.github.io/mazzottidev-/`.

O resultado deve apresentar Carlos Henrique Castro França Júnior como Desenvolvedor Mobile Sênior, com foco em React Native, TypeScript, Android, iOS, arquitetura mobile, performance e qualidade de software. O site será bilíngue, com Português como idioma inicial e English como alternativa.

## Escopo aprovado

- Reescrever a página inicial como uma experiência de portfólio única e responsiva.
- Preservar o endereço e o processo de publicação no GitHub Pages.
- Manter as pastas legadas de projetos existentes no repositório, sem removê-las.
- Usar as informações consolidadas no currículo e no perfil do LinkedIn.
- Destacar visualmente os projetos da Méliuz e da Kahsh com imagens associadas a esses trabalhos.
- Preservar projetos históricos relevantes, como LABTRANSP, JampaBus, Plant Manager e jogos, em uma seção secundária.
- Incluir links atuais de contato e redes sociais: e-mail, LinkedIn, GitHub, Facebook e Instagram `carlos.fjr`.
- Incluir uma ação de download do currículo em PDF, com cópia local versionada no site.

Fora do escopo: backend, banco de dados, CMS, formulário que envie dados para um servidor, autenticação, analytics novo e migração das páginas legadas para o novo visual.

## Direção visual

A interface seguirá uma estética de editor/inspector técnico:

- Fundo quase preto com grid sutil construído em CSS.
- Tipografia sans-serif forte para títulos e texto monoespaçado para rótulos, metadados e marcadores de seção.
- Texto principal claro, textos auxiliares em cinza e azul elétrico como cor de destaque.
- Navegação lateral com marca, indicadores de seção e acesso ao seletor de idioma.
- Hero editorial com frases curtas, cargo, localização, modalidade de trabalho e indicadores profissionais.
- Seções identificadas por marcadores como `01 — SOBRE`, `02 — STACK` e `03 — PROJETOS`.
- Cards de projeto com imagem, categoria, papel desempenhado, descrição curta, tecnologias e link externo quando houver.
- Linha do tempo para a experiência profissional.
- Espaçamento generoso, contraste alto, foco visível e adaptação real para mobile.

A inspiração será interpretada, não copiada literalmente: a identidade, o conteúdo e a hierarquia serão próprios do perfil de Carlos.

## Arquitetura de conteúdo

### 1. Hero

Conteúdo bilíngue:

- Nome completo.
- Cargo principal: `Desenvolvedor Mobile Sênior` / `Senior Mobile Developer`.
- Especialidades: React Native, TypeScript, Android, iOS e arquitetura mobile.
- Localização: João Pessoa, PB, Brasil.
- Modalidade: remoto e aberto a oportunidades compatíveis.
- Ações: ver projetos, entrar em contato e baixar currículo.

### 2. Sobre

Resumo curto derivado do currículo e do LinkedIn, enfatizando mais de seis anos de experiência mobile, ciclo completo de produtos, arquitetura, testes, performance, integrações e colaboração com Produto, QA e Backend.

Ao lado do texto, apresentar dados compactos:

- Foco: Mobile Engineering / React Native.
- Domínios: fintech, energia, logística, governo, saúde e agronegócio.
- Base: João Pessoa, PB.
- Idiomas: Português nativo e Inglês técnico.

### 3. Stack

Agrupar as competências em blocos legíveis:

- Mobile: React Native, Android, iOS, React Navigation e deep linking.
- Arquitetura e estado: TypeScript, JavaScript, Redux, Zustand, Context API e MMKV.
- Qualidade: Jest, Testing Library, testes unitários, testes de UI, code review e documentação.
- Performance e entrega: otimização de renderização, Git, GitFlow, CI/CD, Play Store e App Store.
- Integrações: REST, Firebase, Python, Salesforce e ZEGOCLOUD.
- Processo: Scrum, Kanban, UX/UI e uso prático de IA.

### 4. Projetos em destaque

Os cards principais serão:

1. **Méliuz** — fluxos de Recargas e Gift Cards no core de uma fintech, React Native, TypeScript, performance, componentes reutilizáveis e integração com UX/UI.
2. **Kahsh** — atuação como UI Designer na criação de protótipos mobile de alta fidelidade, jornadas, acessibilidade, heurísticas, arquitetura da informação e Design System em Figma.
3. **Hitss / fiscalização agropecuária** — aplicação React Native para fiscalização, integrações com backend Python e foco em performance e qualidade.
4. **EY / energia e logística** — módulos de autoatendimento, matchmaking de fretes, APIs REST, documentação técnica e colaboração multidisciplinar.

Os dois primeiros cards devem receber as imagens correspondentes observadas no LinkedIn. As imagens serão armazenadas localmente em `assets/images/projects/meliuz/` e `assets/images/projects/kahsh/`, com textos alternativos descritivos.

### 5. Experiência

Linha do tempo bilíngue com as posições atuais do currículo:

- Hitss Brasil — Desenvolvedor Mobile Sênior III — 07/2025 até o presente.
- Ernst & Young (EY) — Especialista II e Desenvolvedor Mobile — 11/2022 a 06/2025.
- Méliuz — Especialista II — 12/2021 a 10/2022.
- Accenture Brasil — Analista Sênior — 08/2020 a 12/2021.

Cada item terá período, empresa, cargo e um resumo de uma ou duas linhas. O detalhamento completo permanecerá enxuto para preservar o caráter de portfólio.

### 6. Portfólio histórico

Uma seção mais compacta preservará trabalhos anteriores e projetos pessoais, sem competir visualmente com Méliuz e Kahsh. Cada item terá nome, imagem já existente quando disponível, contexto curto e link atual quando houver.

### 7. Contato

Encerramento com uma chamada direta para oportunidades e links para:

- `francasense@gmail.com`
- LinkedIn: `linkedin.com/in/francajunior/`
- GitHub: `github.com/francasense`
- Instagram: `instagram.com/carlos.fjr/`

## Comportamento bilíngue

O conteúdo será mantido em um objeto de traduções em JavaScript, com chaves estáveis para navegação, títulos, rótulos, descrições, projetos, experiência e contato. O HTML terá atributos `data-i18n` para os textos que mudam de idioma.

- Idioma inicial: Português.
- Alternância visível: `PT` / `EN` na navegação.
- Preferência persistida em `localStorage`.
- O seletor atualiza textos sem recarregar a página.
- O conteúdo acessível, incluindo `alt`, `aria-label`, títulos de botões e links, também será traduzido.
- O idioma não será inferido de forma a bloquear o usuário; a seleção manual sempre terá prioridade.

## Estrutura técnica proposta

O site continuará estático e sem dependências de servidor:

- `index.html`: estrutura semântica das seções e conteúdo inicial.
- `assets/css/site.css`: identidade visual, layout, animações discretas, grid e breakpoints.
- `assets/js/site.js`: alternância de idioma, navegação ativa, menu mobile e pequenas interações.
- `assets/images/projects/meliuz/`: imagens locais do projeto Méliuz.
- `assets/images/projects/kahsh/`: imagens locais do projeto Kahsh.
- `assets/docs/cv-carlos-franca-junior.pdf`: currículo para download.

Os arquivos e pastas legados continuarão no repositório para não quebrar links históricos, mas deixarão de participar da composição visual da página principal.

## Requisitos de responsividade e acessibilidade

- Desktop: navegação lateral, composição em duas colunas e cards com mídia ampla.
- Tablet: navegação compacta e redução proporcional da tipografia.
- Mobile: navegação recolhida, conteúdo em uma coluna, textos podendo quebrar em múltiplas linhas e imagens sem corte.
- Contraste mínimo adequado entre fundo, texto e destaque.
- HTML semântico, foco visível, navegação por teclado e `alt` em todas as imagens de projeto.
- Respeitar `prefers-reduced-motion` para reduzir transições e efeitos.

## Imagens e direitos de uso

As imagens da Méliuz e da Kahsh foram indicadas pelo próprio usuário como materiais publicados por ele no LinkedIn. A implementação tentará obter os arquivos originais ou versões de melhor qualidade disponíveis na sessão autenticada. Se o LinkedIn não permitir a recuperação direta dos arquivos, a publicação ficará aguardando que o usuário forneça as imagens originais, evitando hotlink frágil ou captura de baixa qualidade.

## Validação e publicação

Antes da publicação:

- Validar que todas as chaves PT/EN possuem tradução.
- Verificar ausência de textos antigos do Mobirise na página principal.
- Testar alternância de idioma, links, download do currículo e navegação por âncoras.
- Conferir o layout em desktop, tablet e mobile.
- Verificar contraste, textos alternativos e foco de teclado.
- Executar `git diff --check` e uma validação automatizada de conteúdo.
- Publicar na branch `gh-pages` somente após a verificação local e confirmação do build do GitHub Pages.

## Critérios de aceitação

O redesign será considerado concluído quando:

1. A página pública apresentar a nova identidade visual em português e inglês.
2. O seletor PT/EN alternar todo o conteúdo relevante sem recarregar a página.
3. Méliuz e Kahsh aparecerem como projetos de destaque com imagens locais e descrições fiéis ao currículo/LinkedIn.
4. Hitss, EY, Méliuz e Accenture aparecerem corretamente na linha do tempo.
5. O site funcionar em desktop, tablet e mobile sem texto cortado ou navegação quebrada.
6. Links de contato e redes sociais apontarem para os destinos atuais.
7. Os projetos históricos continuarem acessíveis na seção correspondente.
8. O build do GitHub Pages estiver concluído a partir do commit publicado.
