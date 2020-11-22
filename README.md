# Tamagopy

Tamagopy est un jeu de type "Tamagotchi" en ligne de commandes. Il faut donc s'occuper d'un animal virtuel, en prendre soin, le nourrir,
pour éviter la mort.

## Installation

### 1. Sous Windows
#### 1.1. Avec l'archive portable

Il existe une version portable du jeu. Pas besoin d'installation :

 * Décompressez l'archive
 * Lancez le fichier "TamaGoPy.exe"
 * Si besoin créez un raccourci sur le bureau : Clic Droit > Envoyer vers > Bureau (créer un raccourci)

#### 1.2. Avec le setup

Si vous avez en revanche envie d'installer le jeu sur votre ordinateur, pour qu'il figure ensuite dans les registres d'applications (ou pour tout autre raison), la procédure est un peu plus longue mais plus simple :

 * Executez le fichier (exe ou msi)
 * Suivez les instructions à l'écran pour installer le jeu

### 2. Sous Linux

#### 2.1. Avec le paquet DEB (Seulement pour les distributions basées sur Debian comme Ubuntu ou Linux Mint)

Sinon, le paquet Debian peut être une bonne option. Installez-le simplement avec la commande <code>sudo dpkg -i TamaGoPy_LinuxDeb_all.deb</code> ou avec [L'installeur de paquets GDebi](http://doc.ubuntu-fr.org/gdebi) ou tout autre installeur de paquets

### 3. Sous macOS (10.11 ou ultérieur)

L'installation sous macOS se fait comme tout autre programme :

 * Une fois téléchargé, double-cliquez sur l'image disque (*.dmg) du jeu
 * Dans la fenêtre qui s'est ouverte, prenez avec votre souris l'application TamaGoPy et glissez-la dans le dossier Applications

### 4. Construire votre propre version avec le code source

Sinon, si vous souhaitez plus de personnalisation, vous pouvez opter pour une construction manuelle en utilisant CX_freeze pour python (le fichier setup est fourni).
Dans le dossier du code source, entrez

 * (en remplaçant *python* par la commande vers python 3.6 ou ultérieur, comme <code>python3</code> par défaut sur Linux) <code>*python* setup.py build
 * Le résultat se trouve dans le dossier "build"

Notez que l'argument <code>build</code> peut être remplacé par un autre. [Voir la liste des arguments (en anglais)](cx-freeze.readthedocs.io/en/latest/distutils.html#distutils-setup-script)

## License

Le contenu et le code est sous la license CC BY-NC 4.0 International de Creative Commons. [En savoir plus sur le site de Creative Commons](http://creativecommons.org/licenses/by-nc/4.0/). Selon cette license, vous avez l'autorisation de Remixer, adapter et partager l'oeuvre en respectant ces consignes :

 * Créditer l'auteur de cette oeuvre, par un court texte comme : "Travail original par [khyrthy](http://khyrthy.github.io)
 * Ne pas redistribuer l'oeuvre à des fins commerciales