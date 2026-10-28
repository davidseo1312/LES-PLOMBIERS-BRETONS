# -*- coding: utf-8 -*-
"""Données éditoriales du site Les Plombiers Bretons (activités, départements, contenus SEO)."""

SITE = {
    "nom": "Les Plombiers Bretons",
    "baseline": "Plomberie · Dégorgement de canalisations",
    # version courte : l'en-tête sticky ne doit jamais repousser le bouton d'appel
    "baseline_courte": "Plomberie · Dégorgement",
    "tel": "02 20 05 00 76",
    "tel_lien": "+33220050076",
    "email": "contact@les-plombiers-bretons.fr",
    "url": "https://les-plombiers-bretons.fr",
    # Point d'arrivée des formulaires. Le script formulaire.php, à la racine du
    # site, fonctionne sur tout hébergement PHP. Pour un service externe,
    # remplacez simplement l'URL (Formspree, Brevo, etc.).
    "form_endpoint": "/formulaire.php",
    # --- Identité légale : à compléter avant mise en ligne ---
    # L'article 6 III de la LCEN impose que les mentions légales nomment la
    # personne (ou la société) éditrice, avec ses numéros d'immatriculation
    # (article R.123-237 du Code de commerce).
    "denomination": "Les Plombiers Bretons",
    "nom_commercial": "Les Plombiers Bretons",
    "forme": "en attente de documents",
    "siren": "en attente de documents",
    "siret": "en attente de documents",
    "tva": "en attente de documents",
    "rcs": "en attente de documents",
    "greffe": "en attente de documents",
    "rcs_date": "en attente de documents",
    "rne_date": "en attente de documents",
    "creation": "en attente de documents",
    "naf": "43.22A",
    "naf_libelle": "Travaux d'installation d'eau et de gaz en tous locaux",
    "dirigeant": "le représentant légal des Plombiers Bretons",  # à remplacer par nom et prénom
    "siege": "en attente de documents",
    "adresse": "Bretagne — interventions sur les départements 22, 29, 35 et 56",
    # --- Hébergeur (à confirmer) ---
    "hebergeur": "Hostinger International Ltd",
    "hebergeur_adresse": "61 Lordou Vironos Street, 6023 Larnaca, Chypre",
    "hebergeur_site": "https://www.hostinger.fr",
}

