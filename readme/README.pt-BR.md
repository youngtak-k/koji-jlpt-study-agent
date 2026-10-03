# Koji — JLPT Study Agent

Estude para o JLPT N5–N1 com seu próprio livro, no seu idioma. Tire dúvidas difíceis, escolha tarefas que caibam no seu dia e retome de onde parou.

## Comece com uma pergunta

**Em um chat de IA que você já usa:** envie ou cole o [guia do Koji](../agent/COACH.md) e faça sua pergunta. Inclua a frase, as alternativas e sua resposta quando necessário. Use um trecho curto ou uma foto legível que o chat consiga processar.

> Siga este guia do Koji. Explique em português do Brasil. Escolhi B, mas o gabarito diz C. Aqui estão o texto e meu raciocínio. Por que C é melhor?

**No Codex ou Claude Code com acesso a arquivos:** [baixe este repositório](https://github.com/youngtak-k/koji-jlpt-study-agent/archive/refs/heads/main.zip), descompacte e abra a pasta. Peça:

> Leia AGENTS.md e me ajude a estudar com o Koji. Explique em português do Brasil e mantenha minhas notas nesse idioma. Aqui está minha dúvida sobre o livro.

Você pode escrever qualquer um desses pedidos no seu idioma. Não precisa de servidor do Koji, aplicativo separado, instalação do Python ou chave de API do projeto. É necessário ter acesso a um assistente de IA que consiga ler o guia; os limites e custos desse serviço continuam valendo.

## Ou escolha o que estudar hoje

Diga ao Koji qual seção do livro está aberta e quanto tempo você tem. Informe o nível do JLPT desejado, caso ele ainda não saiba.

> Estou estudando para o N3. Estou no início desta seção de gramática e tenho 25 minutos. Me ajude a escolher o que estudar hoje.

O Koji propõe onde começar, onde parar e uma divisão do tempo que inclui revisão, perguntas e um breve encerramento. Só o título do livro não basta para deduzir páginas ou conteúdo. Você pode começar com uma seção antes de planejar toda a preparação para o exame.

## Encerre com uma mensagem

> Terminei as questões 1–4 em 18 minutos. Precisei de uma dica na questão 3. A próxima é a 5.

O Koji resume o que você realmente fez, o que ainda está incerto e onde retomar. Fazer uma pergunta não conta automaticamente como erro; uma resposta com dica continua diferente de uma resposta independente.

Com acesso funcional aos arquivos, o Koji salva e verifica seu registro atual em `local/CURRENT.md`, com notas complementares das sessões. Em um chat comum, fornece uma nota de estudo curta e atualizada para você salvar. Gerar uma nota não significa salvá-la automaticamente no seu dispositivo.

## Volte e continue

> Vamos continuar. Hoje tenho 15 minutos.

Mantenha a mesma pasta de estudos ou forneça sua última nota salva no novo chat. O Koji usa evidências anteriores relevantes para sugerir uma revisão curta e a próxima tarefa do livro. Por exemplo, pode verificar rapidamente, sem ajuda, uma distinção que você resolveu com uma dica antes de seguir adiante.

Depois de uma pausa, avise:

> Fiquei uma semana sem estudar. Hoje tenho 10 minutos.

O Koji parte do progresso confirmado e reduz a tarefa para caber no tempo. Os dias sem estudar não viram horas extras de recuperação obrigatória. Você também pode pedir uma revisão semanal, corrigir um registro, exportar sua nota atual ou dizer “não salve esta sessão”.

## Suas notas crescem com seus estudos

O guia é o fermento inicial; seu estudo fornece o material. Explicações úteis que se repetem podem virar páginas de conhecimento interligadas, separadas das evidências do que você consegue responder. Você não precisa organizar pastas nem manter um segundo caderno por conta própria.

Seus arquivos de estudo ficam em `local/`, excluído do Git por padrão. Preserve essa pasta ao atualizar o Koji; substitua os arquivos do guia compartilhado, não seus registros de aprendizado. Armazenamento local não significa processamento de IA offline. O Koji trabalha durante suas conversas, sem lembretes em segundo plano nem sincronização automática entre cópias.

As explicações e notas seguem suas preferências de idioma, com exemplos em japonês e leituras de kanji. O guia é escrito em inglês. As traduções do README foram feitas por IA e não passaram por revisão independente de falantes nativos; a edição em inglês é a referência.

## Idiomas do README

- [English](../README.md)
- [한국어](README.ko.md)
- [日本語](README.ja.md)
- [Español](README.es.md)
- [Français](README.fr.md)
- [Deutsch](README.de.md)
- [简体中文](README.zh-CN.md)
- [繁體中文](README.zh-TW.md)
- [Português (Brasil)](README.pt-BR.md)
- [Italiano](README.it.md)
- [Русский](README.ru.md)
- [Українська](README.uk.md)
- [Polski](README.pl.md)
- [Nederlands](README.nl.md)
- [Svenska](README.sv.md)
- [Dansk](README.da.md)
- [Norsk (bokmål)](README.no.md)
- [Suomi](README.fi.md)
- [Čeština](README.cs.md)
- [Türkçe](README.tr.md)
- [Bahasa Indonesia](README.id.md)
- [Tiếng Việt](README.vi.md)
- [ไทย](README.th.md)
- [हिन्दी](README.hi.md)
- [বাংলা](README.bn.md)
- [العربية](README.ar.md)
- [فارسی](README.fa.md)
- [עברית](README.he.md)
- [Bahasa Melayu](README.ms.md)
- [Filipino](README.tl.md)
