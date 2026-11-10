-- ------------------------------
-- OPTION
-- ------------------------------

OPTION IMPORT;

-- ------------------------------
-- TABLE: disciplina
-- ------------------------------

DEFINE TABLE disciplina TYPE ANY SCHEMALESS PERMISSIONS NONE;




-- ------------------------------
-- TABLE DATA: disciplina
-- ------------------------------

INSERT [ { carga_horaria: 33, codigo: '13', descricao: 'Estudo da comunicação escrita, interpretação de textos, gramática e produção textual.', id: disciplina:3klccpl9j5xhus6n5u4t, nome: 'Português  Instrumental I', periodo: 1 }, { carga_horaria: 33, codigo: '21', descricao: 'Estudo de conceitos matemáticos aplicados à computação, incluindo raciocínio lógico, funções e resolução de problemas.', id: disciplina:a3g7u18p6lircwbevhxk, nome: 'Matemática  Aplicada à  Computação', periodo: 2 }, { carga_horaria: 67, codigo: '14', descricao: 'Introdução à lógica de programação, algoritmos, estruturas condicionais, estruturas de repetição e resolução de problemas computacionais.', id: disciplina:f0cjbdae2hvpxyvanwll, nome: 'Algoritmos e  Lógica de  Programação', periodo: 1 }, { carga_horaria: 33, codigo: '24', descricao: 'Aprofundamento das técnicas de comunicação, interpretação e produção de textos, com foco na linguagem acadêmica e profissional.', id: disciplina:fxuni5hay5sg37ajy4wj, nome: 'Português  Instrumental II', periodo: 2 }, { carga_horaria: 60, codigo: 'ADS001', descricao: 'Teste de duplicidade', id: disciplina:gqm57ll6u8mx5z75vwx8, nome: 'Outra Lógica de Programação', periodo: 1 }, { carga_horaria: 33, codigo: '22', descricao: 'Aprofundamento da leitura e interpretação de textos em inglês, com foco em conteúdos e terminologias da área de tecnologia.', id: disciplina:h5v48cj58041uxxrmx7h, nome: 'Inglês  Instrumental II', periodo: 2 }, { carga_horaria: 100, codigo: '26', descricao: 'Introdução à programação orientada a objetos, abordando classes, objetos, atributos, métodos, encapsulamento, herança e polimorfismo.', id: disciplina:hc01pf5es3hvgo3h2o86, nome: 'Programação  Orientada a  Objetos', periodo: 2 }, { carga_horaria: 33, codigo: '12', descricao: 'Desenvolvimento de habilidades básicas de leitura e interpretação de textos em inglês, com foco em vocabulário técnico.', id: disciplina:hk1io2zkcxt7uutm26p6, nome: 'Inglês  Instrumental I', periodo: 1 }, { carga_horaria: 33, codigo: '25', descricao: 'Estudo das relações interpessoais, comunicação, ética, trabalho em equipe e comportamento no ambiente profissional.', id: disciplina:m1jc5s4u58sar63dkiau, nome: 'Relações  Humanas no  Trabalho', periodo: 2 }, { carga_horaria: 67, codigo: '11', descricao: 'Estudo de conceitos fundamentais da matemática, incluindo operações, frações, porcentagem, equações e resolução de problemas.', id: disciplina:q0l6uv7h60zsm6p3wm3q, nome: 'Matemática  Básica', periodo: 1 }, { carga_horaria: 67, codigo: '15', descricao: 'Aplicação prática dos conceitos de algoritmos e lógica de programação por meio da elaboração e execução de programas.', id: disciplina:qdrnt3gk6vbsytlbdkur, nome: 'Laboratório de  Algoritmos e  Lógica  Programação', periodo: 1 }, { carga_horaria: 67, codigo: '16', descricao: 'Apresentação dos fundamentos da computação, evolução dos computadores, hardware, software e sistemas computacionais.', id: disciplina:svl7uq3dcja2u053wjvu, nome: 'Introdução à  Computação', periodo: 1 }, { carga_horaria: 67, codigo: '27', descricao: 'Estudo dos fundamentos das redes de computadores, modelos de comunicação, protocolos, equipamentos e transmissão de dados.', id: disciplina:vg375kl99fcvew8spm2w, nome: 'Introdução à  Redes de  Computadores', periodo: 2 }, { carga_horaria: 33, codigo: '23', descricao: 'Estudo dos métodos de pesquisa científica, elaboração de trabalhos acadêmicos, produção de textos e organização de referências.', id: disciplina:ys5qrcntnjfjw5j4etc6, nome: 'Metodologia da  Pesquisa  Científica', periodo: 2 }, { carga_horaria: 100, codigo: '31', descricao: 'Estuda formas de organizar, armazenar e manipular dados de maneira eficiente.', id: disciplina:z1lig32d9ba2kfd8cukw, nome: 'Estrutura de Dados e Algoritmos', periodo: 3 } ];

-- ------------------------------
-- TABLE: prerequisito
-- ------------------------------

DEFINE TABLE prerequisito TYPE RELATION SCHEMALESS PERMISSIONS NONE;

DEFINE FIELD OVERWRITE in ON prerequisito TYPE record PERMISSIONS FULL;
DEFINE FIELD OVERWRITE out ON prerequisito TYPE record PERMISSIONS FULL;



-- ------------------------------
-- TABLE DATA: prerequisito
-- ------------------------------

INSERT RELATION [ { id: prerequisito:2hbu7tuxr8a8ex32imfo, in: disciplina:3klccpl9j5xhus6n5u4t, out: disciplina:ys5qrcntnjfjw5j4etc6 }, { id: prerequisito:8245r8b2053ph5d5nvqo, in: disciplina:q0l6uv7h60zsm6p3wm3q, out: disciplina:a3g7u18p6lircwbevhxk }, { id: prerequisito:9ray8akcj8rr0l0dtks2, in: disciplina:3klccpl9j5xhus6n5u4t, out: disciplina:fxuni5hay5sg37ajy4wj }, { id: prerequisito:agxk52ejz5acvetjb45h, in: disciplina:hk1io2zkcxt7uutm26p6, out: disciplina:h5v48cj58041uxxrmx7h }, { id: prerequisito:hy9sjyy42fz5x1v22qy1, in: disciplina:f0cjbdae2hvpxyvanwll, out: disciplina:hc01pf5es3hvgo3h2o86 }, { id: prerequisito:k8huu9z48c8vdmbmn46l, in: disciplina:qdrnt3gk6vbsytlbdkur, out: disciplina:hc01pf5es3hvgo3h2o86 }, { id: prerequisito:sf3jrczicsrfrlvmlegz, in: disciplina:svl7uq3dcja2u053wjvu, out: disciplina:vg375kl99fcvew8spm2w }, { id: prerequisito:tm8d2su22z8mm4csnhr9, in: disciplina:hc01pf5es3hvgo3h2o86, out: disciplina:z1lig32d9ba2kfd8cukw }, { id: prerequisito:u9hubh00uqetms3hlw9d, in: disciplina:svl7uq3dcja2u053wjvu, out: disciplina:hc01pf5es3hvgo3h2o86 }, { id: prerequisito:yo9s4uk8wugphsvhdb7m, in: disciplina:a3g7u18p6lircwbevhxk, out: disciplina:z1lig32d9ba2kfd8cukw } ];

