# Flask-SQLite3

Lembre-se de criar uma maquina virtual usando python para trabalhar com esse projeto.

Instalar VM:
python -m venv nome-do-ambiente
Acesso a VM:
nome-do-ambiente\Scripts\activate



O SQLite3 é um sistema de gerenciamento de banco de dados (SGBD) que tem suas vantagens e desvantagens, dependendo do contexto em que será usado. Abaixo estão algumas das principais vantagens e desvantagens de se usar o SQLite3:

Vantagens:

Leve e Incorporado: O SQLite3 é um SGBD incorporado, o que significa que não requer um servidor separado. Ele é uma biblioteca C que pode ser incorporada diretamente em aplicativos, tornando-o uma escolha popular para aplicativos móveis, desktop e incorporados, onde o tamanho e a simplicidade são críticos.

Simplicidade: O SQLite3 é fácil de usar e não requer configuração complicada. Você pode criar um banco de dados SQLite3 em um único arquivo e começar a usá-lo imediatamente.

Transações ACID: O SQLite3 suporta transações ACID (Atomicidade, Consistência, Isolamento e Durabilidade), garantindo que as operações no banco de dados sejam seguras e confiáveis, mesmo em situações de falha.

Ampla Disponibilidade: O SQLite3 é amplamente suportado por várias linguagens de programação, incluindo Python, C++, Java, C#, entre outras. Isso o torna uma escolha flexível para desenvolvedores.

Portátil: Os bancos de dados SQLite3 são portáteis e podem ser facilmente movidos entre sistemas operacionais e plataformas, desde que a biblioteca SQLite3 seja suportada.

Desvantagens:

Escalabilidade Limitada: O SQLite3 não é adequado para aplicativos que requerem alta escalabilidade ou manipulação simultânea por muitos usuários. Ele funciona bem para aplicativos de pequeno a médio porte, mas pode não ser a melhor escolha para aplicativos de grande escala.

Concorrência Limitada: O SQLite3 possui um bloqueio exclusivo que impede que várias operações de gravação ocorram simultaneamente. Isso pode levar a problemas de concorrência em aplicativos com muitos escritores concorrentes.

Desempenho em Grandes Conjuntos de Dados: Em comparação com alguns SGBDs mais robustos, o SQLite3 pode não ter o mesmo desempenho ao lidar com grandes conjuntos de dados ou consultas complexas.

Recursos Limitados: O SQLite3 não suporta todos os recursos encontrados em SGBDs mais avançados, como suporte a stored procedures, triggers complexos e replicação de dados.

Restrições de SQL: Algumas implementações do SQLite3 podem ter restrições na sintaxe SQL, o que significa que você pode encontrar diferenças no comportamento em comparação com outros SGBDs.

Em resumo, o SQLite3 é uma escolha sólida para muitos cenários, especialmente em aplicativos leves e incorporados, onde a simplicidade, a portabilidade e a facilidade de uso são cruciais. No entanto, para aplicativos de alto tráfego e alta concorrência, ou aqueles que exigem recursos SQL mais avançados, pode ser apropriado considerar SGBDs mais robustos. A escolha entre o SQLite3 e outros SGBDs depende das necessidades específicas do seu projeto.