# --------------------------------------------------------------------------
# Départements
# --------------------------------------------------------------------------
DEPARTEMENTS = [
    {
        "num": "22",
        "nom": "Côtes-d'Armor",
        "nom_court": "Côtes-d'Armor",
        "slug": "cotes-d-armor",
        "article": "dans les",           # « … dans les Côtes-d'Armor »
        "article_maj": "Dans les",
        "prefecture": "Saint-Brieuc",
        "gentile": "costarmoricains",
        "villes": ["Saint-Brieuc", "Lannion", "Dinan", "Guingamp", "Lamballe-Armor",
                   "Plérin", "Ploufragan", "Paimpol", "Trégueux", "Loudéac",
                   "Perros-Guirec", "Pordic", "Saint-Quay-Portrieux", "Quintin",
                   "Bégard", "Plestin-les-Grèves", "Callac", "Rostrenen"],
        "contexte": ("un habitat côtier très exposé au sel et à l'humidité, "
                     "de nombreuses longères rénovées et des réseaux d'assainissement "
                     "individuels fréquents dans l'arrière-pays"),
        "axes": "la RN12 entre Saint-Brieuc, Lamballe et Guingamp",
    },
    {
        "num": "29",
        "nom": "Finistère",
        "nom_court": "Finistère",
        "slug": "finistere",
        "article": "dans le",
        "article_maj": "Dans le",
        "prefecture": "Quimper",
        "gentile": "finistériens",
        "villes": ["Brest", "Quimper", "Concarneau", "Morlaix", "Douarnenez",
                   "Landerneau", "Quimperlé", "Plougastel-Daoulas", "Guipavas",
                   "Pont-l'Abbé", "Crozon", "Le Relecq-Kerhuon", "Plouzané",
                   "Saint-Renan", "Châteaulin", "Fouesnant", "Carhaix-Plouguer", "Bénodet"],
        "contexte": ("un parc immobilier ancien à Brest et Quimper, des résidences "
                     "secondaires nombreuses sur la côte et des canalisations "
                     "régulièrement mises à l'épreuve par les fortes pluies"),
        "axes": "la RN165 reliant Brest, Châteaulin et Quimper",
    },
    {
        "num": "35",
        "nom": "Ille-et-Vilaine",
        "nom_court": "Ille-et-Vilaine",
        "slug": "ille-et-vilaine",
        "article": "en",
        "article_maj": "En",
        "prefecture": "Rennes",
        "gentile": "bretilliens",
        "villes": ["Rennes", "Saint-Malo", "Fougères", "Vitré", "Cesson-Sévigné",
                   "Bruz", "Redon", "Dinard", "Betton", "Chantepie", "Saint-Grégoire",
                   "Combourg", "Pacé", "Châteaubourg", "Le Rheu", "Saint-Jacques-de-la-Lande",
                   "Montfort-sur-Meu", "Janzé"],
        "contexte": ("une forte densité d'appartements et de copropriétés sur Rennes "
                     "métropole, des immeubles anciens intra-rocade et un bassin "
                     "locatif qui impose des interventions rapides"),
        "axes": "la rocade rennaise et la N137 vers Saint-Malo",
    },
    {
        "num": "56",
        "nom": "Morbihan",
        "nom_court": "Morbihan",
        "slug": "morbihan",
        "article": "dans le",
        "article_maj": "Dans le",
        "prefecture": "Vannes",
        "gentile": "morbihannais",
        "villes": ["Vannes", "Lorient", "Lanester", "Pontivy", "Ploemeur",
                   "Hennebont", "Auray", "Guidel", "Quiberon", "Séné", "Saint-Avé",
                   "Sarzeau", "Pluvigner", "Caudan", "Questembert", "Baud",
                   "Le Palais", "Locminé"],
        "contexte": ("un littoral très touristique du golfe du Morbihan à Quiberon, "
                     "de nombreuses locations saisonnières et des installations "
                     "sollicitées par pics en haute saison"),
        "axes": "la RN165 entre Lorient, Auray et Vannes",
    },
]

