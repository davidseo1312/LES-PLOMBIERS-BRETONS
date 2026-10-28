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
pied de page. Le favicon (`favicon.svg` / `favicon.png`) reprend la goutte
bleue sur fond marine, plus lisible à 32 px que le logo complet.

## Photos

Les **5 photos de plomberie** sont en place (fuite sous évier, chaudière,
canalisation encastrée, WC suspendu, mitigeur de douche). Les photos de
dégorgement et la photo d'équipe de l'accueil sont **en attente** : chaque
emplacement vide affiche un cadre « Photo en attente » avec le nom de fichier
attendu. La liste complète
est dans `assets/img/photos/LISEZ-MOI.txt` — déposez les fichiers sous ces
noms puis relancez le build.

## ⚠ À compléter avant mise en ligne

- **Identité légale** (`SITE` dans `tools/data.py`) : forme juridique, siège,
  SIREN/SIRET, RCS, TVA, nom du dirigeant — obligatoires dans les mentions
  légales (LCEN art. 6-III, C. com. R.123-237).
- **Assurance** : assureur et numéro de contrat (mentions légales).
- **Médiateur de la consommation** (mentions légales).
- **Avis clients et tarifs** : repris comme exemples ; à remplacer par vos
  avis réels et vos propres tarifs.
- **Hébergeur** : Hostinger par défaut, à confirmer.
