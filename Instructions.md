# Installation du projet et configuration



English below



Étape 1 : Acquisition du projet

\- Faire un git clone sur votre PC ou télécharger le fichier .zip directement depuis l’interface web de la branche du dépôt.



Étape 2 : Ouverture du projet

\- Une fois le dossier sur votre PC, ouvrez-le avec l’IDE de votre choix (ex. : VS Code, Visual Studio, Cursor, etc.).

\- Si le projet est au format .zip, décompressez-le avant de l’ouvrir.

\- Je recommande fortement d’ouvrir le répertoire avec PowerShell, un Shell ou l’invite de commandes (CMD).



Étape 3 : Installation des dépendances

\- Dans le dossier fourni, un dossier node\_modules peut déjà être présent : il contient les dépendances installées pour le projet.

\- J’ai utilisé pnpm pour installer les dépendances, mais avec Node.js installé sur votre PC vous pouvez aussi utiliser npm.



Téléchargement de Node.js :

\- Si vous n’avez pas Node.js : https://nodejs.org/en/download



**Si vous souhaitez utiliser pnpm :**

\- Installez pnpm si nécessaire : https://pnpm.io/installation

\- Suivez les instructions d’installation, puis exécutez dans votre terminal (PowerShell, Shell, CMD, ou Ctrl+J dans VS Code) :



pnpm install

pnpm start    #ou pnpm run dev



\- La première commande installe localement les dépendances requises. Exemple de résultat attendu :



dependencies:

\+ express 4.22.1

\+ socket.io 4.8.1



devDependencies:

\+ nodemon 2.0.22



Done in 22.8s using pnpm v10.23.0



Note : les versions des modules/dépendances peuvent varier.



\- La seconde commande lance le serveur Node.js. Par défaut, il écoute sur le port 3000. Exemple de sortie :



> observer-pattern-chat@1.0.0 start C:\\Users\\User\\Documents\\Sites Webs\\observer\_pattern

> node server.js



🚀 Serveur démarré sur http://localhost:3000

📱 Ouvrez plusieurs onglets pour voir la communication en temps réel!





\- Pour accéder à l’interface déployée, copiez-collez l’URL affichée (ex. http://localhost:3000) dans un navigateur. Vous aurez alors accès à une interface de messagerie instantanée.



**Pour ceux qui utilisent npm :**

\- Même procédure que pour pnpm :



npm install

npm start    #ou npm run dev



\- Les commandes produisent les mêmes résultats.



Quelques précisions :

\- Seule la page ./public/index.html est exécutée et déployée sur le serveur. Le serveur enregistre chaque message en clair et en temps réel lorsqu’ils sont envoyés.

\- index.html est la version la plus aboutie du projet de messagerie instantanée ; elle illustre concrètement l’application du patron observateur : transmission et mise à jour en temps réel des messages entre différentes sessions/instances connectées au serveur.

\- mporol.html est une version basique respectant le diagramme de classes élaboré lors de l’étude de faisabilité (disponible dans la branche). Le patron observateur étant un système de notification, l’envoi d’un message selon différents observateurs (cases à cocher) entraîne la mise à jour de l’interface avec différentes vues permettant de distinguer les destinataires. Il n’est pas nécessaire de déployer ce fichier sur le serveur car il est statique et non dynamique : les messages ne s’échangent pas entre instances.



Pour arrêter le serveur :

\- Appuyez sur Ctrl+C dans le terminal ou fermez la fenêtre du terminal.





**English version**



# Project installation and configuration



Step 1: Acquire the project

\- Run git clone on your machine or download the .zip file directly from the repository branch via the web interface.



Step 2: Open the project

\- Once the folder is on your PC, open it with the IDE of your choice (e.g., VS Code, Visual Studio, Cursor, etc.).

\- If the project is a .zip, unzip it before opening.

\- I strongly recommend opening the directory with PowerShell, a shell, or the Command Prompt (CMD).



Step 3: Install dependencies

\- The provided folder may already contain a node\_modules directory with the installed dependencies.

\- I used pnpm to install dependencies, but if Node.js is installed on your PC you can use npm by default.



Node.js download:

\- If you don’t have Node.js: https://nodejs.org/en/download



**If you want to use pnpm:**

\- Install pnpm if needed: https://pnpm.io/installation

\- Follow the installation instructions, then run in your terminal (PowerShell, shell, CMD, or Ctrl+J in VS Code):



pnpm install

pnpm start    # or

pnpm run dev





\- The first command installs the required local dependencies. Example expected output:



dependencies:

\+ express 4.22.1

\+ socket.io 4.8.1



devDependencies:

\+ nodemon 2.0.22



Done in 22.8s using pnpm v10.23.0



Note: module/dependency versions may vary.



\- The second command starts the Node.js server. By default it runs on port 3000. Example output:



> observer-pattern-chat@1.0.0 start C:\\Users\\User\\Documents\\Sites Webs\\observer\_pattern

> node server.js



🚀 Server started at http://localhost:3000

📱 Open multiple tabs to see real-time communication!





\- To access the deployed interface, copy and paste the displayed URL (e.g. http://localhost:3000) into a browser. You will then have access to an instant messaging interface.



**For npm users:**

\- Same steps as with pnpm:



npm install

npm start    # or

npm run dev



\- The commands produce the same results.



Notes:

\- Only ./public/index.html is executed and served by the server. The server records each message in plain text and in real time when messages are sent.

\- index.html is the most complete version of the messaging project; it clearly demonstrates the Observer pattern: real-time transmission and update of messages among different sessions/instances connected to the server.

\- mporol.html is a basic version following the class diagram from the feasibility study (available in the branch). Since the Observer pattern is a basic notification system, sending a message based on different observers (checkboxes) updates the messaging interface with different views to distinguish recipients. It is not necessary to deploy this file on the server because it is static and not dynamic—messages are not exchanged between instances.



To stop the server:

\- Press Ctrl+C in the terminal or simply close the terminal window.







