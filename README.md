# Les Plombiers Bretons — Plomberie · Dégorgement (Bretagne)

Site vitrine statique orienté conversion : **8 pages métier** (plomberie et
dégorgement × 4 départements bretons) et **58 articles de conseils
d'urgence** géolocalisés, générés à partir de gabarits uniques.

- **Téléphone :** 02 20 05 00 76 · **E-mail :** contact@les-plombiers-bretons.fr
- **Domaine prévu :** https://les-plombiers-bretons.fr (à changer dans `tools/data.py` si besoin)
- **Zones :** Côtes-d'Armor (22), Finistère (29), Ille-et-Vilaine (35), Morbihan (56)

## Générer le site

```bash
python3 tools/build.py
```

Aucune dépendance. Le script écrit toutes les pages HTML, `sitemap.xml` et
`robots.txt` à la racine. Les URL sont sans extension : chaque page est un
`index.html` dans son propre dossier, servi tel quel par n'importe quel
hébergeur (Hostinger, OVH, Netlify, GitHub Pages…).

| URL | Rôle |
| --- | --- |
| `/` | Accueil |
| `/plomberie-depannage-{dept}/` | 4 pages Plomberie |
| `/degorgement-canalisation-{dept}/` | 4 pages Dégorgement |
| `/conseils/`, `/conseils/{dept}/`, `/conseils/{article}/` | Rubrique conseils paginée et 58 articles |
| `/contact/` | Formulaire de devis |
| `/mentions-legales/`, `/politique-de-confidentialite/`, `/cgu/` | Pages légales |

## Où modifier quoi

| Fichier | Contenu |
| --- | --- |
| `tools/data.py` | Coordonnées, identité légale, prestations, tarifs, FAQ, avis, légendes photo |
| `tools/articles.py` | Les articles de conseils (un dictionnaire par article) |
| `tools/build.py` | Gabarits HTML de toutes les pages |
| `assets/css/style.css` | Design (couleurs dans `:root`) |
| `formulaire.php` | Réception des demandes de rappel (destinataire : contact@les-plombiers-bretons.fr) |

## Design

Charte alignée sur le logo : **bleu marine `#0b2a5b`** et **bleu roi
`#1557c0`** pour la structure, **gris acier** pour le texte et les fonds
neutres, et **orange `#d4600f` réservé aux boutons d'appel**. Titres en
**Montserrat**, texte en **Inter** — deux fontes libres (OFL) hébergées
localement, sans aucune requête vers un service tiers. **Angles droits**
partout (une seule règle en tête de `style.css`), seul le voyant « en ligne »
reste rond.

**Logo** : `assets/img/logo-original.png` (fichier fourni, marges blanches
retirées), décliné en `logo-200.webp` et `logo-400.webp` pour l'en-tête et le
pied de page, et en favicon carré sur fond blanc (`favicon-48.png`,
`favicon.png` 180 px pour iPhone, `favicon-512.png`).

**Un seul formulaire par page**, en bas (`cta_final()`, ancre `#devis`) :
tous les boutons « Être rappelé » y descendent. En haut de page, la place du
formulaire est prise par une photo d'intervention (`photo_hero` dans
`tools/data.py` pour les pages métier). Sur la page Contact, ce formulaire du
bas est la version détaillée (département, type de panne, urgence, message).

## Photos et équipe

Toutes les photos sont en place, **six par métier** :

- **Plomberie** : fuite sous évier, chaudière, canalisation encastrée, WC
  suspendu, mitigeur de douche, recherche de fuite acoustique ;
- **Dégorgement** : WC, évier, douche et regard extérieur au furet,
  hydrocurage haute pression, inspection caméra.

Sur chaque page métier, la photo de l'équipe accompagne la carte des communes.
La liste et la marche à suivre pour en changer sont dans
`assets/img/photos/LISEZ-MOI.txt`.

**Bandeau équipe** (accueil et page contact) : la photo de **Maxime, Pierre et
Jérôme** devant le camion, en pleine largeur, avec le prénom de chacun posé
sous lui, puis une bande marine avec le texte et le bouton d'appel. Prénoms et
positions : `EQUIPE` dans `tools/data.py` ; le bandeau : `bandeau_equipe()`
dans `tools/build.py`.

## ⚠ À compléter avant mise en ligne

- **Identité légale** (`SITE` dans `tools/data.py`) : forme juridique, siège,
  SIREN/SIRET, RCS, TVA, nom du dirigeant — obligatoires dans les mentions
  légales (LCEN art. 6-III, C. com. R.123-237).
- **Assurance** : assureur et numéro de contrat (mentions légales).
- **Médiateur de la consommation** (mentions légales).
- **Avis clients et tarifs** : repris comme exemples ; à remplacer par vos
  avis réels et vos propres tarifs.
- **Hébergeur** : Hostinger par défaut, à confirmer.