# --------------------------------------------------------------------------
# Activités
# --------------------------------------------------------------------------
ACTIVITES = [
    {
        "key": "plomberie",
        "slug": "plomberie-depannage",
        "nom": "Plomberie & Dépannage",
        "nom_court": "Plomberie",
        "metier": "Plomberie et dépannage sanitaire",
        "pro": "plombier",
        "pro_pluriel": "plombiers",
        "h1": "Plomberie & Dépannage d'Urgence",
        "accroche": ("Fuite d'eau, chauffe-eau en panne, dégât des eaux&nbsp;? "
                     "Un plombier qualifié se déplace chez vous en urgence, 7j/7."),
        "mots_cles": "plombier, dépannage plomberie, recherche de fuite, chauffe-eau, dégât des eaux",
        "hero_points": [
            "Recherche de fuite non destructive (caméra thermique, gaz traceur)",
            "Véhicules équipés&nbsp;: réparation immédiate dans la majorité des cas",
            "Tarifs annoncés avant intervention, garantie décennale",
        ],
        "prestations": [
            ("Recherche de fuite non destructive",
             "Caméra thermique, gaz traceur et détection acoustique pour localiser la fuite sans casser."),
            ("Réparation de fuite d'eau",
             "Fuite sur canalisation encastrée, raccord, colonne ou compteur&nbsp;: réparation ou remplacement."),
            ("Dépannage et remplacement de chauffe-eau",
             "Ballon électrique, thermodynamique ou chauffe-eau gaz&nbsp;: diagnostic, résistance, groupe de sécurité."),
            ("Robinetterie et sanitaires",
             "Mitigeur qui goutte, chasse d'eau défectueuse, WC, lavabo, douche&nbsp;: remplacement soigné."),
            ("Dégât des eaux et assèchement",
             "Coupure, mise en sécurité, réparation et rapport détaillé pour votre déclaration d'assurance."),
            ("Remplacement de canalisations",
             "Reprise de réseaux plomb, cuivre ou PER vétustes, avec mise en conformité sanitaire."),
            ("Installation de salle de bain",
             "Création ou rénovation complète&nbsp;: alimentation, évacuation, pose des sanitaires."),
            ("Détartrage et entretien",
             "Traitement du calcaire, adoucisseur, entretien préventif des installations sanitaires."),
        ],
        "urgences": [
            "Fuite d'eau active ou canalisation percée",
            "Absence totale d'eau chaude dans le logement",
            "Dégât des eaux en cours chez vous ou chez le voisin",
            "Canalisation gelée ou éclatée en période de froid",
        ],
        "tarifs": [
            ("Déplacement + diagnostic plomberie", "à partir de 79 € TTC"),
            ("Réparation de fuite simple", "à partir de 149 € TTC"),
            ("Recherche de fuite non destructive", "à partir de 250 € TTC"),
            ("Remplacement de chauffe-eau 200 L", "à partir de 690 € TTC pose comprise"),
            ("Remplacement de mitigeur ou robinet", "à partir de 110 € TTC"),
            ("Majoration nuit, dimanche et jours fériés", "sur devis validé avant intervention"),
        ],
        "faq": [
            ("Sous quel délai un plombier peut-il intervenir {art} {dept}&nbsp;?",
             "Pour une fuite active, nous visons une intervention dans l'heure autour de "
             "{prefecture} et des principales villes {du_dept}. Sur les communes plus "
             "éloignées, comptez 2 à 3 heures. Le créneau exact vous est confirmé lors de "
             "l'appel, avec le nom du technicien."),
            ("Combien coûte une recherche de fuite&nbsp;?",
             "Une recherche de fuite non destructive démarre à 250 € TTC selon la surface et "
             "la technologie nécessaire (caméra thermique, gaz traceur, corrélation acoustique). "
             "Elle est très souvent prise en charge par votre assurance habitation dans le cadre "
             "d'un dégât des eaux&nbsp;: nous fournissons le rapport nécessaire."),
            ("Que faire immédiatement en cas de fuite importante&nbsp;?",
             "Fermez le robinet d'arrêt général (souvent sous l'évier, dans le garage ou au "
             "compteur), coupez l'électricité de la zone si l'eau approche d'une prise, puis "
             "appelez-nous au {tel}. Nous vous guidons par téléphone en attendant l'arrivée du "
             "technicien."),
            ("Intervenez-vous sur les chauffe-eau de toutes marques&nbsp;?",
             "Oui&nbsp;: Atlantic, Thermor, Ariston, De Dietrich, Chaffoteaux, Saunier Duval et "
             "les autres marques courantes. Nous dépannons en priorité (résistance, thermostat, "
             "groupe de sécurité) et ne proposons un remplacement que lorsque la réparation "
             "n'est plus rentable."),
            ("Vos travaux sont-ils garantis&nbsp;?",
             "Oui. Nos artisans sont assurés en responsabilité civile professionnelle et "
             "couverts par la garantie décennale pour les travaux qui l'exigent. Les pièces "
             "posées bénéficient de la garantie constructeur, et la main-d'œuvre est garantie."),
            ("Puis-je obtenir un devis avant de m'engager&nbsp;?",
             "Toujours. Le devis est gratuit, détaillé et sans engagement. Rien ne commence "
             "avant votre accord écrit ou signé sur tablette, et le montant validé est celui qui "
             "figure sur la facture."),
        ],
        "avis": [
            ("Fuite sous l'évier un samedi soir, plombier arrivé en 45 minutes. Réparation "
             "propre, explications claires, facture conforme au devis annoncé. Impeccable.",
             "Nathalie R.", 5),
            ("Chauffe-eau HS avec trois enfants à la maison. Diagnostic fait le jour même et "
             "remplacement dès le lendemain matin. Efficaces, ponctuels et très corrects.",
             "Yann K.", 5),
            ("Recherche de fuite sur une dalle sans rien casser. Rapport complet transmis à "
             "l'assurance qui a tout pris en charge. Vrai professionnalisme.",
             "Christophe M.", 5),
        ],
        "prose_titre": "Plombier {art} {dept} ({num})&nbsp;: dépannage, réparation et rénovation",
        "prose": [
            "Une fuite d'eau non traitée, c'est en moyenne plusieurs centaines de litres perdus "
            "par jour, une facture qui grimpe et, très vite, des dégâts sur les cloisons et les "
            "sols. C'est pourquoi nos {pro_pluriel} {art} {dept} interviennent en priorité "
            "sur les fuites actives et les coupures d'eau chaude, tous les jours de l'année.",
            "Le parc immobilier local a ses réalités&nbsp;: {contexte}. "
            "Nos véhicules sont donc équipés des pièces les plus courantes pour traiter la "
            "majorité des pannes dès le premier passage, de {ville1} à {ville2} jusqu'à {ville3}.",
            "Nous travaillons dans les deux sens&nbsp;: l'urgence, avec une intervention rapide et "
            "un tarif annoncé avant de commencer&nbsp;; et le travail de fond, avec la rénovation "
            "de salle de bain, le remplacement de réseaux vétustes et la mise en conformité "
            "sanitaire. Dans les deux cas, même exigence de propreté du chantier et de clarté "
            "sur le prix.",
        ],
        "photos": [
            ("plomberie-1.jpg",
             "Plombier des Plombiers Bretons démontant le siphon sous un évier de cuisine",
             "Fuite sous évier et démontage de siphon",
             "Une trace d'humidité sous un meuble peut venir du siphon, d'un flexible ou "
             "d'un raccord mural. Nous isolons chaque point avant de toucher quoi que ce "
             "soit, bassine en place, pour réparer ce qui fuit réellement. Le diagnostic "
             "vous est expliqué et chiffré avant toute intervention."),
            ("plomberie-2.jpg",
             "Plombier des Plombiers Bretons intervenant sur une chaudière murale et son chauffe-eau",
             "Intervention sur chaudière et chauffe-eau",
             "Plus d'eau chaude, pression qui chute, appareil en défaut&nbsp;: nous "
             "contrôlons les organes un par un — circulateur, vase d'expansion, sécurité — "
             "avant d'envisager un remplacement. Dans bien des cas, une pièce suffit, et "
             "l'appareil est remis en service devant vous."),
            ("plomberie-3.jpg",
             "Plombier des Plombiers Bretons remplaçant une canalisation PVC encastrée dans un mur ouvert",
             "Reprise de canalisation encastrée",
             "Quand une canalisation encastrée fuit ou se fissure, la réparation passe par "
             "la reprise du tronçon. Nous ouvrons au plus juste, remplaçons la section "
             "défectueuse avec des raccords adaptés, puis testons l'étanchéité avant de "
             "refermer la cloison."),
            ("plomberie-4.jpg",
             "Plombier des Plombiers Bretons posant une cuvette de WC suspendu sur son bâti-support",
             "Pose de WC suspendu",
             "Sur une salle de bain neuve ou rénovée, nous reprenons les alimentations et "
             "les évacuations, puis posons bâti-support et cuvette. Chaque raccord est mis "
             "en pression et vérifié avant d'être encastré&nbsp;: c'est à ce moment précis "
             "que se jouent les fuites futures."),
        ],
        "photo_equipe": ("plomberie-equipe.jpg",
                         "Plombier des Plombiers Bretons réparant un mitigeur thermostatique de douche",
                         "Réparation de mitigeur de douche",
                         "Un mitigeur qui goutte ou ne tient plus la température se répare "
                         "le plus souvent sans changer l'appareil&nbsp;: cartouche, joints "
                         "ou clapets, remplacés sur place."),
        "prose_h3": [
            ("Les dépannages les plus demandés {art} {dept}",
             ["Fuite sur flexible, siphon ou raccord sous évier",
              "Panne de chauffe-eau&nbsp;: plus d'eau chaude ou eau tiède",
              "Fuite encastrée détectée par une facture d'eau anormale",
              "Chasse d'eau qui fuit en continu et gonfle la consommation",
              "Canalisation gelée ou éclatée après un épisode de grand froid"]),
            ("Nos engagements sur chaque chantier",
             ["Devis gratuit et détaillé, validé avant toute intervention",
              "Techniciens qualifiés, assurés et couverts par la garantie décennale",
              "Chantier protégé et nettoyé avant notre départ",
              "Facture conforme au devis, sans frais ajoutés à la fin"]),
        ],
    },

    {
        "key": "degorgement",
        "slug": "degorgement-canalisation",
        "nom": "Dégorgement & Canalisations",
        "nom_court": "Dégorgement",
        "metier": "Dégorgement et curage de canalisations",
        "pro": "technicien assainissement",
        "pro_pluriel": "techniciens assainissement",
        "h1": "Dégorgement & Débouchage de Canalisations",
        "accroche": ("Canalisation bouchée, WC qui refoule, évacuation qui déborde&nbsp;? "
                     "Nos camions hydrocureurs interviennent en urgence, 7j/7."),
        "mots_cles": "dégorgement, débouchage canalisation, curage, hydrocurage, WC bouché, fosse septique",
        "hero_points": [
            "Camion hydrocureur et furet électrique haute performance",
            "Inspection par caméra avant et après intervention",
            "Débouchage garanti ou nous revenons sans frais",
        ],
        "prestations": [
            ("Débouchage WC, éviers et douches",
             "Furet électrique ou pompe haute pression selon le type de bouchon et la nature du réseau."),
            ("Hydrocurage haute pression",
             "Curage complet des canalisations jusqu'à 200 bars pour éliminer graisses, tartre et racines."),
            ("Inspection vidéo par caméra",
             "Diagnostic précis de l'état du réseau, localisation exacte du bouchon ou de la casse, rapport remis."),
            ("Débouchage de colonnes d'immeuble",
             "Intervention sur chutes d'eaux usées et colonnes collectives pour syndics et copropriétés."),
            ("Vidange de fosse septique et micro-station",
             "Pompage, nettoyage et contrôle du bon fonctionnement, avec bordereau d'élimination des déchets."),
            ("Dégraissage de bacs à graisse",
             "Entretien périodique pour restaurants, cantines et collectivités, avec contrat possible."),
            ("Pompage de cave et de regard inondés",
             "Évacuation des eaux après un refoulement ou de fortes pluies, remise en état du regard."),
            ("Détection et mise à jour de réseaux",
             "Localisation de canalisation enterrée, regard introuvable, plan de réseau et préconisations."),
        ],
        "urgences": [
            "WC bouché dans un logement sans autre sanitaire",
            "Refoulement d'eaux usées dans une douche ou une cave",
            "Colonne d'immeuble engorgée impactant plusieurs logements",
            "Débordement de regard ou de fosse septique",
        ],
        "tarifs": [
            ("Débouchage simple (WC, évier, douche)", "à partir de 129 € TTC"),
            ("Débouchage avec camion hydrocureur", "à partir de 249 € TTC"),
            ("Hydrocurage préventif de réseau", "à partir de 290 € TTC"),
            ("Inspection vidéo par caméra", "à partir de 179 € TTC"),
            ("Vidange de fosse septique (3 m³)", "à partir de 280 € TTC"),
            ("Majoration nuit, dimanche et jours fériés", "sur devis validé avant intervention"),
        ],
        "faq": [
            ("Combien de temps pour un dégorgement d'urgence {art} {dept}&nbsp;?",
             "Nos équipes sont positionnées sur {prefecture} et les principales villes {du_dept}. "
             "En urgence, nous visons une intervention dans l'heure sur les secteurs proches et "
             "sous 2 à 3 heures sur les zones rurales. Le délai vous est annoncé au téléphone, "
             "avant tout déplacement."),
            ("Le devis est-il vraiment gratuit&nbsp;?",
             "Oui. Le diagnostic et le devis sont gratuits et sans engagement. Le tarif est "
             "annoncé et validé avec vous avant le démarrage des travaux&nbsp;: aucune surprise "
             "ne s'ajoute sur la facture finale."),
            ("Quelle différence entre un débouchage et un hydrocurage&nbsp;?",
             "Le débouchage lève le bouchon pour rétablir l'écoulement immédiatement. "
             "L'hydrocurage nettoie la paroi complète de la canalisation à haute pression&nbsp;: "
             "il retire les dépôts de graisse et de tartre qui provoquent les bouchons à répétition. "
             "C'est la solution durable quand le problème revient."),
            ("Qui paie le dégorgement en location&nbsp;: locataire ou propriétaire&nbsp;?",
             "L'entretien courant des évacuations relève du locataire. En revanche, un défaut "
             "structurel (canalisation affaissée, racines, vétusté) est à la charge du "
             "propriétaire. Notre rapport d'inspection vidéo permet de trancher objectivement et "
             "sert de justificatif auprès de l'assurance ou du bailleur."),
            ("Intervenez-vous pour les copropriétés et les professionnels&nbsp;?",
             "Oui. Nous travaillons avec des syndics, bailleurs, restaurants et collectivités "
             "{du_dept}, en dépannage ponctuel comme en contrat d'entretien annuel "
             "(colonnes, bacs à graisse, réseaux extérieurs)."),
            ("Que faire en attendant votre arrivée&nbsp;?",
             "N'utilisez plus les évacuations concernées, coupez l'arrivée d'eau si l'eau monte, "
             "et évitez les déboucheurs chimiques&nbsp;: ils abîment les joints et rendent "
             "l'intervention plus dangereuse pour le technicien."),
        ],
        "avis": [
            ("WC bouché un dimanche matin, technicien sur place en 50 minutes. Débouché et "
             "nettoyé proprement, prix exactement celui annoncé au téléphone. Rien à redire.",
             "Sébastien L.", 5),
            ("Colonne d'immeuble engorgée sur nos 6 logements. Hydrocurage complet et passage "
             "caméra avec rapport pour le syndic. Travail sérieux et parfaitement documenté.",
             "Marie-Hélène T.", 5),
            ("Fosse septique à vider dans une maison familiale. Rendez-vous tenu, bordereau "
             "fourni, équipe agréable et soigneuse. Je les rappellerai pour l'entretien.",
             "Gwenaël P.", 5),
        ],
        "prose_titre": "Dégorgement {art} {dept} ({num})&nbsp;: nos interventions au quotidien",
        "prose": [
            "Une canalisation ne se bouche jamais du jour au lendemain. Les dépôts de graisse, "
            "de calcaire, de cheveux et de lingettes s'accumulent pendant des mois, réduisent le "
            "diamètre utile du tuyau, puis l'obstruent totalement au plus mauvais moment. "
            "{Art} {dept}, nos {pro_pluriel} traitent chaque semaine des évacuations "
            "d'éviers saturées, des WC qui refoulent et des regards extérieurs débordants.",
            "Le territoire a ses particularités&nbsp;: {contexte}. "
            "Ces contraintes locales, nous les connaissons parce que nous intervenons sur le "
            "terrain tous les jours, de {ville1} à {ville2} en passant par {ville3}.",
            "Notre méthode est toujours la même&nbsp;: identifier la cause avant d'agir. Un "
            "bouchon ponctuel se traite au furet en moins d'une heure. Un réseau encrassé "
            "demande un hydrocurage haute pression. Une canalisation affaissée ou percée "
            "nécessite une inspection caméra et un chiffrage de réparation. Vous repartez "
            "toujours avec un diagnostic clair, pas seulement avec un écoulement rétabli.",
        ],
        "photos": [
            ("degorgement-1.jpg",
             "Technicien débouchant des WC à la ventouse",
             "Débouchage de WC",
             "Un WC qui refoule est l'urgence la plus fréquente. Nous commençons "
             "toujours par la ventouse&nbsp;: elle suffit dans la majorité des cas et "
             "n'abîme ni la céramique ni les joints. Si le bouchon résiste, le furet "
             "électrique prend le relais dans la foulée. L'évacuation est testée devant "
             "vous avant notre départ."),
            ("degorgement-2.jpg",
             "Débouchage d'un lavabo au furet électrique par un technicien",
             "Débouchage de lavabo au furet",
             "Sur un lavabo ou un évier, le bouchon se forme au siphon ou juste après, "
             "là où graisses et cheveux s'accumulent. Le furet électrique traverse le "
             "coude et racle la paroi sur plusieurs mètres, sans démonter le meuble. "
             "Un rinçage final vérifie que l'écoulement est bien rétabli."),
            ("degorgement-3.jpg",
             "Débouchage d'un receveur de douche au furet électrique",
             "Débouchage de receveur de douche",
             "Une douche qui se vide lentement annonce un bouchon de cheveux et de savon "
             "dans la bonde. Le furet est introduit par la grille d'évacuation, sans "
             "casser ni déposer le receveur. L'intervention prend généralement moins "
             "d'une heure."),
            ("degorgement-4.jpg",
             "Inspection vidéo d'une canalisation par caméra endoscopique",
             "Inspection vidéo par caméra",
             "Quand le bouchon revient sans cesse, la caméra dit pourquoi. Elle descend "
             "dans la canalisation et montre en direct l'état de la paroi&nbsp;: dépôt de "
             "graisse, racine infiltrée, tuyau affaissé ou fissuré. Vous repartez avec un "
             "diagnostic précis et la localisation exacte du défaut."),
            ("degorgement-5.jpg",
             "Hydrocurage haute pression d'un regard d'assainissement par nos techniciens",
             "Hydrocurage haute pression",
             "L'hydrocurage nettoie toute la paroi de la canalisation, pas seulement le "
             "bouchon. Un jet pouvant atteindre 200&nbsp;bars décolle graisses, tartre et "
             "racines sur toute la longueur du réseau. C'est la solution durable lorsque "
             "les débouchages se répètent."),
            ("degorgement-6.jpg",
             "Camion hydrocureur et son équipe lors d'un pompage sur regard",
             "Pompage et vidange sur regard",
             "Regard qui déborde, fosse pleine, cave inondée&nbsp;: le camion pompe et "
             "évacue, puis nous contrôlons le bon écoulement du réseau. Les matières sont "
             "acheminées vers un centre agréé et un bordereau d'élimination vous est "
             "remis."),
        ],
        "photo_equipe": None,
        "prose_h3": [
            ("Les bouchons les plus fréquents {art} {dept}",
             ["Lingettes et produits d'hygiène dans les WC — première cause d'urgence",
              "Graisses figées dans les évacuations de cuisine, aggravées par l'eau froide",
              "Cheveux et savon dans les bondes de douche et de baignoire",
              "Racines d'arbustes infiltrées dans les réseaux enterrés anciens",
              "Calcaire et tartre sur les canalisations en fonte des bâtiments anciens"]),
            ("Prévenir plutôt que déboucher",
             ["Un hydrocurage préventif tous les 2 à 3 ans sur une maison individuelle",
              "Un dégraissage semestriel pour les cuisines professionnelles",
              "Une vidange de fosse septique tous les 4 ans environ selon l'occupation",
              "Des grilles anti-cheveux sur les douches et un bac à graisse entretenu"]),
        ],
    },
]

