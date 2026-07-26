# TAKOVA — Website institucional

> **Soluções que Transformam, Tecnologia que Resolve**
> Lichinga, Niassa — Moçambique

Site institucional multi-página da **Takova**, construído como HTML/CSS/JS estático
(sem build, sem dependências de servidor). Carrega depressa em qualquer dispositivo
e publica-se em qualquer alojamento. Fiel ao *Takova Design System* — cores, a fonte
de marca **Melfira**, tipografia Roboto, tokens de espaçamento/sombra/movimento — com
animações temáticas que respeitam `prefers-reduced-motion`.

---

## ⚠️ ANTES DE PUBLICAR — substitua estes dados de exemplo

| Onde | Ficheiro | O que mudar |
|---|---|---|
| **WhatsApp** (número real) | `assets/js/main.js` → objecto `TAKOVA` | `whatsapp` (só dígitos, ex.: `25884XXXXXXX`) e `whatsappLabel` |
| **Facebook** | `assets/js/main.js` → `TAKOVA` | `facebookUrl` e `facebookLabel` |
| **Email** | `assets/js/main.js` → `TAKOVA` | `email` (actualmente `geral@takova.co.mz`, a confirmar) |
| **Localização / horário** | `assets/js/main.js` (`location`) e `contacto.html` (horário) | morada e horário reais |
| **Estatísticas** | `index.html`, `sobre.html` | `+250`, `24h`, etc. — ajuste aos números reais |
| **Domínio** (og:image, og:url, canonical, JSON-LD) | `<head>` de cada página | já configurado com **`https://www.takova.co.mz`** — se o domínio real for outro, faça *localizar/substituir* em todas as páginas. É o que faz a pré-visualização no Facebook/WhatsApp funcionar |

> **Tudo o que é contacto está centralizado num único sítio:** o objecto `TAKOVA`
> no topo de `assets/js/main.js`. Mude lá e o site inteiro (botões de WhatsApp,
> rodapé, página de contacto) actualiza-se sozinho.

O formulário de contacto **abre o WhatsApp** com a mensagem já preenchida — não precisa
de servidor nem de backend.

---

## Estrutura

```
takova-website/
├── index.html          Início (herói, serviços, trabalhos científicos, Somara, sobre, CTA)
├── servicos.html       Serviços em detalhe + "como trabalhamos"
├── sobre.html          História, missão, visão, números, valores
├── somara.html         App Somara (gamificada) — funcionalidades, módulos, planos, FAQ
├── contacto.html       Canais, formulário (WhatsApp) e mapa
├── README.md           este ficheiro
└── assets/
    ├── css/styles.css  tokens da marca + componentes + animações + responsivo
    ├── js/main.js      navegação, revelar-ao-scroll, contadores, WhatsApp  ← editar contactos aqui
    ├── fonts/Melfira-Regular.ttf
    └── img/            emblema, wordmark, 4 fotos de serviço (optimizadas), sprite de ícones
```

## Ver localmente

Os ícones estão embutidos em cada página, por isso o site funciona mesmo abrindo
`index.html` directamente no browser. Para uma pré-visualização 100 % igual à de
produção (e para o mapa carregar), sirva por HTTP a partir desta pasta:

```bash
python -m http.server 8000      # depois abra http://localhost:8000
```
(ou a extensão **Live Server** do VS Code, ou `npx serve`.)

## Publicar

É um site estático — basta enviar a pasta `takova-website/` para qualquer alojamento:

- **Netlify / Vercel / Cloudflare Pages** — arraste a pasta (deploy instantâneo).
- **GitHub Pages** — coloque os ficheiros no repositório e active Pages.
- **Alojamento tradicional (cPanel/FTP)** — envie o conteúdo para `public_html/`.

Não há passo de build.

## Personalização

- **Cores / tipografia / espaçamento / movimento** — tokens CSS em `:root` no topo de
  `assets/css/styles.css` (ex.: `--green-700`, `--gold-500`, `--font-display`).
- **Imagens de serviço** — em `assets/img/` (versões `-1200` e `-640` para `srcset`).
  Para trocar, mantenha os nomes ou actualize os `src`/`srcset` no HTML.
- **Animações** — secção *ANIMATIONS* em `styles.css`. Todo o movimento colapsa
  automaticamente quando o utilizador tem *“reduzir movimento”* activado.
- **Ícones** — [Lucide](https://lucide.dev) (traço) + marcas WhatsApp/Facebook
  ([Simple Icons](https://simpleicons.org)), embutidos como sprite SVG.

## Acessibilidade & desempenho

- Português pré-Acordo (pré-1997), conforme o brandbook da marca.
- Contraste **WCAG AA** (texto dourado a ≥ 4,5:1), `alt` em imagens, `label` em formulários, navegação por teclado, *skip link*.
- **SEO:** título/descrição por página, Open Graph + canonical, e dados estruturados `JSON-LD` (`ProfessionalService`) — telefone/email/Facebook sincronizam-se a partir do objecto `TAKOVA` em `main.js`.
- Imagens optimizadas (1,8 MB → ~60–140 KB) com `loading="lazy"`, `width/height` e `srcset`.
- Fonte Melfira auto-alojada (`font-display: swap`); Roboto via Google Fonts.
- O conteúdo aparece mesmo sem JavaScript (as revelações só se escondem quando há JS).

---

*Construído sobre o Takova Design System (handoff Claude Design). Melfira © Takova.*
