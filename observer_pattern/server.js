const express = require('express');
const http = require('http');
const socketIo = require('socket.io');
const path = require('path');

const app = express();
const server = http.createServer(app);
const io = socketIo(server);

// Servir les fichiers statiques
app.use(express.static('public'));

// Route principale
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

// Gestion des connexions WebSocket
io.on('connection', (socket) => {
    console.log('Nouvelle connexion:', socket.id);

    // Recevoir et diffuser les messages
    socket.on('send_notification', (data) => {
        console.log('Message reçu:', data);
        // Diffuser à tous les clients (y compris l'émetteur)
        io.emit('receive_notification', data);
    });

    socket.on('disconnect', () => {
        console.log('Déconnexion:', socket.id);
    });
});

const PORT = process.env.PORT || 3000;
server.listen(PORT, () => {
    console.log(`🚀 Serveur démarré sur http://localhost:${PORT}`);
    console.log('📱 Ouvrez plusieurs onglets pour voir la communication en temps réel!');
});