# --------------------------------------------------------------------------
# Éléments transverses
# --------------------------------------------------------------------------
# (titre, texte, icône)
REASSURANCE = [
    ("Intervention 24/7 en urgence",
     "Astreinte réelle nuits, week-ends et jours fériés. Un interlocuteur au bout du fil, "
     "pas un répondeur, et un délai annoncé dès l'appel.", "horloge"),
    ("Devis gratuit sans engagement",
     "Diagnostic et chiffrage offerts. Le prix est validé avec vous avant de commencer&nbsp;: "
     "la facture ne dépasse jamais le devis accepté.", "devis"),
    ("Artisans qualifiés & expérimentés",
     "Des professionnels du métier, formés et équipés, qui interviennent en Bretagne toute "
     "l'année. Pas de sous-traitance improvisée.", "medaille"),
    ("Garantie décennale",
     "Responsabilité civile professionnelle et garantie décennale sur les travaux concernés. "
     "Vous êtes couvert, et nous assumons nos interventions.", "bouclier"),
]

ETAPES = [
    ("Vous appelez", "Un technicien vous répond directement, qualifie la panne au téléphone et "
     "vous annonce un créneau réaliste ainsi qu'un ordre de prix."),
    ("Nous diagnostiquons", "Sur place, l'intervenant identifie la cause exacte du problème avec "
     "le matériel adapté, et vous l'explique simplement."),
    ("Vous validez le devis", "Le montant est présenté avant les travaux. Rien ne démarre sans "
     "votre accord&nbsp;: c'est vous qui décidez, sans pression."),
    ("Nous intervenons", "Réparation réalisée, chantier nettoyé, fonctionnement vérifié devant "
     "vous, facture détaillée remise avec la garantie."),
]

