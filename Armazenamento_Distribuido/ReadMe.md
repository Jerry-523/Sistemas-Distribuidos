**Sistema de Armazenamento Distribuído**

Este repositório contém um sistema distribuído para facilitar o upload e download de arquivos entre clientes e servidores. O sistema permite que os usuários compartilhem arquivos de forma eficiente através de uma interface amigável.

---

**Funcionamento:**

O sistema segue uma arquitetura cliente-servidor, onde os clientes interagem com um servidor central para acessar serviços de upload e download de arquivos. A comunicação entre o cliente e o servidor é realizada por meio de solicitações HTTP sobre a rede.

O servidor atua como o ponto central do sistema, gerenciando as solicitações dos clientes e coordenando o armazenamento e recuperação de arquivos. Ele fornece endpoints para lidar com operações de upload e download, bem como para listar os arquivos disponíveis para download.

Os clientes são a interface de usuário através da qual os usuários interagem com o sistema. Eles podem enviar arquivos para o servidor através da função de upload, selecionar arquivos para download e visualizar a lista de arquivos disponíveis para download no servidor.

---

**Diretórios:**

- **server:** Contém o código-fonte do servidor implementado em python.
- **client:** Contém os arquivos necessários para o cliente, incluindo HTML e JavaScript para a interface de usuário.
- **files:** Diretório onde os arquivos enviados pelos clientes são armazenados no servidor.

---

**Funcionalidades a serem Implementadas:**

1. **Upload de Arquivos:** Permitir que os clientes enviem arquivos para o servidor através de uma interface intuitiva.
2. **Download de Arquivos:** Permitir que os clientes baixem arquivos do servidor, escolhendo a partir de uma lista de arquivos disponíveis.
3. **Listagem de Arquivos:** Fornecer uma funcionalidade para listar os arquivos disponíveis para download no servidor.
4. **Interface de Usuário Responsiva:** Desenvolver uma interface de usuário atraente e responsiva para melhorar a experiência do usuário.
5. **Segurança:** Implementar medidas de segurança para proteger os dados transferidos entre o cliente e o servidor.

---

**Implementação da API:**

No futuro, está prevista a implementação de uma API para gerenciar diferentes instâncias do servidor. Essa API pode incluir funcionalidades como monitoramento de saúde, escalabilidade automática, configuração dinâmica e registro de eventos. A API proporcionará uma maneira flexível e eficiente de gerenciar e monitorar o sistema distribuído.