PHOTOS_ACCUEIL = [
    ("degorgement-1.jpg", "Technicien débouchant des WC",
     "Débouchage de WC",
     "L'urgence la plus fréquente. Ventouse d'abord, furet électrique ensuite si le "
     "bouchon résiste, et test de l'évacuation devant vous avant notre départ."),
    ("degorgement-5.jpg", "Hydrocurage haute pression d'un regard par nos techniciens",
     "Hydrocurage haute pression",
     "Un jet pouvant atteindre 200&nbsp;bars décolle graisses, tartre et racines sur "
     "toute la longueur du réseau. La solution quand les débouchages se répètent."),
    ("degorgement-4.jpg", "Inspection vidéo d'une canalisation par caméra",
     "Inspection vidéo par caméra",
     "La caméra montre en direct l'état de la paroi et localise le défaut au mètre "
     "près&nbsp;: racine, affaissement, fissure. Diagnostic remis par écrit."),
    ("plomberie-1.jpg", "Démontage d'un siphon sous évier par un plombier",
     "Recherche de fuite",
     "Siphon, flexible ou raccord mural&nbsp;: nous identifions le point de fuite avant "
     "de démonter quoi que ce soit, et nous chiffrons la réparation avant d'agir."),
    ("plomberie-2.jpg", "Intervention sur une chaudière murale par un plombier",
     "Chaudière et chauffe-eau",
     "Circulateur, vase d'expansion, sécurités&nbsp;: chaque organe est contrôlé "
     "avant d'envisager un remplacement. Souvent, une pièce suffit."),
    ("plomberie-4.jpg", "Pose d'une cuvette de WC suspendu par un plombier",
     "Pose de WC suspendu",
     "Alimentations et évacuations reprises avant la pose du bâti et de la cuvette, chaque "
     "raccord mis en pression et vérifié avant d'être encastré."),
]

PHOTO_EQUIPE = ("equipe.jpg", "L'équipe des Plombiers Bretons et son véhicule d'intervention",
                "Nos équipes et nos véhicules",
                "Nos véhicules embarquent le matériel des deux métiers&nbsp;: furet, "
                "pompe et caméra pour les canalisations, détection de fuite et pièces "
                "courantes pour la plomberie. C'est ce qui permet de résoudre la "
                "majorité des pannes dès le premier passage.")

STATS = [
    ("24/7", "Astreinte urgence"),
    ("4", "Départements couverts"),
    ("&lt; 1 h", "Délai visé en urgence"),
    ("100 %", "Devis gratuits"),
]
